"""Test cloning with the 'unlink' option."""

import pytest


def test_store_after_unlink(load_model_from_tempfile):
    """
    Check that a model cloned with 'unlink=True' can be stored on another model.
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = model1.create_fabric(thickness=0.001, material=material)
        cloned_fabric = fabric.clone(unlink=True)
        cloned_fabric.store(parent=model2)


def test_error_on_store_with_linked(load_model_from_tempfile):
    """
    Check the error which is raised when trying to store with links to another model
    """
    with load_model_from_tempfile() as model1, load_model_from_tempfile() as model2:
        material = list(model1.materials.values())[0]
        fabric = model1.create_fabric(thickness=0.001, material=material)
        with pytest.raises(ValueError) as excinfo:
            cloned_fabric = fabric.clone()
            cloned_fabric.store(parent=model2)
        assert "contains links" in str(excinfo.value)
