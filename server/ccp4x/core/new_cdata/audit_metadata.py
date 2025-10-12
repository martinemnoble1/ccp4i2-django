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


def analyze_current_decorators():
    """Analyze what metadata is currently in decorators vs what should be there"""
    metadata = load_json_metadata()

    # Get all Python files
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    # Track what we find
    classes_with_decorators = {}
    classes_needing_metadata = {}

    print("Analyzing current decorator metadata coverage...")

    for file in py_files:
        with open(file, "r") as f:
            content = f.read()

        # Find all classes with decorators
        decorator_matches = re.finditer(
            r"@cdata_class\s*\(([^@]*?)\)\s*class\s+([A-Z][A-Za-z0-9_]*)",
            content,
            re.DOTALL,
        )

        for match in decorator_matches:
            decorator_content = match.group(1)
            class_name = match.group(2)

            has_qualifiers = "qualifiers=" in decorator_content
            has_error_codes = "error_codes=" in decorator_content
            has_attributes = "attributes=" in decorator_content

            classes_with_decorators[class_name] = {
                "file": file,
                "has_qualifiers": has_qualifiers,
                "has_error_codes": has_error_codes,
                "has_attributes": has_attributes,
            }

    # Check what should be there from JSON
    for class_name, json_metadata in metadata.items():
        should_have_qualifiers = (
            "QUALIFIERS" in json_metadata
            and isinstance(json_metadata["QUALIFIERS"], dict)
            and json_metadata["QUALIFIERS"]
        )
        should_have_error_codes = (
            "ERROR_CODES" in json_metadata
            and isinstance(json_metadata["ERROR_CODES"], dict)
            and json_metadata["ERROR_CODES"]
        )
        should_have_contents = (
            "CONTENTS" in json_metadata
            and isinstance(json_metadata["CONTENTS"], dict)
            and json_metadata["CONTENTS"]
        )

        if should_have_qualifiers or should_have_error_codes or should_have_contents:
            classes_needing_metadata[class_name] = {
                "should_have_qualifiers": should_have_qualifiers,
                "should_have_error_codes": should_have_error_codes,
                "should_have_contents": should_have_contents,
                "json_qualifiers": (
                    json_metadata.get("QUALIFIERS") if should_have_qualifiers else None
                ),
                "json_error_codes": (
                    json_metadata.get("ERROR_CODES")
                    if should_have_error_codes
                    else None
                ),
                "json_contents": (
                    json_metadata.get("CONTENTS") if should_have_contents else None
                ),
            }

    # Find gaps
    print(f"\nFound {len(classes_with_decorators)} classes with decorators")
    print(
        f"Found {len(classes_needing_metadata)} classes that should have metadata from JSON"
    )

    missing_qualifiers = []
    missing_error_codes = []
    missing_contents = []

    for class_name, needed in classes_needing_metadata.items():
        current = classes_with_decorators.get(class_name, {})

        if needed["should_have_qualifiers"] and not current.get(
            "has_qualifiers", False
        ):
            missing_qualifiers.append(class_name)

        if needed["should_have_error_codes"] and not current.get(
            "has_error_codes", False
        ):
            missing_error_codes.append(class_name)

        if needed["should_have_contents"] and not current.get("has_attributes", False):
            missing_contents.append(class_name)

    print(f"\nMissing metadata:")
    print(f"  Classes missing QUALIFIERS: {len(missing_qualifiers)}")
    if missing_qualifiers:
        print(f"    Examples: {', '.join(missing_qualifiers[:5])}")

    print(f"  Classes missing ERROR_CODES: {len(missing_error_codes)}")
    if missing_error_codes:
        print(f"    Examples: {', '.join(missing_error_codes[:5])}")

    print(f"  Classes missing CONTENTS (attributes): {len(missing_contents)}")
    if missing_contents:
        print(f"    Examples: {', '.join(missing_contents[:5])}")

    return {
        "missing_qualifiers": missing_qualifiers,
        "missing_error_codes": missing_error_codes,
        "missing_contents": missing_contents,
        "classes_needing_metadata": classes_needing_metadata,
    }


def main():
    analysis = analyze_current_decorators()

    # Show specific examples of what's missing
    print(f"\nDetailed examples of missing metadata:")

    for category, missing_list in [
        ("QUALIFIERS", analysis["missing_qualifiers"][:3]),
        ("ERROR_CODES", analysis["missing_error_codes"][:3]),
        ("CONTENTS", analysis["missing_contents"][:3]),
    ]:
        if missing_list:
            print(f"\n{category} missing from:")
            for class_name in missing_list:
                needed = analysis["classes_needing_metadata"][class_name]
                if category == "QUALIFIERS" and needed["json_qualifiers"]:
                    print(
                        f"  {class_name}: {list(needed['json_qualifiers'].keys())[:3]}"
                    )
                elif category == "ERROR_CODES" and needed["json_error_codes"]:
                    print(
                        f"  {class_name}: codes {list(needed['json_error_codes'].keys())}"
                    )
                elif category == "CONTENTS" and needed["json_contents"]:
                    print(
                        f"  {class_name}: attributes {list(needed['json_contents'].keys())}"
                    )


if __name__ == "__main__":
    main()
