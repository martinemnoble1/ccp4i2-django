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
        # Add more mappings as needed
    }
    return mapping.get(ccp4_type, "AttributeType.STRING")


def format_qualifiers(qualifiers):
    """Format qualifiers dictionary for decorator"""
    if not qualifiers:
        return ""

    # Handle both dict and string cases
    if isinstance(qualifiers, str):
        # Skip unparseable qualifiers
        if qualifiers.startswith("<Unparseable:"):
            return ""
        return ""

    if not isinstance(qualifiers, dict):
        return ""

    lines = ["    qualifiers={"]
    for key, value in qualifiers.items():
        if value is None:
            lines.append(f'        "{key}": None,')
        elif isinstance(value, str):
            lines.append(f'        "{key}": "{value}",')
        elif isinstance(value, list):
            lines.append(f'        "{key}": {value},')
        else:
            lines.append(f'        "{key}": {value},')
    lines.append("    },")
    return "\n".join(lines)


def format_error_codes(error_codes):
    """Format error codes dictionary for decorator"""
    if not error_codes:
        return ""

    # Handle both dict and string cases
    if isinstance(error_codes, str):
        # Skip unparseable error codes
        if error_codes.startswith("<Unparseable:"):
            return ""
        return ""

    if not isinstance(error_codes, dict):
        return ""

    lines = ["    error_codes={"]
    for code, info in error_codes.items():
        if isinstance(info, dict) and "description" in info:
            description = info["description"]
        else:
            description = str(info)
        lines.append(f'        "{code}": "{description}",')
    lines.append("    },")
    return "\n".join(lines)


def format_attributes(contents):
    """Format attributes from CONTENTS for decorator"""
    if not contents:
        return ""

    # Handle both dict and string cases
    if isinstance(contents, str):
        # Skip unparseable contents
        if contents.startswith("<Unparseable:"):
            return ""
        return ""

    if not isinstance(contents, dict):
        return ""

    lines = ["    attributes={"]
    for attr_name, attr_info in contents.items():
        attr_type = map_ccp4_type_to_attribute_type(
            attr_info.get("class", "CCP4Data.CString")
        )

        # Get tooltip from qualifiers if available
        tooltip = attr_name + " attribute"  # default
        if "qualifiers" in attr_info and "toolTip" in attr_info["qualifiers"]:
            tooltip = attr_info["qualifiers"]["toolTip"]

        if "custom_class=" in attr_type:
            lines.append(
                f'        "{attr_name}": attribute({attr_type}, tooltip="{tooltip}"),'
            )
        else:
            lines.append(
                f'        "{attr_name}": attribute({attr_type}, tooltip="{tooltip}"),'
            )
    lines.append("    },")
    return "\n".join(lines)


def create_decorator(class_name, metadata):
    """Create @cdata_class decorator string from metadata"""
    parts = []

    # Add qualifiers
    if "QUALIFIERS" in metadata and metadata["QUALIFIERS"]:
        parts.append(format_qualifiers(metadata["QUALIFIERS"]))

    # Add attributes from CONTENTS
    if "CONTENTS" in metadata and metadata["CONTENTS"]:
        parts.append(format_attributes(metadata["CONTENTS"]))

    # Add error_codes
    if "ERROR_CODES" in metadata and metadata["ERROR_CODES"]:
        parts.append(format_error_codes(metadata["ERROR_CODES"]))

    if not parts:
        return ""

    decorator_content = ",\n".join(parts)
    return f"@cdata_class(\n{decorator_content}\n)"


def find_classes_without_decorators(file_path):
    """Find classes in a file that don't have @cdata_class decorators"""
    with open(file_path, "r") as f:
        content = f.read()

    # Find all class definitions
    class_matches = re.finditer(r"class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):", content)
    classes_without_decorators = []

    for match in class_matches:
        class_name = match.group(1)
        class_start = match.start()

        # Check if there's a @cdata_class decorator before this class
        before_class = content[:class_start]
        # Look for @cdata_class in the last 500 characters before the class
        recent_before = before_class[-500:]
        if "@cdata_class" not in recent_before:
            # Find the line number
            line_num = content[:class_start].count("\n") + 1
            classes_without_decorators.append(
                {"name": class_name, "line": line_num, "match": match}
            )

    return classes_without_decorators


def add_decorator_to_class(file_path, class_info, decorator_str):
    """Add decorator to a specific class in a file"""
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Find the class line (convert to 0-based index)
    class_line_idx = class_info["line"] - 1

    # Find the right place to insert decorator (before any existing decorators or the class)
    insert_idx = class_line_idx

    # Look backwards to find where to insert (skip empty lines and comments)
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


def main():
    """Main function to add decorators systematically"""
    # Load JSON metadata
    print("Loading JSON metadata...")
    metadata = load_json_metadata()
    print(f"Loaded metadata for {len(metadata)} classes")

    # Get all Python class files
    class_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_added = 0

    for file_path in class_files:
        print(f"\nProcessing {file_path}...")

        # Find classes without decorators
        classes_without_decorators = find_classes_without_decorators(file_path)

        if not classes_without_decorators:
            print(f"  No classes need decorators in {file_path}")
            continue

        print(f"  Found {len(classes_without_decorators)} classes without decorators")

        # Process each class that needs a decorator
        classes_processed = []
        for class_info in classes_without_decorators:
            class_name = class_info["name"]

            if class_name in metadata:
                class_metadata = metadata[class_name]

                # Check if this class actually has metadata to add
                has_qualifiers = (
                    "QUALIFIERS" in class_metadata and class_metadata["QUALIFIERS"]
                )
                has_contents = (
                    "CONTENTS" in class_metadata and class_metadata["CONTENTS"]
                )
                has_error_codes = (
                    "ERROR_CODES" in class_metadata and class_metadata["ERROR_CODES"]
                )

                if has_qualifiers or has_contents or has_error_codes:
                    decorator_str = create_decorator(class_name, class_metadata)
                    if decorator_str:
                        print(f"    Adding decorator to {class_name}")
                        classes_processed.append((class_info, decorator_str))
                    else:
                        print(f"    Skipping {class_name} - no valid metadata")
                else:
                    print(f"    Skipping {class_name} - no metadata in JSON")
            else:
                print(f"    Skipping {class_name} - not found in JSON metadata")

        # Add decorators in reverse order (so line numbers stay valid)
        for class_info, decorator_str in reversed(classes_processed):
            add_decorator_to_class(file_path, class_info, decorator_str)
            total_added += 1

        print(f"  Added {len(classes_processed)} decorators to {file_path}")

    print(f"\n✅ Total decorators added: {total_added}")

    # Verify syntax of all modified files
    print("\n🔍 Verifying syntax of modified files...")
    for file_path in class_files:
        try:
            with open(file_path, "r") as f:
                compile(f.read(), file_path, "exec")
            print(f"  ✅ {file_path} - syntax OK")
        except SyntaxError as e:
            print(f"  ❌ {file_path} - syntax error: {e}")


if __name__ == "__main__":
    main()
