window.BENCHMARK_DATA = {
  "lastUpdate": 1694071131193,
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
          "id": "547644ec4e9bda2d04380d4b271c91574ce5aeca",
          "message": "Bump hypothesis from 6.76.0 to 6.79.1 (#214)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.76.0 to 6.79.1.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.76.0...hypothesis-python-6.79.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-19T09:41:30+02:00",
          "tree_id": "b34e18a8289fefdcb02d91d9af9569105b1abf0b",
          "url": "https://github.com/ansys-internal/pyacp/commit/547644ec4e9bda2d04380d4b271c91574ce5aeca"
        },
        "date": 1687160770842,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.829838400949816,
            "unit": "iter/sec",
            "range": "stddev: 0.00431180682630975",
            "extra": "mean: 146.41634857142907 msec\nrounds: 7"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4649420352981903,
            "unit": "iter/sec",
            "range": "stddev: 0.005180493711978858",
            "extra": "mean: 405.68905299999375 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37892118110643,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6390712630000053 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041198112188974,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.27295686299999 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.780036318607714,
            "unit": "iter/sec",
            "range": "stddev: 0.004994277719805651",
            "extra": "mean: 264.5477227500095 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7317856220613739,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3665204260000223 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08363821086563103,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.956257667999978 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1098.3442146186624,
            "unit": "iter/sec",
            "range": "stddev: 0.0002967130829597056",
            "extra": "mean: 910.4613896902924 usec\nrounds: 1319"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 368.9066184665805,
            "unit": "iter/sec",
            "range": "stddev: 0.00010115835974459695",
            "extra": "mean: 2.7107130909081008 msec\nrounds: 363"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.70943190720435,
            "unit": "iter/sec",
            "range": "stddev: 0.00009541559412279936",
            "extra": "mean: 20.960216041662722 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.966877414387734,
            "unit": "iter/sec",
            "range": "stddev: 0.00006483605811643106",
            "extra": "mean: 201.33373880000818 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 880.8767413038349,
            "unit": "iter/sec",
            "range": "stddev: 0.0001593016746363722",
            "extra": "mean: 1.1352326075948425 msec\nrounds: 869"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 216.7425048691015,
            "unit": "iter/sec",
            "range": "stddev: 0.00010697998160870096",
            "extra": "mean: 4.613769692308094 msec\nrounds: 221"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.773175054385913,
            "unit": "iter/sec",
            "range": "stddev: 0.00011359565295420629",
            "extra": "mean: 38.80003134615059 msec\nrounds: 26"
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
          "id": "32ec0aa95d055755291d667bd4344ff82928e266",
          "message": "Bump mypy from 1.3.0 to 1.4.0 (#216)\n\nBumps [mypy](https://github.com/python/mypy) from 1.3.0 to 1.4.0.\r\n- [Commits](https://github.com/python/mypy/compare/v1.3.0...v1.4.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-21T09:52:40+02:00",
          "tree_id": "7e72cff7077a7ab7f57efcb0b19d118209be275b",
          "url": "https://github.com/ansys-internal/pyacp/commit/32ec0aa95d055755291d667bd4344ff82928e266"
        },
        "date": 1687334283720,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.809706770127866,
            "unit": "iter/sec",
            "range": "stddev: 0.010360734910315654",
            "extra": "mean: 207.912882800008 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.161828754414721,
            "unit": "iter/sec",
            "range": "stddev: 0.0069910332237487155",
            "extra": "mean: 462.5713289999851 msec\nrounds: 2"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3749282852173185,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6671767359999876 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04114443493121514,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.304623497000023 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0514344698340343,
            "unit": "iter/sec",
            "range": "stddev: 0.001987073819196288",
            "extra": "mean: 327.7147223333259 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7132010399369865,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4021291949999863 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08328172627787353,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.00743602099999 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 917.5846973390065,
            "unit": "iter/sec",
            "range": "stddev: 0.0004616774100474397",
            "extra": "mean: 1.0898176516020783 msec\nrounds: 686"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 323.9823825963944,
            "unit": "iter/sec",
            "range": "stddev: 0.0005223286626423068",
            "extra": "mean: 3.086587585368072 msec\nrounds: 328"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.97094457610898,
            "unit": "iter/sec",
            "range": "stddev: 0.00024385662981747286",
            "extra": "mean: 21.289757083331768 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9614184128450685,
            "unit": "iter/sec",
            "range": "stddev: 0.00011686121288609812",
            "extra": "mean: 201.55526439999676 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 674.202591407195,
            "unit": "iter/sec",
            "range": "stddev: 0.0004203521435499753",
            "extra": "mean: 1.483233693766737 msec\nrounds: 738"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.8179116236423,
            "unit": "iter/sec",
            "range": "stddev: 0.0001228572278863605",
            "extra": "mean: 4.766037333331841 msec\nrounds: 198"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.689313113251046,
            "unit": "iter/sec",
            "range": "stddev: 0.00022588720030126838",
            "extra": "mean: 38.92669280768665 msec\nrounds: 26"
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
          "id": "5f55eb71121d4cb2b67b1508385a6e9bac152462",
          "message": "Bump ansys-tools-path from 0.2.4 to 0.2.6 (#217)\n\nBumps [ansys-tools-path](https://github.com/ansys/ansys-tools-path) from 0.2.4 to 0.2.6.\r\n- [Release notes](https://github.com/ansys/ansys-tools-path/releases)\r\n- [Changelog](https://github.com/ansys/ansys-tools-path/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/ansys-tools-path/compare/v0.2.4...v0.2.6)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-tools-path\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-26T14:16:42+02:00",
          "tree_id": "4dedd8baec28ce99d33868c65f07d7ad80006466",
          "url": "https://github.com/ansys-internal/pyacp/commit/5f55eb71121d4cb2b67b1508385a6e9bac152462"
        },
        "date": 1687782080045,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.511809573378178,
            "unit": "iter/sec",
            "range": "stddev: 0.0024734030501607097",
            "extra": "mean: 133.1237154285694 msec\nrounds: 7"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.445515237021532,
            "unit": "iter/sec",
            "range": "stddev: 0.010586218376930611",
            "extra": "mean: 408.9117846666663 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3859296062893023,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5911461149999866 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04131347189620651,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.20517942699999 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.798071416055979,
            "unit": "iter/sec",
            "range": "stddev: 0.017551056342217295",
            "extra": "mean: 263.2915209999993 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7522419207007937,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3293595750000122 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08400999509420673,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.903345535000028 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1000.0883582489759,
            "unit": "iter/sec",
            "range": "stddev: 0.0004544039227885274",
            "extra": "mean: 999.9116495575146 usec\nrounds: 1695"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 350.3314084296906,
            "unit": "iter/sec",
            "range": "stddev: 0.00034164075414797095",
            "extra": "mean: 2.8544400414520466 msec\nrounds: 386"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.90516195924557,
            "unit": "iter/sec",
            "range": "stddev: 0.00023447957813052642",
            "extra": "mean: 20.874577166668 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.978022483734124,
            "unit": "iter/sec",
            "range": "stddev: 0.00004488617315614246",
            "extra": "mean: 200.88298180000947 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 888.8857777884194,
            "unit": "iter/sec",
            "range": "stddev: 0.00024798036280424744",
            "extra": "mean: 1.125003937500313 msec\nrounds: 1024"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 220.94647772747632,
            "unit": "iter/sec",
            "range": "stddev: 0.0002433933780704261",
            "extra": "mean: 4.525982990475357 msec\nrounds: 210"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.011601816027337,
            "unit": "iter/sec",
            "range": "stddev: 0.0001979595054591087",
            "extra": "mean: 38.44438366666981 msec\nrounds: 27"
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
          "id": "bf0fcb69d46f0d55e0975be115ff118259bc010b",
          "message": "Bump ipykernel from 6.23.1 to 6.23.2 (#215)\n\nBumps [ipykernel](https://github.com/ipython/ipykernel) from 6.23.1 to 6.23.2.\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.23.1...v6.23.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>",
          "timestamp": "2023-06-26T14:07:05Z",
          "tree_id": "c128bbf1c4191ccb9c4fc6bf212a2d02f2692ef2",
          "url": "https://github.com/ansys-internal/pyacp/commit/bf0fcb69d46f0d55e0975be115ff118259bc010b"
        },
        "date": 1687788722354,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.177417277433407,
            "unit": "iter/sec",
            "range": "stddev: 0.008066132760084955",
            "extra": "mean: 161.8799499999909 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2751302704897554,
            "unit": "iter/sec",
            "range": "stddev: 0.004462993313518867",
            "extra": "mean: 439.5352709999922 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37650220563255776,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6560269370000356 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04121576242020095,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.262562215999992 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.2247060492799218,
            "unit": "iter/sec",
            "range": "stddev: 0.006992769798605348",
            "extra": "mean: 310.10578474999306 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7271377525257509,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.375255233999951 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08351632910084826,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.973706348999997 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1086.5486054500684,
            "unit": "iter/sec",
            "range": "stddev: 0.0005889395031364666",
            "extra": "mean: 920.34538996604 usec\nrounds: 1136"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 358.66298340907315,
            "unit": "iter/sec",
            "range": "stddev: 0.0003262720784124462",
            "extra": "mean: 2.7881327214061837 msec\nrounds: 341"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.78401481193066,
            "unit": "iter/sec",
            "range": "stddev: 0.0002843165634709853",
            "extra": "mean: 21.374822234046153 msec\nrounds: 47"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96766115676287,
            "unit": "iter/sec",
            "range": "stddev: 0.000055517727901498974",
            "extra": "mean: 201.3019745999827 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 814.7868714220327,
            "unit": "iter/sec",
            "range": "stddev: 0.0003896766257632112",
            "extra": "mean: 1.2273148170081805 msec\nrounds: 776"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 200.5365998850978,
            "unit": "iter/sec",
            "range": "stddev: 0.0003952292484901917",
            "extra": "mean: 4.9866208989928715 msec\nrounds: 198"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.54744324008223,
            "unit": "iter/sec",
            "range": "stddev: 0.0008137669701527988",
            "extra": "mean: 39.14286023076731 msec\nrounds: 26"
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
          "id": "21dfe43b1786e5d62c1b9814f01fa9d37c3cfaec",
          "message": "Bump hypothesis from 6.79.1 to 6.79.3 (#218)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.79.1 to 6.79.3.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.79.1...hypothesis-python-6.79.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-27T09:18:55+02:00",
          "tree_id": "b3e16cbee31a1c5cb6a5c94988a8d3a44959ecc1",
          "url": "https://github.com/ansys-internal/pyacp/commit/21dfe43b1786e5d62c1b9814f01fa9d37c3cfaec"
        },
        "date": 1687850618776,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.430788063587265,
            "unit": "iter/sec",
            "range": "stddev: 0.0024217829343459282",
            "extra": "mean: 134.575228285712 msec\nrounds: 7"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.6516723364238572,
            "unit": "iter/sec",
            "range": "stddev: 0.008002846041476806",
            "extra": "mean: 377.1205009999979 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3867898352482233,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5853833500000007 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04130008732559852,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.21302386399998 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 4.003408782475961,
            "unit": "iter/sec",
            "range": "stddev: 0.004022274501982771",
            "extra": "mean: 249.7871325000034 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.761056252316085,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3139633199999992 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08400798762059634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.903629980000005 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1122.8892956027714,
            "unit": "iter/sec",
            "range": "stddev: 0.0003480948315478396",
            "extra": "mean: 890.5597407651802 usec\nrounds: 1462"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 391.28015857935424,
            "unit": "iter/sec",
            "range": "stddev: 0.0000731628223500643",
            "extra": "mean: 2.55571354200725 msec\nrounds: 369"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.99996668801525,
            "unit": "iter/sec",
            "range": "stddev: 0.0001265508969415561",
            "extra": "mean: 20.833347791670082 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.972146398840169,
            "unit": "iter/sec",
            "range": "stddev: 0.00009456732150545035",
            "extra": "mean: 201.12038540000867 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 933.9589833557886,
            "unit": "iter/sec",
            "range": "stddev: 0.0001644493567263847",
            "extra": "mean: 1.0707108318685696 msec\nrounds: 910"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 232.5284642083636,
            "unit": "iter/sec",
            "range": "stddev: 0.00007028860318247825",
            "extra": "mean: 4.3005487668121445 msec\nrounds: 223"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.901411721334412,
            "unit": "iter/sec",
            "range": "stddev: 0.00009530811529282776",
            "extra": "mean: 38.6079342222232 msec\nrounds: 27"
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
          "id": "e35d6d4ab28817d255647f482b41e1896fdb5736",
          "message": "Bump mypy from 1.4.0 to 1.4.1 (#219)\n\nBumps [mypy](https://github.com/python/mypy) from 1.4.0 to 1.4.1.\r\n- [Commits](https://github.com/python/mypy/compare/v1.4.0...v1.4.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-27T10:43:44+02:00",
          "tree_id": "e2f240b82ebc174233e1a6a83700c73a027fd33d",
          "url": "https://github.com/ansys-internal/pyacp/commit/e35d6d4ab28817d255647f482b41e1896fdb5736"
        },
        "date": 1687855730931,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.928348902137775,
            "unit": "iter/sec",
            "range": "stddev: 0.0020654541721252507",
            "extra": "mean: 168.68103016666205 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3470327396844217,
            "unit": "iter/sec",
            "range": "stddev: 0.0028538951863056584",
            "extra": "mean: 426.0698979999991 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37245013329412885,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6849231900000063 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04104718066799449,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.362209139000015 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3852299666056593,
            "unit": "iter/sec",
            "range": "stddev: 0.012149256654179558",
            "extra": "mean: 295.40090625000914 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7181193028804059,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3925262779999912 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08304874462202957,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.041121206000014 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 988.7509221845133,
            "unit": "iter/sec",
            "range": "stddev: 0.00028917098844261844",
            "extra": "mean: 1.0113770592401907 msec\nrounds: 1131"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 351.53714234034624,
            "unit": "iter/sec",
            "range": "stddev: 0.00014923200745857202",
            "extra": "mean: 2.8446496246243993 msec\nrounds: 333"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.70855761281481,
            "unit": "iter/sec",
            "range": "stddev: 0.00016807977191855754",
            "extra": "mean: 21.40935304167139 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.95531256021967,
            "unit": "iter/sec",
            "range": "stddev: 0.00006333662086188273",
            "extra": "mean: 201.80361740000308 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 810.4900884675957,
            "unit": "iter/sec",
            "range": "stddev: 0.00018227885214401208",
            "extra": "mean: 1.233821380704005 msec\nrounds: 767"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.3991282476907,
            "unit": "iter/sec",
            "range": "stddev: 0.00014493025048584",
            "extra": "mean: 4.775569069309286 msec\nrounds: 202"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.430017363433283,
            "unit": "iter/sec",
            "range": "stddev: 0.00010864899932039725",
            "extra": "mean: 39.32360665384111 msec\nrounds: 26"
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
          "id": "87ce92358f8a947a596f2fe10a11aaf83530a504",
          "message": "Bump ipykernel from 6.23.2 to 6.23.3 (#221)\n\nBumps [ipykernel](https://github.com/ipython/ipykernel) from 6.23.2 to 6.23.3.\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.23.2...v6.23.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-27T08:53:02Z",
          "tree_id": "8523140996347de0f12040a6e752dc89e299079d",
          "url": "https://github.com/ansys-internal/pyacp/commit/87ce92358f8a947a596f2fe10a11aaf83530a504"
        },
        "date": 1687856260527,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.904364687346504,
            "unit": "iter/sec",
            "range": "stddev: 0.0030119386015713934",
            "extra": "mean: 144.83591833332335 msec\nrounds: 6"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5296160767867177,
            "unit": "iter/sec",
            "range": "stddev: 0.007217267514509638",
            "extra": "mean: 395.3169056666752 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3837350537484642,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6059646889999613 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04120857600945622,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.266793391999954 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.853703662938201,
            "unit": "iter/sec",
            "range": "stddev: 0.005134063357479369",
            "extra": "mean: 259.49063225000657 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7436728322865768,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3446773320000034 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08370585408564167,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.946595742 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1137.3700893401644,
            "unit": "iter/sec",
            "range": "stddev: 0.00029411647460654463",
            "extra": "mean: 879.2212924995605 usec\nrounds: 1200"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 370.4033098218152,
            "unit": "iter/sec",
            "range": "stddev: 0.00016503872273275144",
            "extra": "mean: 2.69975989275327 msec\nrounds: 345"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.83188031575405,
            "unit": "iter/sec",
            "range": "stddev: 0.00007706804254136903",
            "extra": "mean: 20.906558416659966 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.967044400491782,
            "unit": "iter/sec",
            "range": "stddev: 0.00008474933435960464",
            "extra": "mean: 201.32697020002297 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 901.1179779344862,
            "unit": "iter/sec",
            "range": "stddev: 0.00015571047411623077",
            "extra": "mean: 1.1097326038175024 msec\nrounds: 838"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 216.89017225818816,
            "unit": "iter/sec",
            "range": "stddev: 0.00010313252438171503",
            "extra": "mean: 4.6106284558139885 msec\nrounds: 215"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.89751413577196,
            "unit": "iter/sec",
            "range": "stddev: 0.00009395539590389",
            "extra": "mean: 38.613744730762036 msec\nrounds: 26"
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
          "id": "64cb46d55f8a8c462e25b6f23e81618621a923be",
          "message": "Bump hypothesis from 6.79.3 to 6.80.0 (#222)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.79.3 to 6.80.0.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.79.3...hypothesis-python-6.80.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-28T22:18:14+02:00",
          "tree_id": "a61a4c2154541bd0174107a1fb7f94dd02eafc0c",
          "url": "https://github.com/ansys-internal/pyacp/commit/64cb46d55f8a8c462e25b6f23e81618621a923be"
        },
        "date": 1687983791611,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.467654115522168,
            "unit": "iter/sec",
            "range": "stddev: 0.008696522985425047",
            "extra": "mean: 182.89379300001656 msec\nrounds: 5"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.245664304348772,
            "unit": "iter/sec",
            "range": "stddev: 0.00832145279514359",
            "extra": "mean: 445.30253166667916 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37917899603352395,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.637276880999991 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04115900062862841,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.296022370000003 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.155138411247237,
            "unit": "iter/sec",
            "range": "stddev: 0.003955736539452075",
            "extra": "mean: 316.9433063333334 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7246922478599694,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3798960910000346 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08384691171026794,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.926497703999985 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 949.1980891932171,
            "unit": "iter/sec",
            "range": "stddev: 0.0003972481430009388",
            "extra": "mean: 1.0535208734458816 msec\nrounds: 885"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 328.5574026591406,
            "unit": "iter/sec",
            "range": "stddev: 0.00027581762169919514",
            "extra": "mean: 3.043608185073956 msec\nrounds: 335"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.758647472240305,
            "unit": "iter/sec",
            "range": "stddev: 0.00016347302845467305",
            "extra": "mean: 20.938616416665685 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.961142240371771,
            "unit": "iter/sec",
            "range": "stddev: 0.00017185536834309355",
            "extra": "mean: 201.56648439998435 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 681.306161512628,
            "unit": "iter/sec",
            "range": "stddev: 0.00025829997897898477",
            "extra": "mean: 1.4677689069768747 msec\nrounds: 946"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.06885283565052,
            "unit": "iter/sec",
            "range": "stddev: 0.00016183961303455145",
            "extra": "mean: 4.7603439848474824 msec\nrounds: 198"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.717336765424044,
            "unit": "iter/sec",
            "range": "stddev: 0.00019472287662385015",
            "extra": "mean: 38.88427519230767 msec\nrounds: 26"
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
          "id": "77c8fc8f82782d01a34180049a8736c8ddd0dd03",
          "message": "Bump typing-extensions from 4.6.3 to 4.7.0 (#223)\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.6.3 to 4.7.0.\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.6.3...4.7.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-06-30T09:26:12+02:00",
          "tree_id": "a0ee2ea18177234fc214aedb1b361a909f80ad1b",
          "url": "https://github.com/ansys-internal/pyacp/commit/77c8fc8f82782d01a34180049a8736c8ddd0dd03"
        },
        "date": 1688110248435,
        "tool": "pytest",
        "benches": [
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.501144093250057,
            "unit": "iter/sec",
            "range": "stddev: 0.002559407161869308",
            "extra": "mean: 133.31299699999835 msec\nrounds: 7"
          },
          {
            "name": "test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4347213567520765,
            "unit": "iter/sec",
            "range": "stddev: 0.006961890511326409",
            "extra": "mean: 410.72461833332835 msec\nrounds: 3"
          },
          {
            "name": "test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3870390929335087,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5837183330000073 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041300740474681734,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.212640948 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.9022691519518005,
            "unit": "iter/sec",
            "range": "stddev: 0.004879442001888922",
            "extra": "mean: 256.26115499999 msec\nrounds: 4"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7627694897024846,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.311012059999996 sec\nrounds: 1"
          },
          {
            "name": "test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08401800177805448,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.902211178999977 sec\nrounds: 1"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1105.402822183089,
            "unit": "iter/sec",
            "range": "stddev: 0.0003640551880730502",
            "extra": "mean: 904.6475908439187 usec\nrounds: 1398"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 383.020030473271,
            "unit": "iter/sec",
            "range": "stddev: 0.0001233024045423518",
            "extra": "mean: 2.6108295139665936 msec\nrounds: 358"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.80864551386232,
            "unit": "iter/sec",
            "range": "stddev: 0.00010979444625365318",
            "extra": "mean: 20.916718916666355 msec\nrounds: 48"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.975064954547367,
            "unit": "iter/sec",
            "range": "stddev: 0.00005358349540757953",
            "extra": "mean: 201.0024008000073 msec\nrounds: 5"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 912.4278163592262,
            "unit": "iter/sec",
            "range": "stddev: 0.00018347763210460082",
            "extra": "mean: 1.0959771086223618 msec\nrounds: 893"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 221.4309783566744,
            "unit": "iter/sec",
            "range": "stddev: 0.00024263708829592542",
            "extra": "mean: 4.516079942478645 msec\nrounds: 226"
          },
          {
            "name": "test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.00540090568251,
            "unit": "iter/sec",
            "range": "stddev: 0.00020058721258330562",
            "extra": "mean: 38.453550615383406 msec\nrounds: 26"
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
          "id": "39d731dc732ecfa630c9b6a15b442ffa2b5e409c",
          "message": "Bump pytest from 7.3.2 to 7.4.0 (#220)\n\n* Bump pytest from 7.3.2 to 7.4.0\r\n\r\nBumps [pytest](https://github.com/pytest-dev/pytest) from 7.3.2 to 7.4.0.\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/7.3.2...7.4.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\n* Add empty pytest.ini_options setion to pyproject.toml\r\n\r\n---------\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>\r\nCo-authored-by: Dominik Gresch <dominik.gresch@ansys.com>\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>",
          "timestamp": "2023-06-30T16:02:11+02:00",
          "tree_id": "dc7c7bcc0a8f600585e9acc7f6c647218aa110ed",
          "url": "https://github.com/ansys-internal/pyacp/commit/39d731dc732ecfa630c9b6a15b442ffa2b5e409c"
        },
        "date": 1688134053590,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.188125117627975,
            "unit": "iter/sec",
            "range": "stddev: 0.018059241751060197",
            "extra": "mean: 192.74785733332558 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.047233172794777,
            "unit": "iter/sec",
            "range": "stddev: 0.013024970606098345",
            "extra": "mean: 488.4641443333256 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37105439774612725,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6950226330000078 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04110506651512255,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.32790127300001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3338093346299886,
            "unit": "iter/sec",
            "range": "stddev: 0.002231683524613674",
            "extra": "mean: 299.9571660000129 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7120108670288342,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4044729459999985 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08366195909824847,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.952863772 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 966.6001627558339,
            "unit": "iter/sec",
            "range": "stddev: 0.0005371208927920705",
            "extra": "mean: 1.0345539329819076 msec\nrounds: 761"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 341.5671368881381,
            "unit": "iter/sec",
            "range": "stddev: 0.0005300662701170186",
            "extra": "mean: 2.927682121619025 msec\nrounds: 222"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.80183886136738,
            "unit": "iter/sec",
            "range": "stddev: 0.00012249521464883438",
            "extra": "mean: 21.36668182979133 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96481991660367,
            "unit": "iter/sec",
            "range": "stddev: 0.00009528505053385226",
            "extra": "mean: 201.41717459997608 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 695.634464315305,
            "unit": "iter/sec",
            "range": "stddev: 0.0006575494136106069",
            "extra": "mean: 1.4375365961551003 msec\nrounds: 728"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.42989172039336,
            "unit": "iter/sec",
            "range": "stddev: 0.00034894900105195283",
            "extra": "mean: 4.820905953843708 msec\nrounds: 195"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.55072886127254,
            "unit": "iter/sec",
            "range": "stddev: 0.00017521419183533815",
            "extra": "mean: 39.13782676922805 msec\nrounds: 26"
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
          "id": "c4f66414733be7ebb957c8e423716409750776f2",
          "message": "Bump typing-extensions from 4.7.0 to 4.7.1 (#225)\n\nBumps [typing-extensions](https://github.com/python/typing_extensions) from 4.7.0 to 4.7.1.\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.7.0...4.7.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-07-03T10:17:47+02:00",
          "tree_id": "5cf413657cbbfb6c0f7ac091df8f5daaf3318aa3",
          "url": "https://github.com/ansys-internal/pyacp/commit/c4f66414733be7ebb957c8e423716409750776f2"
        },
        "date": 1688372579038,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.970382870242649,
            "unit": "iter/sec",
            "range": "stddev: 0.0038563158848330743",
            "extra": "mean: 201.19174440000052 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1490738162720793,
            "unit": "iter/sec",
            "range": "stddev: 0.008428995849049126",
            "extra": "mean: 465.31672966667276 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3725510250792354,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6841960769999673 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041158557634140815,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.296283871000014 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.9257302412760495,
            "unit": "iter/sec",
            "range": "stddev: 0.014455586998762468",
            "extra": "mean: 341.7950110000068 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7013750582159761,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4257706889999895 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08347435014242599,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.979727883999999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 873.3006652036318,
            "unit": "iter/sec",
            "range": "stddev: 0.0006342760182710848",
            "extra": "mean: 1.1450810011312944 msec\nrounds: 883"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 324.01811316004796,
            "unit": "iter/sec",
            "range": "stddev: 0.0006102595574827579",
            "extra": "mean: 3.086247217006824 msec\nrounds: 341"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.877131428976845,
            "unit": "iter/sec",
            "range": "stddev: 0.00009674931571533253",
            "extra": "mean: 21.332363340429477 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96371395052842,
            "unit": "iter/sec",
            "range": "stddev: 0.00006145195812784955",
            "extra": "mean: 201.46205240000654 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 699.2976255923713,
            "unit": "iter/sec",
            "range": "stddev: 0.0005846792516295222",
            "extra": "mean: 1.430006285453787 msec\nrounds: 550"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.7029070550293,
            "unit": "iter/sec",
            "range": "stddev: 0.0001950590831056496",
            "extra": "mean: 4.814569108245834 msec\nrounds: 194"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.57773235675552,
            "unit": "iter/sec",
            "range": "stddev: 0.00009273717612878415",
            "extra": "mean: 39.09650730768878 msec\nrounds: 26"
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
          "id": "373893d9ea83f9a9014aabf0acbdb70aa30e207f",
          "message": "Bump ipykernel from 6.23.3 to 6.24.0 (#226)\n\nBumps [ipykernel](https://github.com/ipython/ipykernel) from 6.23.3 to 6.24.0.\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.23.3...v6.24.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-07-04T09:11:37+02:00",
          "tree_id": "abe1227c6ef96e02c1a9015baa26bd8bef7439bd",
          "url": "https://github.com/ansys-internal/pyacp/commit/373893d9ea83f9a9014aabf0acbdb70aa30e207f"
        },
        "date": 1688455012635,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.051276916231625,
            "unit": "iter/sec",
            "range": "stddev: 0.006229918853817669",
            "extra": "mean: 197.969744400001 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1299377347207717,
            "unit": "iter/sec",
            "range": "stddev: 0.00959543831767097",
            "extra": "mean: 469.49729266667833 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3774211135590048,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6495603030000154 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041138992573728266,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.30783880299998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.8458030556133735,
            "unit": "iter/sec",
            "range": "stddev: 0.021776088620163586",
            "extra": "mean: 351.394660999991 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7076939931145638,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4130401129999655 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08349171667457578,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.97723606400001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 896.8228875070777,
            "unit": "iter/sec",
            "range": "stddev: 0.0004379979603548981",
            "extra": "mean: 1.1150473676912134 msec\nrounds: 1009"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 324.9130834861055,
            "unit": "iter/sec",
            "range": "stddev: 0.00047505385645556713",
            "extra": "mean: 3.077746175286794 msec\nrounds: 348"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.88714919608023,
            "unit": "iter/sec",
            "range": "stddev: 0.00019300088762762668",
            "extra": "mean: 21.327805531917477 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962273546212942,
            "unit": "iter/sec",
            "range": "stddev: 0.00015255695659186923",
            "extra": "mean: 201.52053099998284 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 680.0536858107718,
            "unit": "iter/sec",
            "range": "stddev: 0.00047687113788089113",
            "extra": "mean: 1.4704721419277107 msec\nrounds: 768"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.3800978607822,
            "unit": "iter/sec",
            "range": "stddev: 0.00036998894328479573",
            "extra": "mean: 4.822063497488159 msec\nrounds: 199"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.530841814153977,
            "unit": "iter/sec",
            "range": "stddev: 0.00028539548177286013",
            "extra": "mean: 39.16831286955892 msec\nrounds: 23"
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
          "id": "c1d3a758e62b6877b1772850356fd5bc70431c1d",
          "message": "Bump hypothesis from 6.80.0 to 6.80.1 (#228)\n\nBumps [hypothesis](https://github.com/HypothesisWorks/hypothesis) from 6.80.0 to 6.80.1.\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.80.0...hypothesis-python-6.80.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-07-07T09:33:51+02:00",
          "tree_id": "ed9875e729ad76d7e3c743cc5ca9768b3b472863",
          "url": "https://github.com/ansys-internal/pyacp/commit/c1d3a758e62b6877b1772850356fd5bc70431c1d"
        },
        "date": 1688715525525,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.822723284190118,
            "unit": "iter/sec",
            "range": "stddev: 0.0037897147093426606",
            "extra": "mean: 146.56903971427937 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4118690584711846,
            "unit": "iter/sec",
            "range": "stddev: 0.005151104129644789",
            "extra": "mean: 414.6162066666553 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38227364931277025,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6159271030000184 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04121285183805455,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.264275714999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.763831522149841,
            "unit": "iter/sec",
            "range": "stddev: 0.004729637751392949",
            "extra": "mean: 265.68670625002255 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7335323460869677,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.363266398999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08386230750813782,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.924308187000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1053.4382957975486,
            "unit": "iter/sec",
            "range": "stddev: 0.00039923613223150415",
            "extra": "mean: 949.2724955882766 usec\nrounds: 1360"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 351.7909405258246,
            "unit": "iter/sec",
            "range": "stddev: 0.00024513409112370666",
            "extra": "mean: 2.8425973633809107 msec\nrounds: 355"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.520650972554286,
            "unit": "iter/sec",
            "range": "stddev: 0.0002065151702731441",
            "extra": "mean: 21.043482770839006 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964285717264264,
            "unit": "iter/sec",
            "range": "stddev: 0.00016794308363457107",
            "extra": "mean: 201.43884880000087 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 853.3985061932331,
            "unit": "iter/sec",
            "range": "stddev: 0.00019345361381466777",
            "extra": "mean: 1.1717855055321273 msec\nrounds: 904"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.08421524744006,
            "unit": "iter/sec",
            "range": "stddev: 0.00020043945341368757",
            "extra": "mean: 4.75999588461316 msec\nrounds: 208"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.761850779072702,
            "unit": "iter/sec",
            "range": "stddev: 0.0001754227460327811",
            "extra": "mean: 38.817086884624636 msec\nrounds: 26"
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
          "id": "8df67db66041466856a88a58392ddde7f9696049",
          "message": "Use grouped dependabot updates (#224)",
          "timestamp": "2023-07-10T10:08:44+02:00",
          "tree_id": "20c3733905e47a9602239d3187543b33f6676453",
          "url": "https://github.com/ansys-internal/pyacp/commit/8df67db66041466856a88a58392ddde7f9696049"
        },
        "date": 1688976853438,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.663147265696402,
            "unit": "iter/sec",
            "range": "stddev: 0.010495763523944233",
            "extra": "mean: 214.44744140000012 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.016730981730197,
            "unit": "iter/sec",
            "range": "stddev: 0.0043934594924822015",
            "extra": "mean: 495.8519550000062 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.36739598985910576,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.7218587779999837 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041130448789858394,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.31288812600002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0888593513625873,
            "unit": "iter/sec",
            "range": "stddev: 0.004264837884666039",
            "extra": "mean: 323.7441029999862 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7284286916893407,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3728179729999965 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08363784529721646,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.956309927000007 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 838.2178776958023,
            "unit": "iter/sec",
            "range": "stddev: 0.0004452769437301945",
            "extra": "mean: 1.193007243831311 msec\nrounds: 1013"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 325.09847951629513,
            "unit": "iter/sec",
            "range": "stddev: 0.00035195149578779757",
            "extra": "mean: 3.075991008902508 msec\nrounds: 337"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.738080106470484,
            "unit": "iter/sec",
            "range": "stddev: 0.0000845462150425028",
            "extra": "mean: 20.94763756250136 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962247469365333,
            "unit": "iter/sec",
            "range": "stddev: 0.00010265570369881268",
            "extra": "mean: 201.52159000000438 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 668.5537275719078,
            "unit": "iter/sec",
            "range": "stddev: 0.0002481195631512364",
            "extra": "mean: 1.4957660974112854 msec\nrounds: 811"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.35160265522998,
            "unit": "iter/sec",
            "range": "stddev: 0.0002832560473375787",
            "extra": "mean: 4.776653186872646 msec\nrounds: 198"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.833108221191385,
            "unit": "iter/sec",
            "range": "stddev: 0.00010821298857009778",
            "extra": "mean: 38.71001473913546 msec\nrounds: 23"
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
          "id": "a4c36f50260d2c08aaa2d9e87e0ebddc23620087",
          "message": "Bump the dependencies group with 1 update (#230)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.80.1...hypothesis-python-6.81.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-07-13T09:12:27+02:00",
          "tree_id": "862798b9f6512df24665603a40048015530d567d",
          "url": "https://github.com/ansys-internal/pyacp/commit/a4c36f50260d2c08aaa2d9e87e0ebddc23620087"
        },
        "date": 1689232632423,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.752283505804552,
            "unit": "iter/sec",
            "range": "stddev: 0.004603047059849304",
            "extra": "mean: 148.09804700000484 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.417751713339703,
            "unit": "iter/sec",
            "range": "stddev: 0.011925253042529362",
            "extra": "mean: 413.60740000000834 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37896494039506157,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.638766527999991 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04117842461736071,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.284561862000004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.700315057959868,
            "unit": "iter/sec",
            "range": "stddev: 0.010063580211073356",
            "extra": "mean: 270.24725850002085 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7345483118422251,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3613808430000063 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08357399650287768,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.965444298999955 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1172.55771555269,
            "unit": "iter/sec",
            "range": "stddev: 0.0002924780649831063",
            "extra": "mean: 852.8364844954739 usec\nrounds: 1290"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 357.06207242353247,
            "unit": "iter/sec",
            "range": "stddev: 0.00019421054678140525",
            "extra": "mean: 2.8006334954944214 msec\nrounds: 333"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.26134394838519,
            "unit": "iter/sec",
            "range": "stddev: 0.00013314014279312773",
            "extra": "mean: 21.15894125000158 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.961639510823182,
            "unit": "iter/sec",
            "range": "stddev: 0.00011458745136560968",
            "extra": "mean: 201.54628279999542 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 932.4952894052723,
            "unit": "iter/sec",
            "range": "stddev: 0.00012990506972781324",
            "extra": "mean: 1.0723914762484013 msec\nrounds: 821"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 214.89012949848507,
            "unit": "iter/sec",
            "range": "stddev: 0.00017612275101489203",
            "extra": "mean: 4.6535408691586735 msec\nrounds: 214"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.6177706928221,
            "unit": "iter/sec",
            "range": "stddev: 0.00015018247268612283",
            "extra": "mean: 39.03540288461526 msec\nrounds: 26"
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
          "id": "cb38ef7e276583a50298c189faa885e7e4fdd629",
          "message": "Bump the dependencies group with 1 update (#235)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.81.1...hypothesis-python-6.81.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-07-17T21:12:01+02:00",
          "tree_id": "d4c0c56c5e2353be04c39af6814ff233b316588d",
          "url": "https://github.com/ansys-internal/pyacp/commit/cb38ef7e276583a50298c189faa885e7e4fdd629"
        },
        "date": 1689621401628,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.81795340346107,
            "unit": "iter/sec",
            "range": "stddev: 0.004610208507408814",
            "extra": "mean: 146.67158028571438 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.467977977515148,
            "unit": "iter/sec",
            "range": "stddev: 0.005545812610369364",
            "extra": "mean: 405.1900013333333 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3832625544743896,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.609177412000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041221111342840795,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.25941386400001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.7142773157738875,
            "unit": "iter/sec",
            "range": "stddev: 0.005037857293639546",
            "extra": "mean: 269.23137800001484 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.735433742987717,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.359741798000016 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08365941860298425,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.953226745999984 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1176.0855215640295,
            "unit": "iter/sec",
            "range": "stddev: 0.00034070018068979536",
            "extra": "mean: 850.2783017600112 usec\nrounds: 1193"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 369.75249123975897,
            "unit": "iter/sec",
            "range": "stddev: 0.00008686239191904893",
            "extra": "mean: 2.704511865889144 msec\nrounds: 343"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.89861006101415,
            "unit": "iter/sec",
            "range": "stddev: 0.0001244596537129605",
            "extra": "mean: 21.32259354166403 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.968936312037201,
            "unit": "iter/sec",
            "range": "stddev: 0.0001487676144370302",
            "extra": "mean: 201.2503154000001 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 889.8687316797821,
            "unit": "iter/sec",
            "range": "stddev: 0.0001571027353074751",
            "extra": "mean: 1.1237612519683955 msec\nrounds: 762"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 204.5608938211597,
            "unit": "iter/sec",
            "range": "stddev: 0.0007107671573711285",
            "extra": "mean: 4.888519898990392 msec\nrounds: 198"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.682981679033304,
            "unit": "iter/sec",
            "range": "stddev: 0.00009430450599743481",
            "extra": "mean: 38.936289115385904 msec\nrounds: 26"
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
          "id": "489214eeb4ee6542c14eb71bb012831c8b41cf65",
          "message": "Update to 2023r2_pre1 version of DPF Composites image (#229)\n\n* Update to 2023r2_pre1 version of DPF Composites image\r\n\r\n* Switch to dev version of DPF Composites",
          "timestamp": "2023-07-17T21:17:01+02:00",
          "tree_id": "7a6fda3b8f8e86e349fc2b3202b4a0e129f87fcc",
          "url": "https://github.com/ansys-internal/pyacp/commit/489214eeb4ee6542c14eb71bb012831c8b41cf65"
        },
        "date": 1689621719634,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.423664045451842,
            "unit": "iter/sec",
            "range": "stddev: 0.002214847909385549",
            "extra": "mean: 134.70437157142865 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.6568196805341464,
            "unit": "iter/sec",
            "range": "stddev: 0.004718938509996342",
            "extra": "mean: 376.38986466667274 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38735990477795257,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.581578494999974 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04129805235511578,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.21421696599998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.9181417975869555,
            "unit": "iter/sec",
            "range": "stddev: 0.007525959770736339",
            "extra": "mean: 255.22302449999756 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7625948326615304,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3113123210000026 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08398559807439133,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.906803343999968 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1220.053218654079,
            "unit": "iter/sec",
            "range": "stddev: 0.00025241164543399",
            "extra": "mean: 819.6363770944073 usec\nrounds: 1432"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 380.44585174131197,
            "unit": "iter/sec",
            "range": "stddev: 0.0001686060803184138",
            "extra": "mean: 2.6284949498672945 msec\nrounds: 379"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.140379673592264,
            "unit": "iter/sec",
            "range": "stddev: 0.00013685958341993923",
            "extra": "mean: 20.772582326527782 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.973109383051276,
            "unit": "iter/sec",
            "range": "stddev: 0.00013258656469931955",
            "extra": "mean: 201.0814408000101 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 959.4248282292207,
            "unit": "iter/sec",
            "range": "stddev: 0.00014907714668641034",
            "extra": "mean: 1.0422911421269634 msec\nrounds: 978"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 229.59785743262097,
            "unit": "iter/sec",
            "range": "stddev: 0.0001838025846454395",
            "extra": "mean: 4.355441340707918 msec\nrounds: 226"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 26.022046299762447,
            "unit": "iter/sec",
            "range": "stddev: 0.00011106445710331514",
            "extra": "mean: 38.42895322221946 msec\nrounds: 27"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "105842014+roosre@users.noreply.github.com",
            "name": "René Roos",
            "username": "roosre"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "18a53e0f323352ebb8c9466e88762f1d70db9ede",
          "message": "add read only property ext_id (#236)\n\n* add read only property ext_id\r\n\r\n* add unit test for the ext_id\r\n\r\n* update reference to ansys-api-acp\r\n\r\n* apply pre-commit patch",
          "timestamp": "2023-07-18T13:40:28+02:00",
          "tree_id": "87278186fe1202a8e692c90ebbe082e05af3a874",
          "url": "https://github.com/ansys-internal/pyacp/commit/18a53e0f323352ebb8c9466e88762f1d70db9ede"
        },
        "date": 1689680787164,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.067755639512926,
            "unit": "iter/sec",
            "range": "stddev: 0.005848683624251814",
            "extra": "mean: 197.3260099999834 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1621379789409976,
            "unit": "iter/sec",
            "range": "stddev: 0.0073533462531502935",
            "extra": "mean: 462.5051730000109 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3779379764475078,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6459368000000154 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04111174076665604,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.32395177999996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0142002258117055,
            "unit": "iter/sec",
            "range": "stddev: 0.005018602230850086",
            "extra": "mean: 331.76296366665764 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7153504587703905,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3979162069999802 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08271018243303299,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.090409797000007 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 812.2114503647908,
            "unit": "iter/sec",
            "range": "stddev: 0.0005949962916776729",
            "extra": "mean: 1.231206478991237 msec\nrounds: 1071"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 328.78043664331267,
            "unit": "iter/sec",
            "range": "stddev: 0.0001969388183094586",
            "extra": "mean: 3.041543500001127 msec\nrounds: 348"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.491110102007354,
            "unit": "iter/sec",
            "range": "stddev: 0.00018743366855588048",
            "extra": "mean: 21.056572437495664 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9577620684239,
            "unit": "iter/sec",
            "range": "stddev: 0.00006445210485079969",
            "extra": "mean: 201.7039111999793 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 702.9421089175421,
            "unit": "iter/sec",
            "range": "stddev: 0.00037165284068956054",
            "extra": "mean: 1.4225922551999286 msec\nrounds: 721"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.41885092942277,
            "unit": "iter/sec",
            "range": "stddev: 0.00035980590280650624",
            "extra": "mean: 4.844518780612303 msec\nrounds: 196"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.64697656875471,
            "unit": "iter/sec",
            "range": "stddev: 0.00023347664491217017",
            "extra": "mean: 38.99095073913249 msec\nrounds: 23"
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
          "id": "8ed07ce9742f19940c3b52cea866b7ed7a46724b",
          "message": "Expose mesh data, add plotting capability. (#231)\n\nAdd `elemental_data` and `nodal_data` attributes to tree objects, which fetch the\r\ndata from the mesh query API.\r\n\r\nThe returned objects have a method `to_pyvista`, to convert to a plottable object. Currently,\r\nthis requires the `Model.mesh` to be passed in; we may consider how this can be avoided.\r\n\r\nOptionally, a `component` (name to be improved) can be passed, to select which data to\r\nadd to the PyVista mesh. If a vector component is selected, the data is converted to arrows.\r\n\r\nThe possible string constants for `component` are exposed in the `ElementalDataType` and\r\n`NodalDataType` enums, which are auto-converted from their protobuf equivalent.\r\n\r\nHelper classes and functions for wrapping mesh query data are defined in `_mesh_data.py`:\r\n\r\n- a base class `MeshDataBase` which implements `to_pyvista`, as well as the construction\r\n  from a mesh query response\r\n- base classes `ElementalData` and `NodalData`, which are the classes to be used to define\r\n  the mesh data classes for each tree object type\r\n- property helpers `elemental_data_property` and `nodal_data_property`, for defining\r\n  the `elemental_data` and `nodal_data` properties, respectively.\r\n\r\n\r\nThe mesh data itself is exposed in a separate `mesh` on the `Model`. Its class `MeshData`\r\nalso implements a `to_pyvista` method.\r\n\r\nAdd a `__slots__` class attribute in some places where it was missing, to disallow setting\r\nattributes that are not explicitly defined on tree objects.",
          "timestamp": "2023-08-02T18:08:33+02:00",
          "tree_id": "db9ffa31a2269480b7e1374a489acfadbe9a442a",
          "url": "https://github.com/ansys-internal/pyacp/commit/8ed07ce9742f19940c3b52cea866b7ed7a46724b"
        },
        "date": 1690992842028,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.274697901013739,
            "unit": "iter/sec",
            "range": "stddev: 0.00460094107896553",
            "extra": "mean: 189.58431720000704 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.237483620668974,
            "unit": "iter/sec",
            "range": "stddev: 0.006714096267067295",
            "extra": "mean: 446.93064599999843 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3702241892689194,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.7010660809999933 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04112390580307352,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.316756408999993 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.251340110001192,
            "unit": "iter/sec",
            "range": "stddev: 0.005380249629904136",
            "extra": "mean: 307.5654856666574 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7034569487488133,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4215511010000341 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08263213403855763,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.10182953200001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 947.3248783937535,
            "unit": "iter/sec",
            "range": "stddev: 0.0005161914439535643",
            "extra": "mean: 1.0556040729085048 msec\nrounds: 1111"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 347.9926995698549,
            "unit": "iter/sec",
            "range": "stddev: 0.000461195409414361",
            "extra": "mean: 2.8736235019759757 msec\nrounds: 253"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.59907364245739,
            "unit": "iter/sec",
            "range": "stddev: 0.0001990485404682183",
            "extra": "mean: 21.459654062497908 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.960386310282433,
            "unit": "iter/sec",
            "range": "stddev: 0.00016330300112877554",
            "extra": "mean: 201.59720180000704 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 765.202043754203,
            "unit": "iter/sec",
            "range": "stddev: 0.00038147883584026634",
            "extra": "mean: 1.3068443924872977 msec\nrounds: 772"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.6832837853777,
            "unit": "iter/sec",
            "range": "stddev: 0.0002459688138422801",
            "extra": "mean: 4.815024020100777 msec\nrounds: 199"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.489741467923455,
            "unit": "iter/sec",
            "range": "stddev: 0.00017063477931365524",
            "extra": "mean: 39.23146891302958 msec\nrounds: 23"
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
          "id": "50c8a6f8d3bb27e1582cfe1ca0e7051c82497003",
          "message": "Add tests for mesh data (#249)\n\nAdd tests for the `mesh`, `elemental_data` and `nodal_data` attributes on the\r\ntop-level `Model`, and tests for `elemental_data` and `nodal_data` on the\r\nmodeling ply.\r\n\r\nSince the code in use is mostly the same between mesh data attributes on\r\ndifferent tree objects (apart from defining which elemental and nodal\r\ndata attributes are available), I think it's not really necessary to add tests\r\nfor all other objects.",
          "timestamp": "2023-08-07T10:19:01+02:00",
          "tree_id": "92b81f1dd89cba130cfe9ad4552e22a58375e930",
          "url": "https://github.com/ansys-internal/pyacp/commit/50c8a6f8d3bb27e1582cfe1ca0e7051c82497003"
        },
        "date": 1691396642600,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.798083652460759,
            "unit": "iter/sec",
            "range": "stddev: 0.0029523592468086264",
            "extra": "mean: 147.10027871428468 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5175849131186268,
            "unit": "iter/sec",
            "range": "stddev: 0.004497966061948127",
            "extra": "mean: 397.2060663333347 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37666686396728194,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6548658659999944 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04117720410708055,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.285281666999992 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.6826907103870403,
            "unit": "iter/sec",
            "range": "stddev: 0.011591966031600613",
            "extra": "mean: 271.54058775001033 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7276803807018903,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3742297119999876 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08318645689184145,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.021187550999969 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1233.7829710292967,
            "unit": "iter/sec",
            "range": "stddev: 0.00021553058418585577",
            "extra": "mean: 810.5153203449869 usec\nrounds: 1155"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 368.20351259431965,
            "unit": "iter/sec",
            "range": "stddev: 0.00011794703352274739",
            "extra": "mean: 2.715889354107773 msec\nrounds: 353"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.73627359539634,
            "unit": "iter/sec",
            "range": "stddev: 0.00015838359250544939",
            "extra": "mean: 21.396656666664644 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962289157978211,
            "unit": "iter/sec",
            "range": "stddev: 0.00008815302746155542",
            "extra": "mean: 201.51989700000286 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 925.2538846563701,
            "unit": "iter/sec",
            "range": "stddev: 0.0001558993751405431",
            "extra": "mean: 1.0807844382857035 msec\nrounds: 794"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 211.90552419046708,
            "unit": "iter/sec",
            "range": "stddev: 0.00014953923851618398",
            "extra": "mean: 4.719084147618398 msec\nrounds: 210"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.58385581553019,
            "unit": "iter/sec",
            "range": "stddev: 0.00011149921281022799",
            "extra": "mean: 39.087149615382415 msec\nrounds: 26"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jan.vonrickenbach@ansys.com",
            "name": "janvonrickenbach",
            "username": "janvonrickenbach"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ba6656f665601a9d27370158b1a096a67292ea6a",
          "message": "Jvonrick/production ply object (#244)\n\nImplement the production ply frontend.\r\n\r\nIn order to support read-only objects I simplified the class Hierarchy for TreeObject. Basically there are now three levels:\r\n\r\nGrpcObjectBase: Handles the _GRPC_Properties and its string representation\r\nTreeObjectBase: Handles everything related to storing and instanciating the object.\r\nTreeObject / ReadOnlyTreeObject: Handles the different requests using the stubs.\r\nThe reason why I changed this was because I would have to add a ReadOnly variant of the RootGrpcObject, which makes the already complex class hierarchy even more complicated. I did not fully understand why we need the intermediate classes in the hierarchy (such as RootGrpcObject). In my understanding these subtypes are only needed because the are used as types elsewhere (for example in the property helpers). But I think it is easier to adress this with structural subtyping. Therefore I added Editable and Gettable protocols that are implemented by the new tree object classes (ReadOnlyTreeObjects and TreeObject). The downside of the new implementation is that there is a little bit of code repetition for the _get methods. We could add small subjects to which we delegate the different requests to avoid this (Similar to StubStore).\r\n\r\nOther changes:\r\n\r\nSplit the Mapping object into a readable and editable part\r\nSplit the TreeObjectTester in a readonly and editable part",
          "timestamp": "2023-08-07T11:33:21Z",
          "tree_id": "5b25153fcf7650411c8d4f41562e5ecc4a576c2c",
          "url": "https://github.com/ansys-internal/pyacp/commit/ba6656f665601a9d27370158b1a096a67292ea6a"
        },
        "date": 1691408297550,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.896227561809127,
            "unit": "iter/sec",
            "range": "stddev: 0.0018895010213891713",
            "extra": "mean: 145.0068158333314 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.459649446727021,
            "unit": "iter/sec",
            "range": "stddev: 0.010647331214214727",
            "extra": "mean: 406.5620006666677 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38152619795287523,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.621051989000023 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041204078157285766,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.269442364000042 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.7096136403264657,
            "unit": "iter/sec",
            "range": "stddev: 0.004213387739617485",
            "extra": "mean: 269.5698520000036 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7313544232233601,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3673261120000006 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08300411468736071,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.04759551699999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1101.4109996290201,
            "unit": "iter/sec",
            "range": "stddev: 0.0002905134075134189",
            "extra": "mean: 907.9262875863982 usec\nrounds: 1450"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 358.02722175703957,
            "unit": "iter/sec",
            "range": "stddev: 0.00021373122332008794",
            "extra": "mean: 2.7930837076925084 msec\nrounds: 325"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.40473011376882,
            "unit": "iter/sec",
            "range": "stddev: 0.00017428816237557326",
            "extra": "mean: 21.09494131914797 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96794871253486,
            "unit": "iter/sec",
            "range": "stddev: 0.00006565548812720788",
            "extra": "mean: 201.29032280000274 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 895.2448467800842,
            "unit": "iter/sec",
            "range": "stddev: 0.0001679270036350431",
            "extra": "mean: 1.1170128525136862 msec\nrounds: 895"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 214.1910666594999,
            "unit": "iter/sec",
            "range": "stddev: 0.00016437618365482156",
            "extra": "mean: 4.668728792455674 msec\nrounds: 212"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.683870541745637,
            "unit": "iter/sec",
            "range": "stddev: 0.00013571183705349838",
            "extra": "mean: 38.93494161538605 msec\nrounds: 26"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "105842014+roosre@users.noreply.github.com",
            "name": "René Roos",
            "username": "roosre"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2df92e53cd419a06af64dd87ddafcfe43f1491e6",
          "message": "Exposure of Stackup (#239)\n\n* Add unit test for stackup\r\n\r\n* add GenericObjectList to handle typed graph edge properties such as link between stackup and fabric in the front end.\r\n\r\n* update stackup test\r\n\r\n* Fix MutableSequence interface in linked_object_list\r\n\r\n* Fix string representation of objects containing edge property list\r\n\r\n* implement suggestions from the code review.\r\n\r\n* apply pre-commit check\r\n\r\n---------\r\n\r\nCo-authored-by: Dominik Gresch <dominik.gresch@ansys.com>\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>",
          "timestamp": "2023-08-08T11:17:05+02:00",
          "tree_id": "0d132f9c5841ebc035d5b6a795c726fabfccd8c9",
          "url": "https://github.com/ansys-internal/pyacp/commit/2df92e53cd419a06af64dd87ddafcfe43f1491e6"
        },
        "date": 1691486532612,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.260954832052822,
            "unit": "iter/sec",
            "range": "stddev: 0.003943749369847308",
            "extra": "mean: 137.72293357143488 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.6388327374602207,
            "unit": "iter/sec",
            "range": "stddev: 0.006258353869285546",
            "extra": "mean: 378.9554320000074 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38875416583035793,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5723197019999873 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04130252023320365,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.211597605999998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.9764214629866776,
            "unit": "iter/sec",
            "range": "stddev: 0.004040166146252816",
            "extra": "mean: 251.48239674999218 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7590053268587539,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3175138100000368 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0833980928072287,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.990681876999986 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1185.1871202836912,
            "unit": "iter/sec",
            "range": "stddev: 0.00027966106342051906",
            "extra": "mean: 843.7486223784105 usec\nrounds: 1430"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 389.74090132391404,
            "unit": "iter/sec",
            "range": "stddev: 0.00008264457887599151",
            "extra": "mean: 2.5658071724140115 msec\nrounds: 377"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.18196045984558,
            "unit": "iter/sec",
            "range": "stddev: 0.00016092371306766523",
            "extra": "mean: 20.754655693875122 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.971894289277714,
            "unit": "iter/sec",
            "range": "stddev: 0.00021036043092570708",
            "extra": "mean: 201.13058360001332 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 923.8255706167357,
            "unit": "iter/sec",
            "range": "stddev: 0.00044255782727835124",
            "extra": "mean: 1.0824554242771296 msec\nrounds: 865"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 230.45689719581912,
            "unit": "iter/sec",
            "range": "stddev: 0.0001926257766586814",
            "extra": "mean: 4.339206212389037 msec\nrounds: 226"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.90390789559116,
            "unit": "iter/sec",
            "range": "stddev: 0.0001338422888712403",
            "extra": "mean: 38.60421385184897 msec\nrounds: 27"
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
          "id": "3f31101f3c319e09fcd9284b258a254dfd2d1a09",
          "message": "Expose mesh data on production plies (#251)\n\nAdd elemental and nodal data attributes to the production plies.",
          "timestamp": "2023-08-08T15:08:39+02:00",
          "tree_id": "5b1ea08481d4501d9668d4df6681664e9f1bca8c",
          "url": "https://github.com/ansys-internal/pyacp/commit/3f31101f3c319e09fcd9284b258a254dfd2d1a09"
        },
        "date": 1691500415976,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.810644416091604,
            "unit": "iter/sec",
            "range": "stddev: 0.0026140288153152593",
            "extra": "mean: 146.8289839999995 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4643191983108137,
            "unit": "iter/sec",
            "range": "stddev: 0.011581791270482946",
            "extra": "mean: 405.7915876666698 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3811944052737539,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6233333600000037 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04121250826511238,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.264477997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.710482797001539,
            "unit": "iter/sec",
            "range": "stddev: 0.004566669592328451",
            "extra": "mean: 269.5067069999908 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7365406314296431,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.357698350000021 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08297120733121705,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.052373735000003 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1154.487159984185,
            "unit": "iter/sec",
            "range": "stddev: 0.000268461463970188",
            "extra": "mean: 866.1854671590276 usec\nrounds: 1355"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 371.23046959174525,
            "unit": "iter/sec",
            "range": "stddev: 0.00009888511856034374",
            "extra": "mean: 2.693744403846306 msec\nrounds: 364"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.406619169945344,
            "unit": "iter/sec",
            "range": "stddev: 0.00012369135856284645",
            "extra": "mean: 21.094100729165177 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9660833787199685,
            "unit": "iter/sec",
            "range": "stddev: 0.00009635726635905416",
            "extra": "mean: 201.3659304000157 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 908.7634795056596,
            "unit": "iter/sec",
            "range": "stddev: 0.00014216304039198454",
            "extra": "mean: 1.1003963325462534 msec\nrounds: 845"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 215.95049664859513,
            "unit": "iter/sec",
            "range": "stddev: 0.0001174636823024106",
            "extra": "mean: 4.630690901476589 msec\nrounds: 203"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.634420783356394,
            "unit": "iter/sec",
            "range": "stddev: 0.00013567425119058807",
            "extra": "mean: 39.01004857692232 msec\nrounds: 26"
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
          "id": "31dcf2436ddec4c8e90b6c20421289ebc46b4fcb",
          "message": "Add selection rules (#252)\n\nAdd ``ParallelSelectionRule``, ``CylindricalSelectionRule``, ``SphericalSelectionRule``,\r\n``TubeSelectionRule`` and ``BooleanSelectionRule`` classes.\r\n\r\nAdd links from the Oriented Selection Set and Modeling Ply to the selection rules.\r\n\r\nThe link from ``BooleanSelectionRule`` to its linked selection rules uses the \r\n``EdgePropertyList`` functionality, with edge properties defined in \r\n``LinkedSelectionRule``.\r\nThe polymorphic nature of the selection rule link (all other selection rule types\r\ncan be linked) is enabled by adding a new function ``tree_object_from_resource_path``,\r\nwhose functionality is extracted from the grpc property helpers.",
          "timestamp": "2023-08-09T15:19:25Z",
          "tree_id": "7b2a01526fc3ce501f35c9cb8ebc382ba15cb1ca",
          "url": "https://github.com/ansys-internal/pyacp/commit/31dcf2436ddec4c8e90b6c20421289ebc46b4fcb"
        },
        "date": 1691594659433,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.270096487285852,
            "unit": "iter/sec",
            "range": "stddev: 0.004379217104211105",
            "extra": "mean: 137.54975628574226 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5656491417909217,
            "unit": "iter/sec",
            "range": "stddev: 0.003728819972088424",
            "extra": "mean: 389.7649073333393 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3874959287498086,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5806722749999835 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04129231092678897,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.217583796000042 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.929242264244137,
            "unit": "iter/sec",
            "range": "stddev: 0.006091875655775046",
            "extra": "mean: 254.50199624999925 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7579838761927595,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3192892769999958 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08345182286997484,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.982961732999968 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1167.8426780454997,
            "unit": "iter/sec",
            "range": "stddev: 0.00037393946491088534",
            "extra": "mean: 856.2797188347312 usec\nrounds: 1476"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 376.99272845776414,
            "unit": "iter/sec",
            "range": "stddev: 0.00020439660757623636",
            "extra": "mean: 2.6525710564521767 msec\nrounds: 372"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.21811749938317,
            "unit": "iter/sec",
            "range": "stddev: 0.00015127149133598795",
            "extra": "mean: 20.739092520830837 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974525920367227,
            "unit": "iter/sec",
            "range": "stddev: 0.00017218175058363993",
            "extra": "mean: 201.02418120000038 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 936.9729705480657,
            "unit": "iter/sec",
            "range": "stddev: 0.00016337632288866902",
            "extra": "mean: 1.0672666463527414 msec\nrounds: 1001"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 232.71698869153028,
            "unit": "iter/sec",
            "range": "stddev: 0.00007738125118714641",
            "extra": "mean: 4.29706488392867 msec\nrounds: 224"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.96831904029179,
            "unit": "iter/sec",
            "range": "stddev: 0.00011844981968621192",
            "extra": "mean: 38.50846096154415 msec\nrounds: 26"
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
          "id": "88dbbb6b1980d3dccdfd18903e1170494f82f50f",
          "message": "Bump the dependencies group with 1 update (#255)\n\nBumps the dependencies group with 1 update: [ansys-mapdl-core](https://github.com/ansys/pymapdl).\r\n\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.65.0...v0.65.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-08-10T08:01:08+02:00",
          "tree_id": "441aa6af5a9c874a366b1232df0b58a1a6f1b2c4",
          "url": "https://github.com/ansys-internal/pyacp/commit/88dbbb6b1980d3dccdfd18903e1170494f82f50f"
        },
        "date": 1691647573233,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.13610269786369,
            "unit": "iter/sec",
            "range": "stddev: 0.0032794791777421674",
            "extra": "mean: 140.13251242857905 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5775532946517052,
            "unit": "iter/sec",
            "range": "stddev: 0.01003986635883803",
            "extra": "mean: 387.96482000001714 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38801784459456046,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5772010590000036 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04129082651158044,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.218454423999958 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.8924782485030187,
            "unit": "iter/sec",
            "range": "stddev: 0.0035439053357141756",
            "extra": "mean: 256.90573875000666 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7563593380862986,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.322122897999975 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08350321024626402,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 11.97558749000001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1155.384660061402,
            "unit": "iter/sec",
            "range": "stddev: 0.00025302166265999554",
            "extra": "mean: 865.512616332344 usec\nrounds: 1543"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 389.8366769828972,
            "unit": "iter/sec",
            "range": "stddev: 0.00008792780459903414",
            "extra": "mean: 2.565176801062953 msec\nrounds: 377"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.25661737750285,
            "unit": "iter/sec",
            "range": "stddev: 0.00010229498674648558",
            "extra": "mean: 20.722546551018688 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.975746608838787,
            "unit": "iter/sec",
            "range": "stddev: 0.000011910711172293975",
            "extra": "mean: 200.97486439997283 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 940.6534293134425,
            "unit": "iter/sec",
            "range": "stddev: 0.00015671169391052452",
            "extra": "mean: 1.0630907928862523 msec\nrounds: 956"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 230.9743859149002,
            "unit": "iter/sec",
            "range": "stddev: 0.0001180369448126264",
            "extra": "mean: 4.329484397323772 msec\nrounds: 224"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.967282029628702,
            "unit": "iter/sec",
            "range": "stddev: 0.00013058159005102906",
            "extra": "mean: 38.50999880769187 msec\nrounds: 26"
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
          "id": "05725f6760bdee89f5efa668aa6555d7df05344d",
          "message": "Bump the dependencies group with 1 update (#256)\n\nBumps the dependencies group with 1 update: [mypy](https://github.com/python/mypy).\r\n\r\n- [Commits](https://github.com/python/mypy/compare/v1.4.1...v1.5.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-08-11T08:09:16+02:00",
          "tree_id": "1fdd3f1532b5f2c8cb072ab645e7d7e2c47aff14",
          "url": "https://github.com/ansys-internal/pyacp/commit/05725f6760bdee89f5efa668aa6555d7df05344d"
        },
        "date": 1691734465916,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.372755108989347,
            "unit": "iter/sec",
            "range": "stddev: 0.0060606996274162744",
            "extra": "mean: 156.91800216666252 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4829101912264933,
            "unit": "iter/sec",
            "range": "stddev: 0.004608745595646871",
            "extra": "mean: 402.75319000000803 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3757962590037092,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6610163779999993 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04120801390677967,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.267124405999994 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.6207761587920837,
            "unit": "iter/sec",
            "range": "stddev: 0.004547834118003537",
            "extra": "mean: 276.1838777500145 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7162331045185591,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3961934929999984 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08294184354646546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.056640619999996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1142.7902572551031,
            "unit": "iter/sec",
            "range": "stddev: 0.0002577253351258667",
            "extra": "mean: 875.0512122862557 usec\nrounds: 1286"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 368.12761048405275,
            "unit": "iter/sec",
            "range": "stddev: 0.00010711867233265335",
            "extra": "mean: 2.716449327680407 msec\nrounds: 354"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.01043978562961,
            "unit": "iter/sec",
            "range": "stddev: 0.00012309303857706557",
            "extra": "mean: 21.271870770834294 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.965939618311934,
            "unit": "iter/sec",
            "range": "stddev: 0.00010693020967948755",
            "extra": "mean: 201.3717597999971 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 897.0970818650009,
            "unit": "iter/sec",
            "range": "stddev: 0.00014652891698248868",
            "extra": "mean: 1.114706557645992 msec\nrounds: 850"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.77789615569452,
            "unit": "iter/sec",
            "range": "stddev: 0.0003050968645335798",
            "extra": "mean: 4.744330493086114 msec\nrounds: 217"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.638256987400744,
            "unit": "iter/sec",
            "range": "stddev: 0.00012508212177947829",
            "extra": "mean: 39.00421157691898 msec\nrounds: 26"
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
          "id": "816748238fa27157fe2713afeec838be3aea4a15",
          "message": "Bump the dependencies group with 3 updates (#257)\n\nBumps the dependencies group with 3 updates: [types-protobuf](https://github.com/python/typeshed), [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `types-protobuf` from 4.24.0.0 to 4.24.0.1\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.10.2 to 0.10.3\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.10.2...v0.10.3)\r\n\r\nUpdates `hypothesis` from 6.82.3 to 6.82.4\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.82.3...hypothesis-python-6.82.4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-08-14T07:46:49+02:00",
          "tree_id": "d16347175abe9aef0dd19c92c782d9a3f712e134",
          "url": "https://github.com/ansys-internal/pyacp/commit/816748238fa27157fe2713afeec838be3aea4a15"
        },
        "date": 1691992340932,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.06015890045712,
            "unit": "iter/sec",
            "range": "stddev: 0.0012542196764107744",
            "extra": "mean: 165.01217483333144 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.374796151654142,
            "unit": "iter/sec",
            "range": "stddev: 0.007184424890646504",
            "extra": "mean: 421.0887740000165 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37767992197588773,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6477446690000193 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041051748467382104,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.359498373000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.446636211057544,
            "unit": "iter/sec",
            "range": "stddev: 0.015404724460215808",
            "extra": "mean: 290.13796024999294 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7236826020940931,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.381821253000055 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0825649892268118,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.111671174000037 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 992.5888146666196,
            "unit": "iter/sec",
            "range": "stddev: 0.0004226341484649409",
            "extra": "mean: 1.0074665211050857 msec\nrounds: 1303"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 355.5718098564564,
            "unit": "iter/sec",
            "range": "stddev: 0.00011986817856671813",
            "extra": "mean: 2.812371431817663 msec\nrounds: 352"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.98381295079336,
            "unit": "iter/sec",
            "range": "stddev: 0.00014340159250522173",
            "extra": "mean: 21.2839260416627 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.956564647550245,
            "unit": "iter/sec",
            "range": "stddev: 0.00005789725846059678",
            "extra": "mean: 201.7526394000015 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 841.6557419478429,
            "unit": "iter/sec",
            "range": "stddev: 0.00015938666341003307",
            "extra": "mean: 1.1881342337018945 msec\nrounds: 813"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 211.32478028557293,
            "unit": "iter/sec",
            "range": "stddev: 0.00013974713025321115",
            "extra": "mean: 4.732052713593994 msec\nrounds: 206"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.538745458894592,
            "unit": "iter/sec",
            "range": "stddev: 0.00016089490858639362",
            "extra": "mean: 39.15619119230156 msec\nrounds: 26"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "jan.vonrickenbach@ansys.com",
            "name": "janvonrickenbach",
            "username": "janvonrickenbach"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "0c0d56426067008343380231dbb9101d66dfea75",
          "message": "Jvonrick/analysis ply object (#253)\n\n* Add analysis_ply \r\n* Add missing analysis_plies in production ply",
          "timestamp": "2023-08-14T13:50:56+02:00",
          "tree_id": "41306951b5dcd19279fed617432d4bc5528111a1",
          "url": "https://github.com/ansys-internal/pyacp/commit/0c0d56426067008343380231dbb9101d66dfea75"
        },
        "date": 1692014166627,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 7.279241448883508,
            "unit": "iter/sec",
            "range": "stddev: 0.0032122451801835884",
            "extra": "mean: 137.37695157142784 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3705143346910154,
            "unit": "iter/sec",
            "range": "stddev: 0.008958302678161003",
            "extra": "mean: 421.8493789999987 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3873110009557144,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.581904457999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04127119234455702,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.229975999999994 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.9218343894048826,
            "unit": "iter/sec",
            "range": "stddev: 0.004263360280266257",
            "extra": "mean: 254.982720000001 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.761835049209092,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3126201019999826 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08330584024010222,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.003960312000004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1063.4982874928182,
            "unit": "iter/sec",
            "range": "stddev: 0.0003138739867120249",
            "extra": "mean: 940.2930044743989 usec\nrounds: 1788"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 353.37039316164885,
            "unit": "iter/sec",
            "range": "stddev: 0.000351811642070351",
            "extra": "mean: 2.8298918623398968 msec\nrounds: 385"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.23554561187347,
            "unit": "iter/sec",
            "range": "stddev: 0.0002162285578857849",
            "extra": "mean: 20.73159922449066 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9745725915877195,
            "unit": "iter/sec",
            "range": "stddev: 0.00009953195703773729",
            "extra": "mean: 201.02229520000492 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 933.1527256840444,
            "unit": "iter/sec",
            "range": "stddev: 0.00017895189902240456",
            "extra": "mean: 1.0716359417660741 msec\nrounds: 996"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 220.1401560537623,
            "unit": "iter/sec",
            "range": "stddev: 0.0002461172543512682",
            "extra": "mean: 4.5425606028723875 msec\nrounds: 209"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.912607399408675,
            "unit": "iter/sec",
            "range": "stddev: 0.00025917878700252797",
            "extra": "mean: 38.591253461541655 msec\nrounds: 26"
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
          "id": "8adae81b894a6f12caaaccaace2bb2acda3c35b6",
          "message": "Add look-up tables (#258)\n\nAdd the `LookUpTable1D`, `LookUpTable1DColumn`, `LookUpTable3D` and\r\n`LookUpTable3DColumn` classes. The two column classes use a common \r\nbase, since they have the same attributes.\r\n\r\nThe column `value_type` is settable only in the constructor, since the API\r\nonly allows changing it when the `data` shape is changed to match, or\r\nthe `data` is empty. This would make setting it independently as a property \r\nchallenging / potentially confusing.",
          "timestamp": "2023-08-16T09:30:04Z",
          "tree_id": "ceb3ff5c354b22ca943c8a9fa70d74d339eb2518",
          "url": "https://github.com/ansys-internal/pyacp/commit/8adae81b894a6f12caaaccaace2bb2acda3c35b6"
        },
        "date": 1692178542804,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.106933414872426,
            "unit": "iter/sec",
            "range": "stddev: 0.006049401127542347",
            "extra": "mean: 195.81222600000956 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2056907773443335,
            "unit": "iter/sec",
            "range": "stddev: 0.003805308271976744",
            "extra": "mean: 453.3727076666689 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3768213818816131,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6537772220000306 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041138954541775,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.30786127500005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.1246192358527627,
            "unit": "iter/sec",
            "range": "stddev: 0.007812243612284369",
            "extra": "mean: 320.03899500000443 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7168140798525512,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3950618829999826 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0828056426584938,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.076471697999978 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1046.1057331093632,
            "unit": "iter/sec",
            "range": "stddev: 0.0004083828727475577",
            "extra": "mean: 955.9263163845568 usec\nrounds: 708"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 332.59221787044464,
            "unit": "iter/sec",
            "range": "stddev: 0.00032218553754282043",
            "extra": "mean: 3.00668490201876 msec\nrounds: 347"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.352205725911155,
            "unit": "iter/sec",
            "range": "stddev: 0.00017774373767199243",
            "extra": "mean: 21.118340416670378 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.960713672715376,
            "unit": "iter/sec",
            "range": "stddev: 0.00006273158774159342",
            "extra": "mean: 201.5838981999991 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 712.6818733839964,
            "unit": "iter/sec",
            "range": "stddev: 0.0004468151727673447",
            "extra": "mean: 1.40315060245849 msec\nrounds: 732"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.31610434008743,
            "unit": "iter/sec",
            "range": "stddev: 0.00012219533907878864",
            "extra": "mean: 4.754747636362502 msec\nrounds: 198"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.63902745470173,
            "unit": "iter/sec",
            "range": "stddev: 0.00022353500542254454",
            "extra": "mean: 39.003039478262984 msec\nrounds: 23"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "105842014+roosre@users.noreply.github.com",
            "name": "René Roos",
            "username": "roosre"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "dc16f7a6e2aedbe81d265a9880404a149173475e",
          "message": "Exposure of SubLaminate and add read only properties to Fabric and Stackup (#260)\n\n* Exposure of SubLaminate and add read only properties to Fabric and Stackup\r\n\r\n* update test for the Fabric and Stackup\r\n\r\n* revert accidental changes in poetry.lock\r\n\r\n* run pre-commit checks\r\n\r\n* update reference to the ansys-api-acp git repo",
          "timestamp": "2023-08-17T08:51:19+02:00",
          "tree_id": "d2357bc3010d5dfb86b328efa10f75e20b84e9e5",
          "url": "https://github.com/ansys-internal/pyacp/commit/dc16f7a6e2aedbe81d265a9880404a149173475e"
        },
        "date": 1692255416449,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.220686292834292,
            "unit": "iter/sec",
            "range": "stddev: 0.008786817730571857",
            "extra": "mean: 191.54569800000445 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.301908239114677,
            "unit": "iter/sec",
            "range": "stddev: 0.013146138756441791",
            "extra": "mean: 434.42218200001054 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3707836610823392,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6969904690000135 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.0410532973747988,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.35857930900005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.207572255245443,
            "unit": "iter/sec",
            "range": "stddev: 0.007514881436004246",
            "extra": "mean: 311.7622676666656 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7032069613534355,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4220564569999965 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08258694970794088,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.10845059099995 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 951.4569358783027,
            "unit": "iter/sec",
            "range": "stddev: 0.0005343388885796231",
            "extra": "mean: 1.0510197175417997 msec\nrounds: 1009"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 342.8421739050325,
            "unit": "iter/sec",
            "range": "stddev: 0.00027891222739891516",
            "extra": "mean: 2.916794012270499 msec\nrounds: 326"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.57806080537133,
            "unit": "iter/sec",
            "range": "stddev: 0.0002785669768251539",
            "extra": "mean: 21.469335191487428 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9543890865048406,
            "unit": "iter/sec",
            "range": "stddev: 0.0002731995318433118",
            "extra": "mean: 201.84123259997477 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 746.460432711134,
            "unit": "iter/sec",
            "range": "stddev: 0.0004686539943467181",
            "extra": "mean: 1.3396557354929235 msec\nrounds: 741"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.11790606979065,
            "unit": "iter/sec",
            "range": "stddev: 0.0004233215339012478",
            "extra": "mean: 4.851592076922246 msec\nrounds: 195"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.481645561283806,
            "unit": "iter/sec",
            "range": "stddev: 0.00022153342131897764",
            "extra": "mean: 39.24393334782805 msec\nrounds: 23"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "105842014+roosre@users.noreply.github.com",
            "name": "René Roos",
            "username": "roosre"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "f7a470eb92c787ee12e097d1012d871e09f52d30",
          "message": "Test link between MP and Fabric, Stackup or SubLaminate (#262)\n\n* ModelingPly: test linkage of all possible ply materials (Fabric, Stackup and SubLaminate)\r\n\r\n* run pre-commit checks\r\n\r\n* Update tests/unittests/test_modeling_ply.py\r\n\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>\r\n\r\n---------\r\n\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>",
          "timestamp": "2023-08-17T10:03:44Z",
          "tree_id": "e14d61ea9369d211f74dab63767b8304c1797601",
          "url": "https://github.com/ansys-internal/pyacp/commit/f7a470eb92c787ee12e097d1012d871e09f52d30"
        },
        "date": 1692266926411,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.46571009790458,
            "unit": "iter/sec",
            "range": "stddev: 0.005173298258463225",
            "extra": "mean: 154.66205333333485 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4167983299460016,
            "unit": "iter/sec",
            "range": "stddev: 0.010640750873826222",
            "extra": "mean: 413.7705606666581 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37953857762903587,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.634778277999999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041132000432478784,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.311970959000007 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.422165605838521,
            "unit": "iter/sec",
            "range": "stddev: 0.017440717815800328",
            "extra": "mean: 292.2126264999889 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7212706392891726,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3864421279999988 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.08284614432042796,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.070567775999962 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1170.796429064625,
            "unit": "iter/sec",
            "range": "stddev: 0.000326156196819708",
            "extra": "mean: 854.1194482450908 usec\nrounds: 1140"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 343.01731468083386,
            "unit": "iter/sec",
            "range": "stddev: 0.0003240030121578548",
            "extra": "mean: 2.915304730113891 msec\nrounds: 352"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.216870151740316,
            "unit": "iter/sec",
            "range": "stddev: 0.00022261055645300383",
            "extra": "mean: 21.178870958331448 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.95859542080321,
            "unit": "iter/sec",
            "range": "stddev: 0.00014961164485056218",
            "extra": "mean: 201.67001240000673 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 887.1092010882204,
            "unit": "iter/sec",
            "range": "stddev: 0.00021922231956416808",
            "extra": "mean: 1.1272569360945597 msec\nrounds: 579"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 205.8126606049751,
            "unit": "iter/sec",
            "range": "stddev: 0.0002840512701202695",
            "extra": "mean: 4.858787584109523 msec\nrounds: 214"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.68720708483059,
            "unit": "iter/sec",
            "range": "stddev: 0.00017734180842694943",
            "extra": "mean: 38.92988430768495 msec\nrounds: 26"
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
          "id": "c2f86b6188f17896c88e1c3c974685d0e21ac9f0",
          "message": "Add variable offset selection rule (#264)\n\nAdds a `VariableOffsetSelectionRule` class, and enables linking to it from the\r\n`ModelingPly`, `OrientedSelectionSet` and `BooleanSelectionRule`.",
          "timestamp": "2023-08-21T09:17:50Z",
          "tree_id": "554eb412e228a9adfa3c45d130b6829cddf1aaed",
          "url": "https://github.com/ansys-internal/pyacp/commit/c2f86b6188f17896c88e1c3c974685d0e21ac9f0"
        },
        "date": 1692609772957,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.407607590166345,
            "unit": "iter/sec",
            "range": "stddev: 0.0031327033894135155",
            "extra": "mean: 156.06448833331874 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2603484845261126,
            "unit": "iter/sec",
            "range": "stddev: 0.01056686847065116",
            "extra": "mean: 442.40965799999304 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38230249174132447,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.615729746999989 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04116212144509675,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.294180301999972 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.175612505232742,
            "unit": "iter/sec",
            "range": "stddev: 0.011440260971732338",
            "extra": "mean: 314.89988100003075 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6837336111822484,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.462557908000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07634193806629573,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.09896009099998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1165.9892249762042,
            "unit": "iter/sec",
            "range": "stddev: 0.00023322491931184003",
            "extra": "mean: 857.6408585768949 usec\nrounds: 1195"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 337.11559332150773,
            "unit": "iter/sec",
            "range": "stddev: 0.0002592901236663326",
            "extra": "mean: 2.9663415748505533 msec\nrounds: 334"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.31937574934981,
            "unit": "iter/sec",
            "range": "stddev: 0.00017312867463607553",
            "extra": "mean: 21.132992229166092 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.963891674076036,
            "unit": "iter/sec",
            "range": "stddev: 0.0002069432119904083",
            "extra": "mean: 201.45483940000304 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 866.3189179256857,
            "unit": "iter/sec",
            "range": "stddev: 0.0001917420418454036",
            "extra": "mean: 1.1543093187834341 msec\nrounds: 756"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 203.83953129457726,
            "unit": "iter/sec",
            "range": "stddev: 0.00025567218181243525",
            "extra": "mean: 4.905819757576155 msec\nrounds: 198"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.704654064593267,
            "unit": "iter/sec",
            "range": "stddev: 0.000216067302799042",
            "extra": "mean: 38.90346073077266 msec\nrounds: 26"
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
          "id": "5a47434920bd102c2de5755a71782a12fe7c3a09",
          "message": "Add draping attributes to OSS and Modeling Ply (#263)\n\nAdd the draping-related attributes to the Oriented Selection Set\r\nand Modeling Ply.",
          "timestamp": "2023-08-21T11:35:37+02:00",
          "tree_id": "554eb412e228a9adfa3c45d130b6829cddf1aaed",
          "url": "https://github.com/ansys-internal/pyacp/commit/5a47434920bd102c2de5755a71782a12fe7c3a09"
        },
        "date": 1692610886726,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.995989833867999,
            "unit": "iter/sec",
            "range": "stddev: 0.010832184490155262",
            "extra": "mean: 200.16053540000485 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.185913270148789,
            "unit": "iter/sec",
            "range": "stddev: 0.006852914642207386",
            "extra": "mean: 457.4746919999863 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37211306959264223,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.687355219999972 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041073303231506764,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.346714808 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.018015554936674,
            "unit": "iter/sec",
            "range": "stddev: 0.00494581953897119",
            "extra": "mean: 331.34355400000004 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6598209068698916,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5155627679999952 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07596418840563623,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.164097728000002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 939.7230132292243,
            "unit": "iter/sec",
            "range": "stddev: 0.000499184755108304",
            "extra": "mean: 1.0641433549271528 msec\nrounds: 1096"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 342.8345153180938,
            "unit": "iter/sec",
            "range": "stddev: 0.0004737880353779596",
            "extra": "mean: 2.9168591705889506 msec\nrounds: 340"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.879425180848905,
            "unit": "iter/sec",
            "range": "stddev: 0.00021514738916883386",
            "extra": "mean: 21.331319574466928 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.958575795003995,
            "unit": "iter/sec",
            "range": "stddev: 0.00028096301336343846",
            "extra": "mean: 201.670810600001 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 757.8358368393779,
            "unit": "iter/sec",
            "range": "stddev: 0.00041088848407408473",
            "extra": "mean: 1.3195469934103268 msec\nrounds: 759"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.22249155179472,
            "unit": "iter/sec",
            "range": "stddev: 0.0003729374216347032",
            "extra": "mean: 4.849131597989837 msec\nrounds: 199"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.59688015431381,
            "unit": "iter/sec",
            "range": "stddev: 0.00016731187238464687",
            "extra": "mean: 39.067261086952094 msec\nrounds: 23"
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
          "id": "93785bf164c2425d0f9b5de75123dc7ab01f60e9",
          "message": "Add Sensor class (#265)\n\nSensor attributes which are not set in the API message are exposed as ``None``.\r\n\r\nTo enable this, the ``check_optional`` flag is added to ``grpc_read_only_property``.\r\n\r\nAdd a ``doc`` parameter to grpc property helpers, to set the resulting property's\r\ndocstring.",
          "timestamp": "2023-08-21T10:01:50Z",
          "tree_id": "863ebb0d6f7afeebc1eb013e02b38b0d651fd5cc",
          "url": "https://github.com/ansys-internal/pyacp/commit/93785bf164c2425d0f9b5de75123dc7ab01f60e9"
        },
        "date": 1692612447629,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.550732598010478,
            "unit": "iter/sec",
            "range": "stddev: 0.006754870860306999",
            "extra": "mean: 180.15639960001408 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.271530145365294,
            "unit": "iter/sec",
            "range": "stddev: 0.005089318547846728",
            "extra": "mean: 440.2318859999923 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.368144238429606,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.7163266340000405 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041012096107461884,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.383050244000003 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.231903876146,
            "unit": "iter/sec",
            "range": "stddev: 0.004981950391464395",
            "extra": "mean: 309.4151430000096 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6461470038348199,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5476354360000073 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07569051994333786,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.211694156000021 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 991.8718416933295,
            "unit": "iter/sec",
            "range": "stddev: 0.0005333444886519283",
            "extra": "mean: 1.0081947666674296 msec\nrounds: 1050"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 352.17581514370244,
            "unit": "iter/sec",
            "range": "stddev: 0.00010393392891462237",
            "extra": "mean: 2.8394908366775793 msec\nrounds: 349"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.050039748267345,
            "unit": "iter/sec",
            "range": "stddev: 0.00016820998466116324",
            "extra": "mean: 21.253967166665905 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.954820907408641,
            "unit": "iter/sec",
            "range": "stddev: 0.00011722041802687137",
            "extra": "mean: 201.8236418000015 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 792.8865075257619,
            "unit": "iter/sec",
            "range": "stddev: 0.0002852905049020462",
            "extra": "mean: 1.261214550264634 msec\nrounds: 756"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.30086945924344,
            "unit": "iter/sec",
            "range": "stddev: 0.0005415424639612916",
            "extra": "mean: 4.823906443849267 msec\nrounds: 187"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.51366372141737,
            "unit": "iter/sec",
            "range": "stddev: 0.00021956875515448648",
            "extra": "mean: 39.19468449999805 msec\nrounds: 26"
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
          "id": "a9479e43750c8a657736d528dd76bfa313acc6a9",
          "message": "Expose server version (#270)\n\nAdd ``server_version`` property to the `Client` class.",
          "timestamp": "2023-08-22T17:06:25+02:00",
          "tree_id": "7ffd1913235977c67f494cd7a5c01c761cf71df8",
          "url": "https://github.com/ansys-internal/pyacp/commit/a9479e43750c8a657736d528dd76bfa313acc6a9"
        },
        "date": 1692717182533,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.228266564512017,
            "unit": "iter/sec",
            "range": "stddev: 0.009261258844354992",
            "extra": "mean: 236.50353749998487 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 1.9942796541086463,
            "unit": "iter/sec",
            "range": "stddev: 0.005350235071507674",
            "extra": "mean: 501.4341884999851 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3657288494634019,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.734266114000036 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04107325087333754,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.346745843999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.6496877080717245,
            "unit": "iter/sec",
            "range": "stddev: 0.006389013043319874",
            "extra": "mean: 377.40296599999584 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6422574224190654,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5570080859999962 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07605336160423767,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.148662714000011 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 797.9426444703388,
            "unit": "iter/sec",
            "range": "stddev: 0.0004491947165536322",
            "extra": "mean: 1.2532229063453348 msec\nrounds: 993"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 319.40569523805556,
            "unit": "iter/sec",
            "range": "stddev: 0.0006954608737566556",
            "extra": "mean: 3.1308145562485734 msec\nrounds: 320"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.61442718068106,
            "unit": "iter/sec",
            "range": "stddev: 0.0002282029546679831",
            "extra": "mean: 21.45258582978879 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.956327282499877,
            "unit": "iter/sec",
            "range": "stddev: 0.00021436833403609446",
            "extra": "mean: 201.76230159999022 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 608.0996382246899,
            "unit": "iter/sec",
            "range": "stddev: 0.0007536332295849782",
            "extra": "mean: 1.644467349001291 msec\nrounds: 702"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.16753227958017,
            "unit": "iter/sec",
            "range": "stddev: 0.00020531023855556056",
            "extra": "mean: 4.850424259062855 msec\nrounds: 193"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.44550980429878,
            "unit": "iter/sec",
            "range": "stddev: 0.0002212382015442384",
            "extra": "mean: 39.29966456522162 msec\nrounds: 23"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "Dominik Gresch",
            "username": "greschd",
            "email": "greschd@users.noreply.github.com"
          },
          "committer": {
            "name": "GitHub",
            "username": "web-flow",
            "email": "noreply@github.com"
          },
          "id": "a9479e43750c8a657736d528dd76bfa313acc6a9",
          "message": "Expose server version (#270)\n\nAdd ``server_version`` property to the `Client` class.",
          "timestamp": "2023-08-22T15:06:25Z",
          "url": "https://github.com/ansys-internal/pyacp/commit/a9479e43750c8a657736d528dd76bfa313acc6a9"
        },
        "date": 1692887636279,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.771116684049111,
            "unit": "iter/sec",
            "range": "stddev: 0.009691320792307851",
            "extra": "mean: 209.59453859999257 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2274895717625536,
            "unit": "iter/sec",
            "range": "stddev: 0.011155711847227419",
            "extra": "mean: 448.93588399999845 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38033001109554104,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.629295534999983 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04115933357744689,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.295825833000038 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.860411465669899,
            "unit": "iter/sec",
            "range": "stddev: 0.020702139503693533",
            "extra": "mean: 349.60005299999847 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6752302094257661,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4809763929999917 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07607229199903359,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.145390703000032 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 905.9024463165707,
            "unit": "iter/sec",
            "range": "stddev: 0.0004510704483580152",
            "extra": "mean: 1.1038716189210362 msec\nrounds: 1131"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 345.01656894745895,
            "unit": "iter/sec",
            "range": "stddev: 0.0004980064667547352",
            "extra": "mean: 2.898411525715119 msec\nrounds: 350"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.861737443645936,
            "unit": "iter/sec",
            "range": "stddev: 0.00017491046152763275",
            "extra": "mean: 20.893516479159047 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.967757085604176,
            "unit": "iter/sec",
            "range": "stddev: 0.00005094166364113204",
            "extra": "mean: 201.29808740001636 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 763.1813092728212,
            "unit": "iter/sec",
            "range": "stddev: 0.00030207338171171484",
            "extra": "mean: 1.310304625977837 msec\nrounds: 639"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.95701631860726,
            "unit": "iter/sec",
            "range": "stddev: 0.00033270128786616225",
            "extra": "mean: 4.673835975123536 msec\nrounds: 201"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.904045406078353,
            "unit": "iter/sec",
            "range": "stddev: 0.00016995572175252494",
            "extra": "mean: 38.60400892307544 msec\nrounds: 26"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "Dominik Gresch",
            "username": "greschd",
            "email": "greschd@users.noreply.github.com"
          },
          "committer": {
            "name": "GitHub",
            "username": "web-flow",
            "email": "noreply@github.com"
          },
          "id": "a9479e43750c8a657736d528dd76bfa313acc6a9",
          "message": "Expose server version (#270)\n\nAdd ``server_version`` property to the `Client` class.",
          "timestamp": "2023-08-22T15:06:25Z",
          "url": "https://github.com/ansys-internal/pyacp/commit/a9479e43750c8a657736d528dd76bfa313acc6a9"
        },
        "date": 1692974411804,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.296495645680704,
            "unit": "iter/sec",
            "range": "stddev: 0.003659697285627117",
            "extra": "mean: 158.8185009999942 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.467379935706873,
            "unit": "iter/sec",
            "range": "stddev: 0.0036114392119748345",
            "extra": "mean: 405.2882110000269 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3746524043834529,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6691407509999863 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041165760336423,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.292032791999986 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4336341769715215,
            "unit": "iter/sec",
            "range": "stddev: 0.007893192081946962",
            "extra": "mean: 291.2366165000151 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6658913334290318,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5017465309999807 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07624650102147726,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.115355938999983 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1163.7016833690957,
            "unit": "iter/sec",
            "range": "stddev: 0.00023990677596391486",
            "extra": "mean: 859.3267624266435 usec\nrounds: 1187"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 366.66812129316133,
            "unit": "iter/sec",
            "range": "stddev: 0.00017775160710258543",
            "extra": "mean: 2.7272619077797393 msec\nrounds: 347"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.891833527138736,
            "unit": "iter/sec",
            "range": "stddev: 0.00011748599853609875",
            "extra": "mean: 21.325674958332524 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9649175648023,
            "unit": "iter/sec",
            "range": "stddev: 0.000070965364079293",
            "extra": "mean: 201.41321320000998 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 883.6099387430587,
            "unit": "iter/sec",
            "range": "stddev: 0.00014931307992986713",
            "extra": "mean: 1.1317210865945069 msec\nrounds: 843"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 208.3358079886941,
            "unit": "iter/sec",
            "range": "stddev: 0.00013836710918954808",
            "extra": "mean: 4.799942984617736 msec\nrounds: 195"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.553760908377914,
            "unit": "iter/sec",
            "range": "stddev: 0.0001560939903328282",
            "extra": "mean: 39.13318292307203 msec\nrounds: 26"
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
          "id": "97fc7956913990b0c2b99a736636e37e5c3bf8c9",
          "message": "Bump the dependencies group with 1 update (#274)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.82.6...hypothesis-python-6.82.7)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-08-29T11:46:09+02:00",
          "tree_id": "9d07fb5ac992f90ead8032fcc0c197cf7a20e9e9",
          "url": "https://github.com/ansys-internal/pyacp/commit/97fc7956913990b0c2b99a736636e37e5c3bf8c9"
        },
        "date": 1693302683558,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.706510747475003,
            "unit": "iter/sec",
            "range": "stddev: 0.003926164468153879",
            "extra": "mean: 149.10883433333785 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.467495825539914,
            "unit": "iter/sec",
            "range": "stddev: 0.012688435370691963",
            "extra": "mean: 405.26917599999973 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38809956246873856,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.576658406000007 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04125474474088705,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.23963610199999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.5361809896498584,
            "unit": "iter/sec",
            "range": "stddev: 0.010599772193070863",
            "extra": "mean: 282.7909552500074 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6889465557212204,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4514913989999627 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07668807989961092,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.03983619500002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1099.989258259555,
            "unit": "iter/sec",
            "range": "stddev: 0.0004325686404721118",
            "extra": "mean: 909.0997866490425 usec\nrounds: 1528"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 358.48887932969825,
            "unit": "iter/sec",
            "range": "stddev: 0.00027734573873389407",
            "extra": "mean: 2.7894868088231854 msec\nrounds: 340"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.11384828395025,
            "unit": "iter/sec",
            "range": "stddev: 0.00021854740782351208",
            "extra": "mean: 20.78403693877005 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.969993035856839,
            "unit": "iter/sec",
            "range": "stddev: 0.000182929415434605",
            "extra": "mean: 201.2075254000024 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 928.6132781138355,
            "unit": "iter/sec",
            "range": "stddev: 0.0001511458357955424",
            "extra": "mean: 1.0768745435464402 msec\nrounds: 953"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 227.60181338263044,
            "unit": "iter/sec",
            "range": "stddev: 0.0001498115094183623",
            "extra": "mean: 4.393638104802181 msec\nrounds: 229"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.993494964220993,
            "unit": "iter/sec",
            "range": "stddev: 0.00018268093023477547",
            "extra": "mean: 38.47116370370588 msec\nrounds: 27"
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
          "id": "936de49ae3060c9f56fbd4edf9eb4fb1752702b6",
          "message": "Bump the dependencies group with 1 update (#275)\n\nBumps the dependencies group with 1 update: [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme).\r\n\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.10.4...v0.10.5)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-08-30T08:16:12+02:00",
          "tree_id": "d6cf5bb4b5756c2e569cffdbe0662c5a2489e77a",
          "url": "https://github.com/ansys-internal/pyacp/commit/936de49ae3060c9f56fbd4edf9eb4fb1752702b6"
        },
        "date": 1693376481141,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.51861100489446,
            "unit": "iter/sec",
            "range": "stddev: 0.0022636336277804263",
            "extra": "mean: 153.40691433330753 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5409188986558804,
            "unit": "iter/sec",
            "range": "stddev: 0.004674664360030178",
            "extra": "mean: 393.55840933332803 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3834783687446994,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6077090169999906 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041249667904337754,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.24261941499998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.492680132225107,
            "unit": "iter/sec",
            "range": "stddev: 0.011347784403773858",
            "extra": "mean: 286.3130782500036 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6860603110130785,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4575978000000305 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0767084276656725,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.036377232999996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1216.1267099360562,
            "unit": "iter/sec",
            "range": "stddev: 0.00023553584635552233",
            "extra": "mean: 822.2827373412265 usec\nrounds: 1264"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 382.3974484720817,
            "unit": "iter/sec",
            "range": "stddev: 0.00008129310569625616",
            "extra": "mean: 2.6150802103822315 msec\nrounds: 366"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.74594948456387,
            "unit": "iter/sec",
            "range": "stddev: 0.00014086772146222208",
            "extra": "mean: 20.944185020831913 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974172163175533,
            "unit": "iter/sec",
            "range": "stddev: 0.00007741056173513667",
            "extra": "mean: 201.0384778000116 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 946.0397338087599,
            "unit": "iter/sec",
            "range": "stddev: 0.00014126165454016014",
            "extra": "mean: 1.0570380548119218 msec\nrounds: 821"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 227.9548151481226,
            "unit": "iter/sec",
            "range": "stddev: 0.0000877683205536442",
            "extra": "mean: 4.386834291481014 msec\nrounds: 223"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.8499795403414,
            "unit": "iter/sec",
            "range": "stddev: 0.00011002621920824018",
            "extra": "mean: 38.68475015384066 msec\nrounds: 26"
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
          "id": "943c5ff03c8bd609b7e065397270feaa213d6b47",
          "message": "Bump actions/checkout from 3 to 4 (#277)\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.\r\n- [Release notes](https://github.com/actions/checkout/releases)\r\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/actions/checkout/compare/v3...v4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: actions/checkout\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-05T06:59:26+02:00",
          "tree_id": "7e105f9bb5d157c65566378dd18037a281790298",
          "url": "https://github.com/ansys-internal/pyacp/commit/943c5ff03c8bd609b7e065397270feaa213d6b47"
        },
        "date": 1693890274342,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.151812383601388,
            "unit": "iter/sec",
            "range": "stddev: 0.005795191642584279",
            "extra": "mean: 162.5537219999842 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.413888720077515,
            "unit": "iter/sec",
            "range": "stddev: 0.005429328821557935",
            "extra": "mean: 414.2693040000154 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37768053619386943,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6477403630000254 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04117715900687269,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.28530826599996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4540291431289876,
            "unit": "iter/sec",
            "range": "stddev: 0.0010622070889680733",
            "extra": "mean: 289.5169550000105 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6743643182137753,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4828779829999803 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07626223204801198,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.112650562999988 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1146.481869356097,
            "unit": "iter/sec",
            "range": "stddev: 0.0003033397299380542",
            "extra": "mean: 872.2335928100057 usec\nrounds: 1196"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 366.4924998869267,
            "unit": "iter/sec",
            "range": "stddev: 0.00011747692802074289",
            "extra": "mean: 2.7285687982933573 msec\nrounds: 352"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.086658392052954,
            "unit": "iter/sec",
            "range": "stddev: 0.00012500818910561015",
            "extra": "mean: 21.237438249998537 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.966798980237564,
            "unit": "iter/sec",
            "range": "stddev: 0.00008391025231944432",
            "extra": "mean: 201.33691820001332 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 889.1209472181524,
            "unit": "iter/sec",
            "range": "stddev: 0.00014936804414419994",
            "extra": "mean: 1.1247063778316795 msec\nrounds: 839"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 214.81867688978545,
            "unit": "iter/sec",
            "range": "stddev: 0.00011732868880553583",
            "extra": "mean: 4.65508872169927 msec\nrounds: 212"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.660520373620617,
            "unit": "iter/sec",
            "range": "stddev: 0.00011203280515416475",
            "extra": "mean: 38.97037103846165 msec\nrounds: 26"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "105842014+roosre@users.noreply.github.com",
            "name": "René Roos",
            "username": "roosre"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "73a4d65a3c14dd19afbaa3874db51a6d8bdc5e05",
          "message": "add property use_default_draping_mesh_size to the OSS and MP (#279)\n\n* add property use_default_draping_mesh_size to the OrientedSelectionSet and ModelingPly.\r\nUpdate default of draping_mesh_size.\r\n\r\n* update reference to ansys-api-acp in poetry.lock",
          "timestamp": "2023-09-07T09:12:58+02:00",
          "tree_id": "74b2e27a9b2c5770b2a9d40f07018c01a58c1ff2",
          "url": "https://github.com/ansys-internal/pyacp/commit/73a4d65a3c14dd19afbaa3874db51a6d8bdc5e05"
        },
        "date": 1694071126054,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.277076283421014,
            "unit": "iter/sec",
            "range": "stddev: 0.0033682768497189843",
            "extra": "mean: 189.49887140000214 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.262393357441723,
            "unit": "iter/sec",
            "range": "stddev: 0.003064270064992723",
            "extra": "mean: 442.0097843333413 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3745382015137616,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.669954615999984 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04108696495842045,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.33861934099997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.1036997483180855,
            "unit": "iter/sec",
            "range": "stddev: 0.00254565072034434",
            "extra": "mean: 322.1961146666672 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6586587805942663,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5182368010000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07665627650400596,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.045246202999977 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 992.5920897782223,
            "unit": "iter/sec",
            "range": "stddev: 0.00037944498103213085",
            "extra": "mean: 1.0074631969144876 msec\nrounds: 1102"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 349.1904377084615,
            "unit": "iter/sec",
            "range": "stddev: 0.00013778319867373384",
            "extra": "mean: 2.86376685043964 msec\nrounds: 341"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.5240886537891,
            "unit": "iter/sec",
            "range": "stddev: 0.00014329052952286871",
            "extra": "mean: 21.49424156250627 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.960100145929987,
            "unit": "iter/sec",
            "range": "stddev: 0.00014609150646335896",
            "extra": "mean: 201.6088325999931 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 815.187892865194,
            "unit": "iter/sec",
            "range": "stddev: 0.00019026540138272435",
            "extra": "mean: 1.226711054901999 msec\nrounds: 765"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 208.4380302350557,
            "unit": "iter/sec",
            "range": "stddev: 0.0003547195336277548",
            "extra": "mean: 4.797588995023122 msec\nrounds: 201"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.49297203814344,
            "unit": "iter/sec",
            "range": "stddev: 0.00018132019653717098",
            "extra": "mean: 39.22649734616138 msec\nrounds: 26"
          }
        ]
      }
    ]
  }
}