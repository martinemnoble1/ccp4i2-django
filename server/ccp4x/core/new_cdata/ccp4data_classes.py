"""Generated classes from CCP4Data.py"""

from typing import List, Any, Optional
from .base_classes import CData, CInt, CList, CString
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    qualifiers={
        "default": "NotImplemented",
        "charWidth": 10,
    }
)
class CBaseData(CData):
    """Base class for simple classes"""

    pass


class CCollection(CData):
    """Generated CCollection class from CData metadata."""

    pass


@cdata_class(
    qualifiers={
        "enumerators": ['CPdbDataFile', 'CSeqDataFile', 'CObsDataFile', 'CPhsDataFile', 'CMapCoeffsDataFile', 'CFreeRDataFile', 'CMtzDataFile', 'CDictDataFile', 'CDataFile', 'CInt', 'CFloat', 'CString', 'CRefmacKeywordFile'],
        "menuText": [],
    }
)
class CI2DataType(CString):
    """Generated CI2DataType class from CData metadata."""

    pass


class CJobStatus(CInt):
    """Generated CJobStatus class from CData metadata."""

    pass


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
    }
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
    }
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


class CUUID(CString):
    """Generated CUUID class from CData metadata."""

    pass
