"""Automatic decorator application script.

This script reads the JSON metadata and applies @cdata_class decorators
to all classes that have CONTENTS defined in the metadata.
"""

import json
import re
from typing import Dict, Any, List, Tuple
from pathlib import Path


def load_metadata() -> Dict[str, Any]:
    """Load the JSON metadata."""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        return json.load(f)


def map_class_to_attribute_type(class_name: str) -> str:
    """Map JSON class names to our AttributeType enum values."""
    # Clean up class name
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
        # For custom classes (like CXyz, CAngle, etc.), use custom type
        return f'AttributeType.CUSTOM, custom_class="{clean_name}"'


def generate_attribute_definition(attr_name: str, attr_def: Dict[str, Any]) -> str:
    """Generate an attribute definition string."""
    class_name = attr_def.get("class", "CCP4Data.CString")
    qualifiers = attr_def.get("qualifiers", {})

    # Map to attribute type
    if "." in class_name and class_name.split(".")[-1] in [
        "CInt",
        "CFloat",
        "CBoolean",
        "CBool",
        "CString",
        "CFilePath",
        "CProjectId",
        "CUUID",
        "CJobTitle",
    ]:
        attr_type = map_class_to_attribute_type(class_name)
        params = [attr_type]
    else:
        # Custom class
        clean_class = class_name.split(".")[-1]
        params = [f'AttributeType.CUSTOM, custom_class="{clean_class}"']

    # Add qualifiers as parameters
    if "default" in qualifiers:
        default_val = qualifiers["default"]
        if isinstance(default_val, str):
            params.append(f'default="{default_val}"')
        else:
            params.append(f"default={default_val}")

    if "min" in qualifiers:
        params.append(f'min_value={qualifiers["min"]}')

    if "max" in qualifiers:
        params.append(f'max_value={qualifiers["max"]}')

    if "fileExtensions" in qualifiers:
        extensions = qualifiers["fileExtensions"]
        params.append(f"file_extensions={extensions}")

    # Add tooltip
    tooltip = f'tooltip="{attr_name} attribute"'
    params.append(tooltip)

    param_str = ", ".join(params)
    return f"'{attr_name}': attribute({param_str})"


def generate_decorator_for_class(class_name: str, class_info: Dict[str, Any]) -> str:
    """Generate @cdata_class decorator for a class."""
    contents = class_info.get("CONTENTS", {})
    if not contents:
        return None

    # Generate attribute definitions
    attr_definitions = []
    for attr_name, attr_def in contents.items():
        attr_def_str = generate_attribute_definition(attr_name, attr_def)
        attr_definitions.append(f"        {attr_def_str}")

    # Generate decorator with proper comma separation
    decorator_lines = ["@cdata_class(", "    attributes={"]
    # Add commas between attributes
    for i, attr_def in enumerate(attr_definitions):
        if i < len(attr_definitions) - 1:
            decorator_lines.append(attr_def + ",")
        else:
            decorator_lines.append(attr_def)

    decorator_lines.extend(["    },", f'    gui_label="{class_name}"', ")"])

    return "\n".join(decorator_lines)


def update_class_file(file_path: str, metadata: Dict[str, Any]) -> bool:
    """Update a class file with decorators."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Check if imports are already present
        if "from .class_metadata import" not in content:
            # Add imports at the top after existing imports
            import_line = (
                "from .class_metadata import cdata_class, attribute, AttributeType\n"
            )

            # Find the last import line
            lines = content.split("\n")
            last_import_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("from ") or line.startswith("import "):
                    last_import_idx = i

            lines.insert(last_import_idx + 1, import_line.rstrip())
            content = "\n".join(lines)

        # Find class definitions and add decorators
        modified = False
        class_pattern = r"^class (\w+)\([^)]*\):"

        lines = content.split("\n")
        new_lines = []
        i = 0

        while i < len(lines):
            line = lines[i]
            match = re.match(class_pattern, line)

            if match:
                class_name = match.group(1)

                # Check if this class has metadata
                if (
                    class_name in metadata["classes"]
                    and "CONTENTS" in metadata["classes"][class_name]
                ):
                    # Check if decorator already exists
                    if i > 0 and "@cdata_class" in lines[i - 1]:
                        # Decorator already exists, skip
                        new_lines.append(line)
                    else:
                        # Generate and add decorator
                        decorator = generate_decorator_for_class(
                            class_name, metadata["classes"][class_name]
                        )
                        if decorator:
                            new_lines.append(decorator)
                            modified = True
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

            i += 1

        if modified:
            # Write back the file
            new_content = "\n".join(new_lines)
            with open(file_path, "w") as f:
                f.write(new_content)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to update all class files."""
    print("Loading metadata...")
    metadata = load_metadata()

    # Define files to update
    base_dir = Path("/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/new_cdata")
    class_files = [
        "ccp4mathsdata_classes.py",
        "ccp4modeldata_classes.py",
        "ccp4xtaldata_classes.py",
        "ccp4file_classes.py",
        # Add more files as needed
    ]

    print(
        f"Found {len([c for c in metadata['classes'].values() if 'CONTENTS' in c])} classes with CONTENTS"
    )
    print()

    for file_name in class_files:
        file_path = base_dir / file_name
        if file_path.exists():
            print(f"Processing {file_name}...")
            updated = update_class_file(str(file_path), metadata)
            if updated:
                print(f"  ✓ Updated with decorators")
            else:
                print(f"  - No changes needed")
        else:
            print(f"  ✗ File not found: {file_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
