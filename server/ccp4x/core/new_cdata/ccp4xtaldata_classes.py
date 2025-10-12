"""Generated classes from CCP4XtalData.py"""

from typing import List, Any, Optional
from .base_classes import CData, CDataFile, CContainer

class CAltSpaceGroupList(CData):
    """Generated CAltSpaceGroupList class from CData metadata."""
    pass

class CAsuComponent(CData):
    """A component of the asymmetric unit. This is for use in MR, defining
what we are searching for. """

    # Molecule type
    moleculeType: Any = "PROTEIN"
    seqFile: Any = None
    # Number of copies of sequence
    numberOfCopies: Any = 1

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CAsuComponentList(CData):
    """Generated CAsuComponentList class from CData metadata."""
    pass

class CCell(CData):
    """A unit cell"""

    # Cell length a in A
    a: Any = None
    # Cell length b in A
    b: Any = None
    # Cell length c in A
    c: Any = None
    # Cell angle alpha in degrees
    alpha: Any = None
    # Cell angle beta in degrees
    beta: Any = None
    # Cell angle gamma in degrees
    gamma: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CCellAngle(CData):
    """A cell angle"""
    pass

class CCellLength(CData):
    """A cell length"""
    pass

class CColumnGroup(CData):
    """Groups of columns in MTZ - probably from analysis by hklfile"""

    columnGroupType: Any = None
    contentFlag: Any = None
    dataset: Any = None
    columnList: Any = None
    selected: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CColumnGroupItem(CData):
    """Definition of set of columns that form a 'group'"""

    columnName: Any = None
    defaultList: Any = None
    columnType: Any = None
    partnerTo: Any = None
    partnerOffset: Any = None

class CColumnGroupList(CData):
    """Generated CColumnGroupList class from CData metadata."""
    pass

class CColumnType(CData):
    """A list of recognised MTZ column types"""
    pass

class CColumnTypeList(CData):
    """A list of acceptable MTZ column types"""
    pass

class CCrystalName(CData):
    """Generated CCrystalName class from CData metadata."""
    pass

class CDataset(CData):
    """The experimental data model for ab initio phasing"""

    selected: Any = None
    obsDataFile: Any = None
    crystalName: Any = None
    datasetName: Any = None
    formFactors: Any = None
    formFactorSource: Any = "no"

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CDatasetList(CData):
    """Generated CDatasetList class from CData metadata."""
    pass

class CDatasetName(CData):
    """Generated CDatasetName class from CData metadata."""
    pass

class CDialsJsonFile(CData):
    """Generated CDialsJsonFile class from CData metadata."""
    pass

class CDialsPickleFile(CData):
    """Generated CDialsPickleFile class from CData metadata."""
    pass

class CExperimentalDataType(CData):
    """Experimental data type e.g. native or peak"""
    pass

class CFormFactor(CData):
    """The for factor (Fp and Fpp) for a giving element and wavelength"""

    # CONTENTS: <Unparseable: {'Fp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor F' for element at given wavelength"}}, 'Fpp': {'class': CCP4Data.CFloat, 'qualifiers': {'toolTip': "Form factor F'' for element at given wavelength"}}}>

class CGenericReflDataFile(CData):
    """Generated CGenericReflDataFile class from CData metadata."""
    pass

class CImageFile(CData):
    """Generated CImageFile class from CData metadata."""
    pass

class CImageFileList(CData):
    """Generated CImageFileList class from CData metadata."""
    pass

class CImosflmXmlDataFile(CData):
    """An iMosflm data file"""
    pass

class CImportUnmerged(CData):
    """Generated CImportUnmerged class from CData metadata."""

    file: Any = None
    cell: Any = None
    wavelength: Any = None
    crystalName: Any = None
    dataset: Any = None
    excludeSelection: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CImportUnmergedList(CData):
    """Generated CImportUnmergedList class from CData metadata."""
    pass

class CMapDataFile(CData):
    """A CCP4 Map file"""
    pass

class CMergeMiniMtz(CData):
    """Generated CMergeMiniMtz class from CData metadata."""

    fileName: Any = None
    columnTag: Any = None
    columnNames: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CMergeMiniMtzList(CData):
    """Generated CMergeMiniMtzList class from CData metadata."""
    pass

class CMiniMtzDataFileList(CData):
    """Generated CMiniMtzDataFileList class from CData metadata."""
    pass

class CMtzColumn(CData):
    """An MTZ column with column label and column type"""

    columnLabel: Any = None
    columnType: Any = None
    dataset: Any = None
    groupIndex: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CMtzColumnGroup(CData):
    """Generated CMtzColumnGroup class from CData metadata."""

    groupType: Any = None
    columns: Any = None

class CMtzData(CData):
    """Generated CMtzData class from CData metadata."""

    cell: Any = None
    spaceGroup: Any = None
    resolutionRange: Any = None
    listOfColumns: Any = None
    datasets: Any = None
    crystalNames: Any = None
    wavelengths: Any = None
    datasetCells: Any = None
    merged: Any = None

class CMtzDataFile(CData):
    """An MTZ experimental data file"""
    pass

class CMtzDataset(CData):
    """Generated CMtzDataset class from CData metadata."""

    name: Any = None
    columnGroups: Any = None

class CPhaserRFileDataFile(CData):
    """Generated CPhaserRFileDataFile class from CData metadata."""
    pass

class CPhaserSolDataFile(CData):
    """Generated CPhaserSolDataFile class from CData metadata."""
    pass

class CProgramColumnGroup(CData):
    """A group of MTZ columns required for program input"""
    pass

class CProgramColumnGroup0(CData):
    """Generated CProgramColumnGroup0 class from CData metadata."""

    columnGroup: Any = None
    datasetName: Any = None

class CRefmacKeywordFile(CData):
    """Generated CRefmacKeywordFile class from CData metadata."""
    pass

class CReindexOperator(CData):
    """Generated CReindexOperator class from CData metadata."""

    h: Any = "h"
    k: Any = "k"
    l: Any = "l"

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CResolutionRange(CData):
    """Generated CResolutionRange class from CData metadata."""

    low: Any = None
    high: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CRunBatchRange(CData):
    """Generated CRunBatchRange class from CData metadata."""

    runNumber: Any = None
    batchRange0: Any = None
    batchRange1: Any = None
    resolution: Any = None
    fileNumber: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CRunBatchRangeList(CData):
    """Generated CRunBatchRangeList class from CData metadata."""
    pass

class CShelxFADataFile(CData):
    """Generated CShelxFADataFile class from CData metadata."""
    pass

class CShelxLabel(CData):
    """Generated CShelxLabel class from CData metadata."""
    pass

class CSpaceGroup(CData):
    """A string holding the space group"""
    pass

class CSpaceGroupCell(CData):
    """Cell space group and parameters"""

    spaceGroup: Any = None
    cell: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CUnmergedDataContent(CData):
    """Generated CUnmergedDataContent class from CData metadata."""

    format: Any = "unk"
    merged: Any = "unk"
    crystalName: Any = None
    datasetName: Any = None
    cell: Any = None
    spaceGroup: Any = None
    batchs: Any = None
    lowRes: Any = None
    highRes: Any = None
    knowncell: Any = None
    knownwavelength: Any = None
    numberLattices: Any = None
    wavelength: Any = None
    numberofdatasets: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CUnmergedDataFile(CData):
    """Handle MTZ, XDS and scalepack files. Allow wildcard filename"""
    pass

class CUnmergedDataFileList(CData):
    """Generated CUnmergedDataFileList class from CData metadata."""
    pass

class CWavelength(CData):
    """Wavelength in Angstrom"""
    pass

class CXia2ImageSelection(CData):
    """Generated CXia2ImageSelection class from CData metadata."""

    imageFile: Any = None
    imageStart: Any = None
    imageEnd: Any = None

    def validate(self) -> List[str]:
        """Validate instance data according to class qualifiers."""
        errors = []
        # TODO: Implement validation logic based on qualifiers
        return errors

class CXia2ImageSelectionList(CData):
    """Generated CXia2ImageSelectionList class from CData metadata."""
    pass
