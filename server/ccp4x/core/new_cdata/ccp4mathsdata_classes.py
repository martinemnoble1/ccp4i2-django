"""Generated classes from CCP4MathsData.py"""

from typing import List, Any, Optional
from .base_classes import CData, CFloat
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    gui_label="CAngle"
)
class CAngle(CFloat):
    """An angle"""

    pass



@cdata_class(
    attributes={
            "alpha": attribute(AttributeType.STRING, tooltip="alpha attribute"),
            "beta": attribute(AttributeType.STRING, tooltip="beta attribute"),
            "gamma": attribute(AttributeType.STRING, tooltip="gamma attribute"),
        },
    gui_label="CEulerRotation"
)
class CEulerRotation(CData):
    """Generated CEulerRotation class from CData metadata."""

    pass


@cdata_class(
    gui_label="CMatrix33"
)
class CMatrix33(CData):
    """Generated CMatrix33 class from CData metadata."""

    pass



@cdata_class(
    attributes={
            "translation": attribute(AttributeType.STRING, tooltip="translation attribute"),
            "rotation": attribute(AttributeType.STRING, tooltip="rotation attribute"),
        },
    gui_label="CTransformation"
)
class CTransformation(CData):
    """Generated CTransformation class from CData metadata."""

    pass


@cdata_class(
    attributes={
            "x": attribute(AttributeType.FLOAT, tooltip="x attribute"),
            "y": attribute(AttributeType.FLOAT, tooltip="y attribute"),
            "z": attribute(AttributeType.FLOAT, tooltip="z attribute"),
        },
    error_codes={
            "201": "Attempting arithmetic with inappropriate data type",
            "202": "Attempting arithmetic in unset data object",
            "203": "Attempting arithmetic with unset data object as argument",
        },
    gui_label="CXyz"
)
class CXyz(CData):
    """Generated CXyz class from CData metadata."""

    pass



@cdata_class(
    attributes={
            "xMin": attribute(AttributeType.FLOAT, tooltip="xMin attribute"),
            "yMin": attribute(AttributeType.FLOAT, tooltip="yMin attribute"),
            "zMin": attribute(AttributeType.FLOAT, tooltip="zMin attribute"),
            "xMax": attribute(AttributeType.FLOAT, tooltip="xMax attribute"),
            "yMax": attribute(AttributeType.FLOAT, tooltip="yMax attribute"),
            "zMax": attribute(AttributeType.FLOAT, tooltip="zMax attribute"),
        },
    error_codes={
            "201": "Maximum x,y or z value less than minimum",
        },
    gui_label="CXyzBox"
)
class CXyzBox(CData):
    """Generated CXyzBox class from CData metadata."""

    pass
