#!/usr/bin/env python3
"""
Pytest for testing CData structure integrity from DEF XML parsing.

This test suite validates that DEF XML can be properly parsed into CData structures
and that the resulting hierarchy maintains proper integrity, type safety, and
functionality including the enhanced metadata system.

The test suite includes comprehensive validation of:
- Task structure parsing from DEF XML
- Container hierarchy integrity
- Parameter type safety and validation
- Default value handling and value state tracking
- Path-based navigation functionality
- Parameter modification and state management
- Enhanced metadata system integration
- Complete parsing coverage verification

All tests use a fixture that constructs a real CData structure from SAMPLE_DEF_XML,
ensuring that the XML parsing and CData instantiation work correctly in production.
"""

import pytest
import tempfile
import os
from pathlib import Path
from typing import Any, Dict, List
from xml.etree import ElementTree as ET

# Add the server directory to the Python path
import sys

from ccp4x.core.data_manager.params_xml_handler import ParamsXmlHandler

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from ccp4x.core.task_manager.def_xml_parser import parse_def_xml_file
from ccp4x.core.data_manager.migrating_from_old_ccp4i2.OUTPUT_DIRECTORY.base_classes import (
    CString,
    CContainer,
    ValueState,
)
from ccp4x.core.data_manager.migrating_from_old_ccp4i2.OUTPUT_DIRECTORY.fundamental_types import (
    CInt,
    CFloat,
    CBoolean,
)
from ccp4x.core.data_manager.migrating_from_old_ccp4i2.OUTPUT_DIRECTORY.CCP4ModelData import (
    CPdbDataFile,
)

# Sample DEF XML for comprehensive testing
SAMPLE_DEF_XML = """<?xml version="1.0" encoding="UTF-8"?>
<ns0:ccp4i2 xmlns:ns0="http://www.ccp4.ac.uk/ccp4ns">
  <ccp4i2_header>
    <pluginName>servalcat_pipe</pluginName>
  </ccp4i2_header>
  <ccp4i2_body id="servalcat_pipe">
    <ccp4i2_body>
      <container id="inputData">
        <content id="XYZIN">
          <className>CPdbDataFile</className>
          <qualifiers>
            <mustExist>True</mustExist>
            <toolTip>Input coordinate file</toolTip>
          </qualifiers>
        </content>
      </container>
      <container id="outputData">
        <content id="XYZOUT">
          <className>CPdbDataFile</className>
          <qualifiers>
            <toolTip>Output coordinate file</toolTip>
          </qualifiers>
        </content>
      </container>
      <container id="controlParameters">
        <content id="DATA_METHOD">
          <className>CString</className>
          <qualifiers>
            <onlyEnumerators>True</onlyEnumerators>
            <enumerators>xtal,spa</enumerators>
            <default>xtal</default>
          </qualifiers>
        </content>
        <content id="ADD_WATERS">
          <className>CBoolean</className>
          <qualifiers>
            <default>False</default>
            <toolTip>Add water molecules</toolTip>
          </qualifiers>
        </content>
        <content id="NCYCLES">
          <className>CInt</className>
          <qualifiers>
            <default>10</default>
            <min>1</min>
            <max>100</max>
            <toolTip>Number of refinement cycles</toolTip>
          </qualifiers>
        </content>
        <content id="WEIGHT">
          <className>CFloat</className>
          <qualifiers>
            <min>0.0</min>
            <toolTip>Refinement weight</toolTip>
          </qualifiers>
        </content>
        <content id="B_REFINEMENT_MODE">
          <className>CString</className>
          <qualifiers>
            <onlyEnumerators>True</onlyEnumerators>
            <enumerators>iso,aniso,fix</enumerators>
            <default>iso</default>
            <toolTip>B-factor refinement mode</toolTip>
          </qualifiers>
        </content>
        <content id="OCCUPANCY_REFINEMENT">
          <className>CBoolean</className>
          <qualifiers>
            <default>True</default>
            <toolTip>Refine occupancies</toolTip>
          </qualifiers>
        </content>
      </container>
    </ccp4i2_body>
  </ccp4i2_body>
  <container id="metalCoordPipeline">
    <content id="RUN_METALCOORD">
      <className>CBoolean</className>
      <qualifiers>
        <default>False</default>
      </qualifiers>
    </content>
    <content id="LINKS">
      <className>CString</className>
      <qualifiers>
        <onlyEnumerators>True</onlyEnumerators>
        <enumerators>UPDATE,KEEP,NOTTOUCH</enumerators>
        <default>UPDATE</default>
      </qualifiers>
    </content>
  </container>
</ns0:ccp4i2>"""

# Sample servalcat params XML (shortened for testing)
SAMPLE_PARAMS_XML = """<?xml version='1.0' encoding='utf-8'?>
<ccp4:ccp4i2 xmlns:ccp4="http://www.ccp4.ac.uk/ccp4ns">
  <ccp4i2_header>
    <function>PARAMS</function>
    <userId>test_user</userId>
    <hostName>test-host</hostName>
    <creationTime>19:47 08/Oct/25</creationTime>
    <ccp4iVersion>alpha_rev_90011</ccp4iVersion>
    <pluginName>servalcat_pipe</pluginName>
  </ccp4i2_header>
  <ccp4i2_body>
    <inputData>
      <XYZIN>
        <project>2f376b1b2b734890bc7d700758dc9581</project>
        <baseName>model_from_refinement_mmcif_format_1.cif</baseName>
        <relPath>CCP4_IMPORTED_FILES</relPath>
        <annotation>Imported from Model_from_refinement_mmCIF_format.cif</annotation>
        <dbFileId>7278fed0208146c88336b6da8cbb275f</dbFileId>
        <subType>0</subType>
        <contentFlag>1</contentFlag>
      </XYZIN>
    </inputData>
    <outputData>
      <XYZOUT>
        <project>2f376b1b-2b73-4890-bc7d-700758dc9581</project>
        <baseName>XYZOUT.pdb</baseName>
        <relPath>CCP4_JOBS/job_16</relPath>
        <annotation>Model from refinement (PDB format)</annotation>
        <dbFileId>2e545c8c-8866-489f-8fd9-1a7d29ddc926</dbFileId>
        <subType>1</subType>
        <contentFlag>1</contentFlag>
      </XYZOUT>
    </outputData>
    <controlParameters>
      <DATA_METHOD>xtal</DATA_METHOD>
      <ADD_WATERS>True</ADD_WATERS>
      <NCYCLES>25</NCYCLES>
      <WEIGHT>0.15</WEIGHT>
      <B_REFINEMENT_MODE>aniso</B_REFINEMENT_MODE>
      <OCCUPANCY_REFINEMENT>False</OCCUPANCY_REFINEMENT>
    </controlParameters>
    <metalCoordPipeline>
      <RUN_METALCOORD>True</RUN_METALCOORD>
      <LINKS>KEEP</LINKS>
    </metalCoordPipeline>
  </ccp4i2_body>
</ccp4:ccp4i2>"""


class TestCDataIntegrity:
    """Test suite for CData structure integrity from DEF XML parsing."""

    @pytest.fixture(scope="class")
    def parsed_task(self):
        """
        Setup fixture that constructs a CData structure from SAMPLE_DEF_XML.

        Returns:
            CContainer: The parsed task structure from DEF XML
        """
        # Create a temporary file with the DEF XML content
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".def.xml", delete=False
        ) as f:
            f.write(SAMPLE_DEF_XML)
            temp_path = f.name

        try:
            # Parse the XML file into CData structure
            task = parse_def_xml_file(temp_path)
            return task
        finally:
            # Clean up temporary file
            Path(temp_path).unlink(missing_ok=True)

    def test_task_creation_success(self, parsed_task):
        """Test that the task is successfully created from DEF XML."""
        assert parsed_task is not None
        assert parsed_task.name == "servalcat_pipe"
        assert isinstance(parsed_task, CContainer)

    def test_container_structure_integrity(self, parsed_task):
        """Test that all expected containers exist with correct structure."""
        # Check main containers exist
        assert hasattr(parsed_task, "inputData")
        assert hasattr(parsed_task, "outputData")
        assert hasattr(parsed_task, "controlParameters")
        assert hasattr(parsed_task, "metalCoordPipeline")

        # Verify container types
        assert isinstance(parsed_task.inputData, CContainer)
        assert isinstance(parsed_task.outputData, CContainer)
        assert isinstance(parsed_task.controlParameters, CContainer)
        assert isinstance(parsed_task.metalCoordPipeline, CContainer)

    def test_input_data_structure(self, parsed_task):
        """Test the structure and integrity of inputData container."""
        input_data = parsed_task.inputData

        # Check XYZIN exists and is correct type
        assert hasattr(input_data, "XYZIN")
        assert isinstance(input_data.XYZIN, CPdbDataFile)

    def test_output_data_structure(self, parsed_task):
        """Test the structure and integrity of outputData container."""
        output_data = parsed_task.outputData

        # Check XYZOUT exists and is correct type
        assert hasattr(output_data, "XYZOUT")
        assert isinstance(output_data.XYZOUT, CPdbDataFile)

    def test_control_parameters_structure(self, parsed_task):
        """Test the structure and integrity of controlParameters container."""
        ctrl = parsed_task.controlParameters

        # Check all expected parameters exist with correct types
        assert hasattr(ctrl, "DATA_METHOD")
        assert isinstance(ctrl.DATA_METHOD, CString)

        assert hasattr(ctrl, "ADD_WATERS")
        assert isinstance(ctrl.ADD_WATERS, CBoolean)

        assert hasattr(ctrl, "NCYCLES")
        assert isinstance(ctrl.NCYCLES, CInt)

        assert hasattr(ctrl, "WEIGHT")
        assert isinstance(ctrl.WEIGHT, CFloat)

        assert hasattr(ctrl, "B_REFINEMENT_MODE")
        assert isinstance(ctrl.B_REFINEMENT_MODE, CString)

        assert hasattr(ctrl, "OCCUPANCY_REFINEMENT")
        assert isinstance(ctrl.OCCUPANCY_REFINEMENT, CBoolean)

    def test_metal_coord_pipeline_structure(self, parsed_task):
        """Test the structure and integrity of metalCoordPipeline container."""
        metal = parsed_task.metalCoordPipeline

        # Check metal coordination parameters exist with correct types
        assert hasattr(metal, "RUN_METALCOORD")
        assert isinstance(metal.RUN_METALCOORD, CBoolean)

        assert hasattr(metal, "LINKS")
        assert isinstance(metal.LINKS, CString)

    def test_default_values_and_states(self, parsed_task):
        """Test that default values are correctly set with proper value states."""
        ctrl = parsed_task.controlParameters
        metal = parsed_task.metalCoordPipeline

        # Test default values from DEF XML
        assert ctrl.DATA_METHOD.value == "xtal"
        assert ctrl.DATA_METHOD.getValueState("value") == ValueState.EXPLICITLY_SET

        assert ctrl.ADD_WATERS.value is False
        assert ctrl.ADD_WATERS.getValueState("value") == ValueState.EXPLICITLY_SET

        assert ctrl.NCYCLES.value == 10
        assert ctrl.NCYCLES.getValueState("value") == ValueState.EXPLICITLY_SET

        assert ctrl.B_REFINEMENT_MODE.value == "iso"
        assert (
            ctrl.B_REFINEMENT_MODE.getValueState("value") == ValueState.EXPLICITLY_SET
        )

        assert ctrl.OCCUPANCY_REFINEMENT.value is True
        assert (
            ctrl.OCCUPANCY_REFINEMENT.getValueState("value")
            == ValueState.EXPLICITLY_SET
        )

        # Test parameter without default (should be NOT_SET)
        assert ctrl.WEIGHT.getValueState("value") == ValueState.NOT_SET

        # Metal coordination defaults
        assert metal.RUN_METALCOORD.value is False
        assert metal.RUN_METALCOORD.getValueState("value") == ValueState.EXPLICITLY_SET

        assert metal.LINKS.value == "UPDATE"
        assert metal.LINKS.getValueState("value") == ValueState.EXPLICITLY_SET

    def test_parameter_constraints(self, parsed_task):
        """Test that parameter constraints from DEF XML are properly applied."""
        ctrl = parsed_task.controlParameters

        # Test enumerated string constraints
        data_method = ctrl.DATA_METHOD
        # Note: Actual constraint testing would depend on the CString implementation
        # For now, verify it has expected default from enumerated values
        assert data_method.value in ["xtal", "spa"]

        b_mode = ctrl.B_REFINEMENT_MODE
        assert b_mode.value in ["iso", "aniso", "fix"]

        # Test integer constraints (min/max from DEF XML)
        ncycles = ctrl.NCYCLES
        assert ncycles.value >= 1  # min constraint from DEF XML
        assert ncycles.value <= 100  # max constraint from DEF XML

    def test_path_based_navigation(self, parsed_task):
        """Test that path-based navigation works correctly."""
        # Test path-based access to nested parameters
        ncycles_by_path = parsed_task.find_by_path("controlParameters.NCYCLES")
        assert ncycles_by_path is not None
        assert ncycles_by_path.value == 10

        add_waters_by_path = parsed_task.find_by_path("controlParameters.ADD_WATERS")
        assert add_waters_by_path is not None
        assert add_waters_by_path.value is False

        run_metal_by_path = parsed_task.find_by_path(
            "metalCoordPipeline.RUN_METALCOORD"
        )
        assert run_metal_by_path is not None
        assert run_metal_by_path.value is False

    def test_parameter_modification_and_state_tracking(self, parsed_task):
        """Test parameter modification and value state tracking."""
        ctrl = parsed_task.controlParameters

        # Test modifying a parameter
        original_ncycles = ctrl.NCYCLES.value
        assert ctrl.NCYCLES.getValueState("value") == ValueState.EXPLICITLY_SET

        # Modify the value
        ctrl.NCYCLES.value = 25
        assert ctrl.NCYCLES.value == 25
        assert ctrl.NCYCLES.getValueState("value") == ValueState.EXPLICITLY_SET

        # Test unSet functionality
        ctrl.NCYCLES.unSet("value")
        assert ctrl.NCYCLES.getValueState("value") == ValueState.NOT_SET

        # Reset for other tests
        ctrl.NCYCLES.value = original_ncycles

    def test_type_safety(self, parsed_task):
        """Test that type safety is maintained for different data types."""
        ctrl = parsed_task.controlParameters

        # Test different data types maintain their identity
        assert isinstance(ctrl.DATA_METHOD.value, str)
        assert isinstance(ctrl.ADD_WATERS.value, bool)
        assert isinstance(ctrl.NCYCLES.value, int)
        assert (
            isinstance(ctrl.WEIGHT.value, (int, float))
            or ctrl.WEIGHT.getValueState("value") == ValueState.NOT_SET
        )

    def test_container_hierarchy_integrity(self, parsed_task):
        """Test that the container hierarchy maintains proper parent-child relationships."""
        # Test that child containers have a parent (may be set during parsing)
        # The exact parent relationship depends on the parsing implementation
        assert hasattr(parsed_task.inputData, "parent")
        assert hasattr(parsed_task.outputData, "parent")
        assert hasattr(parsed_task.controlParameters, "parent")
        assert hasattr(parsed_task.metalCoordPipeline, "parent")

        # Test that parameters have parent containers
        assert hasattr(parsed_task.controlParameters.NCYCLES, "parent")
        assert hasattr(parsed_task.controlParameters.ADD_WATERS, "parent")

        # Test that the containers maintain their structural integrity
        assert parsed_task.inputData is not None
        assert parsed_task.outputData is not None
        assert parsed_task.controlParameters is not None
        assert parsed_task.metalCoordPipeline is not None

    def test_enhanced_metadata_integration(self, parsed_task):
        """Test that enhanced metadata system is integrated and accessible."""
        from ccp4x.core.new_cdata.class_metadata import get_class_metadata

        # Test that we can access metadata for the classes used
        container_metadata = get_class_metadata("CContainer")
        assert container_metadata is not None

        # Test for fundamental types - these might not be in metadata registry
        # since they're base classes, so we'll test classes we know are registered
        boolean_metadata = get_class_metadata("CBoolean")
        if boolean_metadata is not None:
            assert isinstance(boolean_metadata.attributes, dict)

        # Test enhanced metadata fields exist where expected
        if hasattr(container_metadata, "contents_order"):
            assert isinstance(container_metadata.contents_order, (list, type(None)))

        if hasattr(container_metadata, "qualifiers_order"):
            assert isinstance(container_metadata.qualifiers_order, (list, type(None)))

    def test_def_xml_parsing_completeness(self, parsed_task):
        """Test that all elements from the DEF XML have been properly parsed."""
        # Count expected elements based on DEF XML structure
        expected_containers = [
            "inputData",
            "outputData",
            "controlParameters",
            "metalCoordPipeline",
        ]
        expected_control_params = [
            "DATA_METHOD",
            "ADD_WATERS",
            "NCYCLES",
            "WEIGHT",
            "B_REFINEMENT_MODE",
            "OCCUPANCY_REFINEMENT",
        ]
        expected_metal_params = ["RUN_METALCOORD", "LINKS"]
        expected_input_params = ["XYZIN"]
        expected_output_params = ["XYZOUT"]

        # Verify all containers exist
        for container_name in expected_containers:
            assert hasattr(
                parsed_task, container_name
            ), f"Missing container: {container_name}"

        # Verify all control parameters exist
        for param_name in expected_control_params:
            assert hasattr(
                parsed_task.controlParameters, param_name
            ), f"Missing control parameter: {param_name}"

        # Verify all metal coordination parameters exist
        for param_name in expected_metal_params:
            assert hasattr(
                parsed_task.metalCoordPipeline, param_name
            ), f"Missing metal parameter: {param_name}"

        # Verify input/output parameters exist
        for param_name in expected_input_params:
            assert hasattr(
                parsed_task.inputData, param_name
            ), f"Missing input parameter: {param_name}"

        for param_name in expected_output_params:
            assert hasattr(
                parsed_task.outputData, param_name
            ), f"Missing output parameter: {param_name}"

    def test_parameter_casting(self, parsed_task):
        """Test casting numerical parameter to python type."""
        ctrl = parsed_task.controlParameters

        # Test modifying a parameter
        original_ncycles = ctrl.NCYCLES
        assert int(original_ncycles) == 10

    def test_parameter_math(self, parsed_task):
        """Test casting numerical parameter to python type."""
        ctrl = parsed_task.controlParameters

        assert ctrl.NCYCLES * 10 == 100
        assert type(ctrl.NCYCLES * CInt(100)) == CInt

    def test_params_overlay(self, parsed_task):
        params_handler = ParamsXmlHandler()
        param_tree = ET.fromstring(SAMPLE_PARAMS_XML)
        # Find the body element
        body = param_tree.find(".//ccp4i2_body")
        if body is None:
            print("❌ No ccp4i2_body found in params XML")
            return False

        # Import all parameter values
        params_handler._import_container_values(body, parsed_task)

        ctrl = parsed_task.controlParameters
        assert ctrl.NCYCLES.value == 25
        inp = parsed_task.inputData
        assert inp.XYZIN.baseName == "model_from_refinement_mmcif_format_1.cif"

    def test_dict_set_parameter(self, parsed_task):
        """Test casting numerical parameter to python type."""

        inp = parsed_task.find_by_path("inputData")
        inp.XYZIN = {"baseName": "new_model.cif"}
        assert parsed_task.find_by_path("inputData.XYZIN").baseName == "new_model.cif"
        assert (
            parsed_task.find_by_path("inputData.XYZIN").dbFileId
            == "7278fed0208146c88336b6da8cbb275f"
        )
