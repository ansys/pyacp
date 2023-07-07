window.BENCHMARK_DATA = {
  "lastUpdate": 1688715528287,
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
      }
    ]
  }
}