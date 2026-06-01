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

"""Tests for LookUpTable1DColumn and LookUpTable3DColumn."""

import numpy as np
import pytest

from ansys.acp.core import (
    LookUpTable1DColumn,
    LookUpTable3DColumn,
    LookUpTableColumnValueType,
    PhysicalDimension,
)

from .common.tree_object_tester import (
    ObjectPropertiesToTest,
    PropertyWithConversion,
    TreeObjectTester,
    WithLockedMixin,
)


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture(params=[LookUpTable1DColumn, LookUpTable3DColumn])
def column_type_to_test(request):
    return request.param


@pytest.fixture
def parent_object(parent_model, column_type_to_test, num_points):
    # Note: We need to add dummy values to the location column. Otherwise
    # a "shape mismatch" error occurs when we try to create columns
    # with data.
    if column_type_to_test == LookUpTable1DColumn:
        lookup_table = parent_model.create_lookup_table_1d()
        lookup_table.columns["Location"].data = np.random.rand(num_points)
        return lookup_table
    lookup_table = parent_model.create_lookup_table_3d()
    lookup_table.columns["Location"].data = np.random.rand(num_points, 3)
    return lookup_table


@pytest.fixture(params=[0, 1, 5])
def num_points(request):
    return request.param


@pytest.fixture(params=[LookUpTableColumnValueType.SCALAR, LookUpTableColumnValueType.DIRECTION])
def column_value_type(request):
    return request.param


@pytest.fixture(params=[False, True])  # Param controls whether the data is converted to a list
def column_data(num_points, column_value_type, request):
    if column_value_type == LookUpTableColumnValueType.SCALAR:
        res = np.random.rand(num_points)
    elif column_value_type == LookUpTableColumnValueType.DIRECTION:
        res = np.random.rand(num_points, 3)
    if request.param:
        if num_points == 0 and column_value_type == LookUpTableColumnValueType.DIRECTION:
            return PropertyWithConversion(res.tolist(), np.zeros(shape=(0, 3)))
        return res.tolist()
    return res


@pytest.fixture
def tree_object(parent_object, column_value_type, num_points, column_type_to_test):
    if column_type_to_test == LookUpTable1DColumn:
        data = np.linspace(-10.0, 10.0, num_points)
    else:
        data = np.random.rand(num_points, 3)
    parent_object.columns["Location"].data = data
    return parent_object.create_column(value_type=column_value_type)


@pytest.fixture
def default_data(num_points):
    # Default data is a NaN array with the same number of entries as as the location column.
    # The default value_type is LookUpTableColumnValueType.SCALAR, so we have one
    # scalar value per location
    return np.full(num_points, np.nan)


class TestLookUpTableColumn(WithLockedMixin, TreeObjectTester):
    INITIAL_OBJECT_NAMES = ("Location",)
    COLLECTION_NAME = "columns"

    @staticmethod
    @pytest.fixture
    def default_properties(default_data):
        return {
            "value_type": LookUpTableColumnValueType.SCALAR,
            "physical_dimension": PhysicalDimension.DIMENSIONLESS,
            "data": default_data,
        }

    CREATE_METHOD_NAME = "create_column"

    @staticmethod
    @pytest.fixture
    def object_properties(column_data, column_value_type):
        return ObjectPropertiesToTest(
            read_write=[
                ("name", "some_name"),
                ("data", column_data),
                ("physical_dimension", PhysicalDimension.TIME),
                ("physical_dimension", PhysicalDimension.CURRENCY),
                ("physical_dimension", PhysicalDimension.MASS),
            ],
            read_only=[
                ("id", "some_id"),
                ("value_type", LookUpTableColumnValueType.SCALAR),
                ("value_type", LookUpTableColumnValueType.DIRECTION),
            ],
            create_args=[
                {
                    "name": "some_name",
                    "data": column_data,
                    "physical_dimension": PhysicalDimension.TIME,
                    "value_type": column_value_type,
                }
            ],
        )
