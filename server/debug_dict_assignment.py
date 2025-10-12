#!/usr/bin/env python3
"""
Debug dictionary assignment specifically.
"""

from ccp4x.core.data_manager.new_cdata.base_classes import CData


def test_dict_assignment():
    """Test dictionary assignment in isolation."""

    print("🔍 DEBUGGING DICTIONARY ASSIGNMENT")
    print("=" * 40)

    # Create a sequence object
    sequence = CData(name="sequence")
    sequence.identifier = "PROT_001"
    sequence.description = "Test protein"
    sequence.length = 150

    print(f"Before: identifier='{sequence.identifier}', length={sequence.length}")
    print(f"Has organism: {hasattr(sequence, 'organism')}")

    # Test direct dictionary assignment
    update_dict = {
        "identifier": "PROT_002_UPDATED",
        "description": "Updated test protein",
        "length": 200,
        "organism": "E. coli",
    }

    print(f"\\nCalling _smart_assign_from_dict directly...")
    sequence._smart_assign_from_dict(update_dict)

    print(
        f"After direct call: identifier='{sequence.identifier}', length={sequence.length}"
    )
    print(f"Has organism: {hasattr(sequence, 'organism')}")
    if hasattr(sequence, "organism"):
        print(f"Organism: '{sequence.organism}'")

    # Test through attribute assignment
    print(f"\\nTesting through container.seq = dict...")
    container = CData(name="container")

    # First set the sequence
    container.seq = sequence
    print(f"Container seq id: {id(container.seq)}")

    # Now try dictionary assignment
    original_id = id(container.seq)
    container.seq = update_dict

    print(f"After dict assignment:")
    print(f"  seq id: {id(container.seq)} (same? {id(container.seq) == original_id})")
    print(f"  identifier: '{container.seq.identifier}'")
    print(f"  Has organism: {hasattr(container.seq, 'organism')}")
    if hasattr(container.seq, "organism"):
        print(f"  Organism: '{container.seq.organism}'")


if __name__ == "__main__":
    test_dict_assignment()
