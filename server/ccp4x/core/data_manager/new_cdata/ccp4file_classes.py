"""Generated classes from CCP4File.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CDataFileContent(CData):
    """Base class for classes holding file contents"""
    pass

class CDataReflFile(CData):
    """Reflection file from DIALS"""
    pass

class CExePath(CData):
    """Generated CExePath class from CData metadata."""

    exeName: Any = None
    exePath: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CExePathList(CData):
    """Generated CExePathList class from CData metadata."""
    pass

class CExportedFile(CData):
    """Generated CExportedFile class from CData metadata."""

    exportId: Any = None

class CExportedFileList(CData):
    """Generated CExportedFileList class from CData metadata."""
    pass

class CFileFunction(CData):
    """List of recognised XML file functions"""
    pass

class CFilePath(CData):
    """A file path"""
    pass

class CI2XmlHeader(CData):
    """Container for header info from XML file"""

    function: Any = None
    userId: Any = None
    hostName: Any = None
    creationTime: Any = None
    ccp4iVersion: Any = None
    pluginName: Any = None
    pluginVersion: Any = None
    pluginTitle: Any = None
    projectName: Any = None
    projectId: Any = None
    jobId: Any = None
    jobNumber: Any = None
    comment: Any = None
    OS: Any = None

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

class CSearchPath(CData):
    """Generated CSearchPath class from CData metadata."""

    name: Any = None
    path: Any = None

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
