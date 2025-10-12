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
    if not qualifiers or not isinstance(qualifiers, dict):
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
    if not error_codes or isinstance(error_codes, str):
        return ""

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
    if not contents or isinstance(contents, str):
        return ""

    if not isinstance(contents, dict):
        return ""

    lines = ["attributes={"]
    for attr_name, attr_info in contents.items():
        if isinstance(attr_info, dict):
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


def format_contents_order(contents_order) -> str:
    """Format contents_order list for decorator"""
    if not contents_order or not isinstance(contents_order, list):
        return ""

    formatted_list = str(contents_order).replace("'", '"')
    return f"    contents_order={formatted_list}"


def format_qualifiers_order(qualifiers_order) -> str:
    """Format qualifiers_order list for decorator"""
    if not qualifiers_order or not isinstance(qualifiers_order, list):
        return ""

    formatted_list = str(qualifiers_order).replace("'", '"')
    return f"    qualifiers_order={formatted_list}"


def format_qualifiers_definition(qualifiers_definition) -> str:
    """Format qualifiers_definition dictionary for decorator"""
    if not qualifiers_definition:
        return ""

    # Handle unparseable strings
    if isinstance(qualifiers_definition, str):
        if qualifiers_definition.startswith("<Unparseable:"):
            return ""  # Skip unparseable definitions
        return ""

    if not isinstance(qualifiers_definition, dict):
        return ""

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
    return "    " + "\n    ".join(lines)


def create_enhanced_decorator(class_name: str, json_meta: Dict) -> str:
    """Create a complete decorator with all metadata including new fields"""
    parts = []

    # Add attributes if present
    if "CONTENTS" in json_meta and json_meta["CONTENTS"]:
        attributes_str = format_attributes(json_meta["CONTENTS"])
        if attributes_str:
            parts.append(attributes_str)

    # Add contents_order if present (NEW)
    if "CONTENTS_ORDER" in json_meta and json_meta["CONTENTS_ORDER"]:
        contents_order_str = format_contents_order(json_meta["CONTENTS_ORDER"])
        if contents_order_str:
            parts.append(contents_order_str)

    # Add qualifiers if present
    if "QUALIFIERS" in json_meta and json_meta["QUALIFIERS"]:
        qualifiers_str = format_qualifiers(json_meta["QUALIFIERS"])
        if qualifiers_str:
            parts.append(qualifiers_str)

    # Add qualifiers_order if present (NEW)
    if "QUALIFIERS_ORDER" in json_meta and json_meta["QUALIFIERS_ORDER"]:
        qualifiers_order_str = format_qualifiers_order(json_meta["QUALIFIERS_ORDER"])
        if qualifiers_order_str:
            parts.append(qualifiers_order_str)

    # Add qualifiers_definition if present (NEW)
    if "QUALIFIERS_DEFINITION" in json_meta and json_meta["QUALIFIERS_DEFINITION"]:
        qualifiers_definition_str = format_qualifiers_definition(
            json_meta["QUALIFIERS_DEFINITION"]
        )
        if qualifiers_definition_str:
            parts.append(qualifiers_definition_str)

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


def analyze_missing_enhanced_metadata(all_classes: Dict, metadata: Dict) -> List[Dict]:
    """Analyze what enhanced metadata is missing from classes"""
    classes_to_update = []

    for class_name, (file_path, position, class_line) in all_classes.items():
        if class_name not in metadata:
            continue

        json_meta = metadata[class_name]

        # Read the current file to check what's already there
        with open(file_path, "r") as f:
            content = f.read()

        # Find the current decorator if it exists
        before_class = content[:position]
        decorator_pattern = r"@cdata_class\s*\([^@]*?\)\s*$"
        decorator_match = re.search(decorator_pattern, before_class, re.DOTALL)

        if decorator_match:
            current_decorator = decorator_match.group(0)

            # Check what enhanced metadata is missing
            missing_contents_order = (
                "CONTENTS_ORDER" in json_meta
                and json_meta["CONTENTS_ORDER"]
                and "contents_order=" not in current_decorator
            )
            missing_qualifiers_order = (
                "QUALIFIERS_ORDER" in json_meta
                and json_meta["QUALIFIERS_ORDER"]
                and "qualifiers_order=" not in current_decorator
            )
            missing_qualifiers_definition = (
                "QUALIFIERS_DEFINITION" in json_meta
                and json_meta["QUALIFIERS_DEFINITION"]
                and "qualifiers_definition=" not in current_decorator
            )

            if (
                missing_contents_order
                or missing_qualifiers_order
                or missing_qualifiers_definition
            ):
                classes_to_update.append(
                    {
                        "class_name": class_name,
                        "file_path": file_path,
                        "position": position,
                        "class_line": class_line,
                        "current_decorator": current_decorator,
                        "json_meta": json_meta,
                        "missing_contents_order": missing_contents_order,
                        "missing_qualifiers_order": missing_qualifiers_order,
                        "missing_qualifiers_definition": missing_qualifiers_definition,
                    }
                )

    return classes_to_update


def update_decorators_with_enhanced_metadata(classes_to_update: List[Dict]) -> int:
    """Update decorators with enhanced metadata"""
    updates_applied = 0

    # Group by file
    files_to_update = {}
    for class_info in classes_to_update:
        file_path = class_info["file_path"]
        if file_path not in files_to_update:
            files_to_update[file_path] = []
        files_to_update[file_path].append(class_info)

    for file_path, file_classes in files_to_update.items():
        print(f"\n📄 Updating {file_path}...")

        with open(file_path, "r") as f:
            content = f.read()

        # Sort by position (reverse order to maintain positions)
        file_classes.sort(key=lambda x: x["position"], reverse=True)

        file_updates = 0
        for class_info in file_classes:
            # Create new enhanced decorator
            new_decorator = create_enhanced_decorator(
                class_info["class_name"], class_info["json_meta"]
            )

            if new_decorator:
                old_text = (
                    class_info["current_decorator"] + "\n" + class_info["class_line"]
                )
                new_text = new_decorator + "\n" + class_info["class_line"]

                if old_text in content:
                    content = content.replace(old_text, new_text, 1)
                    file_updates += 1
                    missing = []
                    if class_info["missing_contents_order"]:
                        missing.append("contents_order")
                    if class_info["missing_qualifiers_order"]:
                        missing.append("qualifiers_order")
                    if class_info["missing_qualifiers_definition"]:
                        missing.append("qualifiers_definition")
                    print(
                        f"    Updated {class_info['class_name']}: {', '.join(missing)}"
                    )

        if file_updates > 0:
            with open(file_path, "w") as f:
                f.write(content)
            updates_applied += file_updates

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
    """Main function for enhanced metadata completion"""
    print("🚀 ENHANCED METADATA COMPLETION SCRIPT")
    print("Adding CONTENTS_ORDER, QUALIFIERS_ORDER, and QUALIFIERS_DEFINITION")
    print("=" * 65)

    # Load data
    metadata = load_json_metadata()
    all_classes = find_all_classes_in_files()

    print(f"Loaded metadata for {len(metadata)} classes from JSON")
    print(f"Found {len(all_classes)} classes in Python files")

    # Find classes missing enhanced metadata
    classes_to_update = analyze_missing_enhanced_metadata(all_classes, metadata)

    if not classes_to_update:
        print("\n✅ All enhanced metadata already present!")
        return

    print(f"\nFound {len(classes_to_update)} classes needing enhanced metadata:")

    # Show summary
    contents_order_count = len(
        [c for c in classes_to_update if c["missing_contents_order"]]
    )
    qualifiers_order_count = len(
        [c for c in classes_to_update if c["missing_qualifiers_order"]]
    )
    qualifiers_definition_count = len(
        [c for c in classes_to_update if c["missing_qualifiers_definition"]]
    )

    print(f"  Classes missing CONTENTS_ORDER: {contents_order_count}")
    print(f"  Classes missing QUALIFIERS_ORDER: {qualifiers_order_count}")
    print(f"  Classes missing QUALIFIERS_DEFINITION: {qualifiers_definition_count}")

    # Apply updates
    updates_applied = update_decorators_with_enhanced_metadata(classes_to_update)

    print(f"\n🎯 Summary:")
    print(f"Enhanced metadata updates applied: {updates_applied}")

    # Validate all modified files
    files_modified = list(set(c["file_path"] for c in classes_to_update))
    all_valid = True

    for file_path in files_modified:
        if validate_file_syntax(file_path):
            print(f"  ✅ {file_path}: Syntax OK")
        else:
            print(f"  ❌ {file_path}: Syntax error - reverting")
            os.system(f"git checkout -- {file_path}")
            all_valid = False

    if all_valid:
        print(
            f"\n🎉 Successfully added enhanced metadata to {len(files_modified)} files!"
        )
    else:
        print(f"\n⚠️ Some files had syntax errors and were reverted")


if __name__ == "__main__":
    main()
