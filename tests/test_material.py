from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st
import numpy.testing as npt
import pytest

from ansys.acp.core._tree_objects.enums import PlyType
from ansys.acp.core._tree_objects.material import (
    ConstantDensity,
    ConstantEngineeringConstants,
    FieldVariable,
    InterpolationOptions,
    VariableDensity,
    VariableEngineeringConstants,
)
from common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


@pytest.fixture
def parent_object(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        yield model


@pytest.fixture
def tree_object(parent_object):
    return parent_object.create_material()


@pytest.fixture
def variable_material(load_model_from_tempfile):
    with load_model_from_tempfile("variable_material.acph5") as model:
        yield model.materials["Variable Material"]


@pytest.fixture
def object_properties():
    return ObjectPropertiesToTest(
        read_write=[
            ("name", "Material Name"),
            ("ply_type", PlyType.WOVEN),
        ],
        read_only=[
            ("locked", True),
            ("id", "some_id"),
        ],
    )


class TestMaterial(WithLockedMixin, TreeObjectTester):
    COLLECTION_NAME = "materials"
    DEFAULT_PROPERTIES = {
        "ply_type": PlyType.UNDEFINED,
    }
    CREATE_METHOD_NAME = "create_material"
    INITIAL_OBJECT_NAMES = ("Structural Steel",)
    DEFAULT_VALUES_BY_PROPERTY_SET = {
        "density": {"rho": 0.0},
        "engineering_constants": {
            "E1": 0.0,
            "E2": 0.0,
            "E3": 0.0,
            "nu12": 0.0,
            "nu13": 0.0,
            "nu23": 0.0,
            "G12": 0.0,
            "G23": 0.0,
            "G31": 0.0,
        },
    }
    DEFAULT_TYPE_BY_PROPERTY_SET = {
        "density": ConstantDensity,
        "engineering_constants": ConstantEngineeringConstants,
    }
    DEFAULT_PROPERTY_SET_ATTRIBUTE_PAIRS = [
        ("density", "rho"),
        ("engineering_constants", "E1"),
        ("engineering_constants", "E2"),
        ("engineering_constants", "E3"),
        ("engineering_constants", "nu12"),
        ("engineering_constants", "nu23"),
        ("engineering_constants", "nu13"),
        ("engineering_constants", "G12"),
        ("engineering_constants", "G23"),
        ("engineering_constants", "G31"),
    ]

    @pytest.fixture
    def default_property_set_attribute_pairs(self):
        return (
            (property_set_name, attr_name)
            for property_set_name in list(self.DEFAULT_NAMES_BY_PROPERTY_SET.keys())
            for attr_name in self.DEFAULT_NAMES_BY_PROPERTY_SET[property_set_name]
        )

    def test_property_sets_default(self, tree_object):
        for propset_name in ["density", "engineering_constants"]:
            default_values = self.DEFAULT_VALUES_BY_PROPERTY_SET[propset_name]
            for attrib_name, attrib_value in default_values.items():
                assert getattr(getattr(tree_object, propset_name), attrib_name) == attrib_value
        with pytest.raises(AttributeError):
            tree_object.engineering_constant.E
        with pytest.raises(AttributeError):
            tree_object.engineering_constant.nu
        for propset_name in [
            "stress_limits",
            "strain_limits",
            "puck_constants",
            "woven_characterization",
            "woven_puck_constants_1",
            "woven_puck_constants_2",
            "woven_stress_limits_1",
            "woven_stress_limits_2",
            "tsai_wu_constants",
            "larc_constants",
            "fabric_fiber_angle",
        ]:
            assert getattr(tree_object, propset_name) is None

    @pytest.mark.parametrize(
        "property_set_name,property_set_value,attributes_to_check",
        [
            ("density", ConstantDensity(), DEFAULT_VALUES_BY_PROPERTY_SET["density"]),
            (
                "engineering_constants",
                ConstantEngineeringConstants(),
                DEFAULT_VALUES_BY_PROPERTY_SET["engineering_constants"],
            ),
        ],
    )
    def test_assign_property_set(
        self, tree_object, property_set_name, property_set_value, attributes_to_check
    ):
        setattr(tree_object, property_set_name, property_set_value)
        for attrib_name, attrib_value in attributes_to_check.items():
            assert getattr(getattr(tree_object, property_set_name), attrib_name) == attrib_value

    @pytest.fixture(
        params=[
            ("density", ConstantDensity),
            ("engineering_constants", ConstantEngineeringConstants),
        ]
    )
    def property_set_types(self, request):
        return request.param

    @pytest.fixture
    def property_set_name(self, property_set_types):
        return property_set_types[0]

    @pytest.fixture
    def property_set_value(self, property_set_types):
        return property_set_types[1]()

    def test_delete_property_set_by_assignment(
        self, tree_object, property_set_name, property_set_value
    ):
        # initialization: ensure the initial value is not None
        setattr(tree_object, property_set_name, property_set_value)
        assert getattr(tree_object, property_set_name) is not None

        setattr(tree_object, property_set_name, None)
        assert getattr(tree_object, property_set_name) is None

    def test_delete_property_set(self, tree_object, property_set_name, property_set_value):
        # initialization: ensure the initial value is not None
        setattr(tree_object, property_set_name, property_set_value)
        assert getattr(tree_object, property_set_name) is not None

        delattr(tree_object, property_set_name)
        assert getattr(tree_object, property_set_name) is None

    @pytest.mark.parametrize(
        "property_set_name,property_set_type,attributes_to_check",
        [
            (
                "density",
                VariableDensity,
                {
                    "rho": (1234.0, 2345.0),
                    "field_variables": (
                        FieldVariable(
                            name="Temperature",
                            values=(15.0, 25.0),
                            default=22.0,
                            lower_limit=10.0,
                            upper_limit=32.0,
                        ),
                    ),
                    "interpolation_options": InterpolationOptions(
                        algorithm="Triangulation-based Linear Multivariate",
                        cached=True,
                        normalized=True,
                    ),
                },
            ),
            (
                "engineering_constants",
                VariableEngineeringConstants,
                {
                    "E1": (1212, 1212.12),
                    "E2": (1313, 1313.13),
                    "E3": (1414, 1414.14),
                    "nu12": (0.1, 0.11),
                    "nu23": (0.2, 0.22),
                    "nu13": (0.3, 0.33),
                    "G12": (12.0, 12.1),
                    "G23": (23.0, 23.2),
                    "G31": (34.0, 34.4),
                    "field_variables": (
                        FieldVariable(
                            name="Temperature",
                            values=(20.0, 30.0),
                            default=22.0,
                            lower_limit=10.0,
                            upper_limit=32.0,
                        ),
                    ),
                    "interpolation_options": InterpolationOptions(
                        algorithm="Triangulation-based Linear Multivariate",
                        cached=True,
                        normalized=True,
                    ),
                },
            ),
        ],
    )
    def test_variable_material(
        self, variable_material, property_set_name, property_set_type, attributes_to_check
    ):
        property_set = getattr(variable_material, property_set_name)
        assert isinstance(property_set, property_set_type)
        for attrib_name, attrib_value in attributes_to_check.items():
            assert getattr(property_set, attrib_name) == attrib_value

    @pytest.mark.parametrize(
        "property_set_name", ["density", "engineering_constants", "stress_limits", "strain_limits"]
    )
    def test_variable_material_delete(self, variable_material, property_set_name):
        with pytest.raises(AttributeError):
            setattr(variable_material, property_set_name, None)
        with pytest.raises(AttributeError):
            delattr(variable_material, property_set_name)

    @pytest.mark.parametrize(
        "property_set_name,attr_name",
        DEFAULT_PROPERTY_SET_ATTRIBUTE_PAIRS,
    )
    @given(val=st.floats())
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_material_property_set(self, val, tree_object, property_set_name, attr_name):
        property_set = getattr(tree_object, property_set_name)
        setattr(property_set, attr_name, val)
        tree_object.density.rho = val
        # The ``npt.assert_equal`` check treats positive and negative zero as different. To avoid
        # this, we use ``npt.assert_allclose`` with zero tolerance.
        npt.assert_allclose(getattr(property_set, attr_name), val, rtol=0.0, atol=0.0)
        # We test also by directly accessing it from the 'tree_object', to ensure the base property
        # works as expected.
        npt.assert_allclose(
            getattr(getattr(tree_object, property_set_name), attr_name), val, rtol=0.0, atol=0.0
        )

    @pytest.mark.parametrize(
        "property_set_name,attr_name",
        DEFAULT_PROPERTY_SET_ATTRIBUTE_PAIRS,
    )
    @given(val=st.floats())
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_material_property_initialize(self, val, tree_object, property_set_name, attr_name):
        delattr(tree_object, property_set_name)
        setattr(
            tree_object,
            property_set_name,
            self.DEFAULT_TYPE_BY_PROPERTY_SET[property_set_name](**{attr_name: val}),
        )
        npt.assert_allclose(
            getattr(getattr(tree_object, property_set_name), attr_name), val, rtol=0.0, atol=0.0
        )
