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

import pytest

from ansys.acp.core import SensorType

from .common.tree_object_tester import NoLockedMixin, ObjectPropertiesToTest, TreeObjectTester


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_sensor()


class TestSensor(NoLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "sensors"

    @staticmethod
    @pytest.fixture
    def default_properties():
        return {
            "status": "NOTUPTODATE",
            "active": True,
            "entities": [],
            "covered_area": None,
            "modeling_ply_area": None,
            "production_ply_area": None,
            "price": None,
            "weight": None,
            "center_of_gravity": None,
        }

    CREATE_METHOD_NAME = "create_sensor"

    @staticmethod
    @pytest.fixture
    def object_properties(parent_object):
        model = parent_object
        elset = model.create_element_set()
        oriented_selection_set = model.create_oriented_selection_set()
        modeling_ply = model.create_modeling_group().create_modeling_ply()
        fabric = model.create_fabric()
        stackup = model.create_stackup()
        sublaminate = model.create_sublaminate()
        solid_model = model.create_solid_model()
        imported_solid_model = model.create_imported_solid_model()
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "Sensor name"),
                ("sensor_type", SensorType.SENSOR_BY_AREA),
                ("entities", [elset, modeling_ply, oriented_selection_set]),
                ("sensor_type", SensorType.SENSOR_BY_MATERIAL),
                ("entities", [stackup, fabric, sublaminate]),
                ("sensor_type", SensorType.SENSOR_BY_PLIES),
                ("entities", [modeling_ply]),
                ("sensor_type", SensorType.SENSOR_BY_SOLID_MODEL),
                ("entities", []),
                ("sensor_type", SensorType.SENSOR_BY_SOLID_MODEL),
                ("entities", [solid_model, imported_solid_model]),
                ("active", False),
            ],
            read_only=[
                ("id", "some_id"),
                ("status", "UPTODATE"),
                ("locked", True),
                ("covered_area", 0.3),
                ("modeling_ply_area", 0.3),
                ("production_ply_area", 0.3),
                ("price", 0.3),
                ("weight", 0.3),
                ("center_of_gravity", (0.1, 0.2, 0.3)),
            ],
        )
