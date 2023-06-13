window.BENCHMARK_DATA = {
  "lastUpdate": 1686642955456,
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
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "55eaaec6cf3a1f6b2e5f1dcfa9857e49c7f6250c",
          "message": "Bump pytest-cov from 4.0.0 to 4.1.0 (#202)\n\nBumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 4.0.0 to 4.1.0.\r\n- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v4.0.0...v4.1.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pytest-cov\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-05-25T10:01:43+02:00",
          "tree_id": "034a148ca98b55737d31412d7d89b4c5d339d400",
          "url": "https://github.com/ansys-internal/pyacp/commit/55eaaec6cf3a1f6b2e5f1dcfa9857e49c7f6250c"
        },
        "date": 1685002013663,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.934281396555317,
            "unit": "iter/sec",
            "range": "stddev: 0.007800704383050835",
            "extra": "mean: 202.66375580000613 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.155598398440951,
            "unit": "iter/sec",
            "range": "stddev: 0.00573981434682128",
            "extra": "mean: 463.90830533333843 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37538090125278506,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.663960784000011 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04110992915104207,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.32502367799998 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.9041719079025015,
            "unit": "iter/sec",
            "range": "stddev: 0.013199713223062052",
            "extra": "mean: 344.33223366664834 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6990389141157279,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4305355250000389 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08338529358656001,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.992522385999962 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 953.8707666969126,
            "unit": "iter/sec",
            "range": "stddev: 0.00036657974479872824",
            "extra": "mean: 1.048360045106346 msec\nrounds: 1042"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 335.7793569121694,
            "unit": "iter/sec",
            "range": "stddev: 0.0002115241895988588",
            "extra": "mean: 2.978146152866605 msec\nrounds: 314"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.62605039662933,
            "unit": "iter/sec",
            "range": "stddev: 0.00018671828251971256",
            "extra": "mean: 20.996912229168885 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.959524398908989,
            "unit": "iter/sec",
            "range": "stddev: 0.00018900165112823176",
            "extra": "mean: 201.63223719999905 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 740.2517195693674,
            "unit": "iter/sec",
            "range": "stddev: 0.00044123185188662476",
            "extra": "mean: 1.3508918298517942 msec\nrounds: 670"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 212.26566166069225,
            "unit": "iter/sec",
            "range": "stddev: 0.00018701280620507543",
            "extra": "mean: 4.711077581632139 msec\nrounds: 196"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.75566682906282,
            "unit": "iter/sec",
            "range": "stddev: 0.0002881713717566527",
            "extra": "mean: 38.826406888894645 msec\nrounds: 27"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "dc8947e7bf234273a0e86dcaaa0a18c8f0213e0a",
          "message": "Bump typing-extensions from 4.6.0 to 4.6.1 (#203)\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.6.0 to 4.6.1.\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.6.0...4.6.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-05-25T10:21:25+02:00",
          "tree_id": "536fd17cd4fc0268a5a4a5ba1071e5135bc7f1a6",
          "url": "https://github.com/ansys-internal/pyacp/commit/dc8947e7bf234273a0e86dcaaa0a18c8f0213e0a"
        },
        "date": 1685003171450,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.620890645321316,
            "unit": "iter/sec",
            "range": "stddev: 0.004354996580825218",
            "extra": "mean: 151.03708150000253 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.473751921282775,
            "unit": "iter/sec",
            "range": "stddev: 0.014331635561394414",
            "extra": "mean: 404.2442539999911 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38748352755214316,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5807548679999854 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04128011475120274,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.22473886099999 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.7652292580789957,
            "unit": "iter/sec",
            "range": "stddev: 0.002962109653192796",
            "extra": "mean: 265.5880775000128 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7582683276972849,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3187943680000558 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08401608616480634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.902482555999995 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1095.466919958496,
            "unit": "iter/sec",
            "range": "stddev: 0.00035656489893103114",
            "extra": "mean: 912.8527587468247 usec\nrounds: 1629"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 393.13696533659373,
            "unit": "iter/sec",
            "range": "stddev: 0.00006486145331653294",
            "extra": "mean: 2.5436427712764833 msec\nrounds: 376"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.505786522038974,
            "unit": "iter/sec",
            "range": "stddev: 0.00007980987167470244",
            "extra": "mean: 20.616097000007255 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.975657412118966,
            "unit": "iter/sec",
            "range": "stddev: 0.00006442349089695066",
            "extra": "mean: 200.97846720000234 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 942.6098772975795,
            "unit": "iter/sec",
            "range": "stddev: 0.0001863890846955503",
            "extra": "mean: 1.060884278941523 msec\nrounds: 907"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 233.1133579679074,
            "unit": "iter/sec",
            "range": "stddev: 0.00006508271699082409",
            "extra": "mean: 4.2897584622227845 msec\nrounds: 225"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.043068189654853,
            "unit": "iter/sec",
            "range": "stddev: 0.00008279990683286671",
            "extra": "mean: 38.39793348147943 msec\nrounds: 27"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "733f12732f4fe4f8fde6107f8699903be9d49a06",
          "message": "Bump hypothesis from 6.75.3 to 6.75.6 (#204)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.75.3 to 6.75.6.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.75.3...hypothesis-python-6.75.6)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-05-29T20:58:01+02:00",
          "tree_id": "3e3066eec8d9e6fef2f10a2e06c633bbd728db50",
          "url": "https://github.com/ansys-internal/pyacp/commit/733f12732f4fe4f8fde6107f8699903be9d49a06"
        },
        "date": 1685386953482,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.612851202755307,
            "unit": "iter/sec",
            "range": "stddev: 0.0037655941396378223",
            "extra": "mean: 151.22070183332426 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.558319074940053,
            "unit": "iter/sec",
            "range": "stddev: 0.004325912929175355",
            "extra": "mean: 390.88165733331454 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38671257270774706,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5858998919999863 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04125465618841243,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.23968813199997 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.474989360472947,
            "unit": "iter/sec",
            "range": "stddev: 0.018370187645366246",
            "extra": "mean: 287.77066525000805 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7376026229479525,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3557435520000354 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08390858200769824,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.917732085000011 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1098.562562273758,
            "unit": "iter/sec",
            "range": "stddev: 0.00031610493480547933",
            "extra": "mean: 910.2804285722632 usec\nrounds: 1589"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 351.69018402565604,
            "unit": "iter/sec",
            "range": "stddev: 0.00028618713850351365",
            "extra": "mean: 2.843411745398755 msec\nrounds: 326"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.010842690328225,
            "unit": "iter/sec",
            "range": "stddev: 0.00018358810525452568",
            "extra": "mean: 20.8286283673469 msec\nrounds: 49"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9745768727135795,
            "unit": "iter/sec",
            "range": "stddev: 0.000221985463977675",
            "extra": "mean: 201.02212220001547 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 934.5929928080294,
            "unit": "iter/sec",
            "range": "stddev: 0.00017548022813010567",
            "extra": "mean: 1.069984482759123 msec\nrounds: 986"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 225.69587696520875,
            "unit": "iter/sec",
            "range": "stddev: 0.00020436297254250297",
            "extra": "mean: 4.430741108106955 msec\nrounds: 222"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.101035420241754,
            "unit": "iter/sec",
            "range": "stddev: 0.00008415269203728181",
            "extra": "mean: 38.31265633333781 msec\nrounds: 27"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "dbfd5c7a982a476d2d03d5bc02362b91685654a5",
          "message": "Bump typing-extensions from 4.6.1 to 4.6.2 (#205)\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.6.1 to 4.6.2.\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.6.1...4.6.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-05-29T19:08:11Z",
          "tree_id": "8a73ec8f15efcd2cbe2615ed30ae609acd7c35cf",
          "url": "https://github.com/ansys-internal/pyacp/commit/dbfd5c7a982a476d2d03d5bc02362b91685654a5"
        },
        "date": 1685387577612,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.23858040853289,
            "unit": "iter/sec",
            "range": "stddev: 0.003852860161660852",
            "extra": "mean: 160.29287666665937 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2622391839653866,
            "unit": "iter/sec",
            "range": "stddev: 0.007579536818036179",
            "extra": "mean: 442.03990766667783 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37884524227164484,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.639600260000009 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041180193191463696,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.283518907999962 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.2915967587059076,
            "unit": "iter/sec",
            "range": "stddev: 0.005868192071080762",
            "extra": "mean: 303.80392050001603 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7216514737646617,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3857104659999777 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08368157622113556,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.950061711999979 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1093.5137732982441,
            "unit": "iter/sec",
            "range": "stddev: 0.00028877825675463953",
            "extra": "mean: 914.4832231822842 usec\nrounds: 1389"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 332.6863595604258,
            "unit": "iter/sec",
            "range": "stddev: 0.0003357375945817423",
            "extra": "mean: 3.005834087460896 msec\nrounds: 343"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.323790415170926,
            "unit": "iter/sec",
            "range": "stddev: 0.0001755937470150359",
            "extra": "mean: 21.13102080849853 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.958346197969616,
            "unit": "iter/sec",
            "range": "stddev: 0.00011349723744398612",
            "extra": "mean: 201.6801489999807 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 832.3910474955698,
            "unit": "iter/sec",
            "range": "stddev: 0.00024063480344986896",
            "extra": "mean: 1.2013584276389306 msec\nrounds: 919"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.28530606545445,
            "unit": "iter/sec",
            "range": "stddev: 0.0002741862695672209",
            "extra": "mean: 4.824268632356556 msec\nrounds: 204"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.729644474192046,
            "unit": "iter/sec",
            "range": "stddev: 0.00023832514858001302",
            "extra": "mean: 38.865675000019664 msec\nrounds: 26"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a292634a6c6aa0858a08febe6fe4d7907b7504c5",
          "message": "Bump hypothesis from 6.75.6 to 6.75.9 (#208)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.75.6 to 6.75.9.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.75.6...hypothesis-python-6.75.9)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-02T09:23:00+02:00",
          "tree_id": "445f2520c0ff420a039beee9b1c77773c6fc23da",
          "url": "https://github.com/ansys-internal/pyacp/commit/a292634a6c6aa0858a08febe6fe4d7907b7504c5"
        },
        "date": 1685690865528,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.079259648630976,
            "unit": "iter/sec",
            "range": "stddev: 0.005934966890695984",
            "extra": "mean: 164.4937143333228 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.313922467398224,
            "unit": "iter/sec",
            "range": "stddev: 0.0027187254714135236",
            "extra": "mean: 432.1665976666888 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37903699295489734,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6382649149999793 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041190180707173826,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.277630805 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.2334898441037927,
            "unit": "iter/sec",
            "range": "stddev: 0.025386697547419176",
            "extra": "mean: 309.26338050001334 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7049446249853852,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.418551137999998 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0835505117834586,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.968807595000044 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1110.537004544962,
            "unit": "iter/sec",
            "range": "stddev: 0.0003535328515673819",
            "extra": "mean: 900.4652667199919 usec\nrounds: 1256"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 365.8997826044873,
            "unit": "iter/sec",
            "range": "stddev: 0.00009107646287662496",
            "extra": "mean: 2.7329887787359843 msec\nrounds: 348"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.27924805167681,
            "unit": "iter/sec",
            "range": "stddev: 0.00014512742248039243",
            "extra": "mean: 21.150928604172964 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.963696112350384,
            "unit": "iter/sec",
            "range": "stddev: 0.00016312654400806002",
            "extra": "mean: 201.46277640000108 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 891.7416630311535,
            "unit": "iter/sec",
            "range": "stddev: 0.00017849679366285377",
            "extra": "mean: 1.1214010082257024 msec\nrounds: 851"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 203.19350615079244,
            "unit": "iter/sec",
            "range": "stddev: 0.000175633090438056",
            "extra": "mean: 4.921417120771012 msec\nrounds: 207"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.64587293863495,
            "unit": "iter/sec",
            "range": "stddev: 0.00008267871320371062",
            "extra": "mean: 38.99262865384948 msec\nrounds: 26"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8ef58ea00ad8a62fc25b1f075f6c3c1bddbfde5d",
          "message": "Bump typing-extensions from 4.6.2 to 4.6.3 (#207)\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.6.2 to 4.6.3.\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.6.2...4.6.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-02T08:55:43+02:00",
          "tree_id": "2150da1270956a241bd5ba22d5c3cddf1937b99e",
          "url": "https://github.com/ansys-internal/pyacp/commit/8ef58ea00ad8a62fc25b1f075f6c3c1bddbfde5d"
        },
        "date": 1685709650947,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.269195086641354,
            "unit": "iter/sec",
            "range": "stddev: 0.004140348945084006",
            "extra": "mean: 234.23619200000445 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.0186343508042017,
            "unit": "iter/sec",
            "range": "stddev: 0.0018348876499595882",
            "extra": "mean: 495.3844165000021 msec\nrounds: 2"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37034527906621834,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.700182928000004 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04105597489287347,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.356990733000004 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.720432311515943,
            "unit": "iter/sec",
            "range": "stddev: 0.008783848976256494",
            "extra": "mean: 367.58863499998523 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6940447787585836,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4408292240000264 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08304646060871722,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.041452371000048 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 770.3995901443894,
            "unit": "iter/sec",
            "range": "stddev: 0.0007412499849088912",
            "extra": "mean: 1.2980276895170448 msec\nrounds: 992"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 318.6525123548902,
            "unit": "iter/sec",
            "range": "stddev: 0.00047429860725246685",
            "extra": "mean: 3.138214704820147 msec\nrounds: 332"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.939061269827086,
            "unit": "iter/sec",
            "range": "stddev: 0.00016780118985891326",
            "extra": "mean: 21.304218127660135 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.958958631858331,
            "unit": "iter/sec",
            "range": "stddev: 0.00003742491150360995",
            "extra": "mean: 201.65524139999889 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 653.4457292777948,
            "unit": "iter/sec",
            "range": "stddev: 0.0004321214890856591",
            "extra": "mean: 1.5303489719111425 msec\nrounds: 712"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.94634280825866,
            "unit": "iter/sec",
            "range": "stddev: 0.0003414377198023787",
            "extra": "mean: 4.8321704381436055 msec\nrounds: 194"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.57097249375502,
            "unit": "iter/sec",
            "range": "stddev: 0.0001376023119934565",
            "extra": "mean: 39.106842739134045 msec\nrounds: 23"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "1f564b88d53c916aeaf51b9dfde874896476c8d2",
          "message": "Bump ansys-mapdl-core from 0.64.1 to 0.65.0 (#210)\n\nBumps [ansys-mapdl-core](https://github.com/ansys/pymapdl) from 0.64.1 to 0.65.0.\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.64.1...v0.65.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-05T08:23:49+02:00",
          "tree_id": "289d0be975ae4be9f8cc11fbd728fe2b59f8b771",
          "url": "https://github.com/ansys-internal/pyacp/commit/1f564b88d53c916aeaf51b9dfde874896476c8d2"
        },
        "date": 1685946543317,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.809404836970238,
            "unit": "iter/sec",
            "range": "stddev: 0.0037151846020935186",
            "extra": "mean: 172.1346726666629 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.342181236285157,
            "unit": "iter/sec",
            "range": "stddev: 0.009177885214786238",
            "extra": "mean: 426.95244266667487 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37463959025164634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6692320459999905 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04118242162960568,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.282204893 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.50611938750406,
            "unit": "iter/sec",
            "range": "stddev: 0.005415594272189596",
            "extra": "mean: 285.21561575000476 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.707615653321538,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4131965500000092 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08356096748879581,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.967309978000003 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1107.759773772286,
            "unit": "iter/sec",
            "range": "stddev: 0.000549422517761854",
            "extra": "mean: 902.7227957508073 usec\nrounds: 1082"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 361.7547809757432,
            "unit": "iter/sec",
            "range": "stddev: 0.00043558151903971414",
            "extra": "mean: 2.76430348011642 msec\nrounds: 352"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.01751755158976,
            "unit": "iter/sec",
            "range": "stddev: 0.00010515204419354605",
            "extra": "mean: 21.268668617026716 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.963662353209856,
            "unit": "iter/sec",
            "range": "stddev: 0.00010243590864191176",
            "extra": "mean: 201.46414660000573 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 892.0567296221983,
            "unit": "iter/sec",
            "range": "stddev: 0.00015950465420796862",
            "extra": "mean: 1.121004939252594 msec\nrounds: 856"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 212.12473358586925,
            "unit": "iter/sec",
            "range": "stddev: 0.00032743923980632877",
            "extra": "mean: 4.7142074528296085 msec\nrounds: 212"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.570202056928526,
            "unit": "iter/sec",
            "range": "stddev: 0.0006779413326406506",
            "extra": "mean: 39.10802103845867 msec\nrounds: 26"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "399fd0ca72c6a7ce97c26e7f3aef0f41a7ba9d05",
          "message": "Bump hypothesis from 6.75.9 to 6.76.0 (#211)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.75.9 to 6.76.0.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.75.9...hypothesis-python-6.76.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-05T10:03:04+02:00",
          "tree_id": "4ec55504710a660203dccc21fa65a943919f7096",
          "url": "https://github.com/ansys-internal/pyacp/commit/399fd0ca72c6a7ce97c26e7f3aef0f41a7ba9d05"
        },
        "date": 1685952503402,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.639255573767812,
            "unit": "iter/sec",
            "range": "stddev: 0.0050130997887377045",
            "extra": "mean: 215.551823800007 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.0893165061100807,
            "unit": "iter/sec",
            "range": "stddev: 0.01331943368442892",
            "extra": "mean: 478.62542466666014 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3758343123820323,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6607469489999858 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04109698944579173,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.3326826 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.873982442686087,
            "unit": "iter/sec",
            "range": "stddev: 0.009713542140609403",
            "extra": "mean: 347.9492376666637 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7102849056884454,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4078857540000058 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08338272858773851,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.992891296999971 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 932.990062672699,
            "unit": "iter/sec",
            "range": "stddev: 0.00037813352566855074",
            "extra": "mean: 1.0718227771208413 msec\nrounds: 1014"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 330.5750658165966,
            "unit": "iter/sec",
            "range": "stddev: 0.00024846471254764784",
            "extra": "mean: 3.0250315386908255 msec\nrounds: 336"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.57491669209628,
            "unit": "iter/sec",
            "range": "stddev: 0.00012754109960089684",
            "extra": "mean: 21.01947979167207 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962592134331494,
            "unit": "iter/sec",
            "range": "stddev: 0.00015302392299833105",
            "extra": "mean: 201.5075938000109 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 705.8781422467836,
            "unit": "iter/sec",
            "range": "stddev: 0.00026099165380609354",
            "extra": "mean: 1.4166751173467955 msec\nrounds: 784"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 208.85520109549424,
            "unit": "iter/sec",
            "range": "stddev: 0.00017784161299878694",
            "extra": "mean: 4.788006210785111 msec\nrounds: 204"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.78243645690553,
            "unit": "iter/sec",
            "range": "stddev: 0.00020891044394420706",
            "extra": "mean: 38.78609384615244 msec\nrounds: 26"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b25fe4311d8d0b0306eb8220062a2d916689a3b0",
          "message": "Bump docker from 6.1.2 to 6.1.3 (#209)\n\nBumps [docker](https://github.com/docker/docker-py) from 6.1.2 to 6.1.3.\r\n- [Release notes](https://github.com/docker/docker-py/releases)\r\n- [Commits](https://github.com/docker/docker-py/compare/6.1.2...6.1.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: docker\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-12T11:39:01+02:00",
          "tree_id": "3d7d8d7f3649c3de71a0a5e2178cce927c39db60",
          "url": "https://github.com/ansys-internal/pyacp/commit/b25fe4311d8d0b0306eb8220062a2d916689a3b0"
        },
        "date": 1686563051040,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.728108518450526,
            "unit": "iter/sec",
            "range": "stddev: 0.004516949042939502",
            "extra": "mean: 174.57769816667223 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1889570042124777,
            "unit": "iter/sec",
            "range": "stddev: 0.01469966336611098",
            "extra": "mean: 456.83857566666575 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3784526743662869,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6423383100000137 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04116708053505315,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.291253763999975 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3729520164759568,
            "unit": "iter/sec",
            "range": "stddev: 0.008507936785455231",
            "extra": "mean: 296.47620099997596 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7311241441024855,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3677567729999964 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08362682439140673,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.957885610000005 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 929.6435458272088,
            "unit": "iter/sec",
            "range": "stddev: 0.0004707540296532291",
            "extra": "mean: 1.0756811086233995 msec\nrounds: 1206"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 354.9763345014107,
            "unit": "iter/sec",
            "range": "stddev: 0.00011419935940511993",
            "extra": "mean: 2.8170892051284784 msec\nrounds: 351"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.536700330680155,
            "unit": "iter/sec",
            "range": "stddev: 0.00012165505430237672",
            "extra": "mean: 21.036378062500916 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964219691581934,
            "unit": "iter/sec",
            "range": "stddev: 0.0000834869988060141",
            "extra": "mean: 201.44152800000938 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 778.5626566507174,
            "unit": "iter/sec",
            "range": "stddev: 0.0003606306412965415",
            "extra": "mean: 1.2844181408621362 msec\nrounds: 859"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 212.69324588149766,
            "unit": "iter/sec",
            "range": "stddev: 0.00012454527332847318",
            "extra": "mean: 4.701606747574633 msec\nrounds: 206"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.777302335734298,
            "unit": "iter/sec",
            "range": "stddev: 0.0001605002498469081",
            "extra": "mean: 38.79381895652169 msec\nrounds: 23"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4ef854db055548c37d5a587a2cbffedb707d556f",
          "message": "Bump pytest from 7.3.1 to 7.3.2 (#212)\n\nBumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.1 to 7.3.2.\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.1...7.3.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-13T07:50:42Z",
          "tree_id": "90c36917df00803b4b4b07939a6d8a86e3c31384",
          "url": "https://github.com/ansys-internal/pyacp/commit/4ef854db055548c37d5a587a2cbffedb707d556f"
        },
        "date": 1686642951586,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.89754057212727,
            "unit": "iter/sec",
            "range": "stddev: 0.004021388236082888",
            "extra": "mean: 169.56220780000422 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3036876285088526,
            "unit": "iter/sec",
            "range": "stddev: 0.007118140554409029",
            "extra": "mean: 434.0866303333352 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37568961647049565,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.661771728999952 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04111850974316057,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.319947543000012 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.39981711397805,
            "unit": "iter/sec",
            "range": "stddev: 0.006183392692237532",
            "extra": "mean: 294.133468499993 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7210969529909634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.386776072000032 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08332101577232541,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.00177399100005 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 985.9364558958481,
            "unit": "iter/sec",
            "range": "stddev: 0.00027352024949390353",
            "extra": "mean: 1.0142641485869122 msec\nrounds: 1097"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 357.0109343600782,
            "unit": "iter/sec",
            "range": "stddev: 0.00009719563590612674",
            "extra": "mean: 2.80103465680244 msec\nrounds: 338"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.11131735309955,
            "unit": "iter/sec",
            "range": "stddev: 0.00014067676068681977",
            "extra": "mean: 21.226322170212203 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.961703788905173,
            "unit": "iter/sec",
            "range": "stddev: 0.00002624465550668749",
            "extra": "mean: 201.543671800016 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 767.3246806869956,
            "unit": "iter/sec",
            "range": "stddev: 0.0005348148073705505",
            "extra": "mean: 1.303229291549292 msec\nrounds: 710"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.37122080495374,
            "unit": "iter/sec",
            "range": "stddev: 0.0004844958178485211",
            "extra": "mean: 4.7535019104497795 msec\nrounds: 201"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.582328728569017,
            "unit": "iter/sec",
            "range": "stddev: 0.00014300243491633207",
            "extra": "mean: 39.08948284615121 msec\nrounds: 26"
          }
        ]
      }
    ]
  }
}