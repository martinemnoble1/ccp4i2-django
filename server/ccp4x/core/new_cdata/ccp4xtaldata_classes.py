"""Generated classes from CCP4XtalData.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile, CDataFileContent, CFloat, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


class CAltSpaceGroupList(CList):
    """Generated CAltSpaceGroupList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "moleculeType": attribute(
            AttributeType.STRING, default="PROTEIN", tooltip="Molecule type"
        ),
        "seqFile": attribute(AttributeType.STRING, tooltip="seqFile attribute"),
        "numberOfCopies": attribute(
            AttributeType.INT, default=1, tooltip="Number of copies of sequence"
        ),
    },
    gui_label="CAsuComponent",
)
class CAsuComponent(CData):
    """A component of the asymmetric unit. This is for use in MR, defining
    what we are searching for."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CAsuComponentList(CList):
    """Generated CAsuComponentList class from CData metadata."""

    pass


@cdata_class(
attributes={
        "a": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellLength",
            tooltip="Cell length a in A",
        ),
        "b": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellLength",
            tooltip="Cell length b in A",
        ),
        "c": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellLength",
            tooltip="Cell length c in A",
        ),
        "alpha": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellAngle",
            tooltip="Cell angle alpha in degrees",
        ),
        "beta": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellAngle",
            tooltip="Cell angle beta in degrees",
        ),
        "gamma": attribute(
            AttributeType.CUSTOM,
            custom_class="CCellAngle",
            tooltip="Cell angle gamma in degrees",
        ),
    },
    gui_label="CCell",
    qualifiers={
            "toolTip": "Cell lengths and angles",
            "helpFile": "crystal_data#cell",
        }
)
class CCell(CData):
    """A unit cell"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CCellAngle(CFloat):
    """A cell angle"""

    pass


class CCellLength(CFloat):
    """A cell length"""

    pass


@cdata_class(
    attributes={
        "columnGroupType": attribute(
            AttributeType.CUSTOM,
            custom_class="COneWord",
            tooltip="columnGroupType attribute",
        ),
        "contentFlag": attribute(AttributeType.INT, tooltip="contentFlag attribute"),
        "dataset": attribute(AttributeType.STRING, tooltip="dataset attribute"),
        "columnList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="columnList attribute"
        ),
        "selected": attribute(AttributeType.BOOLEAN, tooltip="selected attribute"),
    },
    gui_label="CColumnGroup",
)
class CColumnGroup(CData):
    """Groups of columns in MTZ - probably from analysis by hklfile"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
attributes={
        "columnName": attribute(AttributeType.STRING, tooltip="columnName attribute"),
        "defaultList": attribute(AttributeType.STRING, tooltip="defaultList attribute"),
        "columnType": attribute(AttributeType.STRING, tooltip="columnType attribute"),
        "partnerTo": attribute(AttributeType.STRING, tooltip="partnerTo attribute"),
        "partnerOffset": attribute(
            AttributeType.STRING, tooltip="partnerOffset attribute"
        ),
    },
    gui_label="CColumnGroupItem",
    error_codes={
            "1": "Attempting to change immutable object",
            "2": "Attempting to access unknown attribute",
        }
)
class CColumnGroupItem(CData):
    """Definition of set of columns that form a 'group'"""


class CColumnGroupList(CList):
    """Generated CColumnGroupList class from CData metadata."""

    pass


class CColumnType(CString):
    """A list of recognised MTZ column types"""

    pass


class CColumnTypeList(CList):
    """A list of acceptable MTZ column types"""

    pass


class CCrystalName(CString):
    """Generated CCrystalName class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "selected": attribute(AttributeType.BOOLEAN, tooltip="selected attribute"),
        "obsDataFile": attribute(
            AttributeType.CUSTOM,
            custom_class="CObsDataFile",
            tooltip="obsDataFile attribute",
        ),
        "crystalName": attribute(
            AttributeType.CUSTOM,
            custom_class="CCrystalName",
            tooltip="crystalName attribute",
        ),
        "datasetName": attribute(
            AttributeType.CUSTOM,
            custom_class="CDatasetName",
            tooltip="datasetName attribute",
        ),
        "formFactors": attribute(
            AttributeType.CUSTOM,
            custom_class="CFormFactor",
            tooltip="formFactors attribute",
        ),
        "formFactorSource": attribute(
            AttributeType.STRING, default="no", tooltip="formFactorSource attribute"
        ),
    },
    gui_label="CDataset",
)
class CDataset(CData):
    """The experimental data model for ab initio phasing"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CDatasetList(CList):
    """Generated CDatasetList class from CData metadata."""

    pass


class CDatasetName(CString):
    """Generated CDatasetName class from CData metadata."""

    pass


class CDialsJsonFile(CDataFile):
    """Generated CDialsJsonFile class from CData metadata."""

    pass


class CDialsPickleFile(CDataFile):
    """Generated CDialsPickleFile class from CData metadata."""

    pass


class CExperimentalDataType(CString):
    """Experimental data type e.g. native or peak"""

    pass


@cdata_class(
    attributes={
        "Fp": attribute(
            AttributeType.FLOAT,
            tooltip="Form factor F' for element at given wavelength",
        ),
        "Fpp": attribute(
            AttributeType.FLOAT,
            tooltip="Form factor F'' for element at given wavelength",
        ),
    },
    gui_label="CFormFactor",
)
class CFormFactor(CData):
    """The for factor (Fp and Fpp) for a giving element and wavelength"""


class CGenericReflDataFile(CDataFile):
    """Generated CGenericReflDataFile class from CData metadata."""

    pass


class CImageFile(CDataFile):
    """Generated CImageFile class from CData metadata."""

    pass


class CImageFileList(CList):
    """Generated CImageFileList class from CData metadata."""

    pass


class CImosflmXmlDataFile(CDataFile):
    """An iMosflm data file"""

    pass


@cdata_class(
attributes={
        "file": attribute(
            AttributeType.CUSTOM,
            custom_class="CUnmergedDataFile",
            tooltip="file attribute",
        ),
        "cell": attribute(
            AttributeType.CUSTOM, custom_class="CCell", tooltip="cell attribute"
        ),
        "wavelength": attribute(
            AttributeType.CUSTOM,
            custom_class="CWavelength",
            tooltip="wavelength attribute",
        ),
        "crystalName": attribute(AttributeType.STRING, tooltip="crystalName attribute"),
        "dataset": attribute(AttributeType.STRING, tooltip="dataset attribute"),
        "excludeSelection": attribute(
            AttributeType.CUSTOM,
            custom_class="CRangeSelection",
            tooltip="excludeSelection attribute",
        ),
    },
    gui_label="CImportUnmerged",
    qualifiers={
            "toolTip": "Imported data file, cell parameters and crystal/dataset identifiers",
            "helpFile": "import_merged#file_formats",
        }
)
class CImportUnmerged(CData):
    """Generated CImportUnmerged class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CImportUnmergedList(CList):
    """Generated CImportUnmergedList class from CData metadata."""

    pass


class CMapDataFile(CDataFile):
    """A CCP4 Map file"""

    pass


@cdata_class(
attributes={
        "fileName": attribute(AttributeType.STRING, tooltip="fileName attribute"),
        "columnTag": attribute(AttributeType.STRING, tooltip="columnTag attribute"),
        "columnNames": attribute(AttributeType.STRING, tooltip="columnNames attribute"),
    },
    gui_label="CMergeMiniMtz",
    error_codes={
            "201": "Selected file is not a suitable 'mini' MTZ containing experimental data object",
            "202": "Output column name list does not have correct number of names",
        }
)
class CMergeMiniMtz(CData):
    """Generated CMergeMiniMtz class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CMergeMiniMtzList(CList):
    """Generated CMergeMiniMtzList class from CData metadata."""

    pass


class CMiniMtzDataFileList(CList):
    """Generated CMiniMtzDataFileList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "columnLabel": attribute(AttributeType.STRING, tooltip="columnLabel attribute"),
        "columnType": attribute(AttributeType.STRING, tooltip="columnType attribute"),
        "dataset": attribute(AttributeType.STRING, tooltip="dataset attribute"),
        "groupIndex": attribute(AttributeType.INT, tooltip="groupIndex attribute"),
    },
    gui_label="CMtzColumn",
)
class CMtzColumn(CData):
    """An MTZ column with column label and column type"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "groupType": attribute(AttributeType.STRING, tooltip="groupType attribute"),
        "columns": attribute(AttributeType.STRING, tooltip="columns attribute"),
    },
    gui_label="CMtzColumnGroup",
)
class CMtzColumnGroup(CData):
    """Generated CMtzColumnGroup class from CData metadata."""


@cdata_class(
    attributes={
        "cell": attribute(
            AttributeType.CUSTOM, custom_class="CCell", tooltip="cell attribute"
        ),
        "spaceGroup": attribute(
            AttributeType.CUSTOM,
            custom_class="CSpaceGroup",
            tooltip="spaceGroup attribute",
        ),
        "resolutionRange": attribute(
            AttributeType.CUSTOM,
            custom_class="CResolutionRange",
            tooltip="resolutionRange attribute",
        ),
        "listOfColumns": attribute(
            AttributeType.CUSTOM,
            custom_class="CList",
            tooltip="listOfColumns attribute",
        ),
        "datasets": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="datasets attribute"
        ),
        "crystalNames": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="crystalNames attribute"
        ),
        "wavelengths": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="wavelengths attribute"
        ),
        "datasetCells": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="datasetCells attribute"
        ),
        "merged": attribute(AttributeType.BOOLEAN, tooltip="merged attribute"),
    },
    gui_label="CMtzData",
)
class CMtzData(CDataFileContent):
    """Generated CMtzData class from CData metadata."""

    pass


class CMtzDataFile(CDataFile):
    """An MTZ experimental data file"""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "columnGroups": attribute(
            AttributeType.STRING, tooltip="columnGroups attribute"
        ),
    },
    gui_label="CMtzDataset",
)
class CMtzDataset(CData):
    """Generated CMtzDataset class from CData metadata."""


class CPhaserRFileDataFile(CDataFile):
    """Generated CPhaserRFileDataFile class from CData metadata."""

    pass


class CPhaserSolDataFile(CDataFile):
    """Generated CPhaserSolDataFile class from CData metadata."""

    pass


class CProgramColumnGroup(CData):
    """A group of MTZ columns required for program input"""

    pass


@cdata_class(
attributes={
        "columnGroup": attribute(AttributeType.STRING, tooltip="columnGroup attribute"),
        "datasetName": attribute(AttributeType.STRING, tooltip="datasetName attribute"),
    },
    gui_label="CProgramColumnGroup0",
    qualifiers={
            "mustExist": False,
            "mtzFileKey": "",
            "groupTypes": [],
        }
)
class CProgramColumnGroup0(CData):
    """Generated CProgramColumnGroup0 class from CData metadata."""


class CRefmacKeywordFile(CDataFile):
    """Generated CRefmacKeywordFile class from CData metadata."""

    pass


@cdata_class(
attributes={
        "h": attribute(AttributeType.STRING, default="h", tooltip="h attribute"),
        "k": attribute(AttributeType.STRING, default="k", tooltip="k attribute"),
        "l": attribute(AttributeType.STRING, default="l", tooltip="l attribute"),
    },
    gui_label="CReindexOperator",
    error_codes={
            "201": "Operator has bad syntax (needs three comma-separated fields)",
            "202": "Operator contains invalid characters",
            "203": "Operator is not set",
        }
)
class CReindexOperator(CData):
    """Generated CReindexOperator class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
attributes={
        "low": attribute(AttributeType.FLOAT, tooltip="low attribute"),
        "high": attribute(AttributeType.FLOAT, tooltip="high attribute"),
    },
    gui_label="CResolutionRange",
    error_codes={
            "201": "High/low resolution wrong way round?",
        }
)
class CResolutionRange(CData):
    """Generated CResolutionRange class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
attributes={
        "runNumber": attribute(AttributeType.INT, tooltip="runNumber attribute"),
        "batchRange0": attribute(AttributeType.INT, tooltip="batchRange0 attribute"),
        "batchRange1": attribute(AttributeType.INT, tooltip="batchRange1 attribute"),
        "resolution": attribute(AttributeType.FLOAT, tooltip="resolution attribute"),
        "fileNumber": attribute(AttributeType.INT, tooltip="fileNumber attribute"),
    },
    gui_label="CRunBatchRange",
    qualifiers={
            "toolTip": "Specify range of reflections to treat as one run",
        },
    error_codes={
            "101": "End of batch range less than start",
            "102": "All items must be set",
        }
)
class CRunBatchRange(CData):
    """Generated CRunBatchRange class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CRunBatchRangeList(CList):
    """Generated CRunBatchRangeList class from CData metadata."""

    pass


class CShelxFADataFile(CDataFile):
    """Generated CShelxFADataFile class from CData metadata."""

    pass


class CShelxLabel(CString):
    """Generated CShelxLabel class from CData metadata."""

    pass


class CSpaceGroup(CString):
    """A string holding the space group"""

    pass


@cdata_class(
attributes={
        "spaceGroup": attribute(
            AttributeType.CUSTOM,
            custom_class="CSpaceGroup",
            tooltip="spaceGroup attribute",
        ),
        "cell": attribute(
            AttributeType.CUSTOM, custom_class="CCell", tooltip="cell attribute"
        ),
    },
    gui_label="CSpaceGroupCell",
    qualifiers={
            "toolTip": "Space group and cell length and angles",
            "helpFile": "crystal_data#cell_space_group",
        },
    error_codes={
            "101": "Cell lengths should NOT be identical",
            "102": "Cell angles should NOT be identical",
            "103": "Cell angle should be 90",
            "104": "Cell angle should NOT be 90",
            "105": "Cell lengths should be identical",
            "106": "Cell angle should be 120",
            "107": "Cell angle should be identical",
        }
)
class CSpaceGroupCell(CData):
    """Cell space group and parameters"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "format": attribute(
            AttributeType.STRING, default="unk", tooltip="format attribute"
        ),
        "merged": attribute(
            AttributeType.STRING, default="unk", tooltip="merged attribute"
        ),
        "crystalName": attribute(
            AttributeType.CUSTOM,
            custom_class="CCrystalName",
            tooltip="crystalName attribute",
        ),
        "datasetName": attribute(
            AttributeType.CUSTOM,
            custom_class="CDatasetName",
            tooltip="datasetName attribute",
        ),
        "cell": attribute(
            AttributeType.CUSTOM, custom_class="CCell", tooltip="cell attribute"
        ),
        "spaceGroup": attribute(
            AttributeType.CUSTOM,
            custom_class="CSpaceGroup",
            tooltip="spaceGroup attribute",
        ),
        "batchs": attribute(AttributeType.STRING, tooltip="batchs attribute"),
        "lowRes": attribute(AttributeType.FLOAT, tooltip="lowRes attribute"),
        "highRes": attribute(AttributeType.FLOAT, tooltip="highRes attribute"),
        "knowncell": attribute(AttributeType.BOOLEAN, tooltip="knowncell attribute"),
        "knownwavelength": attribute(
            AttributeType.BOOLEAN, tooltip="knownwavelength attribute"
        ),
        "numberLattices": attribute(
            AttributeType.INT, tooltip="numberLattices attribute"
        ),
        "wavelength": attribute(
            AttributeType.CUSTOM,
            custom_class="CWavelength",
            tooltip="wavelength attribute",
        ),
        "numberofdatasets": attribute(
            AttributeType.INT, tooltip="numberofdatasets attribute"
        ),
    },
    gui_label="CUnmergedDataContent",
)
class CUnmergedDataContent(CDataFileContent):
    """Generated CUnmergedDataContent class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CUnmergedDataFile(CDataFile):
    """Handle MTZ, XDS and scalepack files. Allow wildcard filename"""

    pass


class CUnmergedDataFileList(CList):
    """Generated CUnmergedDataFileList class from CData metadata."""

    pass


class CWavelength(CFloat):
    """Wavelength in Angstrom"""

    pass


@cdata_class(
attributes={
        "imageFile": attribute(AttributeType.STRING, tooltip="imageFile attribute"),
        "imageStart": attribute(AttributeType.INT, tooltip="imageStart attribute"),
        "imageEnd": attribute(AttributeType.INT, tooltip="imageEnd attribute"),
    },
    gui_label="CXia2ImageSelection",
    qualifiers={
            "toolTip": "select an image file and an optional range of files to define a dataset",
        }
)
class CXia2ImageSelection(CData):
    """Generated CXia2ImageSelection class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CXia2ImageSelectionList(CList):
    """Generated CXia2ImageSelectionList class from CData metadata."""

    pass
