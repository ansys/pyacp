import pytest


def test_error_formatting(load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        model.modeling_groups["ModelingGroup.1"].create_modeling_ply()
        with pytest.raises(RuntimeError) as excinfo:
            model.update()
        assert len(str(excinfo.value)) < 200
