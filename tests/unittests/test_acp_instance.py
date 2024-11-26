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


from contextlib import contextmanager
import os
import pathlib
import shutil
import tempfile

import pytest


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
