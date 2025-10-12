"""Generated classes from CCP4Annotation.py"""

from typing import List, Any, Optional
from .base_classes import CData, CInt, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "text": attribute(AttributeType.STRING, tooltip="text attribute"),
        "time": attribute(AttributeType.STRING, tooltip="time attribute"),
        "author": attribute(AttributeType.STRING, tooltip="author attribute"),
    },
    qualifiers={
        "label": "Annotation",
        "toolTip": "Enter your comments",
    },
    gui_label="CAnnotation",
)
class CAnnotation(CData):
    """Annotation text with user id and time"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(gui_label="CAnnotationList")
class CAnnotationList(CList):
    """A list of annotation"""

    pass


@cdata_class(gui_label="CAuthor")
class CAuthor(CString):
    """Placeholder for bibliographic author"""

    pass


@cdata_class(
    attributes={
        "pmid": attribute(AttributeType.INT, tooltip="pmid attribute"),
        "title": attribute(AttributeType.STRING, tooltip="title attribute"),
        "authorList": attribute(AttributeType.STRING, tooltip="authorList attribute"),
        "source": attribute(AttributeType.STRING, tooltip="source attribute"),
        "url": attribute(AttributeType.STRING, tooltip="url attribute"),
        "selected": attribute(AttributeType.BOOL, tooltip="selected attribute"),
    },
    error_codes={
        "101": "Failed to load Medline data",
    },
    gui_label="CBibReference",
)
class CBibReference(CData):
    """Bibliographic reference"""


@cdata_class(
    attributes={
        "taskName": attribute(AttributeType.STRING, tooltip="taskName attribute"),
        "version": attribute(AttributeType.STRING, tooltip="version attribute"),
        "title": attribute(AttributeType.STRING, tooltip="title attribute"),
        "references": attribute(AttributeType.STRING, tooltip="references attribute"),
    },
    error_codes={
        "100": "Failed attempting to load MedLine file - file not found",
        "101": "Failed attempting to find references file",
        "102": "Error copying file",
    },
    gui_label="CBibReferenceGroup",
)
class CBibReferenceGroup(CData):
    """Set of bibliographic references for a task"""


@cdata_class(
    attributes={
        "year": attribute(AttributeType.INT, tooltip="year attribute"),
        "month": attribute(AttributeType.STRING, tooltip="month attribute"),
        "day": attribute(AttributeType.INT, tooltip="day attribute"),
        "yearRange": attribute(AttributeType.INT, tooltip="yearRange attribute"),
        "monthRange": attribute(AttributeType.INT, tooltip="monthRange attribute"),
        "dayRange": attribute(AttributeType.INT, tooltip="dayRange attribute"),
    },
    gui_label="CDateRange",
)
class CDateRange(CData):
    """A date range - may be on a scale of years,months or days"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    attributes={
        "family": attribute(AttributeType.STRING, tooltip="family attribute"),
        "style": attribute(AttributeType.INT, tooltip="style attribute"),
        "pointSize": attribute(AttributeType.INT, tooltip="pointSize attribute"),
        "weight": attribute(AttributeType.INT, tooltip="weight attribute"),
    },
    gui_label="CFont",
)
class CFont(CData):
    """Simplified Qt font options"""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "label": "Machine name",
        "toolTip": "Hostname as mycomputer.myplace.ac.uk",
    }
)
class CHostName(CString):
    """Computer name"""

    pass


@cdata_class(
    attributes={
        "tag": attribute(AttributeType.STRING, tooltip="tag attribute"),
    },
    qualifiers={
        "enumeratorsFunction": None,
        "addEnumeratorFunction": None,
    },
    gui_label="CMetaDataTag",
)
class CMetaDataTag(CData):
    """This class will extend list of enumerators if new value for string is entered"""


@cdata_class(
    qualifiers={
        "listMinLength": 1,
    },
    gui_label="CMetaDataTagList",
)
class CMetaDataTagList(CList):
    """Generated CMetaDataTagList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "mechanism": attribute(AttributeType.STRING, tooltip="mechanism attribute"),
        "serverList": attribute(AttributeType.STRING, tooltip="serverList attribute"),
        "userExtensible": attribute(
            AttributeType.BOOL, tooltip="userExtensible attribute"
        ),
        "customCodeFile": attribute(
            AttributeType.FILE, tooltip="customCodeFile attribute"
        ),
        "queueOptionsFile": attribute(
            AttributeType.FILE, tooltip="queueOptionsFile attribute"
        ),
        "ccp4Dir": attribute(AttributeType.STRING, tooltip="ccp4Dir attribute"),
        "tempDir": attribute(AttributeType.STRING, tooltip="tempDir attribute"),
        "sge_root": attribute(AttributeType.STRING, tooltip="sge_root attribute"),
        "keyFilename": attribute(AttributeType.STRING, tooltip="keyFilename attribute"),
        "validate": attribute(AttributeType.STRING, tooltip="validate attribute"),
        "timeout": attribute(AttributeType.FLOAT, tooltip="timeout attribute"),
        "maxTries": attribute(AttributeType.INT, tooltip="maxTries attribute"),
    },
    gui_label="CServerGroup",
)
class CServerGroup(CData):
    """Generated CServerGroup class from CData metadata."""

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors


@cdata_class(
    qualifiers={
        "min": 0,
        "label": "Time",
        "toolTip": "Time and date as hh:mm dd/mm/yyyy",
        "format": "%H:%M %d/%b/%y",
    },
    gui_label="CTime",
)
class CTime(CInt):
    """The time. Uses Python time module"""

    pass


class CUserAddress(CData):
    """User id and platform node"""


class CUserId(CString):
    """A user ID"""

    pass
