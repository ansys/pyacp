"""Tests for LookUpTable1DColumn and LookUpTable3DColumn."""

import numpy as np
import pytest

from ansys.acp.core import (
    DimensionType,
    LookUpTable1DColumn,
    LookUpTable3DColumn,
    LookUpTableColumnValueType,
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
            "dimension_type": DimensionType.DIMENSIONLESS,
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
                ("dimension_type", DimensionType.TIME),
                ("dimension_type", DimensionType.CURRENCY),
                ("dimension_type", DimensionType.MASS),
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
                    "dimension_type": DimensionType.TIME,
                    "value_type": column_value_type,
                }
            ],
        )
