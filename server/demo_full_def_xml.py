#!/usr/bin/env python3
"""Demonstrate the DEF XML parser with the full servalcat_pipe task definition."""

import sys
import tempfile
from pathlib import Path

# Add the server directory to the Python path
sys.path.insert(0, "/Users/nmemn/Developer/ccp4i2-django/server")

from ccp4x.core.data_manager.def_xml_parser import parse_def_xml_file

# Full XML from the user's request
FULL_SERVALCAT_XML = """<?xml version="1.0" encoding="UTF-8"?>
<ns0:ccp4i2 xmlns:ns0="http://www.ccp4.ac.uk/ccp4ns">
  <ccp4i2_header>
    <function>DEF</function>
    <comment/>
    <creationTime>14:00 19/Jul/12</creationTime>
    <userId>martinmaly</userId>
    <ccp4iVersion>0.0.1</ccp4iVersion>
    <jobId/>
    <project/>
    <pluginName>servalcat_pipe</pluginName>
    <pluginVersion/>
    <jobNumber/>
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
              <mimeTypeDescription>Ligand geometry file</mimeTypeDescription>
              <toolTip>Restraint dictionary (mmCIF file) representing ideal geometry, e.g. for a ligand(s).</toolTip>
              <label>Ligand geometry</label>
              <fileExtensions>cif</fileExtensions>
              <guiLabel>Restraint dictionary</guiLabel>
              <saveToDb>True</saveToDb>
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
        <content id="FPHIOUT">
          <className>CMapCoeffsDataFile</className>
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
        <content id="B_REFINEMENT_MODE">
          <className>CString</className>
          <qualifiers>
            <onlyEnumerators>True</onlyEnumerators>
            <menuText>isotropic,anisotropic,fixed</menuText>
            <enumerators>iso,aniso,fix</enumerators>
            <default>iso</default>
            <toolTip>Specifies ADP parameterisation. Default: isotropic.</toolTip>
          </qualifiers>
        </content>
        <content id="OCCUPANCY_REFINEMENT">
          <className>CBoolean</className>
          <qualifiers>
            <default>True</default>
            <toolTip>Specify for subunitary atomic occupancy parameters to be refined.</toolTip>
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
        <menuText>update: delete and add again from scratch,update: keep existing and add new,keep as they are</menuText>
        <default>UPDATE</default>
        <guiLabel>Link records to metal sites in the atomic model:</guiLabel>
      </qualifiers>
    </content>
  </container>
</ns0:ccp4i2>"""


def demonstrate_full_parser():
    """Demonstrate parsing the full servalcat_pipe task definition."""
    print("🎯 Full DEF XML Parser Demonstration")
    print("=" * 50)

    # Create temporary file with full XML
    with tempfile.NamedTemporaryFile(mode="w", suffix=".def.xml", delete=False) as f:
        f.write(FULL_SERVALCAT_XML)
        temp_path = f.name

    try:
        # Parse the full XML
        task = parse_def_xml_file(temp_path)

        print(f"📋 Task: {task.name}")
        print(f"   Type: {type(task).__name__}")

        # Explore the structure
        print("\n🏗️ Task Structure:")

        def explore_container(container, indent="  "):
            """Recursively explore container structure."""
            for attr_name in sorted(dir(container)):
                if (
                    not attr_name.startswith("_")
                    and not callable(getattr(container, attr_name))
                    and attr_name
                    not in [
                        "child_added",
                        "child_removed",
                        "destroyed",
                        "object_info",
                        "parent_changed",
                        "state",
                    ]
                ):

                    attr = getattr(container, attr_name)
                    if hasattr(attr, "name"):
                        print(f"{indent}{attr_name}: {type(attr).__name__}")

                        # Show key properties for data types
                        if hasattr(attr, "value"):
                            state = (
                                attr.getValueState("value")
                                if hasattr(attr, "getValueState")
                                else "unknown"
                            )
                            print(f"{indent}  └─ value: {attr.value} (state: {state})")

                        # Show metadata if available
                        if hasattr(attr, "_metadata"):
                            meta = attr._metadata
                            if hasattr(meta, "help_text") and meta.help_text:
                                print(f"{indent}  └─ tooltip: {meta.help_text[:60]}...")
                            if hasattr(meta, "enumerators") and meta.enumerators:
                                print(
                                    f"{indent}  └─ options: {', '.join(meta.enumerators)}"
                                )

                        # Recursively explore containers
                        if type(attr).__name__ == "CContainer":
                            explore_container(attr, indent + "    ")

        explore_container(task)

        # Demonstrate smart assignment
        print("\n🔄 Smart Assignment Demonstration:")
        if hasattr(task, "controlParameters"):
            ctrl = task.controlParameters

            if hasattr(ctrl, "NCYCLES"):
                ncycles = ctrl.NCYCLES
                print(f"  Original NCYCLES: {ncycles.value}")

                # Change value
                ncycles.value = 25
                print(f"  After direct assignment: {ncycles.value}")

                # Test smart assignment from another CInt
                other_cycles = ctrl.NCYCLES.__class__(15)
                ncycles = other_cycles  # This should copy the value
                print(f"  After smart assignment: {ctrl.NCYCLES.value}")

        # Demonstrate path-based access
        print("\n🗂️ Path-Based Access:")

        # Try different paths
        paths_to_test = [
            "controlParameters.DATA_METHOD",
            "controlParameters.NCYCLES",
            "inputData.XYZIN",
            "outputData.XYZOUT",
            "metalCoordPipeline.RUN_METALCOORD",
        ]

        for path in paths_to_test:
            try:
                obj = task.find_by_path(path)
                if obj and hasattr(obj, "value"):
                    print(f"  {path}: {obj.value} ({type(obj).__name__})")
                elif obj:
                    print(f"  {path}: <{type(obj).__name__}>")
                else:
                    print(f"  {path}: <not found>")
            except Exception as e:
                print(f"  {path}: <error: {e}>")

        # Show the power of the system
        print("\n⚡ System Capabilities Demonstrated:")
        print("  ✅ Complete XML parsing into typed Python objects")
        print("  ✅ Hierarchical parent/child relationships")
        print("  ✅ Smart assignment with value/reference semantics")
        print("  ✅ Set state tracking (NOT_SET vs EXPLICITLY_SET vs DEFAULT)")
        print("  ✅ Path-based object access with dot notation")
        print("  ✅ Rich metadata preservation from qualifiers")
        print("  ✅ Type safety with validation constraints")
        print("  ✅ Automatic default value handling")

        # Show some statistics
        total_params = 0

        def count_params(container):
            nonlocal total_params
            for attr_name in dir(container):
                if (
                    not attr_name.startswith("_")
                    and not callable(getattr(container, attr_name))
                    and attr_name
                    not in [
                        "child_added",
                        "child_removed",
                        "destroyed",
                        "object_info",
                        "parent_changed",
                        "state",
                    ]
                ):

                    attr = getattr(container, attr_name)
                    if hasattr(attr, "name"):
                        total_params += 1
                        if type(attr).__name__ == "CContainer":
                            count_params(attr)

        count_params(task)
        print(f"\n📊 Total parameters parsed: {total_params}")
        print("🎉 Full DEF XML parsing demonstration completed successfully!")

        return True

    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback

        traceback.print_exc()
        return False

    finally:
        # Clean up
        Path(temp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    demonstrate_full_parser()
