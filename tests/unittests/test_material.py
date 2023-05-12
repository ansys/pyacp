from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st
import numpy.testing as npt
import pytest

from ansys.acp.core._tree_objects.enums import PlyType
from ansys.acp.core._tree_objects.material.property_sets import (
    ConstantDensity,
    ConstantEngineeringConstants,
    ConstantFabricFiberAngle,
    ConstantLaRCConstants,
    ConstantPuckConstants,
    ConstantStrainLimits,
    ConstantStressLimits,
    ConstantTsaiWuConstants,
    ConstantWovenCharacterization,
    ConstantWovenStressLimits,
    FieldVariable,
    InterpolationOptions,
    VariableDensity,
    VariableEngineeringConstants,
    VariableStrainLimits,
    VariableStressLimits,
)

from .common.tree_object_tester import ObjectPropertiesToTest, TreeObjectTester, WithLockedMixin


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
        "stress_limits": ConstantStressLimits,
        "strain_limits": ConstantStrainLimits,
        "puck_constants": ConstantPuckConstants,
        "woven_characterization": ConstantWovenCharacterization,
        "woven_puck_constants_1": ConstantPuckConstants,
        "woven_puck_constants_2": ConstantPuckConstants,
        "woven_stress_limits_1": ConstantWovenStressLimits,
        "woven_stress_limits_2": ConstantWovenStressLimits,
        "tsai_wu_constants": ConstantTsaiWuConstants,
        "larc_constants": ConstantLaRCConstants,
        "fabric_fiber_angle": ConstantFabricFiberAngle,
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
    EXTRA_PROPERTY_SET_ATTRIBUTE_PAIRS = [
        ("stress_limits", "Xt"),
        ("stress_limits", "Yt"),
        ("stress_limits", "Zt"),
        ("stress_limits", "Xc"),
        ("stress_limits", "Yc"),
        ("stress_limits", "Zc"),
        ("stress_limits", "Sxy"),
        ("stress_limits", "Syz"),
        ("stress_limits", "Sxz"),
        ("strain_limits", "eXt"),
        ("strain_limits", "eYt"),
        ("strain_limits", "eZt"),
        ("strain_limits", "eXc"),
        ("strain_limits", "eYc"),
        ("strain_limits", "eZc"),
        ("strain_limits", "eSxy"),
        ("strain_limits", "eSyz"),
        ("strain_limits", "eSxz"),
        ("puck_constants", "p_21_pos"),
        ("puck_constants", "p_22_pos"),
        ("puck_constants", "p_21_neg"),
        ("puck_constants", "p_22_neg"),
        ("puck_constants", "s"),
        ("puck_constants", "M"),
        ("puck_constants", "interface_weakening_factor"),
        ("woven_characterization", "orientation_1"),
        ("woven_characterization", "E1_1"),
        ("woven_characterization", "E2_1"),
        ("woven_characterization", "G12_1"),
        ("woven_characterization", "G23_1"),
        ("woven_characterization", "nu12_1"),
        ("woven_characterization", "orientation_2"),
        ("woven_characterization", "E1_2"),
        ("woven_characterization", "E2_2"),
        ("woven_characterization", "G12_2"),
        ("woven_characterization", "G23_2"),
        ("woven_characterization", "nu12_2"),
        ("woven_puck_constants_1", "p_21_pos"),
        ("woven_puck_constants_1", "p_22_pos"),
        ("woven_puck_constants_1", "p_21_neg"),
        ("woven_puck_constants_1", "p_22_neg"),
        ("woven_puck_constants_1", "s"),
        ("woven_puck_constants_1", "M"),
        ("woven_puck_constants_1", "interface_weakening_factor"),
        ("woven_puck_constants_2", "p_21_pos"),
        ("woven_puck_constants_2", "p_22_pos"),
        ("woven_puck_constants_2", "p_21_neg"),
        ("woven_puck_constants_2", "p_22_neg"),
        ("woven_puck_constants_2", "s"),
        ("woven_puck_constants_2", "M"),
        ("woven_puck_constants_2", "interface_weakening_factor"),
        ("woven_stress_limits_1", "Xt"),
        ("woven_stress_limits_1", "Yt"),
        ("woven_stress_limits_1", "Zt"),
        ("woven_stress_limits_1", "Xc"),
        ("woven_stress_limits_1", "Yc"),
        ("woven_stress_limits_1", "Zc"),
        ("woven_stress_limits_1", "Sxy"),
        ("woven_stress_limits_1", "Syz"),
        ("woven_stress_limits_2", "Xt"),
        ("woven_stress_limits_2", "Yt"),
        ("woven_stress_limits_2", "Zt"),
        ("woven_stress_limits_2", "Xc"),
        ("woven_stress_limits_2", "Yc"),
        ("woven_stress_limits_2", "Zc"),
        ("woven_stress_limits_2", "Sxy"),
        ("woven_stress_limits_2", "Syz"),
        ("tsai_wu_constants", "XY"),
        ("tsai_wu_constants", "XZ"),
        ("tsai_wu_constants", "YZ"),
        ("larc_constants", "fracture_angle_under_compression"),
        ("larc_constants", "fracture_toughness_ratio"),
        ("larc_constants", "fracture_toughness_mode_1"),
        ("larc_constants", "fracture_toughness_mode_2"),
        ("larc_constants", "thin_ply_thickness_limit"),
        ("fabric_fiber_angle", "fabric_fiber_angle"),
    ]

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
            (
                "stress_limits",
                VariableStressLimits,
                {
                    "Xt": (11, 11.11),
                    "Yt": (22, 22.22),
                    "Zt": (33, 33.33),
                    "Xc": (-12, -12.12),
                    "Yc": (-23, -23.23),
                    "Zc": (-34, -34.34),
                    "Sxy": (13, 13.13),
                    "Syz": (24, 24.24),
                    "Sxz": (35, 35.35),
                    "field_variables": (
                        FieldVariable(
                            name="Temperature",
                            values=(10.0, 30.0),
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
                "strain_limits",
                VariableStrainLimits,
                {
                    "eXt": (1.23, 0.123),
                    "eYt": (2.34, 0.234),
                    "eZt": (3.45, 0.345),
                    "eXc": (-1.23, -0.123),
                    "eYc": (-2.34, -0.234),
                    "eZc": (-3.45, -0.345),
                    "eSxy": (111, 1111),
                    "eSyz": (222, 2222),
                    "eSxz": (333, 3333),
                    "field_variables": (
                        FieldVariable(
                            name="Temperature",
                            values=(12.0, 32.0),
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
        DEFAULT_PROPERTY_SET_ATTRIBUTE_PAIRS + EXTRA_PROPERTY_SET_ATTRIBUTE_PAIRS,
    )
    @given(val=st.floats())
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_material_property_set_after_init(self, val, tree_object, property_set_name, attr_name):
        setattr(
            tree_object,
            property_set_name,
            self.DEFAULT_TYPE_BY_PROPERTY_SET[property_set_name](**{attr_name: val}),
        )

        property_set = getattr(tree_object, property_set_name)
        setattr(property_set, attr_name, val)
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
        DEFAULT_PROPERTY_SET_ATTRIBUTE_PAIRS + EXTRA_PROPERTY_SET_ATTRIBUTE_PAIRS,
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