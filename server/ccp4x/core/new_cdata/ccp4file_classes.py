"""Generated classes from CCP4File.py"""

from typing import List, Optional
from .base_classes import CData, CDataFile, CContainer
from .class_metadata import cdata_class, attribute, AttributeType


class CDataFileContent(CData):
    """Base class for classes holding file contents"""

    pass


class CDataReflFile(CData):
    """Reflection file from DIALS"""

    pass


@cdata_class(
    attributes={
        "exeName": attribute(AttributeType.STRING, tooltip="exeName attribute"),
        "exePath": attribute(
            AttributeType.CUSTOM, custom_class="CDataFile", tooltip="exePath attribute"
        ),
    },
    gui_label="CExePath",
)
class CExePath(CData):
    """Generated CExePath class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


class CExePathList(CData):
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


class CExportedFileList(CData):
    """Generated CExportedFileList class from CData metadata."""

    pass


class CFileFunction(CData):
    """List of recognised XML file functions"""

    pass


class CFilePath(CData):
    """A file path"""

    pass


@cdata_class(
    attributes={
        "function": attribute(
            AttributeType.CUSTOM,
            custom_class="CFileFunction",
            tooltip="function attribute",
        ),
        "userId": attribute(
            AttributeType.CUSTOM, custom_class="CUserId", tooltip="userId attribute"
        ),
        "hostName": attribute(
            AttributeType.CUSTOM, custom_class="CHostName", tooltip="hostName attribute"
        ),
        "creationTime": attribute(
            AttributeType.CUSTOM, custom_class="CTime", tooltip="creationTime attribute"
        ),
        "ccp4iVersion": attribute(
            AttributeType.CUSTOM,
            custom_class="CVersion",
            tooltip="ccp4iVersion attribute",
        ),
        "pluginName": attribute(AttributeType.STRING, tooltip="pluginName attribute"),
        "pluginVersion": attribute(
            AttributeType.CUSTOM,
            custom_class="CVersion",
            tooltip="pluginVersion attribute",
        ),
        "pluginTitle": attribute(AttributeType.STRING, tooltip="pluginTitle attribute"),
        "projectName": attribute(
            AttributeType.CUSTOM,
            custom_class="CProjectName",
            tooltip="projectName attribute",
        ),
        "projectId": attribute(
            AttributeType.CUSTOM,
            custom_class="CProjectId",
            tooltip="projectId attribute",
        ),
        "jobId": attribute(AttributeType.UUID, tooltip="jobId attribute"),
        "jobNumber": attribute(AttributeType.STRING, tooltip="jobNumber attribute"),
        "comment": attribute(AttributeType.STRING, tooltip="comment attribute"),
        "OS": attribute(AttributeType.STRING, tooltip="OS attribute"),
    },
    gui_label="CI2XmlHeader",
)
@cdata_class(
    attributes={
        "function": attribute(
            AttributeType.CUSTOM,
            custom_class="CFileFunction",
            tooltip="function attribute",
        ),
        "userId": attribute(
            AttributeType.CUSTOM, custom_class="CUserId", tooltip="userId attribute"
        ),
        "hostName": attribute(
            AttributeType.CUSTOM, custom_class="CHostName", tooltip="hostName attribute"
        ),
        "creationTime": attribute(
            AttributeType.CUSTOM, custom_class="CTime", tooltip="creationTime attribute"
        ),
        "ccp4iVersion": attribute(
            AttributeType.CUSTOM,
            custom_class="CVersion",
            tooltip="ccp4iVersion attribute",
        ),
        "pluginName": attribute(AttributeType.STRING, tooltip="pluginName attribute"),
        "pluginVersion": attribute(
            AttributeType.CUSTOM,
            custom_class="CVersion",
            tooltip="pluginVersion attribute",
        ),
        "pluginTitle": attribute(AttributeType.STRING, tooltip="pluginTitle attribute"),
        "projectName": attribute(
            AttributeType.CUSTOM,
            custom_class="CProjectName",
            tooltip="projectName attribute",
        ),
        "projectId": attribute(AttributeType.PROJECT_ID, tooltip="projectId attribute"),
        "jobId": attribute(AttributeType.UUID, tooltip="jobId attribute"),
        "jobNumber": attribute(AttributeType.STRING, tooltip="jobNumber attribute"),
        "comment": attribute(AttributeType.STRING, tooltip="comment attribute"),
        "OS": attribute(AttributeType.STRING, tooltip="OS attribute"),
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


class CMmcifData(CData):
    """Generic mmCIF data.
    This is intended to be a base class for other classes
    specific to coordinates, reflections or geometry data."""

    pass


class CMmcifDataFile(CData):
    """A generic mmCIF format file.
    This is intended to be a base class for other classes
    specific to coordinates, reflections or geometry data."""

    pass


class CPDFDataFile(CData):
    """An PDF format file"""

    pass


class CPostscriptDataFile(CData):
    """A postscript format file"""

    pass


class CProjectName(CData):
    """The name of a CCP4i project or directory alias"""

    pass


class CSceneDataFile(CData):
    """An xml format file for defining scene in CCP4mg."""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "path": attribute(
            AttributeType.CUSTOM, custom_class="CDataFile", tooltip="path attribute"
        ),
    },
    gui_label="CSearchPath",
)
class CSearchPath(CData):
    """Generated CSearchPath class from CData metadata."""


class CSearchPathList(CData):
    """Generated CSearchPathList class from CData metadata."""

    pass


class CTextDataFile(CData):
    """A text data file"""

    pass


class CVersion(CData):
    """A (string) version number of the form n.m.i"""

    pass


class CXmgrDataFile(CData):
    """An xmgr format file. This is the input format for xmgrace, as output by scala or aimless"""

    pass


class CXmlDataFile(CData):
    """A reference to an XML file"""

    pass


class CYmlFile(CData):
    """A yml data file"""

    pass
