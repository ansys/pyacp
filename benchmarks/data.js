window.BENCHMARK_DATA = {
  "lastUpdate": 1683908269203,
  "repoUrl": "https://github.com/ansys-internal/pyacp",
  "entries": {
    "PyACP benchmarks": [
      {
        "commit": {
          "author": {
            "email": "dominik.gresch@ansys.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "committer": {
            "email": "dominik.gresch@ansys.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "distinct": true,
          "id": "6238060603cdd651c6e74e59040744ba9d4a16f6",
          "message": "Add performance benchmarks\n\nAdd a simple performance benchmark using 'pytest-benchmark', and\nCI steps to publish it into the 'gh-pages' branch.",
          "timestamp": "2023-05-12T18:10:54+02:00",
          "tree_id": "8b6eeb0223f379c7a4a0af1d3dc36c2fdd8dca66",
          "url": "https://github.com/ansys-internal/pyacp/commit/6238060603cdd651c6e74e59040744ba9d4a16f6"
        },
        "date": 1683908049528,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1550.8830864966635,
            "unit": "iter/sec",
            "range": "stddev: 0.00011767903197185646",
            "extra": "mean: 644.7939297983643 usec\nrounds: 641"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 382.5057666571109,
            "unit": "iter/sec",
            "range": "stddev: 0.00024331128078826475",
            "extra": "mean: 2.614339670587055 msec\nrounds: 340"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.29131338812981,
            "unit": "iter/sec",
            "range": "stddev: 0.00020510301317696223",
            "extra": "mean: 20.707657958331776 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.979513494719908,
            "unit": "iter/sec",
            "range": "stddev: 0.00007382313234924128",
            "extra": "mean: 200.82283159998724 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000kbit]",
            "value": 225.9514438305156,
            "unit": "iter/sec",
            "range": "stddev: 0.0002195526612159417",
            "extra": "mean: 4.42572963043375 msec\nrounds: 184"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100kbit]",
            "value": 25.163327310588784,
            "unit": "iter/sec",
            "range": "stddev: 0.0027628622786129856",
            "extra": "mean: 39.74037247368307 msec\nrounds: 19"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10kbit]",
            "value": 2.277020513139004,
            "unit": "iter/sec",
            "range": "stddev: 0.04459826610549961",
            "extra": "mean: 439.17039580001074 msec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "ansys-internal",
            "username": "ansys-internal"
          },
          "committer": {
            "name": "ansys-internal",
            "username": "ansys-internal"
          },
          "id": "6238060603cdd651c6e74e59040744ba9d4a16f6",
          "message": "Add performance benchmarks",
          "timestamp": "2023-05-08T11:44:43Z",
          "url": "https://github.com/ansys-internal/pyacp/pull/190/commits/6238060603cdd651c6e74e59040744ba9d4a16f6"
        },
        "date": 1683908266843,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1118.1463449564858,
            "unit": "iter/sec",
            "range": "stddev: 0.00022157242198408335",
            "extra": "mean: 894.3373150666752 usec\nrounds: 438"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 334.040171415687,
            "unit": "iter/sec",
            "range": "stddev: 0.0005628459230674445",
            "extra": "mean: 2.9936519184561727 msec\nrounds: 233"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.65717857668674,
            "unit": "iter/sec",
            "range": "stddev: 0.00022335576420742944",
            "extra": "mean: 20.98319770212303 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9636096630623365,
            "unit": "iter/sec",
            "range": "stddev: 0.00017859685221808353",
            "extra": "mean: 201.4662852000015 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000kbit]",
            "value": 212.51441935477973,
            "unit": "iter/sec",
            "range": "stddev: 0.00016532210416727995",
            "extra": "mean: 4.705563053255984 msec\nrounds: 169"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100kbit]",
            "value": 25.19942379687196,
            "unit": "iter/sec",
            "range": "stddev: 0.0019396641374281422",
            "extra": "mean: 39.68344705263187 msec\nrounds: 19"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10kbit]",
            "value": 2.2759897229504547,
            "unit": "iter/sec",
            "range": "stddev: 0.0447455503910239",
            "extra": "mean: 439.3692950000059 msec\nrounds: 5"
          }
        ]
      }
    ]
  }
}