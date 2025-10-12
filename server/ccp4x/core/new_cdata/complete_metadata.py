#!/usr/bin/env python3.12

import os
import re
import json


def load_json_metadata():
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def find_classes_missing_metadata():
    """Find classes that have decorators but are missing metadata"""
    metadata = load_json_metadata()
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    missing_metadata_classes = []

    for file in py_files:
        with open(file, "r") as f:
            content = f.read()

        # Find all classes with decorators
        decorator_matches = re.finditer(
            r"(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)",
            content,
            re.DOTALL,
        )

        for match in decorator_matches:
            decorator_text = match.group(1)
            class_line = match.group(2)
            class_name = match.group(3)

            if class_name in metadata:
                json_meta = metadata[class_name]

                has_qualifiers = "qualifiers=" in decorator_text
                has_error_codes = "error_codes=" in decorator_text

                should_have_qualifiers = (
                    "QUALIFIERS" in json_meta
                    and isinstance(json_meta["QUALIFIERS"], dict)
                    and json_meta["QUALIFIERS"]
                )
                should_have_error_codes = (
                    "ERROR_CODES" in json_meta
                    and isinstance(json_meta["ERROR_CODES"], dict)
                    and json_meta["ERROR_CODES"]
                )

                missing_qualifiers = should_have_qualifiers and not has_qualifiers
                missing_error_codes = should_have_error_codes and not has_error_codes

                if missing_qualifiers or missing_error_codes:
                    missing_metadata_classes.append(
                        {
                            "file": file,
                            "class_name": class_name,
                            "full_match": match,
                            "missing_qualifiers": missing_qualifiers,
                            "missing_error_codes": missing_error_codes,
                            "json_qualifiers": (
                                json_meta.get("QUALIFIERS")
                                if missing_qualifiers
                                else None
                            ),
                            "json_error_codes": (
                                json_meta.get("ERROR_CODES")
                                if missing_error_codes
                                else None
                            ),
                        }
                    )

    return missing_metadata_classes


def format_qualifiers(qualifiers):
    """Format qualifiers for decorator"""
    if not qualifiers or not isinstance(qualifiers, dict):
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
    """Format error codes for decorator"""
    if not error_codes or not isinstance(error_codes, dict):
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


def add_missing_metadata_to_decorator(file_path, class_info):
    """Add missing metadata to an existing decorator"""
    with open(file_path, "r") as f:
        content = f.read()

    old_decorator = class_info["full_match"].group(1)
    class_line = class_info["full_match"].group(2)

    # Parse the existing decorator to find where to insert new metadata
    decorator_content = old_decorator[
        old_decorator.find("(") + 1 : old_decorator.rfind(")")
    ]

    # Add missing metadata
    new_parts = []

    # Add qualifiers if missing
    if class_info["missing_qualifiers"]:
        qualifiers_str = format_qualifiers(class_info["json_qualifiers"])
        if qualifiers_str:
            new_parts.append(qualifiers_str.strip())

    # Add error_codes if missing
    if class_info["missing_error_codes"]:
        error_codes_str = format_error_codes(class_info["json_error_codes"])
        if error_codes_str:
            new_parts.append(error_codes_str.strip())

    if new_parts:
        # Combine existing and new metadata
        if decorator_content.strip():
            # There's existing content, add comma and new parts
            new_decorator_content = decorator_content + ",\n" + ",\n".join(new_parts)
        else:
            # Empty decorator, just add new parts
            new_decorator_content = "\n" + ",\n".join(new_parts) + "\n"

        new_decorator = f"@cdata_class(\n{new_decorator_content}\n)"

        # Replace in content
        old_full = old_decorator + "\n" + class_line
        new_full = new_decorator + "\n" + class_line

        new_content = content.replace(old_full, new_full)

        # Write back
        with open(file_path, "w") as f:
            f.write(new_content)

        return True

    return False


def main():
    """Main function to add missing metadata"""
    print("Finding classes with missing metadata...")
    missing_classes = find_classes_missing_metadata()

    print(f"Found {len(missing_classes)} classes missing metadata")

    # Group by file
    files_to_process = {}
    for class_info in missing_classes:
        file = class_info["file"]
        if file not in files_to_process:
            files_to_process[file] = []
        files_to_process[file].append(class_info)

    total_fixed = 0

    for file, classes in files_to_process.items():
        print(f"\nProcessing {file} ({len(classes)} classes)...")

        # Sort by position in file (reverse order so we don't mess up positions)
        classes.sort(key=lambda x: x["full_match"].start(), reverse=True)

        file_fixed = 0
        for class_info in classes:
            class_name = class_info["class_name"]
            missing_qual = class_info["missing_qualifiers"]
            missing_err = class_info["missing_error_codes"]

            print(f"  Adding to {class_name}: ", end="")
            if missing_qual:
                print("qualifiers ", end="")
            if missing_err:
                print("error_codes ", end="")

            if add_missing_metadata_to_decorator(file, class_info):
                file_fixed += 1
                total_fixed += 1
                print("✅")
            else:
                print("❌")

        print(f"  Fixed {file_fixed} classes in {file}")

    print(f"\n🎯 Total classes fixed: {total_fixed}")

    # Verify syntax
    if total_fixed > 0:
        print(f"\n🔍 Verifying syntax...")
        for file in files_to_process.keys():
            try:
                with open(file, "r") as f:
                    compile(f.read(), file, "exec")
                print(f"  ✅ {file} - syntax OK")
            except SyntaxError as e:
                print(f"  ❌ {file} - syntax error: {e}")


if __name__ == "__main__":
    main()
