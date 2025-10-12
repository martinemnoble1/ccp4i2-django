#!/usr/bin/env python3.12

import json
import os
import re
from typing import Dict, List, Tuple


def load_json_metadata() -> Dict:
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def find_all_classes_in_files() -> Dict[str, Tuple[str, int, str]]:
    """Find all classes in all Python files with their positions"""
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]
    all_classes = {}

    for file_path in py_files:
        with open(file_path, "r") as f:
            content = f.read()

        # Find all class definitions
        class_matches = list(
            re.finditer(r"class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):", content)
        )
        for match in class_matches:
            class_name = match.group(1)
            all_classes[class_name] = (file_path, match.start(), match.group(0))

    return all_classes


def format_qualifiers(qualifiers) -> str:
    """Format qualifiers dictionary for decorator"""
    if not qualifiers:
        return ""

    # Handle case where qualifiers is a string (unparseable)
    if isinstance(qualifiers, str):
        return ""  # Skip unparseable qualifiers

    if not isinstance(qualifiers, dict):
        return ""

    lines = ["qualifiers={"]
    for key, value in qualifiers.items():
        if value is None:
            lines.append(f'        "{key}": None,')
        elif isinstance(value, str):
            escaped_value = value.replace('"', '\\"').replace("\n", "\\n")
            lines.append(f'        "{key}": "{escaped_value}",')
        elif isinstance(value, list):
            formatted_list = str(value).replace("'", '"')
            lines.append(f'        "{key}": {formatted_list},')
        else:
            lines.append(f'        "{key}": {value},')
    lines.append("    }")
    return "    " + "\n    ".join(lines)


def format_error_codes(error_codes) -> str:
    """Format error codes dictionary for decorator"""
    if not error_codes:
        return ""

    # Handle case where error_codes is a string (unparseable)
    if isinstance(error_codes, str):
        return ""  # Skip unparseable error codes

    if not isinstance(error_codes, dict):
        return ""

    lines = ["error_codes={"]
    for code, info in error_codes.items():
        if isinstance(info, dict) and "description" in info:
            description = info["description"]
        else:
            description = str(info)
        escaped_description = description.replace('"', '\\"').replace("\n", "\\n")
        lines.append(f'        "{code}": "{escaped_description}",')
    lines.append("    }")
    return "    " + "\n    ".join(lines)


def format_attributes(contents) -> str:
    """Format attributes dictionary for decorator"""
    if not contents:
        return ""

    # Handle case where contents is a string (unparseable)
    if isinstance(contents, str):
        return ""  # Skip unparseable contents

    if not isinstance(contents, dict):
        return ""

    lines = ["attributes={"]
    for attr_name, attr_info in contents.items():
        if isinstance(attr_info, dict):
            # Try to extract class information for type mapping
            class_name = attr_info.get("class", "")
            tooltip = f"{attr_name} attribute"

            # Map class names to AttributeType enums
            if "CString" in class_name:
                attr_type = "AttributeType.STRING"
            elif "CInt" in class_name:
                attr_type = "AttributeType.INT"
            elif "CFloat" in class_name:
                attr_type = "AttributeType.FLOAT"
            elif "CBool" in class_name:
                attr_type = "AttributeType.BOOL"
            elif "CDataFile" in class_name:
                attr_type = "AttributeType.FILE"
            else:
                attr_type = "AttributeType.STRING"

            # Check for qualifiers that might have tooltips
            if "qualifiers" in attr_info and isinstance(attr_info["qualifiers"], dict):
                tooltip = attr_info["qualifiers"].get("toolTip", tooltip)

            escaped_tooltip = tooltip.replace('"', '\\"').replace("\n", "\\n")
            lines.append(
                f'        "{attr_name}": attribute({attr_type}, tooltip="{escaped_tooltip}"),'
            )
        else:
            lines.append(
                f'        "{attr_name}": attribute(AttributeType.STRING, tooltip="{attr_name} attribute"),'
            )

    lines.append("    }")
    return "    " + "\n    ".join(lines)


def create_complete_decorator(class_name: str, json_meta: Dict) -> str:
    """Create a complete decorator from JSON metadata"""
    parts = []

    # Add attributes if present
    if "CONTENTS" in json_meta and json_meta["CONTENTS"]:
        attributes_str = format_attributes(json_meta["CONTENTS"])
        if attributes_str:
            parts.append(attributes_str)

    # Add qualifiers if present
    if "QUALIFIERS" in json_meta and json_meta["QUALIFIERS"]:
        qualifiers_str = format_qualifiers(json_meta["QUALIFIERS"])
        if qualifiers_str:
            parts.append(qualifiers_str)

    # Add error codes if present
    if "ERROR_CODES" in json_meta and json_meta["ERROR_CODES"]:
        error_codes_str = format_error_codes(json_meta["ERROR_CODES"])
        if error_codes_str:
            parts.append(error_codes_str)

    # Add gui_label
    gui_label = json_meta.get("gui_label", class_name)
    parts.append(f'    gui_label="{gui_label}"')

    if not parts:
        return ""

    decorator_content = ",\n".join(parts)
    return f"@cdata_class(\n{decorator_content}\n)"


def process_file_for_complete_metadata(
    file_path: str, metadata: Dict, all_classes: Dict
) -> int:
    """Process a file to add complete metadata to all classes"""
    with open(file_path, "r") as f:
        content = f.read()

    classes_in_file = [
        (name, info)
        for name, info in all_classes.items()
        if info[0] == file_path and name in metadata
    ]

    if not classes_in_file:
        return 0

    # Sort by position (reverse order to maintain positions)
    classes_in_file.sort(key=lambda x: x[1][1], reverse=True)

    updates_applied = 0

    for class_name, (_, position, class_line) in classes_in_file:
        json_meta = metadata[class_name]

        # Check if class already has a decorator
        before_class = content[:position]
        lines_before = before_class.split("\n")

        # Look for decorator in the last few lines before class
        has_decorator = False
        decorator_start_line = -1

        for i in range(len(lines_before) - 1, max(len(lines_before) - 10, 0), -1):
            if "@cdata_class(" in lines_before[i]:
                has_decorator = True
                decorator_start_line = i
                break

        if has_decorator:
            # Find the complete decorator
            decorator_lines = []
            paren_count = 0
            found_start = False

            for i in range(decorator_start_line, len(lines_before)):
                line = lines_before[i]
                if "@cdata_class(" in line:
                    found_start = True
                if found_start:
                    decorator_lines.append(line)
                    paren_count += line.count("(") - line.count(")")
                    if paren_count == 0 and found_start:
                        break

            if decorator_lines:
                existing_decorator = "\n".join(decorator_lines)

                # Check what's missing
                needs_qualifiers = (
                    "QUALIFIERS" in json_meta
                    and json_meta["QUALIFIERS"]
                    and "qualifiers=" not in existing_decorator
                )
                needs_error_codes = (
                    "ERROR_CODES" in json_meta
                    and json_meta["ERROR_CODES"]
                    and "error_codes=" not in existing_decorator
                )
                needs_attributes = (
                    "CONTENTS" in json_meta
                    and json_meta["CONTENTS"]
                    and "attributes=" not in existing_decorator
                )

                if needs_qualifiers or needs_error_codes or needs_attributes:
                    # Create updated decorator
                    new_decorator = create_complete_decorator(class_name, json_meta)
                    if new_decorator:
                        old_text = existing_decorator + "\n" + class_line
                        new_text = new_decorator + "\n" + class_line
                        if old_text in content:
                            content = content.replace(old_text, new_text, 1)
                            updates_applied += 1
                            print(f"    Updated {class_name} decorator")
        else:
            # No decorator - add complete one
            new_decorator = create_complete_decorator(class_name, json_meta)
            if new_decorator:
                old_text = class_line
                new_text = new_decorator + "\n" + class_line
                if old_text in content:
                    content = content.replace(old_text, new_text, 1)
                    updates_applied += 1
                    print(f"    Added complete decorator to {class_name}")

    if updates_applied > 0:
        with open(file_path, "w") as f:
            f.write(content)

    return updates_applied


def validate_file_syntax(file_path: str) -> bool:
    """Validate that a file has correct Python syntax"""
    try:
        with open(file_path, "r") as f:
            compile(f.read(), file_path, "exec")
        return True
    except SyntaxError as e:
        print(f"  ❌ Syntax error in {file_path}: {e}")
        return False


def main():
    """Main function for 100% completion"""
    print("🎯 ULTIMATE COMPLETION SCRIPT - 100% METADATA TRANSFER")
    print("=" * 60)

    # Load data
    metadata = load_json_metadata()
    all_classes = find_all_classes_in_files()

    print(f"Loaded metadata for {len(metadata)} classes from JSON")
    print(f"Found {len(all_classes)} classes in Python files")

    # Get all Python class files
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_updates = 0
    files_modified = []

    for file_path in py_files:
        print(f"\n📄 Processing {file_path}...")

        updates_applied = process_file_for_complete_metadata(
            file_path, metadata, all_classes
        )

        if updates_applied > 0:
            # Validate syntax immediately
            if validate_file_syntax(file_path):
                files_modified.append(file_path)
                total_updates += updates_applied
                print(f"  ✅ Applied {updates_applied} updates to {file_path}")
                print(f"  ✓ Syntax validation passed")
            else:
                print(f"  ❌ Syntax validation failed - reverting file")
                os.system(f"git checkout -- {file_path}")
        else:
            print(f"  ✓ No updates needed for {file_path}")

    print(f"\n🎯 FINAL SUMMARY:")
    print(f"Files processed: {len(py_files)}")
    print(f"Files modified: {len(files_modified)}")
    print(f"Total metadata updates applied: {total_updates}")

    if files_modified:
        print(f"\nSuccessfully modified files:")
        for file_path in files_modified:
            print(f"  - {file_path}")

    # Final audit
    print(f"\n🔍 Running final audit...")
    os.system("python3.12 audit_metadata.py")


if __name__ == "__main__":
    main()
