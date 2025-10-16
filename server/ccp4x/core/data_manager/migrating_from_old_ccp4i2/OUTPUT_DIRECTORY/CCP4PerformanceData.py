"""Generated classes from CCP4PerformanceData.py"""

from .base_classes import CData, CString, CDataFile, CContainer
from .fundamental_types import CInt, CList, CBoolean, CFloat
from .class_metadata import cdata_class, attribute, AttributeType


@cdata_class(
    attributes={
        "value": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="value attribute"),
        "annotation": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CString", tooltip="annotation attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['value', 'annotation'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CPerformanceIndicator",
)
class CPerformanceIndicator(CData):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "phaseError": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="phaseError attribute"),
        "weightedPhaseError": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="weightedPhaseError attribute"),
        "reflectionCorrelation": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="reflectionCorrelation attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['phaseError',
                    'weightedPhaseError', 'reflectionCorrelation'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CPhaseErrorPerformance",
)
class CPhaseErrorPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "cutoff": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="cutoff attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['cutoff'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CPairefPerformance",
)
class CPairefPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "RFactor": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="RFactor attribute"),
        "completeness": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="completeness attribute"),
        "annotation": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CString", tooltip="annotation attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['RFactor', 'completeness', 'annotation'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CModelBuildPerformance",
)
class CModelBuildPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "FOM": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="FOM attribute"),
        "CFOM": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="CFOM attribute"),
        "Hand1Score": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="Hand1Score attribute"),
        "Hand2Score": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="Hand2Score attribute"),
        "CC": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="CC attribute"),
        "RFactor": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="RFactor attribute"),
        "RFree": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="RFree attribute"),
        "annotation": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CString", tooltip="annotation attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['FOM', 'CFOM', 'Hand1Score',
                    'Hand2Score', 'CC', 'RFactor', 'RFree', 'annotation'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CExpPhasPerformance",
)
class CExpPhasPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "spaceGroup": attribute(AttributeType.CUSTOM, custom_class="core.CCP4XtalData.CSpaceGroup", tooltip="spaceGroup attribute"),
        "highResLimit": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="highResLimit attribute"),
        "rMeas": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="rMeas attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['spaceGroup', 'highResLimit', 'rMeas'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CDataReductionPerformance",
)
class CDataReductionPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "spaceGroup": attribute(AttributeType.CUSTOM, custom_class="core.CCP4XtalData.CSpaceGroup", tooltip="spaceGroup attribute"),
        "highResLimit": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="highResLimit attribute"),
        "ccHalf": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CFloat", tooltip="ccHalf attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['spaceGroup', 'highResLimit', 'ccHalf'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CDataReductionCCPerformance",
)
class CDataReductionCCPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass


@cdata_class(
    attributes={
        "nAtoms": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CInt", tooltip="nAtoms attribute"),
        "nResidues": attribute(AttributeType.CUSTOM, custom_class="core.CCP4Data.CInt", tooltip="nResidues attribute")
    },
    error_codes={
        "300": {
            "description": "Passed",
            "severity": 0
        },
        "301": {
            "description": "Data value not set"
        },
        "302": {
            "description": "Performance indicator value difference greater than tolereance"
        },
        "303": {
            "description": "Performance indicator value different"
        },
        "304": {
            "description": "Performance indicator value difference greater than tolereance - but improved",
            "severity": 2
        },
        "305": {
            "description": "Performance indicator not used",
            "severity": 0
        }
    },
    qualifiers={
        "allowUndefined": True,
        "guiDefinition": {},
        "saveToDb": False
    },
    contents_order=['nAtoms', 'nResidues'],
    qualifiers_order=[
        'allowUndefined',
        'default',
        'toolTip',
        'guiLabel',
        'guiDefinition',
        'helpFile',
        'saveToDb'
    ],
    qualifiers_definition={
        "allowUndefined": {"type": bool},
        "default": {"type": dict},
        "toolTip": {"type": str},
        "guiLabel": {"type": str},
        "guiDefinition": {"type": dict},
        "helpFile": {"type": str},
        "saveToDb": {"type": bool, "description": "Save this data in the database"}
    },
    gui_label="CAtomCountPerformance",
)
class CAtomCountPerformance(CPerformanceIndicator):
    """QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None"""
    pass
