window.BENCHMARK_DATA = {
  "lastUpdate": 1684919681213,
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
          "id": "63ee2986489921f5effbdea0bda45eb4e2c77aec",
          "message": "Improve dependency specification (#196)\n\n* Make `ansys-dpf-core` and `ansys-dpf-composites` optional in the main\r\n  dependency group, and extend their possible versions.\r\n* Move `hypothesis` to the `test` dependency group\r\n* Sort dependencies",
          "timestamp": "2023-05-16T17:45:02+02:00",
          "tree_id": "755543975f2e81d3e30e204e46328ef26f2b8c07",
          "url": "https://github.com/ansys-internal/pyacp/commit/63ee2986489921f5effbdea0bda45eb4e2c77aec"
        },
        "date": 1684252098730,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.437394415600574,
            "unit": "iter/sec",
            "range": "stddev: 0.002369872972674608",
            "extra": "mean: 155.34235366665902 msec\nrounds: 6"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1164.755415633218,
            "unit": "iter/sec",
            "range": "stddev: 0.0002773744490673541",
            "extra": "mean: 858.5493457064983 usec\nrounds: 1374"
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
          "id": "528550aa5be0de1406d63b5aaea308a63963b14a",
          "message": "Fix --validate-benchmarks-only flag use in CI (#199)\n\nFixes when the ``--validate-benchmarks-only`` flag is passed to the\r\nbenchmarks step\r\nin CI: When the benchmarks are subsequently published, the flag should\r\nnot be passed,\r\nto run a full benchmark.\r\n\r\nThe root cause for this is that the ``${{ <condition> && <optionA> ||\r\n<optionB> }}``\r\nworkaround used to implement a ternary operator in Github Actions only\r\nworks correctly\r\nif ``<optionA>`` evaluates to ``true``.",
          "timestamp": "2023-05-17T14:52:49Z",
          "tree_id": "5cea4656a78cf587be3a6b5ddbf722f540b62591",
          "url": "https://github.com/ansys-internal/pyacp/commit/528550aa5be0de1406d63b5aaea308a63963b14a"
        },
        "date": 1684335476315,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.620717149347334,
            "unit": "iter/sec",
            "range": "stddev: 0.0037901760935207976",
            "extra": "mean: 151.041039428573 msec\nrounds: 7"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5807571539409233,
            "unit": "iter/sec",
            "range": "stddev: 0.003365430412519948",
            "extra": "mean: 387.48318433331025 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3888333283217956,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.571796003999964 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04129549636518221,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.215715708000005 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.7753312599291418,
            "unit": "iter/sec",
            "range": "stddev: 0.0045550551386886115",
            "extra": "mean: 264.87741899998696 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7618379929719276,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3126150300000177 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08396883414296989,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.909180473999982 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1080.0487554344172,
            "unit": "iter/sec",
            "range": "stddev: 0.00037710893429080083",
            "extra": "mean: 925.8841278862269 usec\nrounds: 1689"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 393.15513703704715,
            "unit": "iter/sec",
            "range": "stddev: 0.00008797102997267666",
            "extra": "mean: 2.5435252036545806 msec\nrounds: 383"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.55681784475276,
            "unit": "iter/sec",
            "range": "stddev: 0.00012201964789082507",
            "extra": "mean: 20.59443028571659 msec\nrounds: 49"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.978092886720586,
            "unit": "iter/sec",
            "range": "stddev: 0.000023962831036338417",
            "extra": "mean: 200.88014080001813 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 948.1276714826421,
            "unit": "iter/sec",
            "range": "stddev: 0.0002665433621366344",
            "extra": "mean: 1.0547102780327486 msec\nrounds: 874"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 233.8788018498991,
            "unit": "iter/sec",
            "range": "stddev: 0.000058126567468073405",
            "extra": "mean: 4.275718842795293 msec\nrounds: 229"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.089912622275257,
            "unit": "iter/sec",
            "range": "stddev: 0.00009588956376329397",
            "extra": "mean: 38.32898999999762 msec\nrounds: 27"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "greschd@users.noreply.github.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "distinct": true,
          "id": "5a1493ebdbf4026b38aa5f632554124bbd16fec7",
          "message": "Bump typing-extensions from 4.5.0 to 4.6.0\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.5.0 to 4.6.0.\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/python/typing_extensions/compare/4.5.0...4.6.0)\n\n---\nupdated-dependencies:\n- dependency-name: typing-extensions\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "timestamp": "2023-05-23T10:44:25+02:00",
          "tree_id": "79d7b62e6384fe215a40720ea7f5d1c46daf83dc",
          "url": "https://github.com/ansys-internal/pyacp/commit/5a1493ebdbf4026b38aa5f632554124bbd16fec7"
        },
        "date": 1684831752384,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.435758584956116,
            "unit": "iter/sec",
            "range": "stddev: 0.0024443898316857367",
            "extra": "mean: 155.38183833333127 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5462318856670345,
            "unit": "iter/sec",
            "range": "stddev: 0.0022881846070904053",
            "extra": "mean: 392.73720733334966 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38601747908453454,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5905562680000003 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041278281979133996,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.225814448999984 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.7123891509253295,
            "unit": "iter/sec",
            "range": "stddev: 0.007687905575702698",
            "extra": "mean: 269.368312250009 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.757019729451964,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3209695350000175 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08383479952827416,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.928220806000013 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1188.1912667423203,
            "unit": "iter/sec",
            "range": "stddev: 0.00030811108443494137",
            "extra": "mean: 841.6153425716662 usec\nrounds: 1299"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 390.8734774190454,
            "unit": "iter/sec",
            "range": "stddev: 0.00007407369442718814",
            "extra": "mean: 2.5583726135706204 msec\nrounds: 339"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.517656862522216,
            "unit": "iter/sec",
            "range": "stddev: 0.00011277913942526754",
            "extra": "mean: 20.6110530612301 msec\nrounds: 49"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.976600071254692,
            "unit": "iter/sec",
            "range": "stddev: 0.00003918220808218412",
            "extra": "mean: 200.9403981999867 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 936.4113851452794,
            "unit": "iter/sec",
            "range": "stddev: 0.00016212381199621267",
            "extra": "mean: 1.0679067083799447 msec\nrounds: 919"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 225.63287009799208,
            "unit": "iter/sec",
            "range": "stddev: 0.00015705284694524506",
            "extra": "mean: 4.431978370729856 msec\nrounds: 205"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.8541328116174,
            "unit": "iter/sec",
            "range": "stddev: 0.00008796933714318488",
            "extra": "mean: 38.678535740740685 msec\nrounds: 27"
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
          "id": "52593dcde93f52558e54d89fce0ba88c8d7a94f3",
          "message": "Do not run benchmarks in nightly workflows (#201)\n\nRun only `tests/unittests` in the nightly check, skipping `tests/benchmarks`.",
          "timestamp": "2023-05-24T11:09:52+02:00",
          "tree_id": "5887d0101ec1a44063dd6c1c099e1594fb6e8ed4",
          "url": "https://github.com/ansys-internal/pyacp/commit/52593dcde93f52558e54d89fce0ba88c8d7a94f3"
        },
        "date": 1684919679280,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.278286637328301,
            "unit": "iter/sec",
            "range": "stddev: 0.006094807121791806",
            "extra": "mean: 159.27912466665362 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4478853191577867,
            "unit": "iter/sec",
            "range": "stddev: 0.006160878059687353",
            "extra": "mean: 408.5158696666629 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38212211351427067,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6169644850000395 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04120332770639925,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.269884391999994 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.6132534936676484,
            "unit": "iter/sec",
            "range": "stddev: 0.004964309095608764",
            "extra": "mean: 276.75888275000204 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7417117056450939,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3482327330000317 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08361352168009206,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.959788081 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1133.5632851910775,
            "unit": "iter/sec",
            "range": "stddev: 0.0002535241967150585",
            "extra": "mean: 882.1739492307538 usec\nrounds: 1300"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 372.1296108337985,
            "unit": "iter/sec",
            "range": "stddev: 0.0001322512110982341",
            "extra": "mean: 2.6872357664830457 msec\nrounds: 364"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.65526543167063,
            "unit": "iter/sec",
            "range": "stddev: 0.00012875635555696603",
            "extra": "mean: 20.98404008333195 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964391876600329,
            "unit": "iter/sec",
            "range": "stddev: 0.00006124993886598722",
            "extra": "mean: 201.43454120000115 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 886.3935042574926,
            "unit": "iter/sec",
            "range": "stddev: 0.000192313283748679",
            "extra": "mean: 1.1281671122327013 msec\nrounds: 891"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 217.78742161791507,
            "unit": "iter/sec",
            "range": "stddev: 0.0001650845998921814",
            "extra": "mean: 4.591633403670088 msec\nrounds: 218"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.785290808424858,
            "unit": "iter/sec",
            "range": "stddev: 0.00011328389663232312",
            "extra": "mean: 38.78180034615971 msec\nrounds: 26"
          }
        ]
      }
    ]
  }
}