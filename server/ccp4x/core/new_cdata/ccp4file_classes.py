"""Generated classes from CCP4File.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile, CString
from .fundamental_types import CList
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(gui_label="CDataFileContent")
class CDataFileContent(CData):
    """Base class for classes holding file contents"""

    pass


@cdata_class(
    qualifiers={
        "guiLabel": "Reflections from DIALS",
        "fileExtensions": ["refl"],
    },
    gui_label="CDataReflFile",
)
class CDataReflFile(CDataFile):
    """Reflection file from DIALS"""

    pass


@cdata_class(
    attributes={
        "exeName": attribute(AttributeType.STRING, tooltip="exeName attribute"),
        "exePath": attribute(AttributeType.FILEPATH, tooltip="exePath attribute"),
    },
    gui_label="CExePath",
    contents_order=["exeName", "exePath"],
)
class CExePath(CData):
    """Generated CExePath class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "listMinLength": 1,
    },
    gui_label="CExePathList",
)
class CExePathList(CList):
    """Generated CExePathList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "exportId": attribute(AttributeType.UUID, tooltip="exportId attribute")
    },
    gui_label="CExportedFile",
)
class CExportedFile(CData):
    """Generated CExportedFile class from CData metadata."""


@cdata_class(gui_label="CExportedFileList")
class CExportedFileList(CList):
    """Generated CExportedFileList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "enumerators": [
            "DEF",
            "PARAMS",
            "LOG",
            "PROJECTDIRECTORIES",
            "COM",
            "REFMAC",
            "OUTPUT",
            "STATUS",
            "PROJECTDATABASE",
            "MGSCENE",
            "JOBSERVERSTATUS",
            "WORKFLOW",
            "COMFILEPATCH",
            "CUSTOMTASK",
            "IMPORTEDJOB",
            "I1SUPPLEMENT",
            "ASUCONTENT",
            "UNKNOWN",
        ],
        "onlyEnumerators": True,
    },
    gui_label="CFileFunction",
    qualifiers_definition={
        "enumerators": {"type": "list"},
        "onlyEnumerators": {"type": "bool", "editable": False},
    },
)
class CFileFunction(CString):
    """List of recognised XML file functions"""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": True,
        "allowedCharacters": "",
        "allowedCharactersMode": "ALLOWED_CHARACTERS_WARN",
        "default": None,
    },
    gui_label="CFilePath",
    qualifiers_order=[
        "allowUndefined",
        "allowedCharacters",
        "allowedCharactersMode",
        "default",
    ],
    qualifiers_definition={
        "allowUndefined": {
            "type": "bool",
            "description": "Flag if allow undefined value at run time",
        },
        "allowedCharacters": {
            "type": "str",
            "description": "Set of characters allowed in file name",
        },
        "allowedCharactersMode": {
            "type": "int",
            "description": "Handling of violation of allowed characters",
        },
        "default": {"type": "str", "description": "Default file path"},
    },
)
class CFilePath(CString):
    """A file path"""

    pass


@cdata_class(
    attributes={
        "function": attribute(AttributeType.STRING, tooltip="function attribute"),
        "userId": attribute(AttributeType.STRING, tooltip="userId attribute"),
        "hostName": attribute(AttributeType.STRING, tooltip="hostName attribute"),
        "creationTime": attribute(
            AttributeType.STRING, tooltip="creationTime attribute"
        ),
        "ccp4iVersion": attribute(
            AttributeType.STRING, tooltip="ccp4iVersion attribute"
        ),
        "pluginName": attribute(AttributeType.STRING, tooltip="pluginName attribute"),
        "pluginVersion": attribute(
            AttributeType.STRING, tooltip="pluginVersion attribute"
        ),
        "pluginTitle": attribute(AttributeType.STRING, tooltip="pluginTitle attribute"),
        "projectName": attribute(AttributeType.STRING, tooltip="projectName attribute"),
        "projectId": attribute(AttributeType.STRING, tooltip="projectId attribute"),
        "jobId": attribute(AttributeType.STRING, tooltip="jobId attribute"),
        "jobNumber": attribute(AttributeType.STRING, tooltip="jobNumber attribute"),
        "comment": attribute(AttributeType.STRING, tooltip="comment attribute"),
        "OS": attribute(AttributeType.STRING, tooltip="OS attribute"),
    },
    error_codes={
        "101": "Attempting to read header from non-existant Xml file",
        "102": "Error loading file to read header",
        "103": "Error finding <ccp4i2_header> in file",
        "104": "Error interpreting header from file",
        "105": "File does not have <ccp4i2> root node",
    },
    gui_label="CI2XmlHeader",
)
class CI2XmlHeader(CData):
    """Container for header info from XML file"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(gui_label="CMmcifData")
class CMmcifData(CDataFileContent):
    """Generic mmCIF data.
    This is intended to be a base class for other classes
    specific to coordinates, reflections or geometry data."""

    pass


@cdata_class(
    qualifiers={
        "fileExtensions": ["cif", "ent"],
    },
    gui_label="CMmcifDataFile",
)
class CMmcifDataFile(CDataFile):
    """A generic mmCIF format file.
    This is intended to be a base class for other classes
    specific to coordinates, reflections or geometry data."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/x-pdf",
        "fileExtensions": ["pdf"],
        "guiLabel": "PDF file",
    },
    gui_label="CPDFDataFile",
)
class CPDFDataFile(CDataFile):
    """An PDF format file"""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/postscript",
        "fileExtensions": ["ps"],
        "guiLabel": "Postscript file",
    },
    gui_label="CPostscriptDataFile",
)
class CPostscriptDataFile(CDataFile):
    """A postscript format file"""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": True,
        "allowAlias": True,
        "allowUnfound": True,
        "default": None,
    },
    gui_label="CProjectName",
    qualifiers_order=["allowUndefined", "allowAlias", "allowUnfound", "default"],
    qualifiers_definition={
        "allowUndefined": {
            "type": "bool",
            "description": "Flag if allow undefined value at run time",
        },
        "allowAlias": {
            "type": "bool",
            "description": "Flag if allow project to be directory alias at run time",
        },
        "allowUnfound": {
            "type": "bool",
            "description": "Flag if allow unfound project at run time",
        },
        "default": {"type": "str"},
    },
)
class CProjectName(CString):
    """The name of a CCP4i project or directory alias"""

    pass


@cdata_class(
    qualifiers={
        "fileLabel": "scene",
        "mimeTypeName": "application/CCP4-scene",
        "mimeTypeDescription": "CCP4mg scene file",
        "guiLabel": "CCP4mg scene",
        "fileExtensions": ["scene.xml"],
        "fileContentClassName": "NotImplemented",
    },
    gui_label="CSceneDataFile",
)
class CSceneDataFile(CDataFile):
    """An xml format file for defining scene in CCP4mg."""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "path": attribute(AttributeType.FILEPATH, tooltip="path attribute"),
    },
    gui_label="CSearchPath",
)
class CSearchPath(CData):
    """Generated CSearchPath class from CData metadata."""


@cdata_class(gui_label="CSearchPathList")
class CSearchPathList(CList):
    """Generated CSearchPathList class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": '"text/plain"',
        "mimeTypeDescription": "Standard plain text",
        "fileLabel": None,
        "fileExtensions": ["txt", "log"],
    },
    gui_label="CTextDataFile",
)
class CTextDataFile(CDataFile):
    """A text data file"""

    pass


@cdata_class(
    qualifiers={
        "allowUndefined": True,
        "default": None,
        "charWidth": 10,
    },
    error_codes={
        "101": "Version is not of form n.m or n.m.i",
    },
    gui_label="CVersion",
    qualifiers_order=["allowUndefined", "default", "charWidth"],
    qualifiers_definition={
        "allowUndefined": {
            "type": "bool",
            "description": "Flag if allow an unset value at run time",
        },
        "default": {"description": "A default value"},
        "charWidth": {
            "type": "int",
            "description": "Number of characters allowed for widget in GUI",
        },
    },
)
class CVersion(CString):
    """A (string) version number of the form n.m.i"""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": "application/grace",
        "fileExtensions": ["xmgr"],
    },
    gui_label="CXmgrDataFile",
)
class CXmgrDataFile(CDataFile):
    """An xmgr format file. This is the input format for xmgrace, as output by scala or aimless"""

    pass


@cdata_class(
    qualifiers={
        "fileExtensions": ["xml"],
        "saveToDb": False,
        "mimeTypeName": "application/xml",
    },
    error_codes={
        "1001": "Unknown error reading XML file",
        "1002": "Error trying to find root node in XML",
        "1006": "Attempting to save XML file with incorrect body",
        "1007": "Error creating XML text",
        "1008": "Error saving XML text to file",
        "1009": "Error reading XML file",
        "1010": "XML file does not exist",
        "1011": "No file name given for making I2XMlDataFile",
        "1012": "Error creating I2XMlDataFile object",
        "1013": "Error creating I2XMlDataFile file",
    },
    gui_label="CXmlDataFile",
)
class CXmlDataFile(CDataFile):
    """A reference to an XML file"""

    pass


@cdata_class(
    qualifiers={
        "mimeTypeName": '"text/plain"',
        "mimeTypeDescription": "Standard plain text",
        "guiLabel": "yml file",
        "fileExtensions": ["yml"],
    },
    gui_label="CYmlFile",
)
class CYmlFile(CDataFile):
    """A yml data file"""

    pass
