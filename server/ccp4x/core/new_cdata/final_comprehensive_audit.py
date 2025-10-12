#!/usr/bin/env python3.12

import json
import os
import re
from collections import defaultdict


def load_json_metadata():
    """Load the JSON metadata file"""
    json_path = "/Users/nmemn/Developer/ccp4i2-django/server/ccp4x/core/data_manager/migrating_from_old_ccp4i2/cdata_lookup_enhanced_full.json"
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["classes"]


def analyze_all_files():
    """Complete analysis of all files and their current state"""
    metadata = load_json_metadata()
    py_files = [f for f in os.listdir(".") if f.endswith("_classes.py")]

    total_stats = {
        "classes_with_decorators": 0,
        "classes_with_qualifiers": 0,
        "classes_with_error_codes": 0,
        "classes_with_attributes": 0,
        "classes_in_json": len(metadata),
        "decorators_found": 0,
    }

    file_results = {}
    all_missing_qualifiers = []
    all_missing_error_codes = []
    all_complete_classes = []

    for file_path in py_files:
        print(f"\n📄 Analyzing {file_path}...")

        with open(file_path, "r") as f:
            content = f.read()

        # Find all decorators
        decorator_matches = list(
            re.finditer(r"@cdata_class\s*\([^@]*?\)", content, re.DOTALL)
        )
        class_matches = list(
            re.finditer(r"class\s+([A-Z][A-Za-z0-9_]*)\s*\([^)]+\):", content)
        )

        file_classes = []
        classes_with_decorators = 0
        classes_with_qualifiers = 0
        classes_with_error_codes = 0
        classes_with_attributes = 0

        for class_match in class_matches:
            class_name = class_match.group(1)
            if class_name not in metadata:
                continue

            file_classes.append(class_name)

            # Find corresponding decorator if it exists
            decorator_found = False
            has_qualifiers = False
            has_error_codes = False
            has_attributes = False

            # Look for decorator before this class
            class_start = class_match.start()
            for decorator_match in decorator_matches:
                if (
                    decorator_match.end() < class_start
                    and (class_start - decorator_match.end()) < 200
                ):  # Within reasonable distance
                    decorator_found = True
                    decorator_text = decorator_match.group(0)

                    if "qualifiers=" in decorator_text:
                        has_qualifiers = True
                    if "error_codes=" in decorator_text:
                        has_error_codes = True
                    if "attributes=" in decorator_text:
                        has_attributes = True
                    break

            if decorator_found:
                classes_with_decorators += 1
                if has_qualifiers:
                    classes_with_qualifiers += 1
                if has_error_codes:
                    classes_with_error_codes += 1
                if has_attributes:
                    classes_with_attributes += 1

            # Check what should be present from JSON
            json_meta = metadata[class_name]
            should_have_qualifiers = bool(json_meta.get("QUALIFIERS"))
            should_have_error_codes = bool(json_meta.get("ERROR_CODES"))

            # Track missing metadata
            if should_have_qualifiers and not has_qualifiers:
                all_missing_qualifiers.append(f"{class_name} ({file_path})")
            if should_have_error_codes and not has_error_codes:
                all_missing_error_codes.append(f"{class_name} ({file_path})")

            # Track complete classes
            if (not should_have_qualifiers or has_qualifiers) and (
                not should_have_error_codes or has_error_codes
            ):
                all_complete_classes.append(f"{class_name} ({file_path})")

        file_results[file_path] = {
            "total_classes": len(file_classes),
            "classes_with_decorators": classes_with_decorators,
            "classes_with_qualifiers": classes_with_qualifiers,
            "classes_with_error_codes": classes_with_error_codes,
            "classes_with_attributes": classes_with_attributes,
        }

        total_stats["classes_with_decorators"] += classes_with_decorators
        total_stats["classes_with_qualifiers"] += classes_with_qualifiers
        total_stats["classes_with_error_codes"] += classes_with_error_codes
        total_stats["classes_with_attributes"] += classes_with_attributes
        total_stats["decorators_found"] += len(decorator_matches)

        print(f"  Classes found in JSON: {len(file_classes)}")
        print(f"  Classes with decorators: {classes_with_decorators}")
        print(f"  Classes with qualifiers: {classes_with_qualifiers}")
        print(f"  Classes with error_codes: {classes_with_error_codes}")
        print(f"  Classes with attributes: {classes_with_attributes}")

    return (
        total_stats,
        file_results,
        all_missing_qualifiers,
        all_missing_error_codes,
        all_complete_classes,
    )


def main():
    """Main comprehensive analysis"""
    print("🔍 Final Comprehensive Metadata Analysis")
    print("=" * 50)

    stats, file_results, missing_qualifiers, missing_error_codes, complete_classes = (
        analyze_all_files()
    )

    print(f"\n🎯 OVERALL SUMMARY:")
    print(f"Total classes in JSON metadata: {stats['classes_in_json']}")
    print(
        f"Total classes with @cdata_class decorators: {stats['classes_with_decorators']}"
    )
    print(f"Total decorators found in all files: {stats['decorators_found']}")
    print(f"Classes with qualifiers: {stats['classes_with_qualifiers']}")
    print(f"Classes with error_codes: {stats['classes_with_error_codes']}")
    print(f"Classes with attributes: {stats['classes_with_attributes']}")

    print(f"\n📊 COMPLETION RATES:")
    if stats["classes_in_json"] > 0:
        decorator_rate = (
            stats["classes_with_decorators"] / stats["classes_in_json"]
        ) * 100
        print(
            f"Decorator coverage: {decorator_rate:.1f}% ({stats['classes_with_decorators']}/{stats['classes_in_json']})"
        )

    print(f"\n❌ REMAINING MISSING METADATA:")
    print(f"Classes missing QUALIFIERS: {len(missing_qualifiers)}")
    if missing_qualifiers:
        print("  Examples:", ", ".join(missing_qualifiers[:5]))
        if len(missing_qualifiers) > 5:
            print(f"  ... and {len(missing_qualifiers) - 5} more")

    print(f"Classes missing ERROR_CODES: {len(missing_error_codes)}")
    if missing_error_codes:
        print("  Examples:", ", ".join(missing_error_codes[:5]))
        if len(missing_error_codes) > 5:
            print(f"  ... and {len(missing_error_codes) - 5} more")

    print(f"\n✅ COMPLETE CLASSES:")
    print(f"Classes with all required metadata: {len(complete_classes)}")

    print(f"\n📁 FILE BREAKDOWN:")
    for file_path, data in file_results.items():
        if data["total_classes"] > 0:
            completion = ""
            if data["classes_with_decorators"] == data["total_classes"]:
                completion = "✅ COMPLETE"
            elif data["classes_with_decorators"] > 0:
                completion = "🔄 PARTIAL"
            else:
                completion = "❌ NONE"

            print(
                f"  {file_path}: {data['classes_with_decorators']}/{data['total_classes']} {completion}"
            )


if __name__ == "__main__":
    main()
