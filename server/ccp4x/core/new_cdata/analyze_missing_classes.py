#!/usr/bin/env python3.12

import json
import os
import re


def load_json_metadata():
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def find_all_classes_in_files():
    """Find all classes in all Python files"""
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
            all_classes[class_name] = file_path

    return all_classes


def analyze_missing_metadata():
    """Analyze exactly what's missing and why"""
    metadata = load_json_metadata()
    all_classes = find_all_classes_in_files()

    print("🔍 DETAILED ANALYSIS OF MISSING METADATA")
    print("=" * 60)

    # Check a few specific missing classes to understand the pattern
    missing_qualifiers_examples = ["CMDLMolDataFile", "CMol2DataFile", "CSeqDataFile"]
    missing_error_codes_examples = [
        "CSeqDataFile",
        "CSeqDataFileList",
        "CSeqAlignDataFile",
    ]

    print("\n📋 ANALYZING MISSING QUALIFIERS:")
    for class_name in missing_qualifiers_examples:
        if class_name in metadata and class_name in all_classes:
            file_path = all_classes[class_name]
            json_meta = metadata[class_name]

            print(f"\n{class_name} (in {file_path}):")
            print(f"  JSON QUALIFIERS: {json_meta.get('QUALIFIERS', 'None')}")

            # Check current decorator in file
            with open(file_path, "r") as f:
                content = f.read()

            # Find this class and its decorator
            class_pattern = (
                rf"(@cdata_class\s*\([^@]*?\))?\s*class\s+{class_name}\s*\([^)]+\):"
            )
            match = re.search(class_pattern, content, re.DOTALL)
            if match:
                decorator_text = match.group(1) if match.group(1) else "NO DECORATOR"
                has_qualifiers = "qualifiers=" in decorator_text
                print(f"  HAS DECORATOR: {decorator_text is not None}")
                print(f"  HAS QUALIFIERS: {has_qualifiers}")
                if decorator_text and decorator_text != "NO DECORATOR":
                    # Show first few lines of decorator
                    lines = decorator_text.split("\n")[:3]
                    print(f"  DECORATOR START: {' '.join(lines)}")

    print("\n📋 ANALYZING MISSING ERROR_CODES:")
    for class_name in missing_error_codes_examples:
        if class_name in metadata and class_name in all_classes:
            file_path = all_classes[class_name]
            json_meta = metadata[class_name]

            print(f"\n{class_name} (in {file_path}):")
            print(f"  JSON ERROR_CODES: {json_meta.get('ERROR_CODES', 'None')}")

            # Check current decorator in file
            with open(file_path, "r") as f:
                content = f.read()

            # Find this class and its decorator
            class_pattern = (
                rf"(@cdata_class\s*\([^@]*?\))?\s*class\s+{class_name}\s*\([^)]+\):"
            )
            match = re.search(class_pattern, content, re.DOTALL)
            if match:
                decorator_text = match.group(1) if match.group(1) else "NO DECORATOR"
                has_error_codes = "error_codes=" in decorator_text
                print(f"  HAS DECORATOR: {decorator_text is not None}")
                print(f"  HAS ERROR_CODES: {has_error_codes}")

    print("\n📊 SUMMARY OF ISSUES:")
    classes_without_decorators = []
    classes_with_incomplete_decorators = []

    for class_name in metadata:
        if class_name in all_classes:
            file_path = all_classes[class_name]
            json_meta = metadata[class_name]

            # Check if class has decorator
            with open(file_path, "r") as f:
                content = f.read()

            class_pattern = (
                rf"(@cdata_class\s*\([^@]*?\))?\s*class\s+{class_name}\s*\([^)]+\):"
            )
            match = re.search(class_pattern, content, re.DOTALL)

            if not match or not match.group(1):
                classes_without_decorators.append(class_name)
            else:
                decorator_text = match.group(1)
                should_have_qualifiers = bool(json_meta.get("QUALIFIERS"))
                should_have_error_codes = bool(json_meta.get("ERROR_CODES"))
                has_qualifiers = "qualifiers=" in decorator_text
                has_error_codes = "error_codes=" in decorator_text

                if (should_have_qualifiers and not has_qualifiers) or (
                    should_have_error_codes and not has_error_codes
                ):
                    classes_with_incomplete_decorators.append(class_name)

    print(f"Classes WITHOUT decorators: {len(classes_without_decorators)}")
    if classes_without_decorators:
        print(f"  Examples: {', '.join(classes_without_decorators[:5])}")

    print(
        f"Classes WITH incomplete decorators: {len(classes_with_incomplete_decorators)}"
    )
    if classes_with_incomplete_decorators:
        print(f"  Examples: {', '.join(classes_with_incomplete_decorators[:5])}")

    return classes_without_decorators, classes_with_incomplete_decorators


if __name__ == "__main__":
    no_decorators, incomplete_decorators = analyze_missing_metadata()
