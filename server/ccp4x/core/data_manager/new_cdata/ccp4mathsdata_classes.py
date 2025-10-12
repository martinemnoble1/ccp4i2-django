"""Generated classes from CCP4MathsData.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CAngle(CData):
    """An angle"""
    pass

class CEulerRotation(CData):
    """Generated CEulerRotation class from CData metadata."""

    alpha: Any = None
    beta: Any = None
    gamma: Any = None

class CMatrix33(CData):
    """Generated CMatrix33 class from CData metadata."""
    pass

class CTransformation(CData):
    """Generated CTransformation class from CData metadata."""

    translation: Any = None
    rotation: Any = None

class CXyz(CData):
    """Generated CXyz class from CData metadata."""

    x: Any = None
    y: Any = None
    z: Any = None

class CXyzBox(CData):
    """Generated CXyzBox class from CData metadata."""

    xMin: Any = None
    yMin: Any = None
    zMin: Any = None
    xMax: Any = None
    yMax: Any = None
    zMax: Any = None
