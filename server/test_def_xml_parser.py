#!/usr/bin/env python3
"""Test the DEF XML parser with the servalcat_pipe example."""

import sys
import tempfile
from pathlib import Path

# Add the server directory to the Python path
sys.path.insert(0, "/Users/nmemn/Developer/ccp4i2-django/server")

from ccp4x.core.data_manager.def_xml_parser import parse_def_xml_file

# Sample XML content from the user's request (shortened for testing)
SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<ns0:ccp4i2 xmlns:ns0="http://www.ccp4.ac.uk/ccp4ns">
  <ccp4i2_header>
    <function>DEF</function>
    <pluginName>servalcat_pipe</pluginName>
  </ccp4i2_header>
  <ccp4i2_body id="servalcat_pipe">
    <ccp4i2_body>
      <container id="inputData">
        <content id="XYZIN">
          <className>CPdbDataFile</className>
          <qualifiers>
            <ifAtomSelection>True</ifAtomSelection>
            <mustExist>True</mustExist>
            <allowUndefined>False</allowUndefined>
            <fromPreviousJob>True</fromPreviousJob>
            <requiredSubType>1,0</requiredSubType>
            <toolTip>File containing model coordinates (PDB/mmCIF).</toolTip>
          </qualifiers>
        </content>
        <content id="HKLIN">
          <className>CObsDataFile</className>
          <qualifiers>
            <mustExist>True</mustExist>
            <allowUndefined>True</allowUndefined>
            <fromPreviousJob>True</fromPreviousJob>
            <toolTip>File containing structure factor amplitudes/intensities and uncertainties (F/SigF or I/SigI).</toolTip>
          </qualifiers>
        </content>
        <content id="DICT_LIST">
          <className>CList</className>
          <qualifiers>
            <listMinLength>0</listMinLength>
          </qualifiers>
          <subItem>
            <className>CDictDataFile</className>
            <qualifiers>
              <default>
                <contentFlag>1</contentFlag>
              </default>
              <mimeTypeName>application/refmac-dictionary</mimeTypeName>
              <toolTip>Restraint dictionary (mmCIF file) representing ideal geometry, e.g. for a ligand(s).</toolTip>
              <mustExist>True</mustExist>
              <allowUndefined>True</allowUndefined>
              <fromPreviousJob>True</fromPreviousJob>
            </qualifiers>
          </subItem>
        </content>
      </container>
      <container id="outputData">
        <content id="XYZOUT">
          <className>CPdbDataFile</className>
          <qualifiers>
            <default>
              <subType>1</subType>
              <contentFlag>1</contentFlag>
            </default>
            <saveToDb>True</saveToDb>
          </qualifiers>
        </content>
      </container>
      <container id="controlParameters">
        <content id="DATA_METHOD">
          <className>CString</className>
          <qualifiers>
            <onlyEnumerators>True</onlyEnumerators>
            <menuText>Diffraction data,SPA maps</menuText>
            <enumerators>xtal,spa</enumerators>
            <default>xtal</default>
            <allowUndefined>False</allowUndefined>
          </qualifiers>
        </content>
        <content id="ADD_WATERS">
          <className>CBoolean</className>
          <qualifiers>
            <default>False</default>
            <toolTip>Add waters and perform further refinement.</toolTip>
          </qualifiers>
        </content>
        <content id="NCYCLES">
          <className>CInt</className>
          <qualifiers>
            <default>10</default>
            <min>0</min>
            <toolTip>Number of refinement cycles to perform.</toolTip>
          </qualifiers>
        </content>
        <content id="WEIGHT">
          <className>CFloat</className>
          <qualifiers>
            <min>0.0</min>
            <toolTip>Constant weight controlling the relative contribution of data (reflections) and restraint (geometry) terms.</toolTip>
          </qualifiers>
        </content>
      </container>
    </ccp4i2_body>
  </ccp4i2_body>
</ns0:ccp4i2>"""


def test_def_xml_parser():
    """Test the DEF XML parser with servalcat_pipe example."""
    print("🧪 Testing DEF XML Parser...")

    # Create temporary file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".def.xml", delete=False) as f:
        f.write(SAMPLE_XML)
        temp_path = f.name

    try:
        # Parse the XML
        task_def = parse_def_xml_file(temp_path)

        print(f"✅ Successfully parsed DEF XML!")
        print(f"Task name: {task_def.name}")
        print(f"Task type: {type(task_def)}")

        # Test structure
        print("\n📁 Structure analysis:")

        # Check containers
        containers = ["inputData", "outputData", "controlParameters"]
        for container_name in containers:
            if hasattr(task_def, container_name):
                container = getattr(task_def, container_name)
                print(f"  ✅ {container_name}: {type(container).__name__}")

                # Show some content
                for attr_name in dir(container):
                    if not attr_name.startswith("_") and not callable(
                        getattr(container, attr_name)
                    ):
                        attr = getattr(container, attr_name)
                        if hasattr(attr, "name"):
                            print(f"    - {attr_name}: {type(attr).__name__}")
            else:
                print(f"  ❌ Missing {container_name}")

        # Test specific parameters
        print("\n🔧 Parameter testing:")

        if hasattr(task_def, "controlParameters"):
            ctrl = task_def.controlParameters

            # Test CString with enumerators
            if hasattr(ctrl, "DATA_METHOD"):
                data_method = ctrl.DATA_METHOD
                print(
                    f"  DATA_METHOD: {data_method.value} (type: {type(data_method).__name__})"
                )
                print(f"    Set state: {data_method.getValueState('value')}")

            # Test CBoolean with default
            if hasattr(ctrl, "ADD_WATERS"):
                add_waters = ctrl.ADD_WATERS
                print(
                    f"  ADD_WATERS: {add_waters.value} (type: {type(add_waters).__name__})"
                )
                print(f"    Set state: {add_waters.getValueState('value')}")

            # Test CInt with min constraint
            if hasattr(ctrl, "NCYCLES"):
                ncycles = ctrl.NCYCLES
                print(f"  NCYCLES: {ncycles.value} (type: {type(ncycles).__name__})")
                print(f"    Set state: {ncycles.getValueState('value')}")

            # Test CFloat with no default
            if hasattr(ctrl, "WEIGHT"):
                weight = ctrl.WEIGHT
                print(f"  WEIGHT: {weight.value} (type: {type(weight).__name__})")
                print(f"    Set state: {weight.getValueState('value')}")

        # Test list handling
        print("\n📋 List testing:")
        if hasattr(task_def, "inputData") and hasattr(task_def.inputData, "DICT_LIST"):
            dict_list = task_def.inputData.DICT_LIST
            print(
                f"  DICT_LIST: {type(dict_list).__name__} with {len(dict_list)} items"
            )
            print(f"    Item type: {getattr(dict_list, '_item_type', 'unknown')}")

        # Test path-based access
        print("\n🗂️ Path-based access testing:")
        try:
            ncycles_by_path = task_def.find_by_path("controlParameters.NCYCLES")
            if ncycles_by_path:
                print(f"  Found NCYCLES by path: {ncycles_by_path.value}")
            else:
                print("  ❌ Could not find NCYCLES by path")
        except Exception as e:
            print(f"  ❌ Path access error: {e}")

        # Test assignment and state tracking
        print("\n🔄 Assignment and state tracking:")
        if hasattr(task_def, "controlParameters") and hasattr(
            task_def.controlParameters, "NCYCLES"
        ):
            ncycles = task_def.controlParameters.NCYCLES

            print(
                f"  Original NCYCLES: {ncycles.value} (state: {ncycles.getValueState('value')})"
            )

            # Change the value
            ncycles.value = 20
            print(
                f"  After assignment: {ncycles.value} (state: {ncycles.getValueState('value')})"
            )

            # Test unSet
            ncycles.unSet("value")
            try:
                print(
                    f"  After unSet: {ncycles.value} (state: {ncycles.getValueState('value')})"
                )
            except AttributeError:
                print(
                    f"  After unSet: <unset> (state: {ncycles.getValueState('value')})"
                )

        print("\n🎉 DEF XML Parser test completed successfully!")
        return True

    except Exception as e:
        print(f"❌ DEF XML Parser test failed: {e}")
        import traceback

        traceback.print_exc()
        return False

    finally:
        # Clean up
        Path(temp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    test_def_xml_parser()
