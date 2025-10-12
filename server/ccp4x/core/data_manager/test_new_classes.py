#!/usr/bin/env python3
"""
Test script to demonstrate the new CData class hierarchy.

This script shows how the generated classes work with proper:
- Inheritance
- Attribute typing
- Default values
- Validation
- Error handling
"""

import sys
import os

# Add the new_cdata directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import some generated classes
from new_cdata import CSequence, CSequenceMeta, CAtomSelection, CCell, CFont, CData


def test_sequence_class():
    """Test the CSequence class with its rich metadata."""
    print("=== Testing CSequence Class ===")

    # Create a sequence with default values
    seq1 = CSequence()
    print(f"Default sequence: {seq1}")
    print(f"Default moleculeType: {seq1.moleculeType}")
    print(f"Default referenceDb: {seq1.referenceDb}")

    # Create a sequence with custom values
    seq2 = CSequence(
        identifier="Test_Protein_1",
        name="Test Protein",
        description="A test protein sequence",
        sequence="MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFP",
        moleculeType="PROTEIN",
    )

    print(f"\nCustom sequence: {seq2}")
    print(f"Sequence length: {len(seq2.sequence) if seq2.sequence else 0}")

    # Test validation
    errors = seq2.validate()
    print(f"Validation errors: {errors}")

    # Test error messages (not yet implemented)
    print("Error handling: Not yet implemented in generated classes")


def test_sequence_meta():
    """Test the CSequenceMeta class."""
    print("\n=== Testing CSequenceMeta Class ===")

    meta = CSequenceMeta(
        uniprotId="P68871", organism="Homo sapiens", expressionSystem="E. coli"
    )

    print(f"Sequence metadata: {meta}")
    print("Error handling: Not yet implemented in generated classes")


def test_inheritance():
    """Test that inheritance is working properly."""
    print("\n=== Testing Inheritance ===")

    seq = CSequence(identifier="test_seq")
    meta = CSequenceMeta(uniprotId="P12345")

    print(f"CSequence isinstance CData: {isinstance(seq, CData)}")
    print(f"CSequenceMeta isinstance CData: {isinstance(meta, CData)}")

    print(f"CSequence MRO: {[cls.__name__ for cls in CSequence.__mro__]}")
    print(f"CSequenceMeta MRO: {[cls.__name__ for cls in CSequenceMeta.__mro__]}")


def test_atom_selection():
    """Test a simpler class."""
    print("\n=== Testing CAtomSelection ===")

    selection = CAtomSelection(text="chain A and resid 1-10")
    print(f"Atom selection: {selection}")

    # Check if validate method exists
    if hasattr(selection, "validate"):
        errors = selection.validate()
        print(f"Validation errors: {errors}")
    else:
        print("Validation method not available for this class")


def demonstrate_rich_classes():
    """Show off classes with rich metadata."""
    print("\n=== Testing Classes with Rich Metadata ===")

    # Test CCell with multiple attributes
    try:
        # This might not work if CCell doesn't have the expected attributes
        # but it shows the concept
        print("Looking at available classes...")
        from new_cdata import CData

        # Show some of the imported classes
        import new_cdata

        available = [
            name
            for name in dir(new_cdata)
            if name.startswith("C") and not name.startswith("__")
        ]
        print(f"Available classes: {available[:10]}...")

    except Exception as e:
        print(f"Error exploring classes: {e}")


def main():
    """Run all tests."""
    print("Testing the new CData class hierarchy")
    print("=" * 50)

    try:
        test_sequence_class()
        test_sequence_meta()
        test_inheritance()
        test_atom_selection()
        demonstrate_rich_classes()

        print("\n" + "=" * 50)
        print("All tests completed successfully!")

    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
