# Copyright (C) 2022 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. _materials_example:

Materials
=========

This example demonstrates how to create the different type of materials, import,
or export them. It only shows the PyACP part of the setup. For a complete composite analysis,
see :ref:`pymapdl_workflow_example`.

ACP distinguishes between four types of material:

- Raw **Material** that defines the mechanical properties of the material.
- **Fabric** is where a material can be associated with a set thickness.
- **Stackup** is used to combine fabrics into a non-crimp fabric, such as a [0 45 90] combination.
- **Sublaminate** is used to group fabrics and stackups for frequently used lay-ups.

Fabrics, Stackups and Sublaminates can be used to create plies. It is recommended to look a the
Ansys help for more information on the different types of materials.
"""
import os

# %%
# Import the standard library and third-party dependencies.
import pathlib
import tempfile

# %%
# Import the PyACP dependencies.
from ansys.acp.core import ACPWorkflow, FabricWithAngle, Lamina, PlyType, SymmetryType, launch_acp
from ansys.acp.core.extras import ExampleKeys, get_example_file
from ansys.acp.core.material_property_sets import (
    ConstantEngineeringConstants,
    ConstantStrainLimits,
    ConstantStressLimits,
)

# sphinx_gallery_thumbnail_path = '_static/gallery_thumbnails/sphx_glr_001-materials_thumb.png'


# %%
# Start ACP and load the model
# ----------------------------
# %%
# Get the example file from the server.
tempdir = tempfile.TemporaryDirectory()
WORKING_DIR = pathlib.Path(tempdir.name)
input_file = get_example_file(ExampleKeys.BASIC_FLAT_PLATE_DAT, WORKING_DIR)

# %%
# Launch the PyACP server and connect to it.
acp = launch_acp()

# %%
# Define the input file and instantiate an ``ACPWorkflow`` instance.
workflow = ACPWorkflow.from_cdb_or_dat_file(
    acp=acp,
    cdb_or_dat_file_path=input_file,
    local_working_directory=WORKING_DIR,
)

model = workflow.model

# %%
# Create a Material
# -----------------
# %%
# Create property sets elastic constants, strain and stress limits.
engineering_constants_ud = ConstantEngineeringConstants.from_orthotropic_constants(
    E1=5e10, E2=1e10, E3=1e10, nu12=0.28, nu13=0.28, nu23=0.3, G12=5e9, G23=4e9, G31=4e9
)

strain_limit_tension = 0.01
strain_limit_compression = 0.008
strain_limit_shear = 0.012
strain_limits = ConstantStrainLimits.from_orthotropic_constants(
    eXc=strain_limit_compression,
    eYc=strain_limit_compression,
    eZc=strain_limit_compression,
    eXt=strain_limit_tension,
    eYt=strain_limit_tension,
    eZt=strain_limit_tension,
    eSxy=strain_limit_shear,
    eSyz=strain_limit_shear,
    eSxz=strain_limit_shear,
)

stress_limits = ConstantStressLimits.from_orthotropic_constants(
    Xt=7.8e8,
    Yt=3.1e7,
    Zt=3.1e7,
    Xc=-4.8e8,
    Yc=-1e8,
    Zc=-1e8,
    Sxy=3.5e7,
    Syz=2.5e7,
    Sxz=3.5e7,
)

# %%
# Create a uni-directional (UD) material
ud_material = model.create_material(
    name="E-Glass UD",
    ply_type=PlyType.REGULAR,
    engineering_constants=engineering_constants_ud,
    strain_limits=strain_limits,
    stress_limits=stress_limits,
)

# %%
# Create a Fabric
# ---------------
#
# Create a fabric with a thickness of 0.2 mmm. A material can be used for
# multiple fabrics.
ud_fabric_02mm = model.create_fabric(
    name="E-Glass UD 0.2mm", material=ud_material, thickness=0.0002
)
ud_fabric_03mm = model.create_fabric(
    name="E-Glass UD 0.3mm", material=ud_material, thickness=0.0003
)

# %%
# Create a Stackup
# ----------------
# Create a non-crimped fabric. In that case a biax.
biax_glass_ud = model.create_stackup(
    name="Biax E-Glass UD [-45, 45]",
    fabrics=(
        FabricWithAngle(ud_fabric_02mm, -45),
        FabricWithAngle(ud_fabric_02mm, 45),
    ),
)

# %%
# Create a Sub-Laminate
# ---------------------
# A Sublaminate is a group of fabrics and stackups which eases the modeling
# if the same sequence of materials is used multiple times.
# The final material sequence of this Sublaminate is
# [E-Glass -45°, E-Glass 45°, E-Glass 90°, E-Glass 45°, E-Glass -45°].
sublaminate = model.create_sublaminate(
    name="Sublaminate",
    materials=(
        Lamina(biax_glass_ud, 0),
        Lamina(ud_fabric_02mm, 90),
    ),
    symmetry=SymmetryType.ODD_SYMMETRY,
)

# %%
# Import and Export Materials
# ---------------------------
# Materials can be imported and exported from and to external sources.
# By default, materials are loaded from the CDB file when the model is loaded.
# An alternative is to load materials from an Engineering Data
# file via :meth:`.Model.import_materials`.
engd_file_path = get_example_file(ExampleKeys.MATERIALS_XML, WORKING_DIR)
remote_engd_file_path = acp.upload_file(engd_file_path)
model.import_materials(matml_path=remote_engd_file_path)

# %%
# Some workflows require the materials to be exported to an XML file.
engd_file_name = "exported_materials.xml"
model.export_materials(path=engd_file_name)
acp.download_file(engd_file_name, os.path.join(WORKING_DIR, engd_file_name))
