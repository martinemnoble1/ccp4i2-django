"""Generated classes from CCP4Data.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CBaseData(CData):
    """Base class for simple classes"""
    pass

class CCollection(CData):
    """Generated CCollection class from CData metadata."""
    pass

class CI2DataType(CData):
    """Generated CI2DataType class from CData metadata."""
    pass

class CJobStatus(CData):
    """Generated CJobStatus class from CData metadata."""
    pass

class CJobTitle(CData):
    """Generated CJobTitle class from CData metadata."""
    pass

class COneWord(CData):
    """A single word string - no white space"""
    pass

class COutputFileList(CData):
    """A list with all items of one CData sub-class"""
    pass

class CPatchSelection(CData):
    """Generated CPatchSelection class from CData metadata."""

    taskName: str = None
    patch: str = None

class CRange(CData):
    """Base class for CIntRange and CFloatRange"""
    pass

class CRangeSelection(CData):
    """Generated CRangeSelection class from CData metadata."""
    pass

class CUUID(CData):
    """Generated CUUID class from CData metadata."""
    pass
