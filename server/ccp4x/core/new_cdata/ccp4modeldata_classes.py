"""Generated classes from CCP4ModelData.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CAsuContent(CData):
    """Generated CAsuContent class from CData metadata."""

    seqList: Any = None

class CAsuContentSeq(CData):
    """Generated CAsuContentSeq class from CData metadata."""

    sequence: Any = None
    nCopies: Any = 1
    polymerType: Any = "PROTEIN"
    name: Any = None
    description: Any = None
    source: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CAsuContentSeqList(CData):
    """Generated CAsuContentSeqList class from CData metadata."""
    pass

class CAtomRefmacSelection(CData):
    """A residue range selection for rigid body groups"""

    groupId: Any = None
    chainId: Any = None
    firstRes: Any = None
    lastRes: Any = None

class CAtomRefmacSelectionGroups(CData):
    """A group selection for occupancy groups"""

    groupIds: Any = None

class CAtomRefmacSelectionList(CData):
    """Generated CAtomRefmacSelectionList class from CData metadata."""
    pass

class CAtomRefmacSelectionOccupancy(CData):
    """A residue range selection for occupancy groups"""

    groupId: Any = None
    chainIds: Any = None
    firstRes: Any = None
    lastRes: Any = None
    atoms: Any = None
    alt: Any = None

class CAtomSelection(CData):
    """Generated CAtomSelection class from CData metadata."""

    text: Any = None

class CBlastData(CData):
    """Generated CBlastData class from CData metadata."""

    queryId: Any = None
    alignmentList: Any = None

class CBlastDataFile(CData):
    """Generated CBlastDataFile class from CData metadata."""
    pass

class CBlastItem(CData):
    """Generated CBlastItem class from CData metadata."""

    hitId: Any = None
    querySequence: Any = None
    hitSequence: Any = None

class CChemComp(CData):
    """Component of CDictDataFile contents"""

    id: Any = None
    three_letter_code: Any = None
    name: Any = None
    group: Any = None
    number_atoms_all: Any = None
    number_atoms_nh: Any = None
    desc_level: Any = None

class CDictData(CData):
    """Generated CDictData class from CData metadata."""

    monomerList: Any = None

class CDictDataFile(CData):
    """A refmac dictionary file"""
    pass

class CEnsemble(CData):
    """An ensemble of models. Typically, this would be a set of related
PDB files, but models could also be xtal or EM maps. This should
be indicated by the types entry.
A single ensemble is a CList of structures."""

    label: Any = None
    number: Any = 1
    use: Any = True
    pdbItemList: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CEnsembleList(CData):
    """Generated CEnsembleList class from CData metadata."""
    pass

class CHhpredData(CData):
    """Generated CHhpredData class from CData metadata."""

    alignmentList: Any = None

class CHhpredDataFile(CData):
    """Generated CHhpredDataFile class from CData metadata."""
    pass

class CHhpredItem(CData):
    """Generated CHhpredItem class from CData metadata."""

    annotation: Any = None
    identifier: Any = None
    chain: Any = None

class CMDLMolDataFile(CData):
    """A molecule definition file (MDL)"""
    pass

class CMol2DataFile(CData):
    """A molecule definition file (MOL2)"""
    pass

class CMonomer(CData):
    """A monomer compound. ?smiles"""

    # The name you use for the monomer
    identifier: Any = None
    # The formula for the monomer
    formula: Any = None
    # The REFMAC dictionary name if not the same as the name
    dictionaryName: Any = None
    # The smiles string for the monomer
    smiles: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class COccRefmacSelectionList(CData):
    """Generated COccRefmacSelectionList class from CData metadata."""
    pass

class COccRelationRefmacList(CData):
    """Generated COccRelationRefmacList class from CData metadata."""
    pass

class CPdbData(CData):
    """Contents of a PDB file - a subset with functionality for GUI"""
    pass

class CPdbDataFile(CData):
    """Generated CPdbDataFile class from CData metadata."""
    pass

class CPdbDataFileList(CData):
    """Generated CPdbDataFileList class from CData metadata."""
    pass

class CPdbEnsembleItem(CData):
    """Generated CPdbEnsembleItem class from CData metadata."""

    structure: Any = None
    identity_to_target: Any = None
    rms_to_target: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CResidueRange(CData):
    """A residue range selection"""

    chainId: Any = ""
    firstRes: Any = None
    lastRes: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CResidueRangeList(CData):
    """A list of residue range selections"""
    pass

class CSeqAlignDataFile(CData):
    """A (multiple) sequence alignment file"""
    pass

class CSeqDataFile(CData):
    """A sequence file"""
    pass

class CSeqDataFileList(CData):
    """Generated CSeqDataFileList class from CData metadata."""
    pass

class CSequence(CData):
    """A string of sequence one-letter codes
Need to be able to parse common seq file formats
Do we need to support alternative residues
What about nucleic/polysach?"""

    # Description of sequence
    identifier: Any = None
    referenceDb: Any = "unk"
    # Optional reference for sequence
    reference: Any = None
    # User friendly name of sequence
    name: Any = None
    # User friendly description of sequence
    description: Any = None
    # Single letter sequence (white space and dash ignored)
    sequence: Any = None
    # Molecule type
    moleculeType: Any = "PROTEIN"

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CSequenceAlignment(CData):
    """An alignment of two or more sequences.
Each sequence is obviously related to class CSequence, but
will also contain gaps relevant to the alignment. We could
implement the contents as a list of CSequence objects?
The alignment is typically formatted in a file as consecutive 
or interleaved sequences."""

    # Optional convenient name for sequence alignment
    identifier: Any = None
    # Molecule type
    moleculeType: Any = "PROTEIN"

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CSequenceMeta(CData):
    """Generated CSequenceMeta class from CData metadata."""

    uniprotId: Any = None
    organism: Any = None
    expressionSystem: Any = None

class CSequenceString(CData):
    """Generated CSequenceString class from CData metadata."""
    pass

class CTLSDataFile(CData):
    """A refmac TLS file"""
    pass
