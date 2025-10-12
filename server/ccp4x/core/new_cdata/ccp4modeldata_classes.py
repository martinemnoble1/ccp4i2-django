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
        "sequence": attribute(
            AttributeType.CUSTOM,
            custom_class="CSequenceString",
            tooltip="sequence attribute",
        ),
        "nCopies": attribute(AttributeType.INT, default=1, tooltip="nCopies attribute"),
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
class CAsuContentSeq(CData):
    """Generated CAsuContentSeq class from CData metadata."""

    pass

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


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
        "chainId": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="chainId attribute"
        ),
        "firstRes": attribute(AttributeType.INT, tooltip="firstRes attribute"),
        "lastRes": attribute(AttributeType.INT, tooltip="lastRes attribute"),
    },
    gui_label="CAtomRefmacSelection",
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
        "alt": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="alt attribute"
        ),
    },
    gui_label="CAtomRefmacSelectionOccupancy",
)
class CAtomRefmacSelectionOccupancy(CData):
    """A residue range selection for occupancy groups"""


@cdata_class(
    attributes={"text": attribute(AttributeType.STRING, tooltip="text attribute")},
    gui_label="CAtomSelection",
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
        "alignmentList": attribute(
            AttributeType.CUSTOM,
            custom_class="CList",
            tooltip="alignmentList attribute",
        ),
    },
    gui_label="CBlastData",
)
class CBlastData(CDataFileContent):
    """Generated CBlastData class from CData metadata."""


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
        "querySequence": attribute(
            AttributeType.STRING, tooltip="querySequence attribute"
        ),
        "hitSequence": attribute(AttributeType.STRING, tooltip="hitSequence attribute"),
    },
    gui_label="CBlastItem",
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
)
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
)
class CChemComp(CData):
    """Component of CDictDataFile contents"""

    pass


@cdata_class(
    attributes={
        "monomerList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="monomerList attribute"
        )
    },
    gui_label="CDictData",
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
)
@cdata_class(
    attributes={
        "label": attribute(
            AttributeType.CUSTOM, custom_class="COneWord", tooltip="label attribute"
        ),
        "number": attribute(AttributeType.INT, default=1, tooltip="number attribute"),
        "use": attribute(AttributeType.BOOLEAN, default=True, tooltip="use attribute"),
        "pdbItemList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="pdbItemList attribute"
        ),
    },
    gui_label="CEnsemble",
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
)
class CHhpredData(CDataFileContent):
    """Generated CHhpredData class from CData metadata."""


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


class CMDLMolDataFile(CDataFile):
    """A molecule definition file (MDL)"""

    pass


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


class COccRefmacSelectionList(CList):
    """Generated COccRefmacSelectionList class from CData metadata."""

    pass


class COccRelationRefmacList(CList):
    """Generated COccRelationRefmacList class from CData metadata."""

    pass


class CPdbData(CDataFileContent):
    """Contents of a PDB file - a subset with functionality for GUI"""

    pass


class CPdbDataFile(CDataFile):
    """Generated CPdbDataFile class from CData metadata."""

    pass


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
)
@cdata_class(
    attributes={
        "structure": attribute(
            AttributeType.CUSTOM,
            custom_class="CPdbDataFile",
            tooltip="structure attribute",
        ),
        "identity_to_target": attribute(
            AttributeType.FLOAT, tooltip="identity_to_target attribute"
        ),
        "rms_to_target": attribute(
            AttributeType.FLOAT, tooltip="rms_to_target attribute"
        ),
    },
    gui_label="CPdbEnsembleItem",
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
)
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
)
class CResidueRange(CData):
    """A residue range selection"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CResidueRangeList(CList):
    """A list of residue range selections"""

    pass


class CSeqAlignDataFile(CDataFile):
    """A (multiple) sequence alignment file"""

    pass


class CSeqDataFile(CDataFile):
    """A sequence file"""

    pass


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
class CSequenceMeta(CData):
    """Generated CSequenceMeta class from CData metadata."""

    pass


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
class CTLSDataFile(CDataFile):
    """A refmac TLS file"""

    pass
