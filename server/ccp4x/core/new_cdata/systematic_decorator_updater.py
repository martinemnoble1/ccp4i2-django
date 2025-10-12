#!/usr/bin/env python3
"""Systematic decorator updater for all CData class files.

This script systematically processes all *_classes.py files in the new_cdata directory
to apply @cdata_class decorators and remove manual attribute declarations.
"""

import json
import re
from typing import Dict, Any, List, Tuple
from pathlib import Path


def load_metadata() -> Dict[str, Any]:
    """Load the JSON metadata."""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
        # Extract the classes dictionary
        return data.get("classes", {})


def map_class_to_attribute_type(class_name: str) -> str:
    """Map JSON class names to our AttributeType enum values."""
    clean_name = class_name.split(".")[-1]

    mapping = {
        "CInt": "AttributeType.INT",
        "CFloat": "AttributeType.FLOAT",
        "CBoolean": "AttributeType.BOOLEAN",
        "CBool": "AttributeType.BOOLEAN",
        "CString": "AttributeType.STRING",
        "CFilePath": "AttributeType.FILEPATH",
        "CProjectId": "AttributeType.PROJECT_ID",
        "CUUID": "AttributeType.UUID",
        "CJobTitle": "AttributeType.JOB_TITLE",
    }

    if clean_name in mapping:
        return mapping[clean_name]
    else:
        return f'AttributeType.CUSTOM, custom_class="{clean_name}"'


def generate_attribute_definition(attr_name: str, attr_def: Dict[str, Any]) -> str:
    """Generate an attribute definition string."""
    class_name = attr_def.get("class", "CCP4Data.CString")
    qualifiers = attr_def.get("qualifiers", {})

    # Get attribute type
    attr_type = map_class_to_attribute_type(class_name)

    # Build attribute parameters
    params = [attr_type]

    # Add qualifiers as parameters
    if "default" in qualifiers:
        default_val = qualifiers["default"]
        if isinstance(default_val, str):
            params.append(f'default="{default_val}"')
        else:
            params.append(f"default={default_val}")

    # Add tooltip
    params.append(f'tooltip="{attr_name} attribute"')

    return f'attribute({", ".join(params)})'


def generate_class_decorator(class_name: str, metadata: Dict[str, Any]) -> str:
    """Generate @cdata_class decorator for a class."""
    class_info = metadata.get(class_name, {})
    contents = class_info.get("CONTENTS", {})

    if not contents:
        return None

    # Generate attributes dictionary
    attributes = {}
    for attr_name, attr_def in contents.items():
        attr_definition = generate_attribute_definition(attr_name, attr_def)
        attributes[attr_name] = attr_definition

    # Build decorator string
    decorator_lines = ["@cdata_class(", "    attributes={"]

    for attr_name, attr_def in attributes.items():
        decorator_lines.append(f'        "{attr_name}": {attr_def},')

    decorator_lines.extend(["    },", f'    gui_label="{class_name}",', ")"])

    return "\n".join(decorator_lines)


def find_class_definitions(file_content: str) -> List[Tuple[str, int, int]]:
    """Find all class definitions in the file content.

    Returns list of (class_name, start_line, end_line) tuples.
    """
    lines = file_content.split("\n")
    classes = []

    for i, line in enumerate(lines):
        # Look for class definitions
        class_match = re.match(r"^class\s+(\w+)\s*\([^)]*\):", line.strip())
        if class_match:
            class_name = class_match.group(1)
            start_line = i

            # Find end of class (next class or end of file)
            end_line = len(lines) - 1
            for j in range(i + 1, len(lines)):
                if re.match(r"^class\s+\w+\s*\([^)]*\):", lines[j].strip()):
                    end_line = j - 1
                    break

            classes.append((class_name, start_line, end_line))

    return classes


def remove_manual_attributes(
    class_content: str, class_name: str, metadata: Dict[str, Any]
) -> str:
    """Remove manually declared attributes that will be automatically created."""
    class_info = metadata.get(class_name, {})
    contents = class_info.get("CONTENTS", {})

    if not contents:
        return class_content

    lines = class_content.split("\n")
    filtered_lines = []

    for line in lines:
        # Skip lines that declare attributes that will be auto-created
        skip_line = False
        for attr_name in contents.keys():
            # Look for manual attribute declarations
            if re.match(rf"^\s*{attr_name}\s*:", line) or re.match(
                rf"^\s*self\.{attr_name}\s*=", line
            ):
                skip_line = True
                break

        if not skip_line:
            filtered_lines.append(line)

    return "\n".join(filtered_lines)


def has_existing_decorator(file_content: str, class_name: str) -> bool:
    """Check if class already has @cdata_class decorator."""
    lines = file_content.split("\n")

    for i, line in enumerate(lines):
        if f"class {class_name}" in line:
            # Look backwards for decorator
            for j in range(max(0, i - 10), i):
                if "@cdata_class" in lines[j]:
                    return True
            break

    return False


def process_file(file_path: Path, metadata: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Process a single class file.

    Returns (changed, messages) tuple.
    """
    if not file_path.exists():
        return False, [f"File {file_path} does not exist"]

    with open(file_path, "r") as f:
        original_content = f.read()

    content = original_content
    messages = []
    changed = False

    # Find all classes in the file
    classes = find_class_definitions(content)

    for class_name, start_line, end_line in reversed(
        classes
    ):  # Process in reverse to maintain line numbers
        if has_existing_decorator(content, class_name):
            messages.append(f"  ✓ {class_name} already has decorator")
            continue

        # Check if class has CONTENTS in metadata
        class_info = metadata.get(class_name, {})
        contents = class_info.get("CONTENTS", {})

        if not contents:
            messages.append(f"  - {class_name} has no CONTENTS in metadata")
            continue

        # Generate decorator
        decorator = generate_class_decorator(class_name, metadata)
        if not decorator:
            continue

        lines = content.split("\n")

        # Insert decorator before class definition
        class_line = start_line
        lines.insert(class_line, decorator)
        lines.insert(class_line, "")  # Add blank line before decorator

        # Update class content to remove manual attributes
        new_end_line = end_line + 2  # Account for inserted lines
        class_content = "\n".join(
            lines[class_line + 2 : new_end_line + 1]
        )  # Skip decorator lines
        filtered_class_content = remove_manual_attributes(
            class_content, class_name, metadata
        )

        # Replace class content
        lines[class_line + 2 : new_end_line + 1] = filtered_class_content.split("\n")

        content = "\n".join(lines)
        messages.append(f"  ✓ {class_name} decorated with {len(contents)} attributes")
        changed = True

    if changed:
        # Ensure proper imports
        if "@cdata_class" in content and "from .class_metadata import" not in content:
            import_line = (
                "from .class_metadata import cdata_class, attribute, AttributeType"
            )
            if "from .base_classes import CData" in content:
                content = content.replace(
                    "from .base_classes import CData",
                    f"from .base_classes import CData\n{import_line}",
                )
            else:
                # Add at the top after other imports
                lines = content.split("\n")
                for i, line in enumerate(lines):
                    if line.startswith("from ") or line.startswith("import "):
                        continue
                    else:
                        lines.insert(i, import_line)
                        lines.insert(i, "")
                        break
                content = "\n".join(lines)
            messages.append("  ✓ Added required imports")

        # Fix any incorrect imports that might have been added
        if "CDataFile, CContainer" in content:
            content = content.replace(
                "from .class_metadata import cdata_class, attribute, AttributeType, CDataFile, CContainer",
                "from .class_metadata import cdata_class, attribute, AttributeType",
            )
            messages.append("  ✓ Fixed import statement")

        # Write back to file
        with open(file_path, "w") as f:
            f.write(content)

    return changed, messages


def get_class_files_to_process() -> List[Path]:
    """Get list of class files to process."""
    base_dir = Path("/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/new_cdata")

    # Get all *_classes.py files except base_classes.py
    files = []
    for file_path in base_dir.glob("*_classes.py"):
        if file_path.name not in ["base_classes.py", "example_classes.py"]:
            files.append(file_path)

    return sorted(files)


def main():
    """Main execution function."""
    print("🔄 Starting systematic decorator update for all CData class files")
    print("=" * 70)

    # Load metadata
    print("Loading metadata...")
    try:
        metadata = load_metadata()
        print(f"✓ Loaded metadata for {len(metadata)} classes")
    except Exception as e:
        print(f"❌ Failed to load metadata: {e}")
        return

    # Get files to process
    files_to_process = get_class_files_to_process()
    print(f"Found {len(files_to_process)} class files to process\n")

    total_changed = 0
    total_classes_decorated = 0

    # Process each file
    for file_path in files_to_process:
        print(f"Processing {file_path.name}...")
        try:
            changed, messages = process_file(file_path, metadata)

            for message in messages:
                print(message)

            if changed:
                total_changed += 1
                decorated_count = len(
                    [msg for msg in messages if "decorated with" in msg]
                )
                total_classes_decorated += decorated_count
                print(f"  📝 File updated with {decorated_count} decorated classes")
            else:
                print("  - No changes needed")

        except Exception as e:
            print(f"  ❌ Error processing {file_path.name}: {e}")

        print()

    print("=" * 70)
    print(f"🎉 Processing complete!")
    print(f"✓ Files updated: {total_changed}")
    print(f"✓ Classes decorated: {total_classes_decorated}")
    print("✓ All class files now use the decorator-based metadata system")


if __name__ == "__main__":
    main()
