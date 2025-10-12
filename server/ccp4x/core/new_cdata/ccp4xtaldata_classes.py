"""Generated classes from CCP4XtalData.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile, CDataFileContent, CFloat, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(gui_label="CAltSpaceGroupList")
class CAltSpaceGroupList(CList):
    """Generated CAltSpaceGroupList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "moleculeType": attribute(AttributeType.STRING, tooltip="Molecule type"),
        "seqFile": attribute(AttributeType.STRING, tooltip="seqFile attribute"),
        "numberOfCopies": attribute(
            AttributeType.INT, tooltip="Number of copies of sequence"
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


@cdata_class(
    qualifiers={
        "listMinLength": 1,
        "guiLabel": "Contents of asymmetric unit",
    },
    gui_label="CAsuComponentList",
)
class CAsuComponentList(CList):
    """Generated CAsuComponentList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "a": attribute(AttributeType.STRING, tooltip="Cell length a in A"),
        "b": attribute(AttributeType.STRING, tooltip="Cell length b in A"),
        "c": attribute(AttributeType.STRING, tooltip="Cell length c in A"),
        "alpha": attribute(AttributeType.STRING, tooltip="Cell angle alpha in degrees"),
        "beta": attribute(AttributeType.STRING, tooltip="Cell angle beta in degrees"),
        "gamma": attribute(AttributeType.STRING, tooltip="Cell angle gamma in degrees"),
    },
    qualifiers={
        "toolTip": "Cell lengths and angles",
        "helpFile": "crystal_data#cell",
    },
    gui_label="CCell",
    contents_order=["a", "b", "c", "alpha", "beta", "gamma"],
)
class CCell(CData):
    """A unit cell"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "min": 0.0,
        "max": 180.0,
        "default": None,
        "allowUndefined": True,
        "toolTip": "Cell angle in degrees",
    },
    gui_label="CCellAngle",
)
class CCellAngle(CFloat):
    """A cell angle"""

    pass


@cdata_class(
    qualifiers={
        "min": 0.0,
        "default": None,
        "allowUndefined": False,
        "toolTip": "Cell length in A",
    },
    gui_label="CCellLength",
)
class CCellLength(CFloat):
    """A cell length"""

    pass


@cdata_class(
    attributes={
        "columnGroupType": attribute(
            AttributeType.STRING, tooltip="columnGroupType attribute"
        ),
        "contentFlag": attribute(AttributeType.INT, tooltip="contentFlag attribute"),
        "dataset": attribute(AttributeType.STRING, tooltip="dataset attribute"),
        "columnList": attribute(AttributeType.STRING, tooltip="columnList attribute"),
        "selected": attribute(AttributeType.BOOL, tooltip="selected attribute"),
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
            AttributeType.INT, tooltip="partnerOffset attribute"
        ),
    },
    error_codes={
        "1": "Attempting to change immutable object",
        "2": "Attempting to access unknown attribute",
    },
    gui_label="CColumnGroupItem",
)
class CColumnGroupItem(CData):
    """Definition of set of columns that form a 'group'"""


@cdata_class(gui_label="CColumnGroupList")
class CColumnGroupList(CList):
    """Generated CColumnGroupList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "enumerators": [
            "H",
            "J",
            "F",
            "D",
            "Q",
            "G",
            "L",
            "K",
            "M",
            "E",
            "P",
            "W",
            "A",
            "B",
            "Y",
            "I",
            "R",
        ],
        "onlyEnumerators": True,
        "default": "F",
    },
    gui_label="CColumnType",
)
class CColumnType(CString):
    """A list of recognised MTZ column types"""

    pass


@cdata_class(gui_label="CColumnTypeList")
class CColumnTypeList(CList):
    """A list of acceptable MTZ column types"""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": False,
        "minLength": 1,
        "allowedChars": 1,
        "toolTip": "Unique identifier for crystal (one word)",
    },
    gui_label="CCrystalName",
)
class CCrystalName(CString):
    """Generated CCrystalName class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "selected": attribute(AttributeType.BOOL, tooltip="selected attribute"),
        "obsDataFile": attribute(AttributeType.STRING, tooltip="obsDataFile attribute"),
        "crystalName": attribute(AttributeType.STRING, tooltip="crystalName attribute"),
        "datasetName": attribute(AttributeType.STRING, tooltip="datasetName attribute"),
        "formFactors": attribute(AttributeType.STRING, tooltip="formFactors attribute"),
        "formFactorSource": attribute(
            AttributeType.STRING, tooltip="formFactorSource attribute"
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


@cdata_class(gui_label="CDatasetList")
class CDatasetList(CList):
    """Generated CDatasetList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": False,
        "allowedChars": 1,
        "minLength": 1,
        "toolTip": "Unique identifier for dataset (one word)",
    },
    gui_label="CDatasetName",
)
class CDatasetName(CString):
    """Generated CDatasetName class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/dials-jfile",
        "mimeTypeDescription": "Dials json data file",
        "fileExtensions": ["json", "expt", "jsn"],
        "fileContentClassName": None,
        "fileLabel": "dials_jdata",
        "guiLabel": "json data",
        "toolTip": "json data files",
    },
    gui_label="CDialsJsonFile",
)
class CDialsJsonFile(CDataFile):
    """Generated CDialsJsonFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/dials-pfile",
        "mimeTypeDescription": "Dials pickle data file",
        "fileExtensions": ["pickle", "refl"],
        "fileContentClassName": None,
        "fileLabel": "dials_pdata",
        "guiLabel": "Xia2/Dials pickle data",
        "toolTip": "Xia2/Dials pickle data files",
    },
    gui_label="CDialsPickleFile",
)
class CDialsPickleFile(CDataFile):
    """Generated CDialsPickleFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "onlyEnumerators": True,
        "enumerators": [
            "native",
            "derivative",
            "SAD",
            "peak",
            "inflection",
            "high_remote",
            "low_remote",
            "",
        ],
        "default": "SAD",
    },
    gui_label="CExperimentalDataType",
)
class CExperimentalDataType(CString):
    """Experimental data type e.g. native or peak"""

    pass


@cdata_class(gui_label="CFormFactor", contents_order=["Fp", "Fpp"])
class CFormFactor(CData):
    """The for factor (Fp and Fpp) for a giving element and wavelength"""


@cdata_class(
    qualifiers={
        "guiLabel": "Reflection data",
        "mimeTypeName": "application/CCP4-generic-reflections",
        "toolTip": "A reflection data file in MTZ or a non-CCP4 format",
        "fileContentClassName": "CUnmergedDataContent",
        "fileExtensions": ["mtz", "hkl", "HKL", "sca", "SCA", "mmcif", "cif", "ent"],
        "downloadModes": ["ebiSFs"],
        "helpFile": "import_merged#file_formats",
    },
    gui_label="CGenericReflDataFile",
)
class CGenericReflDataFile(CDataFile):
    """Generated CGenericReflDataFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/CCP4-image",
        "mimeTypeDescription": "Image file",
        "fileExtensions": ["img", "cbf", "mccd", "mar1600", "h5", "nxs"],
        "fileContentClassName": None,
        "guiLabel": "Image file",
        "toolTip": "First image file in a directory",
    },
    gui_label="CImageFile",
)
class CImageFile(CDataFile):
    """Generated CImageFile class from CData metadata."""

    pass


@cdata_class(gui_label="CImageFileList")
class CImageFileList(CList):
    """Generated CImageFileList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "fileLabel": "imosflm",
        "mimeTypeName": "application/iMosflm-xml",
        "mimeTypeDescription": "iMosflm data",
        "guiLabel": "iMosflm data",
        "fileExtensions": ["imosflm.xml"],
        "fileContentClassName": None,
    },
    gui_label="CImosflmXmlDataFile",
)
class CImosflmXmlDataFile(CDataFile):
    """An iMosflm data file"""

    pass


@cdata_class(
    attributes={
        "file": attribute(AttributeType.STRING, tooltip="file attribute"),
        "cell": attribute(AttributeType.STRING, tooltip="cell attribute"),
        "wavelength": attribute(AttributeType.STRING, tooltip="wavelength attribute"),
        "crystalName": attribute(AttributeType.STRING, tooltip="crystalName attribute"),
        "dataset": attribute(AttributeType.STRING, tooltip="dataset attribute"),
        "excludeSelection": attribute(
            AttributeType.STRING, tooltip="excludeSelection attribute"
        ),
    },
    qualifiers={
        "toolTip": "Imported data file, cell parameters and crystal/dataset identifiers",
        "helpFile": "import_merged#file_formats",
    },
    gui_label="CImportUnmerged",
    contents_order=["file", "crystalName", "dataset", "excludeSelection"],
)
class CImportUnmerged(CData):
    """Generated CImportUnmerged class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "listMinLength": 1,
    },
    gui_label="CImportUnmergedList",
)
class CImportUnmergedList(CList):
    """Generated CImportUnmergedList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/CCP4-map",
        "mimeTypeDescription": "Map",
        "fileExtensions": ["map", "mrc"],
        "fileContentClassName": None,
        "guiLabel": "Map",
        "toolTip": "A map in CCP4/MRC format",
        "helpFile": "data_files#map_files",
    },
    gui_label="CMapDataFile",
)
class CMapDataFile(CDataFile):
    """A CCP4 Map file"""

    pass


@cdata_class(
    attributes={
        "fileName": attribute(AttributeType.STRING, tooltip="fileName attribute"),
        "columnTag": attribute(AttributeType.STRING, tooltip="columnTag attribute"),
        "columnNames": attribute(AttributeType.STRING, tooltip="columnNames attribute"),
    },
    error_codes={
        "201": "Selected file is not a suitable 'mini' MTZ containing experimental data object",
        "202": "Output column name list does not have correct number of names",
    },
    gui_label="CMergeMiniMtz",
    contents_order=["fileName", "columnTag", "columnNames"],
)
class CMergeMiniMtz(CData):
    """Generated CMergeMiniMtz class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "listMinLength": 2,
        "saveToDb": True,
    },
    gui_label="CMergeMiniMtzList",
)
class CMergeMiniMtzList(CList):
    """Generated CMergeMiniMtzList class from CData metadata."""

    pass


@cdata_class(gui_label="CMiniMtzDataFileList")
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
        "cell": attribute(AttributeType.STRING, tooltip="cell attribute"),
        "spaceGroup": attribute(AttributeType.STRING, tooltip="spaceGroup attribute"),
        "resolutionRange": attribute(
            AttributeType.STRING, tooltip="resolutionRange attribute"
        ),
        "listOfColumns": attribute(
            AttributeType.STRING, tooltip="listOfColumns attribute"
        ),
        "datasets": attribute(AttributeType.STRING, tooltip="datasets attribute"),
        "crystalNames": attribute(
            AttributeType.STRING, tooltip="crystalNames attribute"
        ),
        "wavelengths": attribute(AttributeType.STRING, tooltip="wavelengths attribute"),
        "datasetCells": attribute(
            AttributeType.STRING, tooltip="datasetCells attribute"
        ),
        "merged": attribute(AttributeType.BOOL, tooltip="merged attribute"),
    },
    gui_label="CMtzData",
)
class CMtzData(CDataFileContent):
    """Generated CMtzData class from CData metadata."""

    pass


@cdata_class(
    gui_label="CMtzDataFile",
    qualifiers_definition={
        "sameCrystalAs": {
            "type": "str",
            "description": "Name of CMtzDataFile object that crystal parameters should match - probably the observed data",
        },
        "sameCrystalLevel": {
            "type": "int",
            "description": "Rigour of same crystal test",
        },
    },
)
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


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/phaser-rfile",
        "mimeTypeDescription": "Phaser rotation solution file",
        "fileExtensions": ["phaser_rlist.pkl"],
        "fileContentClassName": None,
        "fileLabel": "phaser_rfile",
        "guiLabel": "Phaser rotation solution",
        "toolTip": "Phaser rfile solutions for rotation search",
    },
    gui_label="CPhaserRFileDataFile",
)
class CPhaserRFileDataFile(CDataFile):
    """Generated CPhaserRFileDataFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/phaser-sol",
        "mimeTypeDescription": "Phaser solution file",
        "fileExtensions": ["phaser_sol.pkl"],
        "fileContentClassName": None,
        "fileLabel": "phaser_sol",
        "guiLabel": "Phaser solutions",
        "toolTip": "Possible solutions passed between runs of the Phaser program",
        "helpFile": "data_files#phasersol",
    },
    gui_label="CPhaserSolDataFile",
)
class CPhaserSolDataFile(CDataFile):
    """Generated CPhaserSolDataFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mustExist": False,
        "mtzFileKey": "",
        "toolTipList": [],
        "default": [],
    },
    error_codes={
        "101": "Column not in MTZ file",
        "102": "Column wrong type",
        "103": "Error setting columnGroup qualifier",
        "104": "Missing column selection",
        "105": "Specified column not found in MTZ file",
        "106": "Specified column has wrong type in MTZ file",
        "107": "Error reading columnGroup qualifier from XML file",
        "108": "No columnGroup qualifier",
    },
    gui_label="CProgramColumnGroup",
    qualifiers_order=["mtzFileKey", "mustExist", "toolTipList", "default"],
    qualifiers_definition={
        "mtzFileKey": {
            "type": "str",
            "description": "The key for a CMtxDataFile in the same CContainer",
        },
        "mustExist": {
            "type": "bool",
            "description": "Flag if the parameter must be set at run time",
        },
        "toolTipList": {"type": "list", "description": "Tooltips for columns in group"},
        "default": {
            "type": "list",
            "listItemType": "str",
            "description": "Preferred values for column names",
        },
    },
)
class CProgramColumnGroup(CData):
    """A group of MTZ columns required for program input"""

    pass


@cdata_class(
    attributes={
        "columnGroup": attribute(AttributeType.STRING, tooltip="columnGroup attribute"),
        "datasetName": attribute(AttributeType.STRING, tooltip="datasetName attribute"),
    },
    qualifiers={
        "mustExist": False,
        "mtzFileKey": "",
        "groupTypes": [],
    },
    gui_label="CProgramColumnGroup0",
    qualifiers_order=["groupTypes", "mtzFileKey", "mustExist"],
    qualifiers_definition={
        "groupTypes": {
            "type": "list",
            "description": "Type of columnGroup required by program",
        },
        "mtzFileKey": {
            "type": "str",
            "description": "The key for a CMtxDataFile in the same CContainer",
        },
        "mustExist": {
            "type": "bool",
            "description": "Flag if the parameter must be set at run time",
        },
    },
)
class CProgramColumnGroup0(CData):
    """Generated CProgramColumnGroup0 class from CData metadata."""


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/refmac-keywords",
        "mimeTypeDescription": "Refmac keyword file",
        "fileExtensions": ["txt"],
        "fileContentClassName": None,
        "fileLabel": "refmac_keywords",
        "guiLabel": "Refmac keyword file",
        "toolTip": "A file containing keywords as they are meant to be read by refmac5",
    },
    gui_label="CRefmacKeywordFile",
)
class CRefmacKeywordFile(CDataFile):
    """Generated CRefmacKeywordFile class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "h": attribute(AttributeType.STRING, tooltip="h attribute"),
        "k": attribute(AttributeType.STRING, tooltip="k attribute"),
        "l": attribute(AttributeType.STRING, tooltip="l attribute"),
    },
    error_codes={
        "201": "Operator has bad syntax (needs three comma-separated fields)",
        "202": "Operator contains invalid characters",
        "203": "Operator is not set",
    },
    gui_label="CReindexOperator",
    contents_order=["h", "k", "l"],
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
    error_codes={
        "201": "High/low resolution wrong way round?",
    },
    gui_label="CResolutionRange",
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
    qualifiers={
        "toolTip": "Specify range of reflections to treat as one run",
    },
    error_codes={
        "101": "End of batch range less than start",
        "102": "All items must be set",
    },
    gui_label="CRunBatchRange",
)
class CRunBatchRange(CData):
    """Generated CRunBatchRange class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "listMinLength": 1,
    },
    gui_label="CRunBatchRangeList",
)
class CRunBatchRangeList(CList):
    """Generated CRunBatchRangeList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/CCP4-shelx-FA",
        "mimeTypeDescription": "Shelx FA",
        "fileExtensions": ["hkl"],
        "fileContentClassName": None,
        "fileLabel": "shelx_FA",
        "guiLabel": "Shelx FA",
        "toolTip": "Data used by Shelx programs",
        "helpFile": "data_files#shelxfa",
    },
    gui_label="CShelxFADataFile",
)
class CShelxFADataFile(CDataFile):
    """Generated CShelxFADataFile class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "onlyEnumerators": True,
        "default": "UNDEFINED",
        "enumerators": ["UNDEFINED", "HREM", "LREM", "PEAK", "INFL", "NAT", "DERI"],
        "menuText": [
            "undefined",
            "high remote",
            "low remote",
            "peak",
            "inflection",
            "native",
            "derivative",
        ],
        "toolTip": "Hint to Shelx for the use of the dataset",
    },
    gui_label="CShelxLabel",
)
class CShelxLabel(CString):
    """Generated CShelxLabel class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": True,
        "toolTip": "Hermann-Mauguin space group name",
        "helpFile": "crystal_data#space_group",
    },
    gui_label="CSpaceGroup",
)
class CSpaceGroup(CString):
    """A string holding the space group"""

    pass


@cdata_class(
    attributes={
        "spaceGroup": attribute(AttributeType.STRING, tooltip="spaceGroup attribute"),
        "cell": attribute(AttributeType.STRING, tooltip="cell attribute"),
    },
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
    },
    gui_label="CSpaceGroupCell",
    contents_order=["spaceGroup", "cell"],
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
        "format": attribute(AttributeType.STRING, tooltip="format attribute"),
        "merged": attribute(AttributeType.STRING, tooltip="merged attribute"),
        "crystalName": attribute(AttributeType.STRING, tooltip="crystalName attribute"),
        "datasetName": attribute(AttributeType.STRING, tooltip="datasetName attribute"),
        "cell": attribute(AttributeType.STRING, tooltip="cell attribute"),
        "spaceGroup": attribute(AttributeType.STRING, tooltip="spaceGroup attribute"),
        "batchs": attribute(AttributeType.STRING, tooltip="batchs attribute"),
        "lowRes": attribute(AttributeType.FLOAT, tooltip="lowRes attribute"),
        "highRes": attribute(AttributeType.FLOAT, tooltip="highRes attribute"),
        "knowncell": attribute(AttributeType.BOOL, tooltip="knowncell attribute"),
        "knownwavelength": attribute(
            AttributeType.BOOL, tooltip="knownwavelength attribute"
        ),
        "numberLattices": attribute(
            AttributeType.INT, tooltip="numberLattices attribute"
        ),
        "wavelength": attribute(AttributeType.STRING, tooltip="wavelength attribute"),
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


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/CCP4-unmerged-experimental",
        "mimeTypeDescription": "Unmerged experimental data",
        "fileExtensions": ["mtz", "hkl", "HKL", "sca", "SCA", "ent", "cif"],
        "fileContentClassName": "CUnmergedDataContent",
        "guiLabel": "Unmerged reflections",
        "toolTip": "Unmerged experimental data in any format",
        "helpFile": "data_files#unmerged_data",
    },
    gui_label="CUnmergedDataFile",
)
class CUnmergedDataFile(CDataFile):
    """Handle MTZ, XDS and scalepack files. Allow wildcard filename"""

    pass


@cdata_class(gui_label="CUnmergedDataFileList")
class CUnmergedDataFileList(CList):
    """Generated CUnmergedDataFileList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "min": 0.0,
        "toolTip": "Data collection wavelength in Angstrom",
    },
    gui_label="CWavelength",
)
class CWavelength(CFloat):
    """Wavelength in Angstrom"""

    pass


@cdata_class(
    attributes={
        "imageFile": attribute(AttributeType.STRING, tooltip="imageFile attribute"),
        "imageStart": attribute(AttributeType.INT, tooltip="imageStart attribute"),
        "imageEnd": attribute(AttributeType.INT, tooltip="imageEnd attribute"),
    },
    qualifiers={
        "toolTip": "select an image file and an optional range of files to define a dataset",
    },
    gui_label="CXia2ImageSelection",
    contents_order=["imageFile", "imageStart", "imageEnd"],
)
class CXia2ImageSelection(CData):
    """Generated CXia2ImageSelection class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(gui_label="CXia2ImageSelectionList")
class CXia2ImageSelectionList(CList):
    """Generated CXia2ImageSelectionList class from CData metadata."""

    pass
