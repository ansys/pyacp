def test_create_modeling_group(benchmark, load_model_from_tempfile):
    with load_model_from_tempfile() as model:
        benchmark(model.create_modeling_group)
