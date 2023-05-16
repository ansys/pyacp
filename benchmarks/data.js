window.BENCHMARK_DATA = {
  "lastUpdate": 1684243170777,
  "repoUrl": "https://github.com/ansys-internal/pyacp",
  "entries": {
    "PyACP benchmarks": [
      {
        "commit": {
          "author": {
            "email": "greschd@users.noreply.github.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4772a76d95f4b3ff3d8a975bc90301331ed0f222",
          "message": "Add performance benchmarks (#190)\n\nAdd a simple performance benchmark using `pytest-benchmark`, and \r\nCI steps to publish it into the `gh-pages` branch.\r\n\r\nRendered at https://acp.docs.pyansys.com/benchmarks/",
          "timestamp": "2023-05-16T14:44:28+02:00",
          "tree_id": "667bbe2319dbb07082e9c34f44fe4b3c839a2dd9",
          "url": "https://github.com/ansys-internal/pyacp/commit/4772a76d95f4b3ff3d8a975bc90301331ed0f222"
        },
        "date": 1684241278835,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.029314004808175,
            "unit": "iter/sec",
            "range": "stddev: 0.01102751877272644",
            "extra": "mean: 248.18120374999353 msec\nrounds: 4"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 797.3004846922356,
            "unit": "iter/sec",
            "range": "stddev: 0.0007740440713619837",
            "extra": "mean: 1.254232274029042 msec\nrounds: 978"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "greschd@users.noreply.github.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "5e2365394e0c5c8e812561fad0bc2d9b9287081b",
          "message": "Implement stop timeout (#192)\n\nImplement the `timeout` parameter in the `stop` method for\r\nboth the `direct` and `docker_compose` launcher.\r\n\r\nSet the timeout to 1 second in tests, to speed up tear-down.\r\nThis previously took ~13s for the benchmark tests.",
          "timestamp": "2023-05-16T15:16:09+02:00",
          "tree_id": "87ccda3de28d8e893992cafa858551a935bacfa7",
          "url": "https://github.com/ansys-internal/pyacp/commit/5e2365394e0c5c8e812561fad0bc2d9b9287081b"
        },
        "date": 1684243167843,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.612659256365068,
            "unit": "iter/sec",
            "range": "stddev: 0.004483852106056033",
            "extra": "mean: 151.2250913333304 msec\nrounds: 6"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1141.433399444726,
            "unit": "iter/sec",
            "range": "stddev: 0.00033193261914098095",
            "extra": "mean: 876.0914132059485 usec\nrounds: 1469"
          }
        ]
      }
    ]
  }
}