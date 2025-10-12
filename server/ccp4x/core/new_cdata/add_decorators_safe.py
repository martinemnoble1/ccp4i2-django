#!/usr/bin/env python3.12

import json
import os
import re
from pathlib import Path


def load_json_metadata():
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def map_ccp4_type_to_attribute_type(ccp4_type):
    """Map CCP4Data types to AttributeType values"""
    mapping = {
        "CCP4Data.CString": "AttributeType.STRING",
        "CCP4Data.CInt": "AttributeType.INT",
        "CCP4Data.CFloat": "AttributeType.FLOAT",
        "CCP4Data.COneWord": 'AttributeType.CUSTOM, custom_class="COneWord"',
        "CCP4Data.CBoolean": "AttributeType.BOOLEAN",
        "CCP4Data.CList": "AttributeType.LIST",
    }
    return mapping.get(ccp4_type, "AttributeType.STRING")


def create_simple_decorator(class_name, metadata):
    """Create a simple @cdata_class decorator from metadata"""
    decorator_parts = []

    # Handle QUALIFIERS (only if it's a proper dict)
    if (
        "QUALIFIERS" in metadata
        and isinstance(metadata["QUALIFIERS"], dict)
        and metadata["QUALIFIERS"]
    ):
        qualifiers_str = "qualifiers={\n"
        for key, value in metadata["QUALIFIERS"].items():
            if value is None:
                qualifiers_str += f'        "{key}": None,\n'
            elif isinstance(value, str):
                qualifiers_str += f'        "{key}": "{value}",\n'
            elif isinstance(value, list):
                qualifiers_str += f'        "{key}": {value},\n'
            else:
                qualifiers_str += f'        "{key}": {value},\n'
        qualifiers_str += "    }"
        decorator_parts.append(qualifiers_str)

    # Handle ERROR_CODES (only if it's a proper dict)
    if (
        "ERROR_CODES" in metadata
        and isinstance(metadata["ERROR_CODES"], dict)
        and metadata["ERROR_CODES"]
    ):
        error_codes_str = "error_codes={\n"
        for code, info in metadata["ERROR_CODES"].items():
            if isinstance(info, dict) and "description" in info:
                description = info["description"]
            else:
                description = str(info)
            error_codes_str += f'        "{code}": "{description}",\n'
        error_codes_str += "    }"
        decorator_parts.append(error_codes_str)

    # Handle CONTENTS as attributes (only if it's a proper dict)
    if (
        "CONTENTS" in metadata
        and isinstance(metadata["CONTENTS"], dict)
        and metadata["CONTENTS"]
    ):
        attributes_str = "attributes={\n"
        for attr_name, attr_info in metadata["CONTENTS"].items():
            attr_type = map_ccp4_type_to_attribute_type(
                attr_info.get("class", "CCP4Data.CString")
            )
            tooltip = attr_name + " attribute"  # default
            if (
                isinstance(attr_info, dict)
                and "qualifiers" in attr_info
                and "toolTip" in attr_info["qualifiers"]
            ):
                tooltip = attr_info["qualifiers"]["toolTip"]
            attributes_str += (
                f'        "{attr_name}": attribute({attr_type}, tooltip="{tooltip}"),\n'
            )
        attributes_str += "    }"
        decorator_parts.append(attributes_str)

    if not decorator_parts:
        return None

    # Combine all parts
    decorator_content = ",\n    ".join(decorator_parts)
    return f"@cdata_class(\n    {decorator_content}\n)"


def find_classes_needing_decorators():
    """Find all classes that need decorators added"""
    metadata = load_json_metadata()

    # Get all Python class files
    class_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    classes_to_process = []

    for file_path in class_files:
        with open(file_path, "r") as f:
            content = f.read()

        # Find all class definitions that don't have @cdata_class decorators
        lines = content.split("\n")
        for i, line in enumerate(lines):
            class_match = re.match(
                r"\s*class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):", line
            )
            if class_match:
                class_name = class_match.group(1)

                # Check if this class has metadata
                if class_name in metadata:
                    class_metadata = metadata[class_name]

                    # Check if it has any useful metadata
                    has_qualifiers = (
                        "QUALIFIERS" in class_metadata
                        and isinstance(class_metadata["QUALIFIERS"], dict)
                        and class_metadata["QUALIFIERS"]
                    )
                    has_contents = (
                        "CONTENTS" in class_metadata
                        and isinstance(class_metadata["CONTENTS"], dict)
                        and class_metadata["CONTENTS"]
                    )
                    has_error_codes = (
                        "ERROR_CODES" in class_metadata
                        and isinstance(class_metadata["ERROR_CODES"], dict)
                        and class_metadata["ERROR_CODES"]
                    )

                    if has_qualifiers or has_contents or has_error_codes:
                        # Check if this class already has a decorator
                        has_decorator = False
                        # Look backwards from the class line to see if there's a decorator
                        for j in range(max(0, i - 10), i):
                            if "@cdata_class" in lines[j]:
                                has_decorator = True
                                break

                        if not has_decorator:
                            classes_to_process.append(
                                {
                                    "file": file_path,
                                    "class_name": class_name,
                                    "line_num": i + 1,
                                    "metadata": class_metadata,
                                }
                            )

    return classes_to_process


def add_decorator_safely(file_path, class_name, line_num, decorator_str):
    """Add decorator to a class safely"""
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Find the exact class line (convert to 0-based index)
    class_line_idx = line_num - 1

    # Verify we're at the right class
    if not re.search(rf"class\s+{re.escape(class_name)}\s*\(", lines[class_line_idx]):
        print(
            f"  Warning: Could not find class {class_name} at expected line {line_num}"
        )
        return False

    # Find the right place to insert decorator (before the class line)
    insert_idx = class_line_idx

    # Look backwards to skip empty lines and comments but stop at other code
    while insert_idx > 0:
        prev_line = lines[insert_idx - 1].strip()
        if prev_line == "" or prev_line.startswith("#"):
            insert_idx -= 1
        else:
            break

    # Insert the decorator
    decorator_lines = [line + "\n" for line in decorator_str.split("\n")]
    for i, line in enumerate(decorator_lines):
        lines.insert(insert_idx + i, line)

    # Write back to file
    with open(file_path, "w") as f:
        f.writelines(lines)

    return True


def main():
    """Main function to add decorators systematically"""
    print("🔍 Finding classes that need decorators...")
    classes_to_process = find_classes_needing_decorators()

    print(f"Found {len(classes_to_process)} classes that need decorators")

    # Group by file for better reporting
    files_processed = {}

    for class_info in classes_to_process:
        file_path = class_info["file"]
        class_name = class_info["class_name"]
        line_num = class_info["line_num"]
        metadata = class_info["metadata"]

        # Create decorator
        decorator_str = create_simple_decorator(class_name, metadata)
        if not decorator_str:
            continue

        print(f"  Adding decorator to {class_name} in {file_path}")

        success = add_decorator_safely(file_path, class_name, line_num, decorator_str)
        if success:
            if file_path not in files_processed:
                files_processed[file_path] = 0
            files_processed[file_path] += 1

    print(f"\n✅ Summary:")
    total_added = 0
    for file_path, count in files_processed.items():
        print(f"  {file_path}: {count} decorators added")
        total_added += count

    print(f"\n🎯 Total decorators added: {total_added}")

    # Verify syntax of modified files
    print(f"\n🔍 Verifying syntax of modified files...")
    for file_path in files_processed.keys():
        try:
            with open(file_path, "r") as f:
                compile(f.read(), file_path, "exec")
            print(f"  ✅ {file_path} - syntax OK")
        except SyntaxError as e:
            print(f"  ❌ {file_path} - syntax error: {e}")


if __name__ == "__main__":
    main()
