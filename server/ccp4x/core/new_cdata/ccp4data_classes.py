"""Generated classes from CCP4Data.py"""

from typing import List, Any, Optional
from .base_classes import CData, CInt, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    qualifiers={
        "default": "NotImplemented",
        "charWidth": 10,
    },
    qualifiers_order=["charWidth"],
    qualifiers_definition={
        "charWidth": {"type": "int"},
    },
)
class CBaseData(CData):
    """Base class for simple classes"""

    pass


@cdata_class(gui_label="CCollection")
class CCollection(CData):
    """Generated CCollection class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "enumerators": [
            "CPdbDataFile",
            "CSeqDataFile",
            "CObsDataFile",
            "CPhsDataFile",
            "CMapCoeffsDataFile",
            "CFreeRDataFile",
            "CMtzDataFile",
            "CDictDataFile",
            "CDataFile",
            "CInt",
            "CFloat",
            "CString",
            "CRefmacKeywordFile",
        ],
        "menuText": [],
    }
)
class CI2DataType(CString):
    """Generated CI2DataType class from CData metadata."""

    pass


@cdata_class(gui_label="CJobStatus")
class CJobStatus(CInt):
    """Generated CJobStatus class from CData metadata."""

    pass


@cdata_class(gui_label="CJobTitle")
class CJobTitle(CString):
    """Generated CJobTitle class from CData metadata."""

    pass


@cdata_class(error_codes={"201": "Word contains white space item"})
class COneWord(CString):
    """A single word string - no white space"""

    pass


@cdata_class(
    qualifiers={
        "default": "NotImplemented",
        "listMinLength": 0,
        "listMaxLength": 250,
        "listCompare": "NotImplemented",
        "nameRoot": "NotImplemented",
    },
    gui_label="COutputFileList",
    qualifiers_order=["listMinLength", "listMaxLength", "listCompare", "nameRoot"],
    qualifiers_definition={
        "default": {"type": "list"},
        "listMaxLength": {
            "type": "int",
            "description": "Inclusive maximum length of list",
        },
        "listMinLength": {
            "type": "int",
            "description": "Inclusive minimum length of list",
        },
        "listCompare": {
            "type": "int",
            "description": "If has value 1/-1 consecutive items in list must be greater/less than preceeding item. The list item class must have a __cmp__() method.",
        },
        "nameRoot": {
            "type": "str",
            "description": "Name hint for the base name of output files",
        },
    },
)
class COutputFileList(CList):
    """A list with all items of one CData sub-class"""

    pass


@cdata_class(
    attributes={
        "taskName": attribute(AttributeType.STRING, tooltip="taskName attribute"),
        "patch": attribute(AttributeType.STRING, tooltip="patch attribute"),
    },
    gui_label="CPatchSelection",
    contents_order=["taskName", "patch"],
)
class CPatchSelection(CData):
    """Generated CPatchSelection class from CData metadata."""


@cdata_class(
    qualifiers={
        "compare": "NotImplemented",
    },
    error_codes={
        "101": "End of range less than start",
        "102": "End of range greater than start",
    },
    gui_label="CRange",
    contents_order=["start", "end"],
    qualifiers_order=["compare"],
    qualifiers_definition={
        "compare": {
            "type": "int",
            "description": "If value is  1/-1 the end value must be greater/less than start.",
        },
    },
)
class CRange(CData):
    """Base class for CIntRange and CFloatRange"""

    pass


@cdata_class(
    error_codes={
        "201": "Range selection contains invalid character",
        "202": "Range selection contains bad syntax",
    }
)
class CRangeSelection(CString):
    """Generated CRangeSelection class from CData metadata."""

    pass


@cdata_class(gui_label="CUUID")
class CUUID(CString):
    """Generated CUUID class from CData metadata."""

    pass
