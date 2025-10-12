"""
Example of CSequence with rich metadata system.
Demonstrates how the new metadata system captures and uses CCP4i2 qualifiers.
"""

from typing import List, Optional
from .base_classes import CData
from .metadata_system import (
    MetadataRegistry,
    ClassMetadata,
    FieldMetadata,
    with_metadata,
    metadata_field,
)


class CSequenceEnhanced(CData):
    """
    Enhanced CSequence class with full metadata integration.

    A string of sequence one-letter codes
    Need to be able to parse common seq file formats
    Do we need to support alternative residues
    What about nucleic/polysaccharide?
    """

    def __init__(self, **kwargs):
        # Set defaults from metadata
        self.identifier: Optional[str] = None
        self.referenceDb: str = "unk"
        self.reference: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.sequence: Optional[str] = None
        self.moleculeType: str = "PROTEIN"

        # Apply any provided values
        super().__init__(**kwargs)


# Register comprehensive metadata for CSequence
_sequence_fields = {
    "identifier": FieldMetadata(
        name="identifier", tooltip="Description of sequence", minlength=4, required=True
    ),
    "referenceDb": FieldMetadata(
        name="referenceDb",
        default="unk",
        enumerators=["unk", "sp", "tr", "pdb"],
        menu_text=[
            "Unknown",
            "UniProt/Swiss-Prot",
            "UniProt/TrEMBL",
            "ProteinDatabank",
        ],
        only_enumerators=False,
        tooltip="Reference database for sequence",
    ),
    "reference": FieldMetadata(
        name="reference", tooltip="Optional reference for sequence"
    ),
    "name": FieldMetadata(name="name", tooltip="User friendly name of sequence"),
    "description": FieldMetadata(
        name="description", tooltip="User friendly description of sequence"
    ),
    "sequence": FieldMetadata(
        name="sequence",
        tooltip="Single letter sequence (white space and dash ignored)",
        required=True,
    ),
    "moleculeType": FieldMetadata(
        name="moleculeType",
        default="PROTEIN",
        enumerators=["PROTEIN", "DNA", "RNA"],
        only_enumerators=True,
        tooltip="Type of molecule (protein, DNA, or RNA)",
    ),
}

_sequence_metadata = ClassMetadata(
    name="CSequenceEnhanced",
    docstring="Enhanced sequence class with full metadata support",
    fields=_sequence_fields,
    error_codes={
        201: "Sequence identifier is too short",
        202: "Invalid molecule type",
        203: "Sequence contains invalid characters",
    },
    immediate_parent="CCP4Data.CData",
)

MetadataRegistry.register("CSequenceEnhanced", _sequence_metadata)


# Example of using decorators for simpler metadata (alternative approach)
@with_metadata
class CSequenceDecorated(CData):
    """Alternative approach using decorators for metadata."""

    identifier: str = metadata_field(
        tooltip="Description of sequence", minlength=4, required=True
    )

    moleculeType: str = metadata_field(
        default="PROTEIN",
        enumerators=["PROTEIN", "DNA", "RNA"],
        only_enumerators=True,
        tooltip="Type of molecule",
    )

    sequence: str = metadata_field(tooltip="Single letter sequence", required=True)


def demo_metadata_system():
    """Demonstrate the metadata system functionality."""
    print("🧬 CData Metadata System Demo")
    print("=" * 50)

    # Create enhanced sequence
    seq = CSequenceEnhanced(
        identifier="HGBA_HUMAN",
        name="Hemoglobin subunit alpha",
        sequence="MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF",
    )

    print(f"Created sequence: {seq}")

    # Test metadata access
    metadata = seq.get_metadata()
    print(f"\\nClass metadata: {metadata.name}")
    print(f"Docstring: {metadata.docstring}")

    # Test field metadata
    id_field = seq.get_field_info("identifier")
    print(f"\\nIdentifier field metadata:")
    print(f"  Tooltip: {id_field.tooltip}")
    print(f"  Min length: {id_field.minlength}")
    print(f"  Required: {id_field.required}")

    # Test enumeration support
    ref_field = seq.get_field_info("referenceDb")
    print(f"\\nReferenceDb enumerators: {ref_field.enumerators}")
    print(f"Menu text: {ref_field.menu_text}")

    # Test validation
    print(f"\\nValidation results:")
    errors = seq.validate()
    if errors:
        for error in errors:
            print(f"  ❌ {error}")
    else:
        print("  ✅ No validation errors")

    # Test validation with bad data
    bad_seq = CSequenceEnhanced(identifier="XY")  # Too short
    bad_errors = bad_seq.validate()
    print(f"\\nBad sequence validation:")
    for error in bad_errors:
        print(f"  ❌ {error}")

    # Test error codes
    print(f"\\nError codes:")
    print(f"  201: {seq.get_error_message(201)}")
    print(f"  202: {seq.get_error_message(202)}")

    print("\\n🎉 Metadata system working perfectly!")


if __name__ == "__main__":
    demo_metadata_system()
