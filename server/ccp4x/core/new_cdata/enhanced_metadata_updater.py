#!/usr/bin/env python3.12

import json
import re
import os


def load_json_metadata():
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def format_contents_order(contents_order):
    """Format contents_order list for decorator"""
    if not contents_order or not isinstance(contents_order, list):
        return None

    formatted_list = str(contents_order).replace("'", '"')
    return f"contents_order={formatted_list}"


def format_qualifiers_order(qualifiers_order):
    """Format qualifiers_order list for decorator"""
    if not qualifiers_order or not isinstance(qualifiers_order, list):
        return None

    formatted_list = str(qualifiers_order).replace("'", '"')
    return f"qualifiers_order={formatted_list}"


def format_qualifiers_definition(qualifiers_definition):
    """Format qualifiers_definition dictionary for decorator"""
    if not qualifiers_definition:
        return None

    # Handle unparseable strings
    if isinstance(qualifiers_definition, str):
        if qualifiers_definition.startswith("<Unparseable:"):
            return None
        return None

    if not isinstance(qualifiers_definition, dict):
        return None

    lines = ["qualifiers_definition={"]
    for key, definition in qualifiers_definition.items():
        if isinstance(definition, dict):
            # Format the definition dictionary
            def_parts = []
            for def_key, def_value in definition.items():
                if isinstance(def_value, str):
                    escaped_value = def_value.replace('"', '\\"').replace("\n", "\\n")
                    def_parts.append(f'"{def_key}": "{escaped_value}"')
                else:
                    def_parts.append(f'"{def_key}": {def_value}')

            def_content = "{" + ", ".join(def_parts) + "}"
            lines.append(f'        "{key}": {def_content},')
        else:
            lines.append(f'        "{key}": {definition},')

    lines.append("    }")
    return "\n    ".join(lines)


def update_decorator_with_enhanced_fields(file_path, class_name, json_meta):
    """Update a specific class decorator with enhanced fields"""
    with open(file_path, "r") as f:
        content = f.read()

    # Find the class
    class_pattern = rf"(class\s+{re.escape(class_name)}\s*\([^)]+\):)"
    class_match = re.search(class_pattern, content)

    if not class_match:
        return False, "Class not found"

    class_start = class_match.start()
    before_class = content[:class_start]

    # Find the decorator
    decorator_pattern = r"(@cdata_class\s*\([^@]*?\))\s*$"
    decorator_match = re.search(decorator_pattern, before_class, re.DOTALL)

    if not decorator_match:
        return False, "No decorator found"

    current_decorator = decorator_match.group(1)

    # Check what fields need to be added
    fields_to_add = []

    if "CONTENTS_ORDER" in json_meta and json_meta["CONTENTS_ORDER"]:
        if "contents_order=" not in current_decorator:
            contents_order_str = format_contents_order(json_meta["CONTENTS_ORDER"])
            if contents_order_str:
                fields_to_add.append(contents_order_str)

    if "QUALIFIERS_ORDER" in json_meta and json_meta["QUALIFIERS_ORDER"]:
        if "qualifiers_order=" not in current_decorator:
            qualifiers_order_str = format_qualifiers_order(
                json_meta["QUALIFIERS_ORDER"]
            )
            if qualifiers_order_str:
                fields_to_add.append(qualifiers_order_str)

    if "QUALIFIERS_DEFINITION" in json_meta and json_meta["QUALIFIERS_DEFINITION"]:
        if "qualifiers_definition=" not in current_decorator:
            qualifiers_definition_str = format_qualifiers_definition(
                json_meta["QUALIFIERS_DEFINITION"]
            )
            if qualifiers_definition_str:
                fields_to_add.append(qualifiers_definition_str)

    if not fields_to_add:
        return False, "No fields to add"

    # Modify the decorator
    # Remove the closing parenthesis and add new fields
    if current_decorator.endswith(")"):
        # Check if there are existing parameters
        if current_decorator.count("\n") > 1 or "=" in current_decorator:
            # Has existing parameters, add comma and new fields
            new_decorator = (
                current_decorator[:-1]
                + ",\n    "
                + ",\n    ".join(fields_to_add)
                + "\n)"
            )
        else:
            # No existing parameters
            new_decorator = (
                current_decorator[:-1]
                + "\n    "
                + ",\n    ".join(fields_to_add)
                + "\n)"
            )
    else:
        return False, "Unexpected decorator format"

    # Replace in content
    new_content = content.replace(current_decorator, new_decorator)

    if new_content != content:
        with open(file_path, "w") as f:
            f.write(new_content)
        return True, f"Added: {', '.join(f.split('=')[0] for f in fields_to_add)}"
    else:
        return False, "No changes made"


def find_classes_needing_enhanced_metadata():
    """Find all classes that need enhanced metadata"""
    metadata = load_json_metadata()
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    classes_to_update = []

    for file_path in py_files:
        with open(file_path, "r") as f:
            content = f.read()

        # Find all classes in this file
        class_matches = list(
            re.finditer(r"class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):", content)
        )

        for match in class_matches:
            class_name = match.group(1)

            if class_name not in metadata:
                continue

            json_meta = metadata[class_name]

            # Check if class needs any enhanced metadata
            needs_contents_order = (
                "CONTENTS_ORDER" in json_meta and json_meta["CONTENTS_ORDER"]
            )
            needs_qualifiers_order = (
                "QUALIFIERS_ORDER" in json_meta and json_meta["QUALIFIERS_ORDER"]
            )
            needs_qualifiers_definition = (
                "QUALIFIERS_DEFINITION" in json_meta
                and json_meta["QUALIFIERS_DEFINITION"]
            )

            if (
                needs_contents_order
                or needs_qualifiers_order
                or needs_qualifiers_definition
            ):
                # Check current decorator to see what's missing
                class_start = match.start()
                before_class = content[:class_start]
                decorator_pattern = r"@cdata_class\s*\([^@]*?\)\s*$"
                decorator_match = re.search(decorator_pattern, before_class, re.DOTALL)

                if decorator_match:
                    current_decorator = decorator_match.group(0)

                    missing_contents_order = (
                        needs_contents_order
                        and "contents_order=" not in current_decorator
                    )
                    missing_qualifiers_order = (
                        needs_qualifiers_order
                        and "qualifiers_order=" not in current_decorator
                    )
                    missing_qualifiers_definition = (
                        needs_qualifiers_definition
                        and "qualifiers_definition=" not in current_decorator
                    )

                    if (
                        missing_contents_order
                        or missing_qualifiers_order
                        or missing_qualifiers_definition
                    ):
                        classes_to_update.append((file_path, class_name, json_meta))

    return classes_to_update


def main():
    """Main function"""
    print("🚀 ENHANCED METADATA UPDATER")
    print("Adding CONTENTS_ORDER, QUALIFIERS_ORDER, and QUALIFIERS_DEFINITION")
    print("=" * 65)

    classes_to_update = find_classes_needing_enhanced_metadata()

    if not classes_to_update:
        print("✅ No classes need enhanced metadata updates!")
        return

    print(f"Found {len(classes_to_update)} classes needing enhanced metadata")

    updated_count = 0

    for file_path, class_name, json_meta in classes_to_update:
        success, message = update_decorator_with_enhanced_fields(
            file_path, class_name, json_meta
        )

        if success:
            print(f"✅ {class_name} ({file_path}): {message}")
            updated_count += 1
        else:
            print(f"❌ {class_name} ({file_path}): {message}")

    print(f"\n🎯 Summary: Updated {updated_count} classes")

    # Validate syntax of modified files
    modified_files = list(
        set(file_path for file_path, _, _ in classes_to_update if updated_count > 0)
    )

    for file_path in modified_files:
        try:
            with open(file_path, "r") as f:
                compile(f.read(), file_path, "exec")
            print(f"✅ {file_path}: Syntax OK")
        except SyntaxError as e:
            print(f"❌ {file_path}: Syntax error - {e}")


if __name__ == "__main__":
    main()
