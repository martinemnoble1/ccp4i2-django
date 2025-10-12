"""Generated classes from CCP4Annotation.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CAnnotation(CData):
    """Annotation text with user id and time"""

    text: Any = None
    time: Any = None
    author: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CAnnotationList(CData):
    """A list of annotation"""
    pass

class CAuthor(CData):
    """Placeholder for bibliographic author"""
    pass

class CBibReference(CData):
    """Bibliographic reference"""

    pmid: Any = None
    title: Any = None
    authorList: Any = None
    source: Any = None
    url: Any = None
    selected: Any = None

class CBibReferenceGroup(CData):
    """Set of bibliographic references for a task"""

    taskName: Any = None
    version: Any = None
    title: Any = None
    references: Any = None

class CDateRange(CData):
    """A date range - may be on a scale of years,months or days"""

    year: Any = None
    month: Any = "January"
    day: Any = 1
    yearRange: Any = 0
    monthRange: Any = 0
    dayRange: Any = 0

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CFont(CData):
    """Simplified Qt font options"""

    family: Any = "Helvetica"
    style: Any = "StyleNormal"
    pointSize: Any = 12
    weight: Any = 50

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CHostName(CData):
    """Computer name"""
    pass

class CMetaDataTag(CData):
    """This class will extend list of enumerators if new value for string is entered"""

    tag: Any = None

class CMetaDataTagList(CData):
    """Generated CMetaDataTagList class from CData metadata."""
    pass

class CServerGroup(CData):
    """Generated CServerGroup class from CData metadata."""

    name: Any = None
    mechanism: Any = "ssh"
    serverList: Any = None
    userExtensible: Any = False
    customCodeFile: Any = None
    queueOptionsFile: Any = None
    ccp4Dir: Any = None
    tempDir: Any = None
    sge_root: Any = None
    keyFilename: Any = None
    validate: Any = "password"
    timeout: Any = None
    maxTries: Any = 2

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CTime(CData):
    """The time. Uses Python time module"""
    pass

class CUserAddress(CData):
    """User id and platform node"""

    platformNode: Any = None
    userId: Any = None

class CUserId(CData):
    """A user ID"""
    pass
