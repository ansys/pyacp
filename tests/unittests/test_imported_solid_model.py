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


import pathlib
import tempfile

from hypothesis import HealthCheck, assume, given, settings
import hypothesis.strategies as st
from packaging.version import parse as parse_version
import pytest

import ansys.acp.core as pyacp

from .common.tree_object_tester import (
    ObjectPropertiesToTest,
    PropertyWithCustomComparison,
    TreeObjectTester,
    WithLockedMixin,
)


@pytest.fixture(autouse=True)
def skip_if_unsupported_version(acp_instance):
    if parse_version(acp_instance.server_version) < parse_version(
        pyacp.ImportedSolidModel._SUPPORTED_SINCE
    ):
        pytest.skip("ImportedSolidModel is not supported on this version of the server.")


def compare_pb_object(given, expected):
    if not isinstance(given, type(expected)):
        return False
    return given._pb_object == expected._pb_object


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_imported_solid_model()


class TestImportedSolidModel(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "imported_solid_models"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
        }

    CREATE_METHOD_NAME = "create_imported_solid_model"
    INITIAL_OBJECT_NAMES = tuple()

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        modeling_group = model.create_modeling_group()

        return ObjectPropertiesToTest(
            read_write=[
                ("name", "new_name"),
                ("active", False),
                ("format", pyacp.SolidModelImportFormat.ANSYS_H5),
                ("unit_system", pyacp.UnitSystemType.SI),
                ("external_path", "path/to/file"),
                ("delete_bad_elements", False),
                ("warping_limit", 0.6),
                ("minimum_volume", 1.2),
                ("cut_off_material", model.create_material()),
                (
                    "export_settings",
                    PropertyWithCustomComparison(
                        initial_value=pyacp.ImportedSolidModelExportSettings(
                            use_default_section_index=False,
                            section_index=2,
                            use_default_coordinate_system_index=False,
                            coordinate_system_index=3,
                            use_default_material_index=False,
                            material_index=4,
                            use_default_node_index=False,
                            node_index=5,
                            use_default_element_index=False,
                            element_index=6,
                            use_solsh_elements=True,
                            drop_hanging_nodes=False,
                            use_solid_model_prefix=False,
                        ),
                        comparison_function=compare_pb_object,
                    ),
                ),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
            ],
        )


@pytest.fixture
def imported_solid_model_with_elements(parent_object, tempdir_if_local_acp):
    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()
    with tempdir_if_local_acp() as export_dir:
        filename = export_dir / "solid_model.h5"
        solid_model.export(filename, format=pyacp.SolidModelExportFormat.ANSYS_H5)
        del model.solid_models[solid_model.id]
        imported_solid_model = model.create_imported_solid_model(
            external_path=filename,
            format=pyacp.SolidModelImportFormat.ANSYS_H5,
        )
        imported_solid_model.create_layup_mapping_object(
            shell_element_sets=[model.element_sets["All_Elements"]]
        )
        model.update()
        yield imported_solid_model


@pytest.mark.parametrize(
    "format",
    [
        "ansys:h5",
        "ansys:cdb",
        pyacp.SolidModelExportFormat.ANSYS_H5,
        pyacp.SolidModelExportFormat.ANSYS_CDB,
    ],
)
def test_export(tempdir_if_local_acp, acp_instance, imported_solid_model_with_elements, format):
    """Check that the export to a file works."""
    with tempdir_if_local_acp() as export_dir:
        with tempfile.TemporaryDirectory() as tmp_dir:
            if format == "ansys:h5":
                ext = ".h5"
            else:
                ext = ".cdb"

            out_file_name = f"out_file{ext}"
            out_path = export_dir / out_file_name
            tmp_path = pathlib.Path(tmp_dir) / out_file_name

            imported_solid_model_with_elements.export(path=out_file_name, format=format)
            acp_instance.download_file(out_path, tmp_path)

            assert tmp_path.exists()
            assert tmp_path.stat().st_size > 0


@given(invalid_format=st.text())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_export_with_invalid_format_raises(
    imported_solid_model_with_elements, tempdir_if_local_acp, invalid_format
):
    """Check that the export to a file with an invalid format raises an exception."""
    assume(invalid_format not in ["ansys:h5", "ansys:cdb"])

    with tempdir_if_local_acp() as export_dir:
        out_file_name = f"out_file.h5"
        out_path = export_dir / out_file_name

        with pytest.raises(ValueError):
            imported_solid_model_with_elements.export(path=out_path, format=invalid_format)


@pytest.mark.parametrize("format", ["ansys:cdb", "step", "iges", "stl"])
def test_skin_export(
    tempdir_if_local_acp, acp_instance, imported_solid_model_with_elements, format
):
    """Check that the skin export to a file works."""
    with tempdir_if_local_acp() as export_dir:
        with tempfile.TemporaryDirectory() as tmp_dir:
            ext = {"ansys:cdb": ".cdb", "step": ".stp", "iges": ".igs", "stl": ".stl"}[format]

            out_file_name = f"out_file{ext}"
            out_path = export_dir / out_file_name
            tmp_path = pathlib.Path(tmp_dir) / out_file_name

            imported_solid_model_with_elements.export_skin(path=out_file_name, format=format)
            acp_instance.download_file(out_path, tmp_path)

            assert tmp_path.exists()
            assert tmp_path.stat().st_size > 0


@given(invalid_format=st.text())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_skin_export_with_invalid_format_raises(
    imported_solid_model_with_elements, tempdir_if_local_acp, invalid_format
):
    """Check that the export to a file with an invalid format raises an exception."""
    assume(invalid_format not in ["ansys:cdb", "step", "iges", "stl"])

    with tempdir_if_local_acp() as export_dir:
        out_file_name = f"out_file.h5"
        out_path = export_dir / out_file_name

        with pytest.raises(ValueError):
            imported_solid_model_with_elements.export_skin(path=out_path, format=invalid_format)


def test_refresh(tempdir_if_local_acp, parent_object):
    """Check that refreshing works. Does not check the result of the refresh."""
    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempdir_if_local_acp() as tmp_dir:
        out_file_name = f"out_file.h5"
        out_path = pathlib.Path(tmp_dir) / out_file_name
        solid_model.export(path=out_path, format=pyacp.SolidModelExportFormat.ANSYS_H5)

        imported_solid_model = model.create_imported_solid_model(
            external_path=out_path,
            format=pyacp.SolidModelImportFormat.ANSYS_H5,
        )
        imported_solid_model.refresh()


@given(external_path=st.text())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture], deadline=None)
def test_refresh_inexistent_path(parent_object, external_path):
    """Check that refreshing with an inexistent path raises an exception."""
    assume(not pathlib.Path(external_path).exists())
    model = parent_object
    imported_solid_model = model.create_imported_solid_model()
    imported_solid_model.external_path = external_path
    with pytest.raises(RuntimeError):
        imported_solid_model.refresh()


def test_import_initial_mesh(tempdir_if_local_acp, parent_object):
    """Check that the 'import_initial_mesh' method works. Does not check the result."""
    model = parent_object
    solid_model = model.create_solid_model()
    solid_model.element_sets = [model.element_sets["All_Elements"]]
    model.update()

    with tempdir_if_local_acp() as tmp_dir:
        out_file_name = f"out_file.h5"
        out_path = pathlib.Path(tmp_dir) / out_file_name
        solid_model.export(path=out_path, format=pyacp.SolidModelExportFormat.ANSYS_H5)

        imported_solid_model = model.create_imported_solid_model(
            external_path=out_path,
            format=pyacp.SolidModelImportFormat.ANSYS_H5,
        )
        imported_solid_model.import_initial_mesh()
