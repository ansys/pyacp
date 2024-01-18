from ansys.acp.core import ModelingGroup


def test_create_modeling_group(benchmark, load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        benchmark(lambda: model.add_modeling_group(ModelingGroup()))
