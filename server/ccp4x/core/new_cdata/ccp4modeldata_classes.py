"""Generated classes from CCP4ModelData.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile, CDataFileContent, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "seqList": attribute(
            AttributeType.CUSTOM,
            custom_class="CAsuContentSeqList",
            tooltip="seqList attribute",
        )
    },
    gui_label="CAsuContent",
    error_codes={
        "101": "Failed reading file - is it correct file type?",
        "102": "Failed reading file - it is not AU contents file",
    },
)
@cdata_class(
    attributes={
            "seqList": attribute(AttributeType.STRING, tooltip="seqList attribute"),
        },
    error_codes={
            "101": "Failed reading file - is it correct file type?",
            "102": "Failed reading file - it is not AU contents file",
        },
    gui_label="CAsuContent"
)
class CAsuContent(CDataFileContent):
    """Generated CAsuContent class from CData metadata."""


@cdata_class(
    attributes={
        "sequence": attribute(
            AttributeType.CUSTOM,
            custom_class="CSequenceString",
            tooltip="sequence attribute",
        ),
        "nCopies": attribute(
            AttributeType.INT, default=1, min_value=0, tooltip="nCopies attribute"
        ),
        "polymerType": attribute(
            AttributeType.STRING, default="PROTEIN", tooltip="polymerType attribute"
        ),
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "description": attribute(AttributeType.STRING, tooltip="description attribute"),
        "source": attribute(
            AttributeType.CUSTOM, custom_class="CDataFile", tooltip="source attribute"
        ),
    },
    gui_label="CAsuContentSeq",
)
@cdata_class(
    attributes={
            "sequence": attribute(AttributeType.STRING, tooltip="sequence attribute"),
            "nCopies": attribute(AttributeType.INT, tooltip="nCopies attribute"),
            "polymerType": attribute(AttributeType.STRING, tooltip="polymerType attribute"),
            "name": attribute(AttributeType.STRING, tooltip="name attribute"),
            "description": attribute(AttributeType.STRING, tooltip="description attribute"),
            "source": attribute(AttributeType.FILE, tooltip="source attribute"),
        },
    gui_label="CAsuContentSeq"
)
class CAsuContentSeq(CData):
    """Generated CAsuContentSeq class from CData metadata."""

    pass

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
            "listMinLength": 0,
        },
    error_codes={
            "401": "Sequence the same as a sequence that is already loaded",
            "402": "Sequence names are not unique: ",
        },
    gui_label="CAsuContentSeqList"
)
class CAsuContentSeqList(CList):
    """Generated CAsuContentSeqList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "groupId": attribute(AttributeType.INT, tooltip="groupId attribute"),
        "chainId": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="chainId attribute"
        ),
        "firstRes": attribute(AttributeType.INT, tooltip="firstRes attribute"),
        "lastRes": attribute(AttributeType.INT, tooltip="lastRes attribute"),
    },
    gui_label="CAtomRefmacSelection",
)
@cdata_class(
    attributes={
            "groupId": attribute(AttributeType.INT, tooltip="groupId attribute"),
            "chainId": attribute(AttributeType.STRING, tooltip="chainId attribute"),
            "firstRes": attribute(AttributeType.INT, tooltip="firstRes attribute"),
            "lastRes": attribute(AttributeType.INT, tooltip="lastRes attribute"),
        },
    gui_label="CAtomRefmacSelection"
)
class CAtomRefmacSelection(CData):
    """A residue range selection for rigid body groups"""


@cdata_class(
    attributes={
        "groupIds": attribute(AttributeType.STRING, tooltip="groupIds attribute")
    },
    gui_label="CAtomRefmacSelectionGroups",
)
class CAtomRefmacSelectionGroups(CData):
    """A group selection for occupancy groups"""

    pass


@cdata_class(
    gui_label="CAtomRefmacSelectionList"
)
class CAtomRefmacSelectionList(CList):
    """Generated CAtomRefmacSelectionList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "groupId": attribute(AttributeType.INT, tooltip="groupId attribute"),
        "chainIds": attribute(AttributeType.STRING, tooltip="chainIds attribute"),
        "firstRes": attribute(AttributeType.INT, tooltip="firstRes attribute"),
        "lastRes": attribute(AttributeType.INT, tooltip="lastRes attribute"),
        "atoms": attribute(AttributeType.STRING, tooltip="atoms attribute"),
        "alt": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="alt attribute"
        ),
    },
    gui_label="CAtomRefmacSelectionOccupancy",
)
@cdata_class(
    attributes={
            "groupId": attribute(AttributeType.INT, tooltip="groupId attribute"),
            "chainIds": attribute(AttributeType.STRING, tooltip="chainIds attribute"),
            "firstRes": attribute(AttributeType.INT, tooltip="firstRes attribute"),
            "lastRes": attribute(AttributeType.INT, tooltip="lastRes attribute"),
            "atoms": attribute(AttributeType.STRING, tooltip="atoms attribute"),
            "alt": attribute(AttributeType.STRING, tooltip="alt attribute"),
        },
    gui_label="CAtomRefmacSelectionOccupancy"
)
class CAtomRefmacSelectionOccupancy(CData):
    """A residue range selection for occupancy groups"""


@cdata_class(
    attributes={"text": attribute(AttributeType.STRING, tooltip="text attribute")},
    gui_label="CAtomSelection",
    qualifiers={
        "pdbFileKey": "",
    },
)
class CAtomSelection(CData):
    """Generated CAtomSelection class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "queryId": attribute(AttributeType.STRING, tooltip="queryId attribute"),
        "alignmentList": attribute(
            AttributeType.CUSTOM,
            custom_class="CList",
            tooltip="alignmentList attribute",
        ),
    },
    gui_label="CBlastData",
)
@cdata_class(
    attributes={
            "queryId": attribute(AttributeType.STRING, tooltip="queryId attribute"),
            "alignmentList": attribute(AttributeType.STRING, tooltip="alignmentList attribute"),
        },
    gui_label="CBlastData"
)
class CBlastData(CDataFileContent):
    """Generated CBlastData class from CData metadata."""


@cdata_class(
    qualifiers={
            "fileLabel": "Blast sequence search",
            "mimeTypeName": "application/Blast-alignments",
            "mimeTypeDescription": "Blast sequence search results",
            "guiLabel": "Blast results",
            "tooltip": "Output from Blast search",
            "fileExtensions": ["bla", "blast", "xml"],
            "fileContentClassName": "CBlastData",
            "helpFile": "model_data#ali",
        },
    gui_label="CBlastDataFile"
)
class CBlastDataFile(CDataFile):
    """Generated CBlastDataFile class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "hitId": attribute(AttributeType.STRING, tooltip="hitId attribute"),
        "querySequence": attribute(
            AttributeType.STRING, tooltip="querySequence attribute"
        ),
        "hitSequence": attribute(AttributeType.STRING, tooltip="hitSequence attribute"),
    },
    gui_label="CBlastItem",
)
@cdata_class(
    attributes={
            "hitId": attribute(AttributeType.STRING, tooltip="hitId attribute"),
            "querySequence": attribute(AttributeType.STRING, tooltip="querySequence attribute"),
            "hitSequence": attribute(AttributeType.STRING, tooltip="hitSequence attribute"),
        },
    gui_label="CBlastItem"
)
class CBlastItem(CData):
    """Generated CBlastItem class from CData metadata."""


@cdata_class(
    attributes={
        "id": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="id attribute"
        ),
        "three_letter_code": attribute(
            AttributeType.CUSTOM,
            custom_class="COneWord",
            tooltip="three_letter_code attribute",
        ),
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "group": attribute(AttributeType.STRING, tooltip="group attribute"),
        "number_atoms_all": attribute(
            AttributeType.INT, tooltip="number_atoms_all attribute"
        ),
        "number_atoms_nh": attribute(
            AttributeType.INT, tooltip="number_atoms_nh attribute"
        ),
        "desc_level": attribute(AttributeType.INT, tooltip="desc_level attribute"),
    },
    gui_label="CChemComp",
    error_codes={
        "201": "Error reading monomer id and name",
        "202": "Error writing monomer id and name",
    },
)
@cdata_class(
    attributes={
            "id": attribute(AttributeType.STRING, tooltip="id attribute"),
            "three_letter_code": attribute(AttributeType.STRING, tooltip="three_letter_code attribute"),
            "name": attribute(AttributeType.STRING, tooltip="name attribute"),
            "group": attribute(AttributeType.STRING, tooltip="group attribute"),
            "number_atoms_all": attribute(AttributeType.INT, tooltip="number_atoms_all attribute"),
            "number_atoms_nh": attribute(AttributeType.INT, tooltip="number_atoms_nh attribute"),
            "desc_level": attribute(AttributeType.INT, tooltip="desc_level attribute"),
        },
    error_codes={
            "201": "Error reading monomer id and name",
            "202": "Error writing monomer id and name",
        },
    gui_label="CChemComp"
)
class CChemComp(CData):
    """Component of CDictDataFile contents"""

    pass


@cdata_class(
    attributes={
            "monomerList": attribute(AttributeType.STRING, tooltip="monomerList attribute"),
        },
    gui_label="CDictData"
)
class CDictData(CData):
    """Generated CDictData class from CData metadata."""


@cdata_class(
    qualifiers={
        "fileLabel": "dictionary",
        "mimeTypeName": "application/refmac-dictionary",
        "mimeTypeDescription": "Geometry file",
        "guiLabel": "Geometry dictionary",
        "toolTip": "Idealised geometry of ligands for refinement",
        "fileExtensions": ["cif"],
        "fileContentClassName": "CDictData",
        "helpFile": "model_data#ligand_geometry",
    },
    error_codes={
        "201": "Error attempting to merge geometry files - no libcheck script",
        "202": "Error attempting to merge geometry files - failed creating working directory",
        "203": "Error attempting to merge geometry files - setting libcheck parameters",
        "204": "Error attempting to merge geometry files - running libcheck",
        "205": "Error attempting to merge geometry files - failed to run libcheck",
    },
)
@cdata_class(
    qualifiers={
            "fileLabel": "dictionary",
            "mimeTypeName": "application/refmac-dictionary",
            "mimeTypeDescription": "Geometry file",
            "guiLabel": "Geometry dictionary",
            "toolTip": "Idealised geometry of ligands for refinement",
            "fileExtensions": ["cif"],
            "fileContentClassName": "CDictData",
            "helpFile": "model_data#ligand_geometry",
        },
    error_codes={
            "201": "Error attempting to merge geometry files - no libcheck script",
            "202": "Error attempting to merge geometry files - failed creating working directory",
            "203": "Error attempting to merge geometry files - setting libcheck parameters",
            "204": "Error attempting to merge geometry files - running libcheck",
            "205": "Error attempting to merge geometry files - failed to run libcheck",
        },
    gui_label="CDictDataFile"
)
class CDictDataFile(CDataFile):
    """A refmac dictionary file"""

    pass


@cdata_class(
    attributes={
        "label": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="label attribute"
        ),
        "number": attribute(
            AttributeType.INT, default=1, min_value=0, tooltip="number attribute"
        ),
        "use": attribute(AttributeType.BOOLEAN, default=True, tooltip="use attribute"),
        "pdbItemList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="pdbItemList attribute"
        ),
    },
    gui_label="CEnsemble",
    qualifiers={
        "guiLabel": "Ensemble",
        "allowUndefined": False,
    },
)
@cdata_class(
    attributes={
            "label": attribute(AttributeType.STRING, tooltip="label attribute"),
            "number": attribute(AttributeType.INT, tooltip="number attribute"),
            "use": attribute(AttributeType.BOOL, tooltip="use attribute"),
            "pdbItemList": attribute(AttributeType.STRING, tooltip="pdbItemList attribute"),
        },
    qualifiers={
            "guiLabel": "Ensemble",
            "allowUndefined": False,
        },
    gui_label="CEnsemble"
)
class CEnsemble(CData):
    """An ensemble of models. Typically, this would be a set of related
    PDB files, but models could also be xtal or EM maps. This should
    be indicated by the types entry.
    A single ensemble is a CList of structures."""

    pass

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
            "listMinLength": 1,
        },
    gui_label="CEnsembleList"
)
class CEnsembleList(CList):
    """Generated CEnsembleList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "alignmentList": attribute(
            AttributeType.CUSTOM,
            custom_class="CList",
            tooltip="alignmentList attribute",
        )
    },
    gui_label="CHhpredData",
    error_codes={
        "201": "Failed to read HHPred file",
        "202": "Failed to load iotbx software to read HHPred file",
    },
)
@cdata_class(
    attributes={
            "alignmentList": attribute(AttributeType.STRING, tooltip="alignmentList attribute"),
        },
    error_codes={
            "201": "Failed to read HHPred file",
            "202": "Failed to load iotbx software to read HHPred file",
        },
    gui_label="CHhpredData"
)
class CHhpredData(CDataFileContent):
    """Generated CHhpredData class from CData metadata."""


@cdata_class(
    qualifiers={
            "fileLabel": "HHPred sequence search",
            "mimeTypeName": "application/HHPred-alignments",
            "mimeTypeDescription": "HHPred sequence search results",
            "guiLabel": "HHPred results",
            "tooltip": "Output from HHPred search",
            "fileExtensions": ["hhr"],
            "fileContentClassName": "CHhpredData",
            "helpFile": "model_data#ali",
        },
    gui_label="CHhpredDataFile"
)
class CHhpredDataFile(CDataFile):
    """Generated CHhpredDataFile class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "annotation": attribute(AttributeType.STRING, tooltip="annotation attribute"),
        "identifier": attribute(AttributeType.STRING, tooltip="identifier attribute"),
        "chain": attribute(AttributeType.STRING, tooltip="chain attribute"),
    },
    gui_label="CHhpredItem",
)
class CHhpredItem(CData):
    """Generated CHhpredItem class from CData metadata."""


@cdata_class(
    qualifiers={
            "fileLabel": "mol",
            "mimeTypeName": "chemical/x-mdl-molfile",
            "mimeTypeDescription": "MDL Molfile",
            "guiLabel": "Mol file",
            "toolTip": "Structure geometry of ligands for refinement in MDL mol format",
            "fileExtensions": ["mol", "sdf"],
            "fileContentClassName": None,
            "helpFile": "model_data#mol_file",
        },
    gui_label="CMDLMolDataFile"
)
class CMDLMolDataFile(CDataFile):
    """A molecule definition file (MDL)"""

    pass


@cdata_class(
    qualifiers={
            "fileLabel": "mol2",
            "mimeTypeName": "chemical/x-mol2",
            "mimeTypeDescription": "MOL2 file",
            "guiLabel": "MOL2 file",
            "toolTip": "Structure geometry of ligands for refinement in MOL2 format",
            "fileExtensions": ["mol2"],
            "fileContentClassName": None,
            "helpFile": "model_data#mol2_file",
        },
    gui_label="CMol2DataFile"
)
class CMol2DataFile(CDataFile):
    """A molecule definition file (MOL2)"""

    pass


@cdata_class(
    attributes={
        "identifier": attribute(
            AttributeType.STRING, tooltip="The name you use for the monomer"
        ),
        "formula": attribute(
            AttributeType.STRING, tooltip="The formula for the monomer"
        ),
        "dictionaryName": attribute(
            AttributeType.STRING,
            tooltip="The REFMAC dictionary name if not the same as the name",
        ),
        "smiles": attribute(
            AttributeType.STRING, tooltip="The smiles string for the monomer"
        ),
    },
    gui_label="CMonomer",
)
@cdata_class(
    attributes={
            "identifier": attribute(AttributeType.STRING, tooltip="The name you use for the monomer"),
            "formula": attribute(AttributeType.STRING, tooltip="The formula for the monomer"),
            "dictionaryName": attribute(AttributeType.STRING, tooltip="The REFMAC dictionary name if not the same as the name"),
            "smiles": attribute(AttributeType.STRING, tooltip="The smiles string for the monomer"),
        },
    gui_label="CMonomer"
)
class CMonomer(CData):
    """A monomer compound. ?smiles"""

    # The name you use for the monomer
    # The formula for the monomer
    # The REFMAC dictionary name if not the same as the name
    # The smiles string for the monomer

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    gui_label="COccRefmacSelectionList"
)
class COccRefmacSelectionList(CList):
    """Generated COccRefmacSelectionList class from CData metadata."""

    pass


@cdata_class(
    gui_label="COccRelationRefmacList"
)
class COccRelationRefmacList(CList):
    """Generated COccRelationRefmacList class from CData metadata."""

    pass


@cdata_class(
    error_codes={
            "101": "Unable to load mmdb - ensure LD_LIBRARY_PATH is set",
            "102": "Error reading PDB file into MMDB object",
            "103": "Residue range selection does not specify chain",
            "104": "Residue range selection specifies non-existant chain id",
            "105": "Residue range selection - no residues selected",
            "106": "Residue range selection - residue number is not an integer",
            "112": "Atom selection failed. Failed creating CMMDBManager object",
            "113": "Atom selection failed. Faied reading coordinate file.",
            "114": "Atom selection failed. Failed parsing command",
            "115": "Atom selection failed. Error creating PPCAtom",
            "116": "Atom selection failed. Error in GetSelIndex",
            "117": "Atom selection failed. Error loading selection tree",
            "118": "Atom selection failed. Error applying selection tree",
            "119": "Creating new PDB file failed on writing file",
            "120": "Creating new PDB file failed converting from fractional coordinates",
        },
    gui_label="CPdbData"
)
class CPdbData(CDataFileContent):
    """Contents of a PDB file - a subset with functionality for GUI"""

    pass


@cdata_class(
    gui_label="CPdbDataFile"
)
class CPdbDataFile(CDataFile):
    """Generated CPdbDataFile class from CData metadata."""

    pass


@cdata_class(
    gui_label="CPdbDataFileList"
)
class CPdbDataFileList(CList):
    """Generated CPdbDataFileList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "structure": attribute(
            AttributeType.CUSTOM,
            custom_class="CPdbDataFile",
            tooltip="structure attribute",
        ),
        "identity_to_target": attribute(
            AttributeType.FLOAT,
            min_value=0.0,
            max_value=1.0,
            tooltip="identity_to_target attribute",
        ),
        "rms_to_target": attribute(
            AttributeType.FLOAT,
            min_value=0.0,
            max_value=100.0,
            tooltip="rms_to_target attribute",
        ),
    },
    gui_label="CPdbEnsembleItem",
    qualifiers={
        "guiLabel": "Structure in ensemble",
        "toolTip": "Homologous model and its similarity to the target structure",
        "allowUndefined": False,
    },
    error_codes={
        "101": "No sequence identity or structure RMS to target set",
    },
)
@cdata_class(
    attributes={
            "structure": attribute(AttributeType.STRING, tooltip="structure attribute"),
            "identity_to_target": attribute(AttributeType.FLOAT, tooltip="identity_to_target attribute"),
            "rms_to_target": attribute(AttributeType.FLOAT, tooltip="rms_to_target attribute"),
        },
    qualifiers={
            "guiLabel": "Structure in ensemble",
            "toolTip": "Homologous model and its similarity to the target structure",
            "allowUndefined": False,
        },
    error_codes={
            "101": "No sequence identity or structure RMS to target set",
        },
    gui_label="CPdbEnsembleItem"
)
class CPdbEnsembleItem(CData):
    """Generated CPdbEnsembleItem class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "chainId": attribute(
            AttributeType.CUSTOM,
            custom_class="COneWord",
            default="",
            tooltip="chainId attribute",
        ),
        "firstRes": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="firstRes attribute"
        ),
        "lastRes": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="lastRes attribute"
        ),
    },
    gui_label="CResidueRange",
    qualifiers={
        "pdbFileKey": None,
    },
)
@cdata_class(
    attributes={
            "chainId": attribute(AttributeType.STRING, tooltip="chainId attribute"),
            "firstRes": attribute(AttributeType.STRING, tooltip="firstRes attribute"),
            "lastRes": attribute(AttributeType.STRING, tooltip="lastRes attribute"),
        },
    qualifiers={
            "pdbFileKey": None,
        },
    gui_label="CResidueRange"
)
class CResidueRange(CData):
    """A residue range selection"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    gui_label="CResidueRangeList"
)
class CResidueRangeList(CList):
    """A list of residue range selections"""

    pass


@cdata_class(
    error_codes={
            "202": "Error reading from file",
            "203": "Unknown alignment file format",
            "204": "Can not read Blast or HHPred file format",
            "205": "Error reading identifiers from multi-record file",
            "206": "Error attempting to identify file format",
            "250": "Alignment file format not recognised - can not convert",
            "251": "Alignment file conversion failed to overwrite existing file",
            "252": "Alignment file conversion failed writing file",
            "260": "Alignment file does not contain required number of sequences",
        },
    gui_label="CSeqAlignDataFile"
)
class CSeqAlignDataFile(CDataFile):
    """A (multiple) sequence alignment file"""

    pass


@cdata_class(
    qualifiers={
            "fileLabel": "sequence",
            "mimeTypeName": "application/CCP4-seq",
            "mimeTypeDescription": "Sequence file",
            "guiLabel": "Sequence",
            "tooltip": "Sequence in any of the common formats (pir,fasta..)",
            "fileExtensions": ["seq", "pir", "fasta"],
            "fileContentClassName": "CSequence",
            "downloadModes": ["uniprotFasta"],
            "helpFile": "model_data#sequences",
        },
    error_codes={
            "201": "Error reading sequence file",
            "202": "Error in BioPython attempting to identify file type",
        },
    gui_label="CSeqDataFile"
)
class CSeqDataFile(CDataFile):
    """A sequence file"""

    pass


@cdata_class(
    error_codes={
            "150": "No file content information",
            "151": "Two sequences have the same identifier",
            "152": "Failed in merging sequence files to read sequence file",
            "153": "Failed in merging sequence files to write merged file",
        },
    gui_label="CSeqDataFileList"
)
class CSeqDataFileList(CList):
    """Generated CSeqDataFileList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "identifier": attribute(AttributeType.STRING, tooltip="identifier attribute"),
        "referenceDb": attribute(
            AttributeType.STRING, default="unk", tooltip="referenceDb attribute"
        ),
        "reference": attribute(AttributeType.STRING, tooltip="reference attribute"),
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "description": attribute(AttributeType.STRING, tooltip="description attribute"),
        "sequence": attribute(AttributeType.STRING, tooltip="sequence attribute"),
        "moleculeType": attribute(
            AttributeType.STRING, default="PROTEIN", tooltip="moleculeType attribute"
        ),
    },
    gui_label="CSequence",
)
@cdata_class(
    attributes={
            "identifier": attribute(AttributeType.STRING, tooltip="Description of sequence"),
            "referenceDb": attribute(AttributeType.STRING, tooltip="referenceDb attribute"),
            "reference": attribute(AttributeType.STRING, tooltip="Optional reference for sequence"),
            "name": attribute(AttributeType.STRING, tooltip="User friendly name of sequence"),
            "description": attribute(AttributeType.STRING, tooltip="User friendly description of sequence"),
            "sequence": attribute(AttributeType.STRING, tooltip="Single letter sequence (white space and dash ignored)"),
            "moleculeType": attribute(AttributeType.STRING, tooltip="Molecule type"),
        },
    gui_label="CSequence"
)
class CSequence(CData):
    """A string of sequence one-letter codes
    Need to be able to parse common seq file formats
    Do we need to support alternative residues
    What about nucleic/polysach?"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "identifier": attribute(AttributeType.STRING, tooltip="identifier attribute"),
        "moleculeType": attribute(
            AttributeType.STRING, default="PROTEIN", tooltip="moleculeType attribute"
        ),
    },
    gui_label="CSequenceAlignment",
)
@cdata_class(
    attributes={
            "identifier": attribute(AttributeType.STRING, tooltip="Optional convenient name for sequence alignment"),
            "moleculeType": attribute(AttributeType.STRING, tooltip="Molecule type"),
        },
    gui_label="CSequenceAlignment"
)
class CSequenceAlignment(CData):
    """An alignment of two or more sequences.
    Each sequence is obviously related to class CSequence, but
    will also contain gaps relevant to the alignment. We could
    implement the contents as a list of CSequence objects?
    The alignment is typically formatted in a file as consecutive
    or interleaved sequences."""

    # Optional convenient name for sequence alignment
    # Molecule type (already defined in decorator)
    pass

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "uniprotId": attribute(AttributeType.STRING, tooltip="uniprotId attribute"),
        "organism": attribute(AttributeType.STRING, tooltip="organism attribute"),
        "expressionSystem": attribute(
            AttributeType.STRING, tooltip="expressionSystem attribute"
        ),
    },
    error_codes={
        "401": "No uniprot id available",
        "402": "No uniprot xml file available to read",
        "403": "No project id provided to determine uniprot xml filename",
        "404": "Reading uniprot xml file failed",
    },
    gui_label="CSequenceMeta",
)
@cdata_class(
    attributes={
            "uniprotId": attribute(AttributeType.STRING, tooltip="uniprotId attribute"),
            "organism": attribute(AttributeType.STRING, tooltip="organism attribute"),
            "expressionSystem": attribute(AttributeType.STRING, tooltip="expressionSystem attribute"),
        },
    error_codes={
            "401": "No uniprot id available",
            "402": "No uniprot xml file available to read",
            "403": "No project id provided to determine uniprot xml filename",
            "404": "Reading uniprot xml file failed",
        },
    gui_label="CSequenceMeta"
)
class CSequenceMeta(CData):
    """Generated CSequenceMeta class from CData metadata."""

    pass


@cdata_class(
    gui_label="CSequenceString"
)
class CSequenceString(CString):
    """Generated CSequenceString class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "fileLabel": "tls",
        "mimeTypeName": "application/refmac-TLS",
        "mimeTypeDescription": "Refmac TLS file",
        "guiLabel": "TLS coefficients",
        "toolTip": "Definition of model domains for TLS refinement",
        "fileExtensions": ["tls"],
        "fileContentClassName": None,
        "helpFile": "model_data#tls_file",
    }
)
@cdata_class(
    qualifiers={
            "fileLabel": "tls",
            "mimeTypeName": "application/refmac-TLS",
            "mimeTypeDescription": "Refmac TLS file",
            "guiLabel": "TLS coefficients",
            "toolTip": "Definition of model domains for TLS refinement",
            "fileExtensions": ["tls"],
            "fileContentClassName": None,
            "helpFile": "model_data#tls_file",
        },
    gui_label="CTLSDataFile"
)
class CTLSDataFile(CDataFile):
    """A refmac TLS file"""

    pass
