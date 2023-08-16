"""Tests for LookUpTable1DColumn and LookUpTable3DColumn."""

import numpy as np
import pytest

from ansys.acp.core import LookUpTable1DColumn, LookUpTable3DColumn
from ansys.acp.core._tree_objects.enums import DimensionType, LookUpTableColumnValueType

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_model(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture(params=[LookUpTable1DColumn, LookUpTable3DColumn])
def column_type_to_test(request):
    return request.param


@pytest.fixture
def parent_object(parent_model, column_type_to_test):
    if column_type_to_test == LookUpTable1DColumn:
        return parent_model.create_lookup_table_1d()
    return parent_model.create_lookup_table_3d()


@pytest.fixture(params=[0, 1, 5])
def num_points(request):
    return request.param


@pytest.fixture(params=[LookUpTableColumnValueType.SCALAR, LookUpTableColumnValueType.DIRECTION])
def column_value_type(request):
    return request.param


@pytest.fixture
def column_data(num_points, column_value_type):
    if column_value_type == LookUpTableColumnValueType.SCALAR:
        return np.random.rand(num_points)
    elif column_value_type == LookUpTableColumnValueType.DIRECTION:
        return np.random.rand(num_points, 3)


@pytest.fixture
def tree_object(parent_object, column_value_type, num_points, column_type_to_test):
    if column_type_to_test == LookUpTable1DColumn:
        data = np.linspace(-10.0, 10.0, num_points)
    else:
        data = np.random.rand(num_points, 3)
    parent_object.columns["Location"].data = data
    return parent_object.create_column(value_type=column_value_type)


class TestLookUpTableColumn(WithLockedMixin, TreeObjectTester):
    INITIAL_OBJECT_NAMES = ("Location",)
    COLLECTION_NAME = "columns"
    DEFAULT_PROPERTIES = {
        "value_type": LookUpTableColumnValueType.SCALAR,
        "dimension_type": DimensionType.DIMENSIONLESS,
        "data": np.array([]),
    }
    CREATE_METHOD_NAME = "create_column"

    @staticmethod
    @pytest.fixture
    def object_properties(column_data):
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
                ("status", "UPTODATE"),
                ("value_type", LookUpTableColumnValueType.SCALAR),
                ("value_type", LookUpTableColumnValueType.DIRECTION),
            ],
        )
