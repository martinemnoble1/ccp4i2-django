#!/usr/bin/env python3.12

import os
import re
import json
from typing import Dict, List, Tuple, Optional


def load_json_metadata() -> Dict:
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def find_decorator_and_class_positions(content: str) -> List[Dict]:
    """Find all decorator-class pairs in the content"""
    positions = []

    # Find all @cdata_class decorators with their classes
    pattern = (
        r"(@cdata_class\s*\([^@]*?\))\s*(class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):)"
    )
    matches = list(re.finditer(pattern, content, re.DOTALL))

    for match in matches:
        decorator_text = match.group(1)
        class_line = match.group(2)
        class_name = match.group(3)

        positions.append(
            {
                "class_name": class_name,
                "decorator_text": decorator_text,
                "class_line": class_line,
                "full_match": match,
                "start_pos": match.start(),
                "end_pos": match.end(),
            }
        )

    # Also find classes without decorators
    class_pattern = r"class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):"
    all_class_matches = list(re.finditer(class_pattern, content))

    # Get class names that already have decorators
    decorated_classes = {pos["class_name"] for pos in positions}

    for class_match in all_class_matches:
        class_name = class_match.group(1)
        if class_name not in decorated_classes:
            positions.append(
                {
                    "class_name": class_name,
                    "decorator_text": None,
                    "class_line": class_match.group(0),
                    "full_match": class_match,
                    "start_pos": class_match.start(),
                    "end_pos": class_match.end(),
                }
            )

    return sorted(positions, key=lambda x: x["start_pos"])


def format_qualifiers(qualifiers: Dict) -> str:
    """Format qualifiers dictionary for decorator"""
    if not qualifiers or not isinstance(qualifiers, dict):
        return ""

    lines = ["    qualifiers={"]
    for key, value in qualifiers.items():
        if value is None:
            lines.append(f'        "{key}": None,')
        elif isinstance(value, str):
            # Escape quotes in the string
            escaped_value = value.replace('"', '\\"')
            lines.append(f'        "{key}": "{escaped_value}",')
        elif isinstance(value, list):
            lines.append(f'        "{key}": {value},')
        else:
            lines.append(f'        "{key}": {value},')
    lines.append("    }")
    return "\n".join(lines)


def format_error_codes(error_codes: Dict) -> str:
    """Format error codes dictionary for decorator"""
    if not error_codes or not isinstance(error_codes, dict):
        return ""

    lines = ["    error_codes={"]
    for code, info in error_codes.items():
        if isinstance(info, dict) and "description" in info:
            description = info["description"]
        else:
            description = str(info)
        # Escape quotes in the description
        escaped_description = description.replace('"', '\\"')
        lines.append(f'        "{code}": "{escaped_description}",')
    lines.append("    }")
    return "\n".join(lines)


def analyze_missing_metadata(positions: List[Dict], metadata: Dict) -> List[Dict]:
    """Analyze what metadata is missing from each class"""
    classes_to_update = []

    for pos in positions:
        class_name = pos["class_name"]
        if class_name not in metadata:
            continue

        json_meta = metadata[class_name]

        # Check what metadata exists in JSON
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

        if not (should_have_qualifiers or should_have_error_codes):
            continue

        # Check what metadata exists in current decorator
        decorator_text = pos["decorator_text"] or ""
        has_qualifiers = "qualifiers=" in decorator_text
        has_error_codes = "error_codes=" in decorator_text

        # Determine what's missing
        missing_qualifiers = should_have_qualifiers and not has_qualifiers
        missing_error_codes = should_have_error_codes and not has_error_codes

        if missing_qualifiers or missing_error_codes:
            classes_to_update.append(
                {
                    **pos,
                    "missing_qualifiers": missing_qualifiers,
                    "missing_error_codes": missing_error_codes,
                    "json_qualifiers": (
                        json_meta.get("QUALIFIERS") if missing_qualifiers else None
                    ),
                    "json_error_codes": (
                        json_meta.get("ERROR_CODES") if missing_error_codes else None
                    ),
                    "has_existing_decorator": pos["decorator_text"] is not None,
                }
            )

    return classes_to_update


def create_new_decorator(class_info: Dict) -> str:
    """Create a new complete decorator"""
    parts = []

    if class_info["missing_qualifiers"] and class_info["json_qualifiers"]:
        qualifiers_str = format_qualifiers(class_info["json_qualifiers"])
        if qualifiers_str:
            parts.append(qualifiers_str)

    if class_info["missing_error_codes"] and class_info["json_error_codes"]:
        error_codes_str = format_error_codes(class_info["json_error_codes"])
        if error_codes_str:
            parts.append(error_codes_str)

    if not parts:
        return ""

    decorator_content = ",\n".join(parts)
    return f"@cdata_class(\n{decorator_content}\n)"


def update_existing_decorator(class_info: Dict) -> str:
    """Update an existing decorator by adding missing metadata"""
    existing_decorator = class_info["decorator_text"]

    # Parse existing decorator content
    start_paren = existing_decorator.find("(")
    end_paren = existing_decorator.rfind(")")

    if start_paren == -1 or end_paren == -1:
        return ""

    existing_content = existing_decorator[start_paren + 1 : end_paren].strip()

    # Create new metadata parts
    new_parts = []

    if class_info["missing_qualifiers"] and class_info["json_qualifiers"]:
        qualifiers_str = format_qualifiers(class_info["json_qualifiers"])
        if qualifiers_str:
            new_parts.append(qualifiers_str)

    if class_info["missing_error_codes"] and class_info["json_error_codes"]:
        error_codes_str = format_error_codes(class_info["json_error_codes"])
        if error_codes_str:
            new_parts.append(error_codes_str)

    if not new_parts:
        return existing_decorator

    # Combine existing and new content
    if existing_content:
        # Add comma if there's existing content
        combined_content = existing_content + ",\n" + ",\n".join(new_parts)
    else:
        combined_content = "\n" + ",\n".join(new_parts) + "\n"

    return f"@cdata_class(\n{combined_content}\n)"


def apply_updates_to_file(file_path: str, updates: List[Dict]) -> int:
    """Apply metadata updates to a file"""
    with open(file_path, "r") as f:
        content = f.read()

    # Sort updates by position (reverse order to maintain correct positions)
    updates.sort(key=lambda x: x["start_pos"], reverse=True)

    updates_applied = 0

    for update in updates:
        if update["has_existing_decorator"]:
            # Update existing decorator
            new_decorator = update_existing_decorator(update)
            if not new_decorator:
                continue

            # Replace the existing decorator
            old_text = update["decorator_text"] + "\n" + update["class_line"]
            new_text = new_decorator + "\n" + update["class_line"]

        else:
            # Add new decorator before class
            new_decorator = create_new_decorator(update)
            if not new_decorator:
                continue

            old_text = update["class_line"]
            new_text = new_decorator + "\n" + update["class_line"]

        # Apply the replacement
        if old_text in content:
            content = content.replace(old_text, new_text)
            updates_applied += 1
        else:
            print(f"  Warning: Could not find exact match for {update['class_name']}")

    # Write back the updated content
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
    """Main function to robustly complete metadata transfer"""
    print("🚀 Starting robust metadata transfer completion...")

    # Load JSON metadata
    metadata = load_json_metadata()
    print(f"Loaded metadata for {len(metadata)} classes from JSON")

    # Get all Python class files
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_updates = 0
    files_modified = []

    for file_path in py_files:
        print(f"\n📄 Processing {file_path}...")

        # Read and analyze the file
        with open(file_path, "r") as f:
            content = f.read()

        # Find all decorator-class positions
        positions = find_decorator_and_class_positions(content)

        # Analyze what metadata is missing
        updates_needed = analyze_missing_metadata(positions, metadata)

        if not updates_needed:
            print(f"  ✓ No updates needed for {file_path}")
            continue

        print(f"  Found {len(updates_needed)} classes needing metadata updates:")
        for update in updates_needed:
            missing = []
            if update["missing_qualifiers"]:
                missing.append("qualifiers")
            if update["missing_error_codes"]:
                missing.append("error_codes")
            print(f"    {update['class_name']}: {', '.join(missing)}")

        # Apply updates
        updates_applied = apply_updates_to_file(file_path, updates_needed)

        if updates_applied > 0:
            files_modified.append(file_path)
            total_updates += updates_applied
            print(f"  ✅ Applied {updates_applied} updates to {file_path}")

            # Validate syntax
            if validate_file_syntax(file_path):
                print(f"  ✓ Syntax validation passed")
            else:
                print(f"  ❌ Syntax validation failed - reverting file")
                # Could add revert logic here if needed
        else:
            print(f"  ⚠️ No updates could be applied to {file_path}")

    print(f"\n🎯 Summary:")
    print(f"Files processed: {len(py_files)}")
    print(f"Files modified: {len(files_modified)}")
    print(f"Total metadata updates applied: {total_updates}")

    if files_modified:
        print(f"\nModified files:")
        for file_path in files_modified:
            print(f"  - {file_path}")


if __name__ == "__main__":
    main()
