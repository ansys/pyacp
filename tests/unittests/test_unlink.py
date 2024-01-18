"""Test cloning with the 'unlink' option."""

import pytest

from ansys.acp.core import Fabric


def test_add_after_unlink(load_model_from_tempfile):
    """
    Check that a model cloned with 'unlink=True' can be added to another model.
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = Fabric(thickness=0.001, material=material)
        model1.add_fabric(fabric)
        cloned_fabric = fabric.clone(unlink=True)
        model2.add_fabric(cloned_fabric)


def test_error_on_add_with_linked(load_model_from_tempfile):
    """
    Check the error which is raised when trying to store with links to another model
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = Fabric(thickness=0.001, material=material)
        model1.add_fabric(fabric)
        with pytest.raises(ValueError) as excinfo:
            cloned_fabric = fabric.clone()
            model2.add_fabric(cloned_fabric)
        assert "contains links" in str(excinfo.value)
