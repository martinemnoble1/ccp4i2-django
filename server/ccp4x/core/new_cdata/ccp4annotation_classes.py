"""Generated classes from CCP4Annotation.py"""

from typing import List, Any, Optional
from .base_classes import CData
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "text": attribute(AttributeType.STRING, tooltip="text attribute"),
        "time": attribute(
            AttributeType.CUSTOM,
            custom_class="CTime",
            default=None,
            tooltip="time attribute",
        ),
        "author": attribute(
            AttributeType.CUSTOM,
            custom_class="CUserId",
            default=None,
            tooltip="author attribute",
        ),
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


class CAnnotationList(CData):
    """A list of annotation"""

    pass


class CAuthor(CData):
    """Placeholder for bibliographic author"""

    pass


@cdata_class(
    attributes={
        "pmid": attribute(AttributeType.INT, tooltip="pmid attribute"),
        "title": attribute(AttributeType.STRING, tooltip="title attribute"),
        "authorList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="authorList attribute"
        ),
        "source": attribute(AttributeType.STRING, tooltip="source attribute"),
        "url": attribute(AttributeType.STRING, tooltip="url attribute"),
        "selected": attribute(AttributeType.BOOLEAN, tooltip="selected attribute"),
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
        "references": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="references attribute"
        ),
    },
    gui_label="CBibReferenceGroup",
)
class CBibReferenceGroup(CData):
    """Set of bibliographic references for a task"""


@cdata_class(
    attributes={
        "year": attribute(AttributeType.INT, tooltip="year attribute"),
        "month": attribute(
            AttributeType.STRING, default="January", tooltip="month attribute"
        ),
        "day": attribute(AttributeType.INT, default=1, tooltip="day attribute"),
        "yearRange": attribute(
            AttributeType.INT, default=0, tooltip="yearRange attribute"
        ),
        "monthRange": attribute(
            AttributeType.INT, default=0, tooltip="monthRange attribute"
        ),
        "dayRange": attribute(
            AttributeType.INT, default=0, tooltip="dayRange attribute"
        ),
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
        "family": attribute(
            AttributeType.STRING, default="Helvetica", tooltip="family attribute"
        ),
        "style": attribute(
            AttributeType.INT, default="StyleNormal", tooltip="style attribute"
        ),
        "pointSize": attribute(
            AttributeType.INT, default=12, tooltip="pointSize attribute"
        ),
        "weight": attribute(AttributeType.INT, default=50, tooltip="weight attribute"),
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


class CHostName(CData):
    """Computer name"""

    pass


@cdata_class(
    attributes={
        "tag": attribute(AttributeType.STRING, tooltip="tag attribute"),
    },
    gui_label="CMetaDataTag",
)
class CMetaDataTag(CData):
    """This class will extend list of enumerators if new value for string is entered"""


class CMetaDataTagList(CData):
    """Generated CMetaDataTagList class from CData metadata."""

    pass


@cdata_class(
    attributes={
        "name": attribute(AttributeType.STRING, tooltip="name attribute"),
        "mechanism": attribute(
            AttributeType.STRING, default="ssh", tooltip="mechanism attribute"
        ),
        "serverList": attribute(
            AttributeType.CUSTOM, custom_class="CList", tooltip="serverList attribute"
        ),
        "userExtensible": attribute(
            AttributeType.BOOLEAN, default=False, tooltip="userExtensible attribute"
        ),
        "customCodeFile": attribute(
            AttributeType.CUSTOM,
            custom_class="CDataFile",
            tooltip="customCodeFile attribute",
        ),
        "queueOptionsFile": attribute(
            AttributeType.CUSTOM,
            custom_class="CDataFile",
            tooltip="queueOptionsFile attribute",
        ),
        "ccp4Dir": attribute(AttributeType.STRING, tooltip="ccp4Dir attribute"),
        "tempDir": attribute(AttributeType.STRING, tooltip="tempDir attribute"),
        "sge_root": attribute(AttributeType.STRING, tooltip="sge_root attribute"),
        "keyFilename": attribute(AttributeType.STRING, tooltip="keyFilename attribute"),
        "validate": attribute(
            AttributeType.STRING, default="password", tooltip="validate attribute"
        ),
        "timeout": attribute(AttributeType.FLOAT, tooltip="timeout attribute"),
        "maxTries": attribute(
            AttributeType.INT, default=2, tooltip="maxTries attribute"
        ),
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


class CTime(CData):
    """The time. Uses Python time module"""

    pass


@cdata_class(
    attributes={
        "platformNode": attribute(
            AttributeType.STRING, tooltip="platformNode attribute"
        ),
        "userId": attribute(
            AttributeType.CUSTOM, custom_class="CUserId", tooltip="userId attribute"
        ),
    },
    gui_label="CUserAddress",
)
class CUserAddress(CData):
    """User id and platform node"""


class CUserId(CData):
    """A user ID"""

    pass
