# Copyright (C) 2022 - 2026 ANSYS, Inc. and/or its affiliates.
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

from packaging.version import parse as parse_version
import pytest

from ansys.acp.core import CutOffMaterialHandling, DrapingMaterialModel, DropOffMaterialHandling

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_fabric()


class TestFabric(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "fabrics"

    @staticmethod
    @pytest.fixture
    def default_properties(acp_instance):
        if parse_version(acp_instance.server_version) < parse_version("25.1"):
            return {
                "status": "NOTUPTODATE",
                "thickness": 0.0,
                "area_price": 0.0,
                "ignore_for_postprocessing": False,
                "drop_off_material_handling": DropOffMaterialHandling.GLOBAL,
                "cut_off_material_handling": CutOffMaterialHandling.COMPUTED,
                "draping_material_model": DrapingMaterialModel.WOVEN,
                "draping_ud_coefficient": 0.0,
                "material": None,
            }
        else:
            return {
                "status": "NOTUPTODATE",
                "thickness": 0.0,
                "area_price": 0.0,
                "ignore_for_postprocessing": False,
                "drop_off_material_handling": DropOffMaterialHandling.GLOBAL,
                "drop_off_material": None,
                "cut_off_material_handling": CutOffMaterialHandling.COMPUTED,
                "cut_off_material": None,
                "draping_material_model": DrapingMaterialModel.WOVEN,
                "draping_ud_coefficient": 0.0,
                "material": None,
            }

    CREATE_METHOD_NAME = "create_fabric"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object, acp_instance):
        model = parent_object
        material = model.create_material(name="Material")
        cut_off_material = model.create_material(name="Cut-off Material")
        drop_off_material = model.create_material(name="Drop-off Material")
        if parse_version(acp_instance.server_version) < parse_version("25.1"):
            return ObjectPropertiesToTest(
                read_write=[
                    ("name", "Fabric name"),
                    ("thickness", 1e-6),
                    ("area_price", 5.98),
                    ("ignore_for_postprocessing", True),
                    ("drop_off_material_handling", DropOffMaterialHandling.GLOBAL),
                    ("cut_off_material_handling", CutOffMaterialHandling.COMPUTED),
                    ("draping_material_model", DrapingMaterialModel.UD),
                    ("draping_ud_coefficient", 0.55),
                    ("material", material),
                    ("material", None),
                    ("material", material),
                ],
                read_only=[
                    ("id", "some_id"),
                    ("status", "UPTODATE"),
                    ("area_weight", 0.0),
                    # ("draping_ud_coefficient", 4.32), # TODO: enable this check, see backend issue #778698
                ],
            )
        else:
            return ObjectPropertiesToTest(
                read_write=[
                    ("name", "Fabric name"),
                    ("thickness", 1e-6),
                    ("area_price", 5.98),
                    ("ignore_for_postprocessing", True),
                    ("drop_off_material_handling", DropOffMaterialHandling.CUSTOM),
                    ("drop_off_material", drop_off_material),
                    ("cut_off_material_handling", CutOffMaterialHandling.CUSTOM),
                    ("cut_off_material", cut_off_material),
                    ("draping_material_model", DrapingMaterialModel.UD),
                    ("draping_ud_coefficient", 0.55),
                    ("material", material),
                    ("material", None),
                    ("material", material),
                ],
                read_only=[
                    ("id", "some_id"),
                    ("status", "UPTODATE"),
                    ("area_weight", 0.0),
                ],
            )


@pytest.mark.parametrize("material_type", ["cut_off_material", "drop_off_material"])
def test_solid_model_materials(parent_object, tree_object, acp_instance, material_type):
    """Check that solid model materials are supported since 25.1."""
    tree_object.cut_off_material_handling = CutOffMaterialHandling.CUSTOM
    tree_object.drop_off_material_handling = DropOffMaterialHandling.CUSTOM
    if parse_version(acp_instance.server_version) < parse_version("25.1"):
        with pytest.raises(RuntimeError) as exc:
            setattr(tree_object, material_type, parent_object.create_material(name="Material"))
        assert f"The property '{material_type}' is only editable since version" in str(exc.value)
    else:
        material = parent_object.create_material(name="new material")
        setattr(tree_object, material_type, material)
        sm_material = getattr(tree_object, material_type)
        assert sm_material.id == material.id
