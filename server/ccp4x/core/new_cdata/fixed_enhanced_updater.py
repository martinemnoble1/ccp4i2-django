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


def add_enhanced_metadata_to_decorator(decorator_text, json_meta):
    """Add enhanced metadata fields to an existing decorator"""
    # Parse the existing decorator
    lines = decorator_text.split("\n")

    # Find the closing parenthesis
    close_paren_line = -1
    for i, line in enumerate(lines):
        if line.strip() == ")":
            close_paren_line = i
            break

    if close_paren_line == -1:
        return decorator_text  # Can't parse

    # Check what's already in the decorator
    decorator_content = "\n".join(lines[:close_paren_line])

    # Prepare new fields to add
    new_fields = []

    # Add contents_order if missing
    if (
        "CONTENTS_ORDER" in json_meta
        and json_meta["CONTENTS_ORDER"]
        and "contents_order=" not in decorator_content
    ):
        contents_order = str(json_meta["CONTENTS_ORDER"]).replace("'", '"')
        new_fields.append(f"contents_order={contents_order}")

    # Add qualifiers_order if missing
    if (
        "QUALIFIERS_ORDER" in json_meta
        and json_meta["QUALIFIERS_ORDER"]
        and "qualifiers_order=" not in decorator_content
    ):
        qualifiers_order = str(json_meta["QUALIFIERS_ORDER"]).replace("'", '"')
        new_fields.append(f"qualifiers_order={qualifiers_order}")

    # Add qualifiers_definition if missing
    if (
        "QUALIFIERS_DEFINITION" in json_meta
        and json_meta["QUALIFIERS_DEFINITION"]
        and "qualifiers_definition=" not in decorator_content
        and isinstance(json_meta["QUALIFIERS_DEFINITION"], dict)
    ):

        qdef_lines = ["qualifiers_definition={"]
        for key, definition in json_meta["QUALIFIERS_DEFINITION"].items():
            if isinstance(definition, dict):
                def_parts = []
                for def_key, def_value in definition.items():
                    if isinstance(def_value, str):
                        escaped_value = def_value.replace('"', '\\"').replace(
                            "\n", "\\n"
                        )
                        def_parts.append(f'"{def_key}": "{escaped_value}"')
                    else:
                        def_parts.append(f'"{def_key}": {def_value}')

                def_content = "{" + ", ".join(def_parts) + "}"
                qdef_lines.append(f'        "{key}": {def_content},')

        qdef_lines.append("    }")
        new_fields.append("\n    ".join(qdef_lines))

    if not new_fields:
        return decorator_text

    # Reconstruct the decorator
    result_lines = lines[:close_paren_line]

    # Add comma to the last existing parameter if needed
    if close_paren_line > 1 and not result_lines[-1].strip().endswith(","):
        result_lines[-1] = result_lines[-1] + ","

    # Add new fields with proper indentation and commas
    for i, field in enumerate(new_fields):
        # Add comma to all but the last field
        if i < len(new_fields) - 1:
            result_lines.append(f"    {field},")
        else:
            result_lines.append(f"    {field}")

    # Add closing parenthesis
    result_lines.append(")")

    return "\n".join(result_lines)


def update_class_decorator(file_path, class_name, json_meta):
    """Update a specific class decorator with enhanced metadata"""
    with open(file_path, "r") as f:
        content = f.read()

    # Find the class definition
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

    # Update the decorator
    new_decorator = add_enhanced_metadata_to_decorator(current_decorator, json_meta)

    if new_decorator == current_decorator:
        return False, "No changes needed"

    # Replace in content
    new_content = content.replace(current_decorator, new_decorator)

    if new_content != content:
        with open(file_path, "w") as f:
            f.write(new_content)
        return True, "Updated successfully"
    else:
        return False, "Replacement failed"


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
                and isinstance(json_meta["QUALIFIERS_DEFINITION"], dict)
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
    """Main function - FIXED VERSION"""
    print("🚀 FIXED ENHANCED METADATA UPDATER")
    print("🔧 Fixed comma placement between multiple new fields")
    print("=" * 60)

    # First, revert any broken files from previous run
    print("🔄 Reverting any files with syntax errors from previous run...")
    os.system("git checkout -- *.py")

    classes_to_update = find_classes_needing_enhanced_metadata()

    if not classes_to_update:
        print("✅ No classes need enhanced metadata updates!")
        return

    print(f"Found {len(classes_to_update)} classes needing enhanced metadata")

    updated_count = 0
    files_with_errors = []

    for file_path, class_name, json_meta in classes_to_update:
        success, message = update_class_decorator(file_path, class_name, json_meta)

        if success:
            print(f"✅ {class_name} ({file_path}): {message}")
            updated_count += 1
        else:
            print(f"⏭️  {class_name} ({file_path}): {message}")

    print(f"\n🎯 Summary: Updated {updated_count} classes")

    # Validate syntax of modified files
    modified_files = list(
        set(file_path for file_path, _, _ in classes_to_update if updated_count > 0)
    )

    print(f"\n🔍 SYNTAX VALIDATION:")
    for file_path in modified_files:
        try:
            with open(file_path, "r") as f:
                file_content = f.read()
            compile(file_content, file_path, "exec")
            print(f"✅ {file_path}: Syntax OK")
        except SyntaxError as e:
            print(f"❌ {file_path}: Syntax error at line {e.lineno}: {e.msg}")
            files_with_errors.append((file_path, e))

    if files_with_errors:
        print(f"\n⚠️  {len(files_with_errors)} files still have syntax errors")
        print("Let me know if you want to examine these further!")
    else:
        print(f"\n🎉 All {len(modified_files)} files have valid syntax!")
        print("Enhanced metadata transfer completed successfully!")


if __name__ == "__main__":
    main()
