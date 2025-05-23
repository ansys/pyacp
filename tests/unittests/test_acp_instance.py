# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
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


from contextlib import contextmanager
import os
import pathlib
import shutil
import tempfile

import pytest

import ansys.acp.core as pyacp


def test_server_version(acp_instance):
    version = acp_instance.server_version
    assert isinstance(version, str)
    assert version != ""


def test_models(acp_instance, load_model_from_tempfile):
    with load_model_from_tempfile() as m1:
        assert acp_instance.models == (m1,)

        with load_model_from_tempfile() as m2:
            # the order of models is not guaranteed
            current_models = acp_instance.models
            assert len(current_models) == 2
            assert m1 in current_models
            assert m2 in current_models

            acp_instance.clear()
            assert acp_instance.models == ()


@contextmanager
def change_cwd(new_cwd):
    old_cwd = os.getcwd()
    os.chdir(new_cwd)
    try:
        yield
    finally:
        os.chdir(old_cwd)


def test_import_from_differenct_cwd(acp_instance, model_data_dir):
    if acp_instance.is_remote:
        pytest.skip("Test is not relevant for remote instances")
    with tempfile.TemporaryDirectory() as tmp_dir:
        model_filename = "minimal_complete_model.acph5"
        tmp_dir_path = pathlib.Path(tmp_dir)
        shutil.copyfile(model_data_dir / model_filename, tmp_dir_path / model_filename)
        with change_cwd(tmp_dir):
            model = acp_instance.import_model(model_filename)
            export_filename = "exported_model.acph5"
            model.save(export_filename)
            assert (tmp_dir_path / export_filename).exists()
        # Check that the exported file does not exist on the original CWD
        assert not pathlib.Path(export_filename).exists()


def test_import_inexistent(acp_instance):
    """Test that inexistent files raise a FileNotFoundError.

    Regression test for #748 (when run with 'direct' launch mode).
    """
    filename = "inexistent_file.acph5"
    with pytest.raises(FileNotFoundError) as exc:
        acp_instance.import_model(filename)
    assert filename in str(exc.value)


@pytest.mark.parametrize(
    "input_unit_system,expected_unit_system",
    [
        ("SI", pyacp.UnitSystemType.SI),
        ("Si", pyacp.UnitSystemType.SI),
        ("si", pyacp.UnitSystemType.SI),
        (pyacp.UnitSystemType.SI, pyacp.UnitSystemType.SI),
        ("uMKS", pyacp.UnitSystemType.uMKS),
    ],
)
def test_import_unit_system(acp_instance, model_data_dir, input_unit_system, expected_unit_system):
    model = acp_instance.import_model(
        model_data_dir / "class40.cdb",
        unit_system=input_unit_system,
        format="ansys:cdb",
    )
    assert model.unit_system == expected_unit_system


@pytest.mark.parametrize("format", ["ansys:cdb", "AnSYS:cDB", pyacp.FeFormat.ANSYS_CDB])
def test_format_capitalization(acp_instance, model_data_dir, format):
    """Test that the format is case insensitive."""
    acp_instance.import_model(
        model_data_dir / "class40.cdb",
        unit_system="SI",
        format=format,
    )


def test_restart_wait(acp_instance, load_model_from_tempfile):
    """Test that the server is accessible after restart.

    Regression test for missing '.wait()' in the restart method, and
    the 'ACPInstance._channel' not being set to the new channel on restart.
    """
    acp_instance.restart(start_timeout=30)
    # Check that the server is fully functional again (also exercises filetransfer)
    with load_model_from_tempfile():
        pass
