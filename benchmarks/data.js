window.BENCHMARK_DATA = {
  "lastUpdate": 1725866563251,
  "repoUrl": "https://github.com/ansys/pyacp",
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
          "id": "568a10f26f9a0fe467d3299e8850b38e23412ff9",
          "message": "Bump docker/login-action from 2 to 3 (#280)\n\nBumps [docker/login-action](https://github.com/docker/login-action) from 2 to 3.\r\n- [Release notes](https://github.com/docker/login-action/releases)\r\n- [Commits](https://github.com/docker/login-action/compare/v2...v3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: docker/login-action\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-13T08:24:10+02:00",
          "tree_id": "706503eecd9308dc93b47ddcf564378e2dac1550",
          "url": "https://github.com/ansys-internal/pyacp/commit/568a10f26f9a0fe467d3299e8850b38e23412ff9"
        },
        "date": 1694586569768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.365775695406556,
            "unit": "iter/sec",
            "range": "stddev: 0.003800473488441932",
            "extra": "mean: 157.09004650000225 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.464283425582438,
            "unit": "iter/sec",
            "range": "stddev: 0.003976137133113232",
            "extra": "mean: 405.7974783333407 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3818745271963739,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6186611800000037 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04119863817225857,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.27264697000004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.372482458707085,
            "unit": "iter/sec",
            "range": "stddev: 0.004724302759347985",
            "extra": "mean: 296.51747999999145 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6793491349416687,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4719971640000153 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07698228083307022,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.99000223400003 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1121.946740921618,
            "unit": "iter/sec",
            "range": "stddev: 0.00027818300320676205",
            "extra": "mean: 891.3079057376241 usec\nrounds: 1220"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 362.307916290767,
            "unit": "iter/sec",
            "range": "stddev: 0.00022691229865675296",
            "extra": "mean: 2.760083219372604 msec\nrounds: 351"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.209281245868915,
            "unit": "iter/sec",
            "range": "stddev: 0.0003500615200209108",
            "extra": "mean: 21.182275468078764 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.965429512855549,
            "unit": "iter/sec",
            "range": "stddev: 0.00006837932364603493",
            "extra": "mean: 201.39244700000063 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 877.7039364581318,
            "unit": "iter/sec",
            "range": "stddev: 0.00023547639747280205",
            "extra": "mean: 1.1393363507464478 msec\nrounds: 804"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.9717559106594,
            "unit": "iter/sec",
            "range": "stddev: 0.00015273529781353182",
            "extra": "mean: 4.673514014707318 msec\nrounds: 204"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.621407753605784,
            "unit": "iter/sec",
            "range": "stddev: 0.00013415378466398093",
            "extra": "mean: 39.02986165384557 msec\nrounds: 26"
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
          "id": "e17b73a852a2b982f4303245b587c9ed90250ec6",
          "message": "Bump the dependencies group with 7 updates (#281)\n\nBumps the dependencies group with 7 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [ansys-dpf-composites](https://github.com/ansys/pydpf-composites) | `0.3.0` | `0.3.1` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.42.0` | `0.42.2` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.1` | `0.10.2` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.10.5` | `0.11.2` |\r\n| [ipykernel](https://github.com/ipython/ipykernel) | `6.25.1` | `6.25.2` |\r\n| [pytest](https://github.com/pytest-dev/pytest) | `7.4.1` | `7.4.2` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.83.1` | `6.86.1` |\r\n\r\n\r\nUpdates `ansys-dpf-composites` from 0.3.0 to 0.3.1\r\n- [Release notes](https://github.com/ansys/pydpf-composites/releases)\r\n- [Commits](https://github.com/ansys/pydpf-composites/compare/v0.3.0...v0.3.1)\r\n\r\nUpdates `pyvista` from 0.42.0 to 0.42.2\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.42.0...v0.42.2)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.1 to 0.10.2\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.1...v0.10.2)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.10.5 to 0.11.2\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.10.5...v0.11.2)\r\n\r\nUpdates `ipykernel` from 6.25.1 to 6.25.2\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.25.1...v6.25.2)\r\n\r\nUpdates `pytest` from 7.4.1 to 7.4.2\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.1...7.4.2)\r\n\r\nUpdates `hypothesis` from 6.83.1 to 6.86.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.83.1...hypothesis-python-6.86.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-dpf-composites\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-18T10:29:58+02:00",
          "tree_id": "426ab3826e134abb0aec779cc38b747a2f183b9d",
          "url": "https://github.com/ansys-internal/pyacp/commit/e17b73a852a2b982f4303245b587c9ed90250ec6"
        },
        "date": 1695026180459,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.377500616447743,
            "unit": "iter/sec",
            "range": "stddev: 0.0017473511006550813",
            "extra": "mean: 228.4408587500053 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.0649396361616947,
            "unit": "iter/sec",
            "range": "stddev: 0.012769729749800974",
            "extra": "mean: 484.27565749999246 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3704827200785296,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.699181218999996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041096101401721256,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.333208404000004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.780793177205988,
            "unit": "iter/sec",
            "range": "stddev: 0.011574303247163131",
            "extra": "mean: 359.6096280000059 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6562797580006797,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5237404290000427 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07667210585358321,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.042552944999954 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 870.3657138749553,
            "unit": "iter/sec",
            "range": "stddev: 0.00028644597549313405",
            "extra": "mean: 1.1489423170725555 msec\nrounds: 902"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 324.55777415216545,
            "unit": "iter/sec",
            "range": "stddev: 0.00013214907253882304",
            "extra": "mean: 3.0811155351686645 msec\nrounds: 327"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.57771410233349,
            "unit": "iter/sec",
            "range": "stddev: 0.00015941086551448055",
            "extra": "mean: 21.01824391666085 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964531904642935,
            "unit": "iter/sec",
            "range": "stddev: 0.00006133031926400085",
            "extra": "mean: 201.42885959999148 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 671.7681636707617,
            "unit": "iter/sec",
            "range": "stddev: 0.0002599396904016717",
            "extra": "mean: 1.4886087999997972 msec\nrounds: 780"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.38888706970857,
            "unit": "iter/sec",
            "range": "stddev: 0.00019350685761370347",
            "extra": "mean: 4.84522211538573 msec\nrounds: 182"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.669367305914843,
            "unit": "iter/sec",
            "range": "stddev: 0.0002336221951756861",
            "extra": "mean: 38.95693992308006 msec\nrounds: 26"
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
          "id": "c29cbb926cf7a55a37a82bec9d912bf8f7382a90",
          "message": "Bump the dependencies group with 3 updates (#282)\n\nBumps the dependencies group with 3 updates: [typing-extensions](https://github.com/python/typing_extensions), [ansys-mapdl-core](https://github.com/ansys/pymapdl) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `typing-extensions` from 4.7.1 to 4.8.0\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.7.1...4.8.0)\r\n\r\nUpdates `ansys-mapdl-core` from 0.65.2 to 0.66.0\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.65.2...v0.66.0)\r\n\r\nUpdates `hypothesis` from 6.86.1 to 6.86.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.86.1...hypothesis-python-6.86.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-19T08:15:00+02:00",
          "tree_id": "37b3039c22937cd9344a6e057060c381a52c7876",
          "url": "https://github.com/ansys-internal/pyacp/commit/c29cbb926cf7a55a37a82bec9d912bf8f7382a90"
        },
        "date": 1695104408781,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.241828847862821,
            "unit": "iter/sec",
            "range": "stddev: 0.003609786710328837",
            "extra": "mean: 160.20945533333494 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.381706298739778,
            "unit": "iter/sec",
            "range": "stddev: 0.012393366291523471",
            "extra": "mean: 419.8670510000018 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3758380119346599,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6607207579999965 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041142304779720834,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.305881873999994 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3254939413933133,
            "unit": "iter/sec",
            "range": "stddev: 0.007007721029858604",
            "extra": "mean: 300.7072084999862 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6639798064246373,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5060698990000105 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07684119916751,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.013852084999996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1185.1702489063239,
            "unit": "iter/sec",
            "range": "stddev: 0.0002070052018082173",
            "extra": "mean: 843.760633480971 usec\nrounds: 1135"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 354.5908688306417,
            "unit": "iter/sec",
            "range": "stddev: 0.00024558589301890447",
            "extra": "mean: 2.820151582858768 msec\nrounds: 350"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.01467688608995,
            "unit": "iter/sec",
            "range": "stddev: 0.00016493386979622008",
            "extra": "mean: 21.269953687501914 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9613172001869374,
            "unit": "iter/sec",
            "range": "stddev: 0.00015997108100381974",
            "extra": "mean: 201.55937619999804 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 862.8082706487972,
            "unit": "iter/sec",
            "range": "stddev: 0.00017099292556442395",
            "extra": "mean: 1.1590060434261253 msec\nrounds: 829"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.53153957136422,
            "unit": "iter/sec",
            "range": "stddev: 0.0002138039297022791",
            "extra": "mean: 4.772551197045019 msec\nrounds: 203"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.6123105026661,
            "unit": "iter/sec",
            "range": "stddev: 0.0001346864701962968",
            "extra": "mean: 39.04372469230785 msec\nrounds: 26"
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
          "id": "0e8e025f419ea94c32c046a55c4e4fe7ac1d3041",
          "message": "Bump the dependencies group with 2 updates (#284)\n\nBumps the dependencies group with 2 updates: [types-protobuf](https://github.com/python/typeshed) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `types-protobuf` from 4.24.0.1 to 4.24.0.2\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\nUpdates `hypothesis` from 6.86.2 to 6.87.0\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.86.2...hypothesis-python-6.87.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-25T08:55:21+02:00",
          "tree_id": "e3599e04568b011d08910a6a897c4c53e095af75",
          "url": "https://github.com/ansys-internal/pyacp/commit/0e8e025f419ea94c32c046a55c4e4fe7ac1d3041"
        },
        "date": 1695625236575,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.263280902222521,
            "unit": "iter/sec",
            "range": "stddev: 0.0050617201007694115",
            "extra": "mean: 159.66072983332916 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4271021310960537,
            "unit": "iter/sec",
            "range": "stddev: 0.004956353001791517",
            "extra": "mean: 412.01397633333653 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37525220334715903,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6648744260000115 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04117319897189983,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.28764402500002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.494793058021973,
            "unit": "iter/sec",
            "range": "stddev: 0.006046775643000617",
            "extra": "mean: 286.13997550000647 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6645058747505688,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5048775910000245 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07694586049766776,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.996150715999988 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1174.2415278001029,
            "unit": "iter/sec",
            "range": "stddev: 0.00021712614458161596",
            "extra": "mean: 851.6135533661991 usec\nrounds: 1218"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 368.19283791579153,
            "unit": "iter/sec",
            "range": "stddev: 0.00010316754075332375",
            "extra": "mean: 2.7159680934062806 msec\nrounds: 364"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.204577102127345,
            "unit": "iter/sec",
            "range": "stddev: 0.00016467972050594228",
            "extra": "mean: 21.184386375001196 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.965084458594382,
            "unit": "iter/sec",
            "range": "stddev: 0.00007309124164090062",
            "extra": "mean: 201.40644299998485 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 889.9277616363925,
            "unit": "iter/sec",
            "range": "stddev: 0.0001508412036002914",
            "extra": "mean: 1.123686711560956 msec\nrounds: 839"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.39567999542004,
            "unit": "iter/sec",
            "range": "stddev: 0.00012417795136966282",
            "extra": "mean: 4.6861304784682725 msec\nrounds: 209"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.62443215334154,
            "unit": "iter/sec",
            "range": "stddev: 0.00012787935704023276",
            "extra": "mean: 39.02525503846513 msec\nrounds: 26"
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
          "id": "347ce4f8567de3e81392d3449c5bac54bba3e76e",
          "message": "Bump the dependencies group with 3 updates (#286)\n\nBumps the dependencies group with 3 updates: [ansys-mechanical-core](https://github.com/ansys/pymechanical), [numpydoc](https://github.com/numpy/numpydoc) and [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme).\r\n\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.2 to 0.10.3\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.2...v0.10.3)\r\n\r\nUpdates `numpydoc` from 1.5.0 to 1.6.0\r\n- [Release notes](https://github.com/numpy/numpydoc/releases)\r\n- [Changelog](https://github.com/numpy/numpydoc/blob/main/doc/release_notes.rst)\r\n- [Commits](https://github.com/numpy/numpydoc/compare/v1.5.0...v1.6.0)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.11.2 to 0.12.0\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.11.2...v0.12.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: numpydoc\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-27T08:19:43+02:00",
          "tree_id": "4bd941e2be2411d27a49df2425feffbb102f09fb",
          "url": "https://github.com/ansys-internal/pyacp/commit/347ce4f8567de3e81392d3449c5bac54bba3e76e"
        },
        "date": 1695795918516,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.305648532860562,
            "unit": "iter/sec",
            "range": "stddev: 0.0064207614854599904",
            "extra": "mean: 188.47837239999876 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2100280796149208,
            "unit": "iter/sec",
            "range": "stddev: 0.005512425940361323",
            "extra": "mean: 452.48293866666245 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3716806209602696,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.690481945000016 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04106446419053365,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.35195538800002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.1187420167352555,
            "unit": "iter/sec",
            "range": "stddev: 0.009353547482067735",
            "extra": "mean: 320.6421033333224 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6537584441548996,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.529616954000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07648873429798747,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.073820728999976 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 987.4224838722403,
            "unit": "iter/sec",
            "range": "stddev: 0.0003205439607288912",
            "extra": "mean: 1.012737725070262 msec\nrounds: 1073"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 352.32170476698434,
            "unit": "iter/sec",
            "range": "stddev: 0.00010818656471910835",
            "extra": "mean: 2.838315058282804 msec\nrounds: 326"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.958203562500984,
            "unit": "iter/sec",
            "range": "stddev: 0.00018064038142813217",
            "extra": "mean: 21.295533562501134 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.95819270258539,
            "unit": "iter/sec",
            "range": "stddev: 0.00024121771775285374",
            "extra": "mean: 201.68639259998145 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 812.2314011753642,
            "unit": "iter/sec",
            "range": "stddev: 0.00018687014406452686",
            "extra": "mean: 1.2311762369109587 msec\nrounds: 764"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.5241498036027,
            "unit": "iter/sec",
            "range": "stddev: 0.0003698309410181099",
            "extra": "mean: 4.772719521531762 msec\nrounds: 209"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.36121765269845,
            "unit": "iter/sec",
            "range": "stddev: 0.0007599574729870662",
            "extra": "mean: 39.430283423067394 msec\nrounds: 26"
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
          "id": "83936073ea32a73ca00ca63902896d8ed6e95854",
          "message": "Bump the dependencies group with 1 update (#287)\n\nBumps the dependencies group with 1 update: [ansys-dpf-composites](https://github.com/ansys/pydpf-composites).\r\n\r\n- [Release notes](https://github.com/ansys/pydpf-composites/releases)\r\n- [Commits](https://github.com/ansys/pydpf-composites/compare/v0.3.1...v0.3.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-dpf-composites\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-09-28T08:52:51+02:00",
          "tree_id": "c18a3ecc440941fec044cc03a39b0940047d6eb5",
          "url": "https://github.com/ansys-internal/pyacp/commit/83936073ea32a73ca00ca63902896d8ed6e95854"
        },
        "date": 1695884303117,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.060486485371314,
            "unit": "iter/sec",
            "range": "stddev: 0.006429115299511677",
            "extra": "mean: 165.00325549999673 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4057682663059756,
            "unit": "iter/sec",
            "range": "stddev: 0.005386534189724018",
            "extra": "mean: 415.6676326666684 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3727115641342974,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6830399060000047 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041155507053395435,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.29808479099998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4517247510494826,
            "unit": "iter/sec",
            "range": "stddev: 0.004894750657251584",
            "extra": "mean: 289.7102382500094 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6642474023459572,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5054631699999845 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07697071545474056,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.99195407100001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1178.5267135622532,
            "unit": "iter/sec",
            "range": "stddev: 0.00018968417558302576",
            "extra": "mean: 848.5170412279984 usec\nrounds: 1140"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 365.7446011773898,
            "unit": "iter/sec",
            "range": "stddev: 0.00010698406498366095",
            "extra": "mean: 2.7341483559315476 msec\nrounds: 354"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.7440566108146,
            "unit": "iter/sec",
            "range": "stddev: 0.000140045769329178",
            "extra": "mean: 21.393094063826762 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.963916048301841,
            "unit": "iter/sec",
            "range": "stddev: 0.000091787547812962",
            "extra": "mean: 201.45385020000504 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 880.6876925158227,
            "unit": "iter/sec",
            "range": "stddev: 0.00014178556563480005",
            "extra": "mean: 1.13547629710067 msec\nrounds: 828"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 211.71255072342095,
            "unit": "iter/sec",
            "range": "stddev: 0.00013413525868382706",
            "extra": "mean: 4.723385536582522 msec\nrounds: 205"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.603295347361207,
            "unit": "iter/sec",
            "range": "stddev: 0.0001536824378723755",
            "extra": "mean: 39.05747234615502 msec\nrounds: 26"
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
          "id": "8defd403a1899bd5b86158bc6f213421f24921cd",
          "message": "Bump the dependencies group with 3 updates (#288)\n\nBumps the dependencies group with 3 updates: [packaging](https://github.com/pypa/packaging), [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `packaging` from 23.1 to 23.2\r\n- [Release notes](https://github.com/pypa/packaging/releases)\r\n- [Changelog](https://github.com/pypa/packaging/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pypa/packaging/compare/23.1...23.2)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.12.0 to 0.12.1\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.12.0...v0.12.1)\r\n\r\nUpdates `hypothesis` from 6.87.0 to 6.87.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.87.0...hypothesis-python-6.87.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: packaging\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-02T08:44:58+02:00",
          "tree_id": "120520e0e01d26869102d6de506bdbb051c1e3e9",
          "url": "https://github.com/ansys-internal/pyacp/commit/8defd403a1899bd5b86158bc6f213421f24921cd"
        },
        "date": 1696229447222,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.066064562056675,
            "unit": "iter/sec",
            "range": "stddev: 0.00521411914761952",
            "extra": "mean: 197.39187839999204 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1574387210255868,
            "unit": "iter/sec",
            "range": "stddev: 0.005978679573890867",
            "extra": "mean: 463.512585666687 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.381112697714611,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.623895781999977 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041138539884318405,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.308106286999987 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.9332762632496436,
            "unit": "iter/sec",
            "range": "stddev: 0.004876994937223134",
            "extra": "mean: 340.91572366666395 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6719879366446286,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.488121951999915 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07698715042062702,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.989180590999922 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 941.6880626412942,
            "unit": "iter/sec",
            "range": "stddev: 0.0006052969352322265",
            "extra": "mean: 1.0619227742944406 msec\nrounds: 957"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 325.64170326793794,
            "unit": "iter/sec",
            "range": "stddev: 0.0005281837734043309",
            "extra": "mean: 3.070859751575492 msec\nrounds: 318"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.57547410130699,
            "unit": "iter/sec",
            "range": "stddev: 0.000155179245608829",
            "extra": "mean: 21.01923352083901 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.959763669244123,
            "unit": "iter/sec",
            "range": "stddev: 0.00016607487860105443",
            "extra": "mean: 201.62251000003835 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 710.8974867597504,
            "unit": "iter/sec",
            "range": "stddev: 0.0007167704184381853",
            "extra": "mean: 1.4066725774456879 msec\nrounds: 736"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.54606539149665,
            "unit": "iter/sec",
            "range": "stddev: 0.00015894294682968255",
            "extra": "mean: 4.772220361817301 msec\nrounds: 199"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.7957621449477,
            "unit": "iter/sec",
            "range": "stddev: 0.00029763334501933987",
            "extra": "mean: 38.76605755553757 msec\nrounds: 27"
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
          "id": "613787ee5ec0f7578cf9102d1f2cb90aa4e4e17c",
          "message": "Bump the dependencies group with 1 update (#289)\n\nBumps the dependencies group with 1 update: [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme).\r\n\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.12.1...v0.12.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-05T08:33:07+02:00",
          "tree_id": "8039d972f6a238c0687374107b625607985023b9",
          "url": "https://github.com/ansys-internal/pyacp/commit/613787ee5ec0f7578cf9102d1f2cb90aa4e4e17c"
        },
        "date": 1696487916704,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.012579832179104,
            "unit": "iter/sec",
            "range": "stddev: 0.006000037554302479",
            "extra": "mean: 166.31795799999813 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.422778283039284,
            "unit": "iter/sec",
            "range": "stddev: 0.00342008110203302",
            "extra": "mean: 412.74928333332167 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37575071197169857,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.661338935999993 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041132877604999785,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.311452497999994 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4535667352387778,
            "unit": "iter/sec",
            "range": "stddev: 0.005114390787069724",
            "extra": "mean: 289.5557192500178 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6698243463485221,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4929287140000156 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07663011189430254,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.049700375999976 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1221.8559200497298,
            "unit": "iter/sec",
            "range": "stddev: 0.00017309801977859117",
            "extra": "mean: 818.4271022391083 usec\nrounds: 1027"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 367.118331356602,
            "unit": "iter/sec",
            "range": "stddev: 0.00011550090128777674",
            "extra": "mean: 2.7239173710142124 msec\nrounds: 345"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.71031371151533,
            "unit": "iter/sec",
            "range": "stddev: 0.0001305897446078732",
            "extra": "mean: 21.4085481458343 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962217896238077,
            "unit": "iter/sec",
            "range": "stddev: 0.00012481084389179641",
            "extra": "mean: 201.52279099999078 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 893.8450706198404,
            "unit": "iter/sec",
            "range": "stddev: 0.00014228720188541878",
            "extra": "mean: 1.1187621131104366 msec\nrounds: 778"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 211.49440128801592,
            "unit": "iter/sec",
            "range": "stddev: 0.00012590918470042496",
            "extra": "mean: 4.728257551547129 msec\nrounds: 194"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.52062073664295,
            "unit": "iter/sec",
            "range": "stddev: 0.00011193039782206497",
            "extra": "mean: 39.18399988461811 msec\nrounds: 26"
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
          "id": "6e5d4a64323dd123b3797d0a989d5b4874a7feeb",
          "message": "Bump the dependencies group with 3 updates (#290)\n\nBumps the dependencies group with 3 updates: [pyvista](https://github.com/pyvista/pyvista), [ansys-mechanical-core](https://github.com/ansys/pymechanical) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `pyvista` from 0.42.2 to 0.42.3\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.42.2...v0.42.3)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.3 to 0.10.4\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/v0.10.4/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.3...v0.10.4)\r\n\r\nUpdates `hypothesis` from 6.87.1 to 6.87.3\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.87.1...hypothesis-python-6.87.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-09T17:48:05+02:00",
          "tree_id": "eac631781010d441868b75bc4a461e3677a0d0c6",
          "url": "https://github.com/ansys-internal/pyacp/commit/6e5d4a64323dd123b3797d0a989d5b4874a7feeb"
        },
        "date": 1696866801816,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.6519125988753025,
            "unit": "iter/sec",
            "range": "stddev: 0.004785396342100504",
            "extra": "mean: 150.3327028333293 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4332451757791858,
            "unit": "iter/sec",
            "range": "stddev: 0.022379677086747717",
            "extra": "mean: 410.9737933333311 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38675844933016196,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.5855931570000052 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04128360711956908,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.222689580000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.340133647815663,
            "unit": "iter/sec",
            "range": "stddev: 0.011654297623788605",
            "extra": "mean: 299.3892177500044 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.698218548925769,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4322163190000197 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0772408725982881,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.946513502000016 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1195.4055257225955,
            "unit": "iter/sec",
            "range": "stddev: 0.00021851979350820635",
            "extra": "mean: 836.536203390496 usec\nrounds: 1416"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 387.3477531190164,
            "unit": "iter/sec",
            "range": "stddev: 0.00010055202027536165",
            "extra": "mean: 2.5816594828490986 msec\nrounds: 379"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.335788732207995,
            "unit": "iter/sec",
            "range": "stddev: 0.00010709351290766756",
            "extra": "mean: 20.688604163267986 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974692490652699,
            "unit": "iter/sec",
            "range": "stddev: 0.000023588508462111403",
            "extra": "mean: 201.01745019998134 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 928.0290451251411,
            "unit": "iter/sec",
            "range": "stddev: 0.00014176131082367402",
            "extra": "mean: 1.0775524809842065 msec\nrounds: 894"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 227.58521459797575,
            "unit": "iter/sec",
            "range": "stddev: 0.00013210265159264937",
            "extra": "mean: 4.393958552037214 msec\nrounds: 221"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.83663561899061,
            "unit": "iter/sec",
            "range": "stddev: 0.00012736229502400054",
            "extra": "mean: 38.7047297777801 msec\nrounds: 27"
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
          "id": "d33d782d82ebae36d6e257c95df26484b83dbfb1",
          "message": "Bump the dependencies group with 2 updates (#291)\n\nBumps the dependencies group with 2 updates: [mypy](https://github.com/python/mypy) and [pytest-cases](https://github.com/smarie/python-pytest-cases).\r\n\r\n\r\nUpdates `mypy` from 1.5.1 to 1.6.0\r\n- [Commits](https://github.com/python/mypy/compare/v1.5.1...v1.6.0)\r\n\r\nUpdates `pytest-cases` from 3.6.14 to 3.7.0\r\n- [Release notes](https://github.com/smarie/python-pytest-cases/releases)\r\n- [Changelog](https://github.com/smarie/python-pytest-cases/blob/main/docs/changelog.md)\r\n- [Commits](https://github.com/smarie/python-pytest-cases/compare/3.6.14...3.7.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest-cases\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-11T09:36:37+02:00",
          "tree_id": "98c5526ef0e3c329154c9a0bd4ba027a24b50e14",
          "url": "https://github.com/ansys-internal/pyacp/commit/d33d782d82ebae36d6e257c95df26484b83dbfb1"
        },
        "date": 1697010121990,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.266472984330115,
            "unit": "iter/sec",
            "range": "stddev: 0.00331235406970531",
            "extra": "mean: 159.57940016666328 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.201324261789556,
            "unit": "iter/sec",
            "range": "stddev: 0.00931882472963182",
            "extra": "mean: 454.2720113333303 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3789001527875857,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6392177269999877 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041141985965865185,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.306070223000006 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0735676174455313,
            "unit": "iter/sec",
            "range": "stddev: 0.010256938116506392",
            "extra": "mean: 325.35480733334526 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6693845809295313,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4939095230000135 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07679300454211122,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.022019466000017 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1197.3961114622775,
            "unit": "iter/sec",
            "range": "stddev: 0.00019563727458760948",
            "extra": "mean: 835.1455215423954 usec\nrounds: 1114"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 337.5963182039367,
            "unit": "iter/sec",
            "range": "stddev: 0.00029640667755243607",
            "extra": "mean: 2.9621176123014337 msec\nrounds: 374"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.025591926699875,
            "unit": "iter/sec",
            "range": "stddev: 0.00039674132797848095",
            "extra": "mean: 21.265016750001326 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.957513819034911,
            "unit": "iter/sec",
            "range": "stddev: 0.00010519854470260349",
            "extra": "mean: 201.71401160000642 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 878.2195345386933,
            "unit": "iter/sec",
            "range": "stddev: 0.0001452513896211775",
            "extra": "mean: 1.1386674523532148 msec\nrounds: 871"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 215.17823219662057,
            "unit": "iter/sec",
            "range": "stddev: 0.0001560164256046376",
            "extra": "mean: 4.6473102311122405 msec\nrounds: 225"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.87633404967668,
            "unit": "iter/sec",
            "range": "stddev: 0.00016149986638739808",
            "extra": "mean: 38.64535053845832 msec\nrounds: 26"
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
          "id": "8dfaf6b255d71ba37083a5d614bd2c424e989312",
          "message": "Bump the dependencies group with 2 updates (#292)\n\nBumps the dependencies group with 2 updates: [ansys-mapdl-core](https://github.com/ansys/pymapdl) and [pytest-cases](https://github.com/smarie/python-pytest-cases).\r\n\r\n\r\nUpdates `ansys-mapdl-core` from 0.66.0 to 0.67.0\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.66.0...v0.67.0)\r\n\r\nUpdates `pytest-cases` from 3.7.0 to 3.8.0\r\n- [Release notes](https://github.com/smarie/python-pytest-cases/releases)\r\n- [Changelog](https://github.com/smarie/python-pytest-cases/blob/main/docs/changelog.md)\r\n- [Commits](https://github.com/smarie/python-pytest-cases/compare/3.7.0...3.8.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest-cases\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-12T11:48:59+02:00",
          "tree_id": "eb70ae34180c218f50744b381bb9845a5d408744",
          "url": "https://github.com/ansys-internal/pyacp/commit/8dfaf6b255d71ba37083a5d614bd2c424e989312"
        },
        "date": 1697104467322,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.85093574284496,
            "unit": "iter/sec",
            "range": "stddev: 0.014511368292114248",
            "extra": "mean: 170.91283239999484 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2430855648159858,
            "unit": "iter/sec",
            "range": "stddev: 0.0063403240158688215",
            "extra": "mean: 445.8144689999983 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3733290007656575,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.678602514000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041139713423868914,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.307412881000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.277021501961406,
            "unit": "iter/sec",
            "range": "stddev: 0.01231003036533075",
            "extra": "mean: 305.1551536666655 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.671079806028532,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.490135735000024 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07675031774951989,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.029262018999987 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1064.144817192941,
            "unit": "iter/sec",
            "range": "stddev: 0.0005066697776801788",
            "extra": "mean: 939.7217219342892 usec\nrounds: 1158"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 346.83118777002653,
            "unit": "iter/sec",
            "range": "stddev: 0.0007155804519597275",
            "extra": "mean: 2.8832470529238288 msec\nrounds: 359"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.931312625378425,
            "unit": "iter/sec",
            "range": "stddev: 0.00021375971180070318",
            "extra": "mean: 21.307735583326586 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.961666674325545,
            "unit": "iter/sec",
            "range": "stddev: 0.00017960931932358527",
            "extra": "mean: 201.54517940001142 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 823.987667256462,
            "unit": "iter/sec",
            "range": "stddev: 0.0004899161947217499",
            "extra": "mean: 1.2136103970215795 msec\nrounds: 806"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.9085867006336,
            "unit": "iter/sec",
            "range": "stddev: 0.00023142761142597013",
            "extra": "mean: 4.74139064531978 msec\nrounds: 203"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.5030867136253,
            "unit": "iter/sec",
            "range": "stddev: 0.0005036897971282702",
            "extra": "mean: 39.21093988461166 msec\nrounds: 26"
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
          "id": "3a8e5ee80876a791d4ccbb731bd6f0f7e3b6c265",
          "message": "Bump the dependencies group with 1 update (#294)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.87.3...hypothesis-python-6.87.4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-15T16:35:43+02:00",
          "tree_id": "980af5cc1780b5a111271a0592aa14d16bdbbe24",
          "url": "https://github.com/ansys-internal/pyacp/commit/3a8e5ee80876a791d4ccbb731bd6f0f7e3b6c265"
        },
        "date": 1697380857246,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.145066958242172,
            "unit": "iter/sec",
            "range": "stddev: 0.005471354029683817",
            "extra": "mean: 162.7321568333334 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3659085001417384,
            "unit": "iter/sec",
            "range": "stddev: 0.020116414494639724",
            "extra": "mean: 422.6706146666667 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37966567258208733,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.633896273000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04114467422747199,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.304482141999983 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.393932495823314,
            "unit": "iter/sec",
            "range": "stddev: 0.009627479571576952",
            "extra": "mean: 294.64345599997444 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6796789197598545,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4712829410000268 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07683147543572463,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.015499108000029 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1130.5795197679288,
            "unit": "iter/sec",
            "range": "stddev: 0.00021008494478539372",
            "extra": "mean: 884.5021358650364 usec\nrounds: 1369"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 352.67648262658906,
            "unit": "iter/sec",
            "range": "stddev: 0.00022041603089517737",
            "extra": "mean: 2.8354598314931927 msec\nrounds: 362"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.252264435579356,
            "unit": "iter/sec",
            "range": "stddev: 0.00020964347716870242",
            "extra": "mean: 21.16300693617201 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964020309216755,
            "unit": "iter/sec",
            "range": "stddev: 0.00010744057148313955",
            "extra": "mean: 201.44961900000453 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 879.2629902676988,
            "unit": "iter/sec",
            "range": "stddev: 0.00016702210538834086",
            "extra": "mean: 1.1373161512183538 msec\nrounds: 820"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 208.0102239053071,
            "unit": "iter/sec",
            "range": "stddev: 0.00021743807317625634",
            "extra": "mean: 4.807456004928065 msec\nrounds: 203"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.648687566718642,
            "unit": "iter/sec",
            "range": "stddev: 0.00011808082109043644",
            "extra": "mean: 38.98834969230883 msec\nrounds: 26"
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
          "id": "d307a8d8d7a25c39ef420779cb992086e1144d1c",
          "message": "Bump the dependencies group with 1 update (#295)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.87.4...hypothesis-python-6.88.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-16T08:44:27+02:00",
          "tree_id": "0fa57c73eb9ae75249cfe2be37f08f64f66a21d2",
          "url": "https://github.com/ansys-internal/pyacp/commit/d307a8d8d7a25c39ef420779cb992086e1144d1c"
        },
        "date": 1697438977135,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.351494096889752,
            "unit": "iter/sec",
            "range": "stddev: 0.002373920565168903",
            "extra": "mean: 157.44326999999694 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4339328007054437,
            "unit": "iter/sec",
            "range": "stddev: 0.0041955764075797194",
            "extra": "mean: 410.85768666668326 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3803599152503013,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.629088818000014 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04117305823758467,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.287727043000018 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4964456278835434,
            "unit": "iter/sec",
            "range": "stddev: 0.004444693134283809",
            "extra": "mean: 286.0047334999791 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6817979694525083,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4667101470000148 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07693947761437275,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.997228873999973 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1128.4350309166337,
            "unit": "iter/sec",
            "range": "stddev: 0.00021525661461205948",
            "extra": "mean: 886.183052282323 usec\nrounds: 1358"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 364.1262549202041,
            "unit": "iter/sec",
            "range": "stddev: 0.0002842203324152126",
            "extra": "mean: 2.746300181565165 msec\nrounds: 358"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.37523029136331,
            "unit": "iter/sec",
            "range": "stddev: 0.00014541601075767575",
            "extra": "mean: 21.10807681250056 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.967256698213189,
            "unit": "iter/sec",
            "range": "stddev: 0.00006568217772564042",
            "extra": "mean: 201.31836560001375 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 882.1203041777077,
            "unit": "iter/sec",
            "range": "stddev: 0.00014225245005162373",
            "extra": "mean: 1.1336322214373888 msec\nrounds: 849"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.51477739809093,
            "unit": "iter/sec",
            "range": "stddev: 0.00018861606281799667",
            "extra": "mean: 4.683516579911163 msec\nrounds: 219"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.71150948438453,
            "unit": "iter/sec",
            "range": "stddev: 0.00015045741122642908",
            "extra": "mean: 38.89308796153465 msec\nrounds: 26"
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
          "id": "937c71ffb5a87afcc3db98eb35cb2a65ad083b01",
          "message": "Bump the dependencies group with 2 updates (#297)\n\nBumps the dependencies group with 2 updates: [pypandoc](https://github.com/JessicaTegner/pypandoc) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `pypandoc` from 1.11 to 1.12\r\n- [Release notes](https://github.com/JessicaTegner/pypandoc/releases)\r\n- [Changelog](https://github.com/JessicaTegner/pypandoc/blob/master/release.md)\r\n- [Commits](https://github.com/JessicaTegner/pypandoc/compare/v1.11...v1.12)\r\n\r\nUpdates `hypothesis` from 6.88.0 to 6.88.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.88.0...hypothesis-python-6.88.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pypandoc\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-17T07:54:40+02:00",
          "tree_id": "83ef632ee0b3d3963fb2e6bef1a67ff361616436",
          "url": "https://github.com/ansys-internal/pyacp/commit/937c71ffb5a87afcc3db98eb35cb2a65ad083b01"
        },
        "date": 1697522396009,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.66177808238752,
            "unit": "iter/sec",
            "range": "stddev: 0.008960412431077987",
            "extra": "mean: 176.62295933335295 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3456431484273574,
            "unit": "iter/sec",
            "range": "stddev: 0.006119071364179832",
            "extra": "mean: 426.32230766664253 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.36941641759867455,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.706972273999952 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04108427266843229,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.340214273000015 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3872011361823664,
            "unit": "iter/sec",
            "range": "stddev: 0.006051501617139401",
            "extra": "mean: 295.2289987500052 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6603803502627542,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.514278853999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07656067960224643,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.061535048999986 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1229.061642570846,
            "unit": "iter/sec",
            "range": "stddev: 0.00018096668791661865",
            "extra": "mean: 813.6288411932583 usec\nrounds: 1039"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 369.08875726126394,
            "unit": "iter/sec",
            "range": "stddev: 0.00025024530719732575",
            "extra": "mean: 2.7093754017875376 msec\nrounds: 336"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.736989458379,
            "unit": "iter/sec",
            "range": "stddev: 0.0004647150351022253",
            "extra": "mean: 21.396328937501135 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.955495640155533,
            "unit": "iter/sec",
            "range": "stddev: 0.00013783831314045008",
            "extra": "mean: 201.79616179999584 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 901.9885975308811,
            "unit": "iter/sec",
            "range": "stddev: 0.00014953199215339164",
            "extra": "mean: 1.1086614650533464 msec\nrounds: 744"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 211.5400239620599,
            "unit": "iter/sec",
            "range": "stddev: 0.0002362265603657839",
            "extra": "mean: 4.727237811882596 msec\nrounds: 202"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.456430718641656,
            "unit": "iter/sec",
            "range": "stddev: 0.0002962658015750401",
            "extra": "mean: 39.28280484615243 msec\nrounds: 26"
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
          "id": "a1c08f4ad9ef09a5524cf6666d4bf1c1508be06f",
          "message": "Bump the dependencies group with 1 update (#298)\n\nBumps the dependencies group with 1 update: [mypy](https://github.com/python/mypy).\r\n\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.6.0...v1.6.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-19T09:20:19+02:00",
          "tree_id": "05a86721f0df75101694828d3625224a2f2f2d02",
          "url": "https://github.com/ansys-internal/pyacp/commit/a1c08f4ad9ef09a5524cf6666d4bf1c1508be06f"
        },
        "date": 1697700380099,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.659436193962544,
            "unit": "iter/sec",
            "range": "stddev: 0.01259001606683301",
            "extra": "mean: 214.61824100000513 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.0410770845418114,
            "unit": "iter/sec",
            "range": "stddev: 0.009188243095481214",
            "extra": "mean: 489.9374000000023 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3765966320266483,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.655360975000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041156204311387695,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.297673138999983 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.8802286357749485,
            "unit": "iter/sec",
            "range": "stddev: 0.010144975932030072",
            "extra": "mean: 347.1946593333352 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6695143392326306,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.493619989000024 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07692806280835397,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.999157439999976 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 854.5923875136347,
            "unit": "iter/sec",
            "range": "stddev: 0.00044672481086464134",
            "extra": "mean: 1.1701484995781632 msec\nrounds: 1183"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 332.4946804176778,
            "unit": "iter/sec",
            "range": "stddev: 0.00038804811874609834",
            "extra": "mean: 3.007566914285083 msec\nrounds: 315"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.646220428727815,
            "unit": "iter/sec",
            "range": "stddev: 0.00019536108307866582",
            "extra": "mean: 20.988023624997965 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.956983505334194,
            "unit": "iter/sec",
            "range": "stddev: 0.00026984409155494666",
            "extra": "mean: 201.73559159999286 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 727.0408666043916,
            "unit": "iter/sec",
            "range": "stddev: 0.00032749665530282127",
            "extra": "mean: 1.375438501374002 msec\nrounds: 728"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 212.15889447439355,
            "unit": "iter/sec",
            "range": "stddev: 0.00021653647208162003",
            "extra": "mean: 4.713448391958391 msec\nrounds: 199"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.773759025769774,
            "unit": "iter/sec",
            "range": "stddev: 0.00017313590240827347",
            "extra": "mean: 38.79915223076908 msec\nrounds: 26"
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
          "id": "8f038db15853709cc5b0a723828c7cf2148ec787",
          "message": "Bump the dependencies group with 1 update (#299)\n\nBumps the dependencies group with 1 update: [ansys-tools-path](https://github.com/ansys/ansys-tools-path).\r\n\r\n- [Release notes](https://github.com/ansys/ansys-tools-path/releases)\r\n- [Changelog](https://github.com/ansys/ansys-tools-path/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/ansys-tools-path/compare/v0.3.1...v0.3.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-tools-path\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-23T09:20:26+02:00",
          "tree_id": "0acfab8a3d7668101405642dda16115b9dbd2eec",
          "url": "https://github.com/ansys-internal/pyacp/commit/8f038db15853709cc5b0a723828c7cf2148ec787"
        },
        "date": 1698045963700,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.204811568067599,
            "unit": "iter/sec",
            "range": "stddev: 0.004744525724867251",
            "extra": "mean: 192.12991420000094 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2246798672693266,
            "unit": "iter/sec",
            "range": "stddev: 0.009713143531604093",
            "extra": "mean: 449.5028766666754 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37139133008866876,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.692577663999998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041111922055650396,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.323844520000023 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.03243344651089,
            "unit": "iter/sec",
            "range": "stddev: 0.007453244088407839",
            "extra": "mean: 329.76816066667425 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6486995988476146,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5415455809999798 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07669045122873316,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.039432992999991 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1021.2694602013119,
            "unit": "iter/sec",
            "range": "stddev: 0.00022625049416223844",
            "extra": "mean: 979.1735080405526 usec\nrounds: 1057"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 345.2315386907723,
            "unit": "iter/sec",
            "range": "stddev: 0.0002726966151079808",
            "extra": "mean: 2.8966067346926576 msec\nrounds: 343"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.31124922849209,
            "unit": "iter/sec",
            "range": "stddev: 0.00016396984248536693",
            "extra": "mean: 21.59302581250107 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96032657885448,
            "unit": "iter/sec",
            "range": "stddev: 0.00012239067521155195",
            "extra": "mean: 201.59962939999332 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 810.0298486601831,
            "unit": "iter/sec",
            "range": "stddev: 0.00015770041286102132",
            "extra": "mean: 1.234522408839667 msec\nrounds: 724"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 203.50931650388654,
            "unit": "iter/sec",
            "range": "stddev: 0.0001644587780722974",
            "extra": "mean: 4.913779954545238 msec\nrounds: 198"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.50350708388301,
            "unit": "iter/sec",
            "range": "stddev: 0.00014538863040216237",
            "extra": "mean: 39.21029357691562 msec\nrounds: 26"
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
          "id": "72307c17f62c331160d9058afc3312828146f3d2",
          "message": "Bump the dependencies group with 1 update (#300)\n\nBumps the dependencies group with 1 update: [types-protobuf](https://github.com/python/typeshed).\r\n\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-24T08:46:10+02:00",
          "tree_id": "2cc794db36b17ac6b76fe0d138fb68982fa2fbd0",
          "url": "https://github.com/ansys-internal/pyacp/commit/72307c17f62c331160d9058afc3312828146f3d2"
        },
        "date": 1698130289956,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.547852106982233,
            "unit": "iter/sec",
            "range": "stddev: 0.00476098022991953",
            "extra": "mean: 152.72183666666214 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5277252597216506,
            "unit": "iter/sec",
            "range": "stddev: 0.0014779127943590957",
            "extra": "mean: 395.6126149999856 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3866745458462365,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.586154198000031 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04125867272932643,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.23732839300004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.648863674705529,
            "unit": "iter/sec",
            "range": "stddev: 0.003009628863595189",
            "extra": "mean: 274.0579230000151 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6996066128107494,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.429374710999923 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0772210790428269,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.949831993999965 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1127.3699674337793,
            "unit": "iter/sec",
            "range": "stddev: 0.0002428205813072896",
            "extra": "mean: 887.0202585547756 usec\nrounds: 1578"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 384.1436592210531,
            "unit": "iter/sec",
            "range": "stddev: 0.00010140272857619464",
            "extra": "mean: 2.6031927795651995 msec\nrounds: 372"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.08662952727698,
            "unit": "iter/sec",
            "range": "stddev: 0.00016440382808408286",
            "extra": "mean: 20.795801448981848 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.973082524443485,
            "unit": "iter/sec",
            "range": "stddev: 0.0001638760024886165",
            "extra": "mean: 201.08252679999623 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 916.6747766525114,
            "unit": "iter/sec",
            "range": "stddev: 0.00014786439905062823",
            "extra": "mean: 1.0908994394410778 msec\nrounds: 933"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 229.3405571793155,
            "unit": "iter/sec",
            "range": "stddev: 0.00013259828232452885",
            "extra": "mean: 4.3603277688827 msec\nrounds: 225"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.887861061333524,
            "unit": "iter/sec",
            "range": "stddev: 0.00015611452852399435",
            "extra": "mean: 38.62814303703191 msec\nrounds: 27"
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
          "id": "230cf10d4697e7a7c8a61a720bc4cadd38de74e3",
          "message": "Bump the dependencies group with 2 updates (#301)\n\nBumps the dependencies group with 2 updates: [ipykernel](https://github.com/ipython/ipykernel) and [pytest](https://github.com/pytest-dev/pytest).\r\n\r\n\r\nUpdates `ipykernel` from 6.25.2 to 6.26.0\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.25.2...v6.26.0)\r\n\r\nUpdates `pytest` from 7.4.2 to 7.4.3\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.2...7.4.3)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-25T08:11:41+02:00",
          "tree_id": "29a25c141746502ffbe73f30aaddbb5d0c3716e2",
          "url": "https://github.com/ansys-internal/pyacp/commit/230cf10d4697e7a7c8a61a720bc4cadd38de74e3"
        },
        "date": 1698214614409,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.291975822156231,
            "unit": "iter/sec",
            "range": "stddev: 0.0036958537649528327",
            "extra": "mean: 158.93258783332462 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.430312094822128,
            "unit": "iter/sec",
            "range": "stddev: 0.008005295615650877",
            "extra": "mean: 411.4697870000062 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3761429497066387,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6585637210000073 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04115760965651859,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.29684348400002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.501494334925717,
            "unit": "iter/sec",
            "range": "stddev: 0.004889962233371635",
            "extra": "mean: 285.5923512500027 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6715966842057479,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4889888879999944 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07687903268278852,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.007447740999964 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1180.7249040874678,
            "unit": "iter/sec",
            "range": "stddev: 0.00020552719302992042",
            "extra": "mean: 846.9373319205607 usec\nrounds: 1178"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 367.3797378953284,
            "unit": "iter/sec",
            "range": "stddev: 0.00010556300104299522",
            "extra": "mean: 2.721979186247103 msec\nrounds: 349"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.94907546266026,
            "unit": "iter/sec",
            "range": "stddev: 0.00015119052908699987",
            "extra": "mean: 21.299673958336502 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964357486945318,
            "unit": "iter/sec",
            "range": "stddev: 0.0002590256040137834",
            "extra": "mean: 201.43593659998942 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 890.9980634745757,
            "unit": "iter/sec",
            "range": "stddev: 0.00014337075073422877",
            "extra": "mean: 1.1223368949875778 msec\nrounds: 838"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.54837076688733,
            "unit": "iter/sec",
            "range": "stddev: 0.00012262758569959873",
            "extra": "mean: 4.682779814282055 msec\nrounds: 210"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.63475465700313,
            "unit": "iter/sec",
            "range": "stddev: 0.00012478134631840963",
            "extra": "mean: 39.00954050000284 msec\nrounds: 26"
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
          "id": "6ccd17eb84a36ab585f0afa2d2b6efd42aac1ae3",
          "message": "Bump the dependencies group with 1 update (#302)\n\nBumps the dependencies group with 1 update: [types-protobuf](https://github.com/python/typeshed).\r\n\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-10-30T07:24:09+01:00",
          "tree_id": "593ac8c08447d24e757177ae5d41d80a7e178903",
          "url": "https://github.com/ansys-internal/pyacp/commit/6ccd17eb84a36ab585f0afa2d2b6efd42aac1ae3"
        },
        "date": 1698647365200,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.713382724987014,
            "unit": "iter/sec",
            "range": "stddev: 0.005048887585605503",
            "extra": "mean: 148.95620300002102 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5025317007932917,
            "unit": "iter/sec",
            "range": "stddev: 0.00459815017401495",
            "extra": "mean: 399.59533766665345 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38411475957599167,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.603388635999977 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04126251433874595,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.23507185699998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4926284496625084,
            "unit": "iter/sec",
            "range": "stddev: 0.007407359721568763",
            "extra": "mean: 286.3173150000051 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6956246150804457,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4375569500000438 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07702551835026551,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.98271042400006 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1205.8886692159447,
            "unit": "iter/sec",
            "range": "stddev: 0.0002154432769761711",
            "extra": "mean: 829.2639490925715 usec\nrounds: 1375"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 375.1543160377097,
            "unit": "iter/sec",
            "range": "stddev: 0.00020571686215279812",
            "extra": "mean: 2.6655697595639074 msec\nrounds: 366"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.876975869965904,
            "unit": "iter/sec",
            "range": "stddev: 0.00018826803774135294",
            "extra": "mean: 20.886866428573203 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.971831007567803,
            "unit": "iter/sec",
            "range": "stddev: 0.00021309182534038176",
            "extra": "mean: 201.1331435999864 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 934.7913305995363,
            "unit": "iter/sec",
            "range": "stddev: 0.00013886825795034115",
            "extra": "mean: 1.0697574605860343 msec\nrounds: 888"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 225.37479403788225,
            "unit": "iter/sec",
            "range": "stddev: 0.0002092845013845699",
            "extra": "mean: 4.437053417037908 msec\nrounds: 223"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.902118677513474,
            "unit": "iter/sec",
            "range": "stddev: 0.00011622837077110062",
            "extra": "mean: 38.606880481484886 msec\nrounds: 27"
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
          "id": "14068bf54f0d83148626d4fbb194356ee0170a52",
          "message": "Add property rotation_angle to the Oriented Selection Set (#315)\n\n* Add property rotation_angle to the Oriented Selection Set\r\n\r\n* update reference to ansys-api-acp",
          "timestamp": "2023-11-27T14:15:42+01:00",
          "tree_id": "ee9e28c86655a412804d7028f6849df816e6754a",
          "url": "https://github.com/ansys-internal/pyacp/commit/14068bf54f0d83148626d4fbb194356ee0170a52"
        },
        "date": 1701091271853,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.565748177186674,
            "unit": "iter/sec",
            "range": "stddev: 0.004364392500642947",
            "extra": "mean: 152.3055671666782 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5404157644269447,
            "unit": "iter/sec",
            "range": "stddev: 0.0004175322853383484",
            "extra": "mean: 393.63635433335276 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3838095107095588,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.605459145999987 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04126478030396309,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.23374104100003 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.500004501442986,
            "unit": "iter/sec",
            "range": "stddev: 0.006833319054438323",
            "extra": "mean: 285.7139182500248 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6918687741102896,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4453607930000203 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07703176525371835,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.981657589000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1210.7163003864111,
            "unit": "iter/sec",
            "range": "stddev: 0.00023570325067132298",
            "extra": "mean: 825.9573276421908 usec\nrounds: 1230"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 383.9380994100303,
            "unit": "iter/sec",
            "range": "stddev: 0.00012704303119282742",
            "extra": "mean: 2.604586524589842 msec\nrounds: 366"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.0497030933954,
            "unit": "iter/sec",
            "range": "stddev: 0.00012037546350985417",
            "extra": "mean: 20.81178312499195 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974592047262031,
            "unit": "iter/sec",
            "range": "stddev: 0.00002762529637839079",
            "extra": "mean: 201.02150899999742 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 908.2485751022742,
            "unit": "iter/sec",
            "range": "stddev: 0.00016593239763638384",
            "extra": "mean: 1.1010201693819273 msec\nrounds: 921"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 229.9394714999109,
            "unit": "iter/sec",
            "range": "stddev: 0.00008919049732499953",
            "extra": "mean: 4.348970594204342 msec\nrounds: 207"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.88180973234684,
            "unit": "iter/sec",
            "range": "stddev: 0.00008977502274439716",
            "extra": "mean: 38.63717453846395 msec\nrounds: 26"
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
          "id": "859d8ffff3c7e5de1450920439aa6be19723f802",
          "message": "Update vale configuration (#296)\n\nExplicitly ignore inline tags (e.g. ``:class:`ClassName` ``) and code blocks \r\nwhen running vale.\r\nThis configuration became needed with a new version of vale.",
          "timestamp": "2023-11-29T08:33:43+01:00",
          "tree_id": "5978601c6e12c24a36a801abad3ffaba1be9098e",
          "url": "https://github.com/ansys-internal/pyacp/commit/859d8ffff3c7e5de1450920439aa6be19723f802"
        },
        "date": 1701243525439,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.3642337935477125,
            "unit": "iter/sec",
            "range": "stddev: 0.0041664381247660965",
            "extra": "mean: 157.12810566667676 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3132087696730697,
            "unit": "iter/sec",
            "range": "stddev: 0.016090534843582496",
            "extra": "mean: 432.29993466665445 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37712818720548597,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6516182930000127 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041126354712015034,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.31530844400004 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.2240141493468792,
            "unit": "iter/sec",
            "range": "stddev: 0.005866296360659165",
            "extra": "mean: 310.17233600000793 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6730465412383219,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4857813520000036 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07688142925339173,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.00704226900001 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1137.4663501512075,
            "unit": "iter/sec",
            "range": "stddev: 0.00021885113516135747",
            "extra": "mean: 879.146886294321 usec\nrounds: 1328"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 341.38770483305126,
            "unit": "iter/sec",
            "range": "stddev: 0.0002689570131793866",
            "extra": "mean: 2.929220899999986 msec\nrounds: 350"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.15393397028184,
            "unit": "iter/sec",
            "range": "stddev: 0.00023345743649932335",
            "extra": "mean: 21.207138319153543 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.958575318007339,
            "unit": "iter/sec",
            "range": "stddev: 0.0002090423364188547",
            "extra": "mean: 201.6708299999891 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 833.1599594230307,
            "unit": "iter/sec",
            "range": "stddev: 0.00020677347919720912",
            "extra": "mean: 1.2002497103827543 msec\nrounds: 915"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 210.20549714244075,
            "unit": "iter/sec",
            "range": "stddev: 0.00021618585639317345",
            "extra": "mean: 4.757249518181601 msec\nrounds: 220"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.701317560940502,
            "unit": "iter/sec",
            "range": "stddev: 0.00016732943056303048",
            "extra": "mean: 38.908511115389146 msec\nrounds: 26"
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
          "id": "eb884a13dd897868dd0c5d20cbe1214616865cb0",
          "message": "Handle dash in docker-compose version, disable deadline in hypothesis tests (#318)",
          "timestamp": "2023-11-29T09:00:36+01:00",
          "tree_id": "36b1d3cbb5d84405d1abe3cfc65403f2343d998c",
          "url": "https://github.com/ansys-internal/pyacp/commit/eb884a13dd897868dd0c5d20cbe1214616865cb0"
        },
        "date": 1701245169876,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.62871771439621,
            "unit": "iter/sec",
            "range": "stddev: 0.003118367874603492",
            "extra": "mean: 150.85873966667882 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.51623648351056,
            "unit": "iter/sec",
            "range": "stddev: 0.0025513204210349145",
            "extra": "mean: 397.41892566665155 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38572090627751304,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.592548093000005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.0412632333656945,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.234649552000008 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.646592557227412,
            "unit": "iter/sec",
            "range": "stddev: 0.002189612393062307",
            "extra": "mean: 274.228607750004 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6953376761890303,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4381501739999862 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07726429374371555,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.94258902200005 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1175.1844532769153,
            "unit": "iter/sec",
            "range": "stddev: 0.00024035764898261032",
            "extra": "mean: 850.9302494698375 usec\nrounds: 1415"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 387.6572534237021,
            "unit": "iter/sec",
            "range": "stddev: 0.00007751440145316028",
            "extra": "mean: 2.5795983208574684 msec\nrounds: 374"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.09136720152656,
            "unit": "iter/sec",
            "range": "stddev: 0.00011546758552441736",
            "extra": "mean: 20.793752770835283 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974059904543759,
            "unit": "iter/sec",
            "range": "stddev: 0.00007493009408735755",
            "extra": "mean: 201.043014999982 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 922.2764082202764,
            "unit": "iter/sec",
            "range": "stddev: 0.00014457581588646275",
            "extra": "mean: 1.0842736419222818 msec\nrounds: 916"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 231.2064503015719,
            "unit": "iter/sec",
            "range": "stddev: 0.00007295401386221595",
            "extra": "mean: 4.325138847535005 msec\nrounds: 223"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.939629875086347,
            "unit": "iter/sec",
            "range": "stddev: 0.00012467699676407264",
            "extra": "mean: 38.55105122222455 msec\nrounds: 27"
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
          "id": "7770a9567130d7c2f73080972c91f3dfd679ede4",
          "message": "Update supported Python versions (#293)\n\n* Drop support for Python 3.8\r\n* Run `pyupgrade` with `--py39-plus`\r\n* Disallow poetry version `1.7.0`, to avoid https://github.com/python-poetry/poetry/issues/8628\r\n* Remove outdated `poetry config installer.modern-installation false`\r\n* Switch dependabot to weekly schedule\r\n* Fix type hints for paths\r\n* Re-lock dependencies",
          "timestamp": "2023-11-29T08:28:49Z",
          "tree_id": "c01860651b761e50ab10631cb131a7e40619cd65",
          "url": "https://github.com/ansys-internal/pyacp/commit/7770a9567130d7c2f73080972c91f3dfd679ede4"
        },
        "date": 1701246834206,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.748710477491311,
            "unit": "iter/sec",
            "range": "stddev: 0.00514835712317747",
            "extra": "mean: 148.17645583334146 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.107714582301116,
            "unit": "iter/sec",
            "range": "stddev: 0.0013708391885385897",
            "extra": "mean: 474.44754066665 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3752616550354054,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.664807306 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041187118649925455,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.279435725999974 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0205272616278473,
            "unit": "iter/sec",
            "range": "stddev: 0.004474146555476303",
            "extra": "mean: 331.06802666666607 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6595925253988365,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5160875259999784 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07706057866844966,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.976803668999992 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1082.696344812999,
            "unit": "iter/sec",
            "range": "stddev: 0.0002473274839171471",
            "extra": "mean: 923.6200018507661 usec\nrounds: 1621"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 316.6402988097534,
            "unit": "iter/sec",
            "range": "stddev: 0.0003520838770835406",
            "extra": "mean: 3.1581577068963944 msec\nrounds: 348"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.009302455411564,
            "unit": "iter/sec",
            "range": "stddev: 0.0001936957643916554",
            "extra": "mean: 21.27238541666306 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.964604134952438,
            "unit": "iter/sec",
            "range": "stddev: 0.00019235834451426933",
            "extra": "mean: 201.42592899999272 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 780.4267496369987,
            "unit": "iter/sec",
            "range": "stddev: 0.00029234660327463773",
            "extra": "mean: 1.2813502362202882 msec\nrounds: 1016"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 201.64009749753106,
            "unit": "iter/sec",
            "range": "stddev: 0.0002809131583162571",
            "extra": "mean: 4.959331067632737 msec\nrounds: 207"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.69659737582439,
            "unit": "iter/sec",
            "range": "stddev: 0.00025973289005684977",
            "extra": "mean: 38.91565818518875 msec\nrounds: 27"
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
          "id": "08dab83eb6e6bf8910df8a678da387f413d980ab",
          "message": "Extend supported Python versions (#322)\n\nAdd support for Python 3.11 and 3.12:\r\n* Use `enum.StrEnum` instead of `(str, enum.Enum)` as base\r\n  class for string enums for Python 3.11+. The `(str, enum.Enum)`\r\n  approach does not work in Python 3.11+ since the default Enum\r\n  format method has changed. For older Python, `StrEnum` is not\r\n  available.\r\n* When a custom API branch is specified in CI, build it first using \r\n  Python 3.10 and then install it in the test environment.",
          "timestamp": "2023-12-15T10:34:52Z",
          "tree_id": "2bb3401ea0e50464533131a3e452fd1e5f2b33bb",
          "url": "https://github.com/ansys-internal/pyacp/commit/08dab83eb6e6bf8910df8a678da387f413d980ab"
        },
        "date": 1702636839143,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.337003973807259,
            "unit": "iter/sec",
            "range": "stddev: 0.008253917519970727",
            "extra": "mean: 187.37104279999812 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1705856426445553,
            "unit": "iter/sec",
            "range": "stddev: 0.006923311029885454",
            "extra": "mean: 460.7051573333176 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37143514492858215,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6922600449999834 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04112505380175402,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.31607761099997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0845017293081516,
            "unit": "iter/sec",
            "range": "stddev: 0.013263872868550108",
            "extra": "mean: 324.2014716666404 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6637076830393333,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5066873949999717 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07669906803788483,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.037968068999987 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 984.470012490567,
            "unit": "iter/sec",
            "range": "stddev: 0.0003743165361908833",
            "extra": "mean: 1.0157749726374543 msec\nrounds: 1206"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 339.6132524573827,
            "unit": "iter/sec",
            "range": "stddev: 0.0005667113496050461",
            "extra": "mean: 2.9445258474578746 msec\nrounds: 354"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.139685235497865,
            "unit": "iter/sec",
            "range": "stddev: 0.00014159286634659037",
            "extra": "mean: 21.213548520832386 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.965222617533658,
            "unit": "iter/sec",
            "range": "stddev: 0.00004802680313333275",
            "extra": "mean: 201.40083879999793 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 792.2781518724064,
            "unit": "iter/sec",
            "range": "stddev: 0.00021995723014087793",
            "extra": "mean: 1.262182981616596 msec\nrounds: 816"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.38477725055054,
            "unit": "iter/sec",
            "range": "stddev: 0.0002449619577018485",
            "extra": "mean: 4.775896381442269 msec\nrounds: 194"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.633383631647675,
            "unit": "iter/sec",
            "range": "stddev: 0.00012134233821454329",
            "extra": "mean: 39.01162696154451 msec\nrounds: 26"
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
          "id": "08dab83eb6e6bf8910df8a678da387f413d980ab",
          "message": "Extend supported Python versions (#322)\n\nAdd support for Python 3.11 and 3.12:\r\n* Use `enum.StrEnum` instead of `(str, enum.Enum)` as base\r\n  class for string enums for Python 3.11+. The `(str, enum.Enum)`\r\n  approach does not work in Python 3.11+ since the default Enum\r\n  format method has changed. For older Python, `StrEnum` is not\r\n  available.\r\n* When a custom API branch is specified in CI, build it first using \r\n  Python 3.10 and then install it in the test environment.",
          "timestamp": "2023-12-15T10:34:52Z",
          "url": "https://github.com/ansys-internal/pyacp/commit/08dab83eb6e6bf8910df8a678da387f413d980ab"
        },
        "date": 1702882340733,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.698490241460779,
            "unit": "iter/sec",
            "range": "stddev: 0.02051741380976631",
            "extra": "mean: 212.83432519998087 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.216982531807171,
            "unit": "iter/sec",
            "range": "stddev: 0.012144560938886998",
            "extra": "mean: 451.06354499999196 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.369942927624554,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.7031196579999914 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04112675929676879,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.315069241999993 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.9950939881255603,
            "unit": "iter/sec",
            "range": "stddev: 0.0027485144894295434",
            "extra": "mean: 333.87933866670966 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6439586526693839,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5528947329999028 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07681200017090598,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.018799117000071 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 955.4638562898809,
            "unit": "iter/sec",
            "range": "stddev: 0.0004067840767138802",
            "extra": "mean: 1.0466120653512268 msec\nrounds: 1117"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 345.7630647539622,
            "unit": "iter/sec",
            "range": "stddev: 0.0003363773103830242",
            "extra": "mean: 2.8921539109782564 msec\nrounds: 337"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.652572879040086,
            "unit": "iter/sec",
            "range": "stddev: 0.0003183147729550428",
            "extra": "mean: 21.43504502083478 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.965281761829534,
            "unit": "iter/sec",
            "range": "stddev: 0.00008005265418238438",
            "extra": "mean: 201.39843980002752 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 767.7792941740777,
            "unit": "iter/sec",
            "range": "stddev: 0.000620427846740775",
            "extra": "mean: 1.3024576301914066 msec\nrounds: 722"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 208.69697999492374,
            "unit": "iter/sec",
            "range": "stddev: 0.00019632433072067166",
            "extra": "mean: 4.791636179998022 msec\nrounds: 200"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.45555101923173,
            "unit": "iter/sec",
            "range": "stddev: 0.0009496055775178995",
            "extra": "mean: 39.2841623913188 msec\nrounds: 23"
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
          "id": "08dab83eb6e6bf8910df8a678da387f413d980ab",
          "message": "Extend supported Python versions (#322)\n\nAdd support for Python 3.11 and 3.12:\r\n* Use `enum.StrEnum` instead of `(str, enum.Enum)` as base\r\n  class for string enums for Python 3.11+. The `(str, enum.Enum)`\r\n  approach does not work in Python 3.11+ since the default Enum\r\n  format method has changed. For older Python, `StrEnum` is not\r\n  available.\r\n* When a custom API branch is specified in CI, build it first using \r\n  Python 3.10 and then install it in the test environment.",
          "timestamp": "2023-12-15T10:34:52Z",
          "url": "https://github.com/ansys-internal/pyacp/commit/08dab83eb6e6bf8910df8a678da387f413d980ab"
        },
        "date": 1702883671517,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.4335749783736595,
            "unit": "iter/sec",
            "range": "stddev: 0.004056486246473833",
            "extra": "mean: 155.43457616666956 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.38146538072625,
            "unit": "iter/sec",
            "range": "stddev: 0.005336953583186673",
            "extra": "mean: 419.90952633333717 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3802378514532156,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6299328069999888 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04114705389161563,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.303076537000038 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.5716620082417165,
            "unit": "iter/sec",
            "range": "stddev: 0.00550517471631497",
            "extra": "mean: 279.981699749996 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6758757056574992,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4795619839999858 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0769789819790701,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.99055890699998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1203.2169505471377,
            "unit": "iter/sec",
            "range": "stddev: 0.0001948552164978802",
            "extra": "mean: 831.1053127578288 usec\nrounds: 1215"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 354.9368883136245,
            "unit": "iter/sec",
            "range": "stddev: 0.00028380365992983827",
            "extra": "mean: 2.817402284533451 msec\nrounds: 362"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.41680932944708,
            "unit": "iter/sec",
            "range": "stddev: 0.00020313755958896356",
            "extra": "mean: 21.089567479163424 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96453948101201,
            "unit": "iter/sec",
            "range": "stddev: 0.00011904099750554782",
            "extra": "mean: 201.4285522000023 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 881.9136100208773,
            "unit": "iter/sec",
            "range": "stddev: 0.00018154580256914485",
            "extra": "mean: 1.1338979109034584 msec\nrounds: 853"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.0493336395097,
            "unit": "iter/sec",
            "range": "stddev: 0.000250921363394618",
            "extra": "mean: 4.783559854462043 msec\nrounds: 213"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.74641057456964,
            "unit": "iter/sec",
            "range": "stddev: 0.00017407250603170297",
            "extra": "mean: 38.84036561538114 msec\nrounds: 26"
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
          "id": "95d6b0c6c6d352d696833079827b6c3dfcac84c3",
          "message": "Bump actions/upload-artifact from 3 to 4 (#326)\n\nBumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 3 to 4.\r\n- [Release notes](https://github.com/actions/upload-artifact/releases)\r\n- [Commits](https://github.com/actions/upload-artifact/compare/v3...v4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: actions/upload-artifact\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2023-12-18T08:34:35Z",
          "tree_id": "c22e8226fa1e454eda60b668b3f9289d7cf937d8",
          "url": "https://github.com/ansys-internal/pyacp/commit/95d6b0c6c6d352d696833079827b6c3dfcac84c3"
        },
        "date": 1702888794768,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.563703735062849,
            "unit": "iter/sec",
            "range": "stddev: 0.004284140528440334",
            "extra": "mean: 152.35300683333244 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.388543034227048,
            "unit": "iter/sec",
            "range": "stddev: 0.010422992986467155",
            "extra": "mean: 418.6652639999882 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3781333391446926,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.644569775999969 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041216445589634707,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.262160060000042 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3309697022150826,
            "unit": "iter/sec",
            "range": "stddev: 0.015677124897496262",
            "extra": "mean: 300.21287774998484 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6721449197573354,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4877743929999951 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07685977357585541,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.010707077000006 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1190.863757950216,
            "unit": "iter/sec",
            "range": "stddev: 0.00020336125493514116",
            "extra": "mean: 839.7266213905597 usec\nrounds: 1281"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 372.152060221419,
            "unit": "iter/sec",
            "range": "stddev: 0.0001358547654436802",
            "extra": "mean: 2.687073663934659 msec\nrounds: 366"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.19543696815396,
            "unit": "iter/sec",
            "range": "stddev: 0.00015314620096415555",
            "extra": "mean: 21.18848906250766 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9687733365270095,
            "unit": "iter/sec",
            "range": "stddev: 0.0000827911633918052",
            "extra": "mean: 201.25691640000696 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 935.033521233275,
            "unit": "iter/sec",
            "range": "stddev: 0.00012893135053477367",
            "extra": "mean: 1.0694803740095185 msec\nrounds: 754"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 214.9765697036311,
            "unit": "iter/sec",
            "range": "stddev: 0.0001847319720964587",
            "extra": "mean: 4.6516697209310305 msec\nrounds: 215"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.69621012754072,
            "unit": "iter/sec",
            "range": "stddev: 0.00015184921123118577",
            "extra": "mean: 38.91624465384561 msec\nrounds: 26"
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
          "id": "c47c72b9dc06f999986a7a05a26ffb32a2fd2ff9",
          "message": "Bump ansys/actions from 4 to 5 (#328)\n\nBumps [ansys/actions](https://github.com/ansys/actions) from 4 to 5.\r\n- [Release notes](https://github.com/ansys/actions/releases)\r\n- [Commits](https://github.com/ansys/actions/compare/v4...v5)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys/actions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-01-03T09:18:06+01:00",
          "tree_id": "c2ce48657f68fc94a1a2312d878747dd1a25593a",
          "url": "https://github.com/ansys-internal/pyacp/commit/c47c72b9dc06f999986a7a05a26ffb32a2fd2ff9"
        },
        "date": 1704270223700,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.248948863084532,
            "unit": "iter/sec",
            "range": "stddev: 0.00768954030342642",
            "extra": "mean: 190.51433460000453 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.262728621216117,
            "unit": "iter/sec",
            "range": "stddev: 0.015927033878314085",
            "extra": "mean: 441.9442926666761 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37133933387593826,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.692954687999986 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04108368582673582,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.340561949999994 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.137176703012802,
            "unit": "iter/sec",
            "range": "stddev: 0.012378502241428323",
            "extra": "mean: 318.75794533334556 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6615910486423985,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5115077540000357 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07653104192765171,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.066593304000037 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1069.007271814706,
            "unit": "iter/sec",
            "range": "stddev: 0.0002137386719545814",
            "extra": "mean: 935.4473317121951 usec\nrounds: 1028"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 353.2096509114272,
            "unit": "iter/sec",
            "range": "stddev: 0.0001112830173325689",
            "extra": "mean: 2.831179718389874 msec\nrounds: 348"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.62805597093726,
            "unit": "iter/sec",
            "range": "stddev: 0.00018225526194194265",
            "extra": "mean: 21.446315510629237 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962491602719944,
            "unit": "iter/sec",
            "range": "stddev: 0.00010730457152466142",
            "extra": "mean: 201.51167599999553 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 817.7552821727796,
            "unit": "iter/sec",
            "range": "stddev: 0.00015726357575212042",
            "extra": "mean: 1.2228597256418758 msec\nrounds: 780"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.7493130169026,
            "unit": "iter/sec",
            "range": "stddev: 0.0002488727307976362",
            "extra": "mean: 4.8134936548196405 msec\nrounds: 197"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.48380767890203,
            "unit": "iter/sec",
            "range": "stddev: 0.00019405872426783862",
            "extra": "mean: 39.24060378260887 msec\nrounds: 23"
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
          "id": "4f18cabdae7cc41ec7069ed545e7ecbe17d0e440",
          "message": "Update docker Python package (#325)\n\nUpdate the `docker` Python package to the 7.x release, and \r\nmove it to the `test` dependency group since it's only used\r\nin `conftest.py`.\r\n\r\nAdd an explicit reference to `sphinx-design`, which is an\r\nundeclared indirect dependency (via pyvista).",
          "timestamp": "2024-01-10T11:52:07+01:00",
          "tree_id": "ecb446110d77002cadf8a8515ad1fc0fc3887886",
          "url": "https://github.com/ansys-internal/pyacp/commit/4f18cabdae7cc41ec7069ed545e7ecbe17d0e440"
        },
        "date": 1704884333832,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.509937567378373,
            "unit": "iter/sec",
            "range": "stddev: 0.0034385280970094896",
            "extra": "mean: 221.7325594999977 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.042123546074967,
            "unit": "iter/sec",
            "range": "stddev: 0.0037379411006974624",
            "extra": "mean: 489.686337500018 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3738093036830214,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.675160810999955 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04109538145760749,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.333634693999954 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.7502480570192045,
            "unit": "iter/sec",
            "range": "stddev: 0.008916827821918244",
            "extra": "mean: 363.60356566666496 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6604038177564313,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5142250439999998 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07672955669430158,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.032787404000032 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 838.0483511377043,
            "unit": "iter/sec",
            "range": "stddev: 0.00040909384099641944",
            "extra": "mean: 1.1932485740738417 msec\nrounds: 1026"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 321.1785969791916,
            "unit": "iter/sec",
            "range": "stddev: 0.0003660677999205373",
            "extra": "mean: 3.1135325000027563 msec\nrounds: 328"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.202199448141926,
            "unit": "iter/sec",
            "range": "stddev: 0.00014896704836548613",
            "extra": "mean: 21.185453468087584 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9609726236870415,
            "unit": "iter/sec",
            "range": "stddev: 0.00013081137009036015",
            "extra": "mean: 201.5733759999648 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 685.6104582336646,
            "unit": "iter/sec",
            "range": "stddev: 0.0003132366446003794",
            "extra": "mean: 1.458554180425275 msec\nrounds: 654"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.83492479179625,
            "unit": "iter/sec",
            "range": "stddev: 0.000367880129631109",
            "extra": "mean: 4.834773435901204 msec\nrounds: 195"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.58515077526304,
            "unit": "iter/sec",
            "range": "stddev: 0.00013133573155572445",
            "extra": "mean: 39.085171269221064 msec\nrounds: 26"
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
          "id": "1499707a525b7a08a178a54e105c54f91041fab2",
          "message": "Add CAD Geometry exposure (#327)\n\nAdd `CADGeometry`, `CADComponent` and `VirtualGeometry` classes.\r\n\r\nThe `CADGeometry` has a property `visualization_mesh` which provides\r\na tessellated representation that can be converted to a PyVista object.\r\n\r\nThe `VirtualGeometry` has a method `set_cad_components` which can be\r\nused to set the sub-shapes of the virtual geometry to correspond to a \r\nlist of `CADComponent`s.",
          "timestamp": "2024-01-12T15:24:35+01:00",
          "tree_id": "73102b95626e918fa081fc333bc331649ef7ba8d",
          "url": "https://github.com/ansys-internal/pyacp/commit/1499707a525b7a08a178a54e105c54f91041fab2"
        },
        "date": 1705069830927,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.861324132308884,
            "unit": "iter/sec",
            "range": "stddev: 0.0076436352771502986",
            "extra": "mean: 205.7052714000065 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.1215256952461528,
            "unit": "iter/sec",
            "range": "stddev: 0.012633847868063814",
            "extra": "mean: 471.3588915000031 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3716349198490273,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.690812801999982 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04113012187891177,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.31308137000002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.7562205094740135,
            "unit": "iter/sec",
            "range": "stddev: 0.0016529093268426393",
            "extra": "mean: 362.8156733333488 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6537607982831521,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5296114459999899 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0768146302172183,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.018353368000021 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 899.4223759162165,
            "unit": "iter/sec",
            "range": "stddev: 0.0003856001406997443",
            "extra": "mean: 1.1118246852390434 msec\nrounds: 1023"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 330.54988768816065,
            "unit": "iter/sec",
            "range": "stddev: 0.0005147099918332223",
            "extra": "mean: 3.0252619566562844 msec\nrounds: 323"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.05801844269336,
            "unit": "iter/sec",
            "range": "stddev: 0.0002055220069397752",
            "extra": "mean: 21.25036355319098 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.967051017405669,
            "unit": "iter/sec",
            "range": "stddev: 0.00004844927243965242",
            "extra": "mean: 201.32670199999438 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 723.6129870756794,
            "unit": "iter/sec",
            "range": "stddev: 0.00033845838327466963",
            "extra": "mean: 1.38195419079096 msec\nrounds: 608"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.0170964974799,
            "unit": "iter/sec",
            "range": "stddev: 0.0003829946175686478",
            "extra": "mean: 4.830518913263637 msec\nrounds: 196"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.644068165346287,
            "unit": "iter/sec",
            "range": "stddev: 0.00011977148398313374",
            "extra": "mean: 38.99537286955641 msec\nrounds: 23"
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
          "id": "eb4bc078f9bec4c94279dc070efa5f6d1e79f3e2",
          "message": "Add Cutoff- and GeometricalSelectionRule (#329)\n\nImplements tree objects for `CutoffSelectionRule` and `GeometricalSelectionRule`.\r\n\r\nAdds some missing types to the `__init__.py` and `.rst` files.\r\n\r\n---------\r\n\r\nCo-authored-by: janvonrickenbach <jan.vonrickenbach@ansys.com>",
          "timestamp": "2024-01-12T16:21:45+01:00",
          "tree_id": "298b50fa9a66369d4411670e0359b01cce891295",
          "url": "https://github.com/ansys-internal/pyacp/commit/eb4bc078f9bec4c94279dc070efa5f6d1e79f3e2"
        },
        "date": 1705073219740,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.7063183701474225,
            "unit": "iter/sec",
            "range": "stddev: 0.0037911885484204974",
            "extra": "mean: 149.11311166666508 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5603865875134577,
            "unit": "iter/sec",
            "range": "stddev: 0.0027864727817334084",
            "extra": "mean: 390.56602033334303 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.38785660710693304,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.578272437999999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04127885855341041,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.225476067999978 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.6431852656226207,
            "unit": "iter/sec",
            "range": "stddev: 0.0020398281365726764",
            "extra": "mean: 274.4850802499883 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.7005692543431346,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4274106290000077 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07731222167506463,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.934565561999989 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1240.7661934747691,
            "unit": "iter/sec",
            "range": "stddev: 0.00020386615810393948",
            "extra": "mean: 805.9536158053253 usec\nrounds: 1278"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 388.14735917801295,
            "unit": "iter/sec",
            "range": "stddev: 0.00008394977525316408",
            "extra": "mean: 2.5763411146676845 msec\nrounds: 375"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 48.35309267663259,
            "unit": "iter/sec",
            "range": "stddev: 0.00009556556475326607",
            "extra": "mean: 20.68120040816471 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.974158154074695,
            "unit": "iter/sec",
            "range": "stddev: 0.0001637961934798317",
            "extra": "mean: 201.03904400000374 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 948.7571545922391,
            "unit": "iter/sec",
            "range": "stddev: 0.0001361231283528114",
            "extra": "mean: 1.054010496953548 msec\nrounds: 821"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 231.3787075445783,
            "unit": "iter/sec",
            "range": "stddev: 0.00007664082558993754",
            "extra": "mean: 4.321918860262179 msec\nrounds: 229"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.946037699861503,
            "unit": "iter/sec",
            "range": "stddev: 0.00016355507703215693",
            "extra": "mean: 38.541530370370886 msec\nrounds: 27"
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
          "id": "be141037f374c57c358bec0b2830adfa1d73b227",
          "message": "Add modeling ply thickness properties (#331)\n\nAdd advanced thickness properties to the `ModelingPly`:\r\n- thickness by geometry\r\n- thickness by field (look-up table column)\r\n- taper edges\r\n\r\n---------\r\n\r\nCo-authored-by: René Roos <105842014+roosre@users.noreply.github.com>",
          "timestamp": "2024-01-15T10:43:49Z",
          "tree_id": "002b2beab85a2f2132ca62b8223950bfe8c11f82",
          "url": "https://github.com/ansys-internal/pyacp/commit/be141037f374c57c358bec0b2830adfa1d73b227"
        },
        "date": 1705315771114,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.300416885102624,
            "unit": "iter/sec",
            "range": "stddev: 0.006463581580930372",
            "extra": "mean: 188.6644053999987 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.2632546450214717,
            "unit": "iter/sec",
            "range": "stddev: 0.0009837147193221373",
            "extra": "mean: 441.84157633332194 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3723127162966316,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.685914169 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04107633451559294,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.34491810899999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.0680583832200767,
            "unit": "iter/sec",
            "range": "stddev: 0.007074773453418363",
            "extra": "mean: 325.9390386666799 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6569002775526476,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5223010770000087 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07662327664751468,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.050864485999966 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1019.4479041229171,
            "unit": "iter/sec",
            "range": "stddev: 0.00037916770224736103",
            "extra": "mean: 980.9231015687368 usec\nrounds: 1083"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 348.5119749236279,
            "unit": "iter/sec",
            "range": "stddev: 0.00032309184728699286",
            "extra": "mean: 2.8693418647067657 msec\nrounds: 340"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.14004297971242,
            "unit": "iter/sec",
            "range": "stddev: 0.0001969383743844701",
            "extra": "mean: 21.213387531919906 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.962949669978325,
            "unit": "iter/sec",
            "range": "stddev: 0.00015506636329360078",
            "extra": "mean: 201.49307699998644 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 788.53235435568,
            "unit": "iter/sec",
            "range": "stddev: 0.0002884979817969143",
            "extra": "mean: 1.26817878109404 msec\nrounds: 804"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.4626518169532,
            "unit": "iter/sec",
            "range": "stddev: 0.0005345005135590012",
            "extra": "mean: 4.8434910198023875 msec\nrounds: 202"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.596825728983426,
            "unit": "iter/sec",
            "range": "stddev: 0.00034985065494749383",
            "extra": "mean: 39.06734415383758 msec\nrounds: 26"
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
          "id": "7732bc235bfe7df73ff477db2a52b6642e9ee39c",
          "message": "Bump actions/cache from 3 to 4 (#341)\n\nBumps [actions/cache](https://github.com/actions/cache) from 3 to 4.\r\n- [Release notes](https://github.com/actions/cache/releases)\r\n- [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md)\r\n- [Commits](https://github.com/actions/cache/compare/v3...v4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: actions/cache\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-01-23T08:08:28Z",
          "tree_id": "f6976ff6952138da7ae864b2767985838b608842",
          "url": "https://github.com/ansys-internal/pyacp/commit/7732bc235bfe7df73ff477db2a52b6642e9ee39c"
        },
        "date": 1705997650547,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.457116735510092,
            "unit": "iter/sec",
            "range": "stddev: 0.013525490821976072",
            "extra": "mean: 224.36028924998652 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.080822121334067,
            "unit": "iter/sec",
            "range": "stddev: 0.006582518544329231",
            "extra": "mean: 480.57928149998475 msec\nrounds: 2"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37065949067619075,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6978939570000193 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04105161277855952,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.359578888999977 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 2.72014098251353,
            "unit": "iter/sec",
            "range": "stddev: 0.001267963105214997",
            "extra": "mean: 367.6280039999824 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6604494225570262,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.514120484999978 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07666829442170346,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.043201333000013 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 882.7627557302314,
            "unit": "iter/sec",
            "range": "stddev: 0.0002968343579598183",
            "extra": "mean: 1.1328071936754835 msec\nrounds: 1012"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 317.2006569251142,
            "unit": "iter/sec",
            "range": "stddev: 0.0004909093905217319",
            "extra": "mean: 3.152578590769071 msec\nrounds: 325"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.67645357357695,
            "unit": "iter/sec",
            "range": "stddev: 0.0001822072928341704",
            "extra": "mean: 21.42407838298344 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.960548283290665,
            "unit": "iter/sec",
            "range": "stddev: 0.0000502579051818263",
            "extra": "mean: 201.5906191999875 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 690.3308884379084,
            "unit": "iter/sec",
            "range": "stddev: 0.0005164589845351293",
            "extra": "mean: 1.4485806976750177 msec\nrounds: 602"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 207.6254826238037,
            "unit": "iter/sec",
            "range": "stddev: 0.00023095718453757509",
            "extra": "mean: 4.816364481675395 msec\nrounds: 191"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.457820887966804,
            "unit": "iter/sec",
            "range": "stddev: 0.00016139689972842272",
            "extra": "mean: 39.28065973913234 msec\nrounds: 23"
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
          "id": "88b1b7a50f0d9137cb781bec3e3ef571e0098810",
          "message": "Wrap gRPC exceptions in a simplified format (#336)\n\nWrap gRPC RpcError to emit a standard Python exception with a\r\nsimplified error message (containing only the first line of the\r\ngRPC error details).\r\nThe full exception is still available through the traceback, but\r\nthis should improve how the error is typically presented to the\r\nuser.",
          "timestamp": "2024-01-24T10:10:41Z",
          "tree_id": "e438b33be4326ae047092fc58c4e3c5f59b1554f",
          "url": "https://github.com/ansys-internal/pyacp/commit/88b1b7a50f0d9137cb781bec3e3ef571e0098810"
        },
        "date": 1706091356923,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.314623129557479,
            "unit": "iter/sec",
            "range": "stddev: 0.006036245722559785",
            "extra": "mean: 158.36257833332942 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3911547188937705,
            "unit": "iter/sec",
            "range": "stddev: 0.019539094713176327",
            "extra": "mean: 418.20798633332856 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37900866454285287,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.638462107999999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041162889657453995,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.293726906000018 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.478490322885916,
            "unit": "iter/sec",
            "range": "stddev: 0.004944846457433962",
            "extra": "mean: 287.4810355000079 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6666359258620229,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5000691699999606 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07678104879785076,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.02404715299997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1158.8442115696873,
            "unit": "iter/sec",
            "range": "stddev: 0.00020039450302433945",
            "extra": "mean: 862.9287612745388 usec\nrounds: 1286"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 368.7301932806146,
            "unit": "iter/sec",
            "range": "stddev: 0.00009974907680865165",
            "extra": "mean: 2.712010077349349 msec\nrounds: 362"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.380345625806555,
            "unit": "iter/sec",
            "range": "stddev: 0.00011804642041938723",
            "extra": "mean: 21.10579791666467 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9667263357577225,
            "unit": "iter/sec",
            "range": "stddev: 0.0001036781596932292",
            "extra": "mean: 201.3398630000097 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 888.4313025312938,
            "unit": "iter/sec",
            "range": "stddev: 0.00014352022014632593",
            "extra": "mean: 1.1255794310160254 msec\nrounds: 877"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 213.044278909893,
            "unit": "iter/sec",
            "range": "stddev: 0.00017488759947692284",
            "extra": "mean: 4.693859910797932 msec\nrounds: 213"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.722850510481074,
            "unit": "iter/sec",
            "range": "stddev: 0.00009430226436941909",
            "extra": "mean: 38.87594026923799 msec\nrounds: 26"
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
          "id": "0e6e5e28a3d4e3bff141900f959ab5ab594ef276",
          "message": "Fix autocompletion of 'create_*' methods (#340)\n\nSplit the `define_mutable_mapping` functionality into two\r\nfunctions. This allows typing the function which produces the\r\n`create_*` methods with a ParamSpec, which in turn allows the\r\nautocompletion to work (tested on VSCode).\r\n\r\nOther changes:\r\n- Improve the type hints on class decorators, to enable autocompletion\r\n  on the constructors.\r\n- Improve autocompletion for the `define_mutable_mapping` return value\r\n  by introducing a protocol that describes read-only properties.",
          "timestamp": "2024-01-24T13:34:30+01:00",
          "tree_id": "569d1aa814a46bc4f168578d09019cd8e6d20548",
          "url": "https://github.com/ansys-internal/pyacp/commit/0e6e5e28a3d4e3bff141900f959ab5ab594ef276"
        },
        "date": 1706099991747,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.595910147209883,
            "unit": "iter/sec",
            "range": "stddev: 0.00448849408268651",
            "extra": "mean: 151.60909983332735 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.5226728650374506,
            "unit": "iter/sec",
            "range": "stddev: 0.004433895151809975",
            "extra": "mean: 396.4049456666885 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3818062450207909,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6191295010000317 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04126112853077531,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.235885823000046 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.5775703013580404,
            "unit": "iter/sec",
            "range": "stddev: 0.004561778781529981",
            "extra": "mean: 279.5193150000159 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6893881766519444,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4505615759999841 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07721755843698574,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.950422419999995 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1204.95779200075,
            "unit": "iter/sec",
            "range": "stddev: 0.00023374281901089938",
            "extra": "mean: 829.9045880599423 usec\nrounds: 1340"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 385.994113146825,
            "unit": "iter/sec",
            "range": "stddev: 0.00008106094257791074",
            "extra": "mean: 2.590713085874495 msec\nrounds: 361"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.87372574418488,
            "unit": "iter/sec",
            "range": "stddev: 0.0001119645113379488",
            "extra": "mean: 20.888284428572344 msec\nrounds: 49"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.973935414527069,
            "unit": "iter/sec",
            "range": "stddev: 0.00013262690660436648",
            "extra": "mean: 201.04804679999688 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 931.2916302033416,
            "unit": "iter/sec",
            "range": "stddev: 0.00013974405375460376",
            "extra": "mean: 1.0737775016636373 msec\nrounds: 901"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 228.75844326735887,
            "unit": "iter/sec",
            "range": "stddev: 0.0002558491181493844",
            "extra": "mean: 4.371423348213911 msec\nrounds: 224"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.860404604967023,
            "unit": "iter/sec",
            "range": "stddev: 0.00013860807295482507",
            "extra": "mean: 38.66915523077042 msec\nrounds: 26"
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
          "id": "22ec26b30ceea84be51513222c3bc00501103b2e",
          "message": "Improve autocompletion for grpc properties (#351)\n\nImproves the autocompletion for properties defined via either\r\n'`rpc_data_property` or `grpc_data_property_read_only` by defining\r\nprotocols for read-only and read-write properties.\r\n\r\nAdd type annotations to the properties where they cannot be inferred\r\nfrom the `from_protobuf` or `to_protobuf` methods.\r\n\r\nNote: Some properties may still have type annotations which are\r\ntoo broad, if the `from_protobuf` or `to_protobuf` type annotations\r\nare too broad.",
          "timestamp": "2024-01-24T12:52:47Z",
          "tree_id": "e86fc94f65c39628bd16ccf711d6cceff9d6882f",
          "url": "https://github.com/ansys-internal/pyacp/commit/22ec26b30ceea84be51513222c3bc00501103b2e"
        },
        "date": 1706101120313,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 4.8120230497791,
            "unit": "iter/sec",
            "range": "stddev: 0.007442078850960647",
            "extra": "mean: 207.8128033999974 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.169634558716832,
            "unit": "iter/sec",
            "range": "stddev: 0.005351810740333245",
            "extra": "mean: 460.9071126666701 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37235190155616293,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.685631510999997 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04110927803648174,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.32540895300002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.1809772740889093,
            "unit": "iter/sec",
            "range": "stddev: 0.006810111858827245",
            "extra": "mean: 314.3687973333347 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6555249627809555,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.525494918999982 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07672301145474449,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.03389923100002 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 989.719147462948,
            "unit": "iter/sec",
            "range": "stddev: 0.00036306695175829825",
            "extra": "mean: 1.0103876463978758 msec\nrounds: 888"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 341.14903938502636,
            "unit": "iter/sec",
            "range": "stddev: 0.0003631031973605206",
            "extra": "mean: 2.9312701621632993 msec\nrounds: 333"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 46.81390004773227,
            "unit": "iter/sec",
            "range": "stddev: 0.00019931652370329007",
            "extra": "mean: 21.361176893623103 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.958423140995839,
            "unit": "iter/sec",
            "range": "stddev: 0.0005776975041160952",
            "extra": "mean: 201.6770193999946 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 743.6858844934867,
            "unit": "iter/sec",
            "range": "stddev: 0.0003896964514680718",
            "extra": "mean: 1.3446537319732577 msec\nrounds: 735"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 206.24830346757886,
            "unit": "iter/sec",
            "range": "stddev: 0.0004875433610923006",
            "extra": "mean: 4.848524730566789 msec\nrounds: 193"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.5714186657921,
            "unit": "iter/sec",
            "range": "stddev: 0.0003550022869718522",
            "extra": "mean: 39.106160399999226 msec\nrounds: 25"
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
          "id": "ba544a27e831903de433492f65d3367dbdb32d8a",
          "message": "Add explicit type checks (#352)\n\nAdd explicit checks to ensure that `mypy` can correctly infer the\r\ntypes of certain PyACP objects.\r\n\r\nThis is done by adding dummy scripts and using `typing.assert_type`\r\nto check for certain types.\r\nThe scripts are generally not runnable, since the set-up takes some\r\nshortcuts, explicitly ignoring the resulting type errors.\r\n\r\nOther changes:\r\n- Make all arguments in the `__init__` methods of tree objects keyword\r\n  only.",
          "timestamp": "2024-01-25T11:48:58+01:00",
          "tree_id": "25da454c4f7d0d66e00befc5578db8d6310613e5",
          "url": "https://github.com/ansys-internal/pyacp/commit/ba544a27e831903de433492f65d3367dbdb32d8a"
        },
        "date": 1706180090135,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.232846932554791,
            "unit": "iter/sec",
            "range": "stddev: 0.006652384943434688",
            "extra": "mean: 160.44032699999397 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.4161055313918802,
            "unit": "iter/sec",
            "range": "stddev: 0.01573843905062471",
            "extra": "mean: 413.88920600000273 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3768535142518013,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.653550948000003 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04113869264074845,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.30801602599996 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.061577973965298,
            "unit": "iter/sec",
            "range": "stddev: 0.005122891215080701",
            "extra": "mean: 326.62895033335343 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6624521004734476,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.509543103999988 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07700894472207775,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.985504523000031 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1166.1618576213052,
            "unit": "iter/sec",
            "range": "stddev: 0.00020981081115538093",
            "extra": "mean: 857.5138978046871 usec\nrounds: 1321"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 372.0289351760754,
            "unit": "iter/sec",
            "range": "stddev: 0.00011149315942142003",
            "extra": "mean: 2.6879629659094015 msec\nrounds: 352"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.46695853940679,
            "unit": "iter/sec",
            "range": "stddev: 0.00011544428844076918",
            "extra": "mean: 21.067286187502532 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.963917329606399,
            "unit": "iter/sec",
            "range": "stddev: 0.00009949773013296816",
            "extra": "mean: 201.4537981999979 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 925.6833982572035,
            "unit": "iter/sec",
            "range": "stddev: 0.00012827281618374529",
            "extra": "mean: 1.080282958388055 msec\nrounds: 769"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 217.3342101220065,
            "unit": "iter/sec",
            "range": "stddev: 0.0001107588184193858",
            "extra": "mean: 4.601208431192782 msec\nrounds: 218"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.72534757133626,
            "unit": "iter/sec",
            "range": "stddev: 0.00021035237529159806",
            "extra": "mean: 38.8721667307703 msec\nrounds: 26"
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
          "id": "62ec7ae1beb7010538f9c68a70b3d08db905f0dd",
          "message": "Refine tree type hierarchy, fix some docstrings (#353)\n\nRemoves the `NamedTreeObject` class and implements the `name` attribute\r\nin `TreeObjectBase` instead, since `TreeObjectBase` was already relying on\r\nthe existence of the name.\r\n\r\nAdds a `doc` parameter to all gRPC property helpers, which is then set\r\nas `__doc__` attribute on the created property.\r\nThis was previously defined only for `grpc_data_property_read_only`.\r\n\r\nImprove some docstrings.",
          "timestamp": "2024-01-26T09:43:16+01:00",
          "tree_id": "bec6d0649b33a18b6777657e9c20d7e4ada632a5",
          "url": "https://github.com/ansys-internal/pyacp/commit/62ec7ae1beb7010538f9c68a70b3d08db905f0dd"
        },
        "date": 1706258918772,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 6.413178743702671,
            "unit": "iter/sec",
            "range": "stddev: 0.0031286504944344866",
            "extra": "mean: 155.92891449999513 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.3460982317148016,
            "unit": "iter/sec",
            "range": "stddev: 0.009168038307238734",
            "extra": "mean: 426.23961199999866 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.3784782402917038,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6421598219999964 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.04112634257131423,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.315315621999986 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.3299108592771636,
            "unit": "iter/sec",
            "range": "stddev: 0.007584929262646581",
            "extra": "mean: 300.30833924998035 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6733893704353916,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4850249259999941 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.0769591896854004,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 12.993899806999991 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1216.0702019890214,
            "unit": "iter/sec",
            "range": "stddev: 0.0001908960578503164",
            "extra": "mean: 822.3209469028894 usec\nrounds: 1243"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 347.8479041105728,
            "unit": "iter/sec",
            "range": "stddev: 0.0002470930857997972",
            "extra": "mean: 2.874819678896565 msec\nrounds: 327"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.395536054398924,
            "unit": "iter/sec",
            "range": "stddev: 0.00019881579614653693",
            "extra": "mean: 21.099033437500008 msec\nrounds: 48"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.96509361931824,
            "unit": "iter/sec",
            "range": "stddev: 0.00011214898073716452",
            "extra": "mean: 201.4060713999811 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 884.7611536596529,
            "unit": "iter/sec",
            "range": "stddev: 0.0001744752323543899",
            "extra": "mean: 1.1302485375444917 msec\nrounds: 839"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 209.1567214220665,
            "unit": "iter/sec",
            "range": "stddev: 0.00024251992987610067",
            "extra": "mean: 4.781103821101002 msec\nrounds: 218"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.699796005500794,
            "unit": "iter/sec",
            "range": "stddev: 0.00018596204428231067",
            "extra": "mean: 38.91081469230183 msec\nrounds: 26"
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
          "id": "cc7c17d6a1919e7c00d76568268fea79ae85afa2",
          "message": "Various improvements to streamline example code (#350)\n\n* Add self contained example that builds an ACP model from a cdb file that just contains the mesh.\r\n* Add workflow helper to simplify file transfer operations\r\n* Move to_pyvista function one level lower so that the user does not have to specify the component enums.\r\n*Add tree printer\r\n\r\ncloses #343\r\ncloses #232",
          "timestamp": "2024-01-31T16:38:35Z",
          "tree_id": "a08a7a5f67db5156c09a782518ed2ddd2aeeafe5",
          "url": "https://github.com/ansys-internal/pyacp/commit/cc7c17d6a1919e7c00d76568268fea79ae85afa2"
        },
        "date": 1706719426349,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000000.0kbit]",
            "value": 5.992413765967357,
            "unit": "iter/sec",
            "range": "stddev: 0.006107977509573573",
            "extra": "mean: 166.87766216666944 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=1ms, rate=1000000.0kbit]",
            "value": 2.362654648268783,
            "unit": "iter/sec",
            "range": "stddev: 0.018359825655802617",
            "extra": "mean: 423.2527173333362 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=10ms, rate=1000000.0kbit]",
            "value": 0.37823164903249923,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.6438823999999954 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=100ms, rate=1000000.0kbit]",
            "value": 0.041034082937642574,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 24.36998534899999 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=10000.0kbit]",
            "value": 3.4068755514847164,
            "unit": "iter/sec",
            "range": "stddev: 0.002552031203703622",
            "extra": "mean: 293.524076500006 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=1000.0kbit]",
            "value": 0.6719406982983358,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4882265690000054 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_class40.py::test_class40[delay=0ms, rate=100.0kbit]",
            "value": 0.07648125122974596,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 13.075099895999983 sec\nrounds: 1"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000000.0kbit]",
            "value": 1208.1546321924209,
            "unit": "iter/sec",
            "range": "stddev: 0.00019079406790392471",
            "extra": "mean: 827.7086172200609 usec\nrounds: 1173"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=1ms, rate=1000000.0kbit]",
            "value": 363.7982087074781,
            "unit": "iter/sec",
            "range": "stddev: 0.00025068131217333644",
            "extra": "mean: 2.7487765911570974 msec\nrounds: 362"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=10ms, rate=1000000.0kbit]",
            "value": 47.35427246567263,
            "unit": "iter/sec",
            "range": "stddev: 0.0002555278072232623",
            "extra": "mean: 21.117418723408864 msec\nrounds: 47"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=100ms, rate=1000000.0kbit]",
            "value": 4.9612686359217335,
            "unit": "iter/sec",
            "range": "stddev: 0.00021525420141827232",
            "extra": "mean: 201.5613491999943 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=10000.0kbit]",
            "value": 826.5471750331095,
            "unit": "iter/sec",
            "range": "stddev: 0.0002447052343550784",
            "extra": "mean: 1.2098522990656189 msec\nrounds: 963"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=1000.0kbit]",
            "value": 204.17672678810683,
            "unit": "iter/sec",
            "range": "stddev: 0.0003143691809485006",
            "extra": "mean: 4.897717853209553 msec\nrounds: 218"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group[delay=0ms, rate=100.0kbit]",
            "value": 25.743015406050297,
            "unit": "iter/sec",
            "range": "stddev: 0.00020954170813076173",
            "extra": "mean: 38.84548815384593 msec\nrounds: 26"
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
          "id": "1bb85ddabcb6d6623edf74249287816a8a723872",
          "message": "Merge client and server functionality (#359)\n\nMerge the Client and Server classes into a single `ACP` class.\r\nThe server and file transfer functionality is exposed via composition,\r\nwhereas the model-related functions are implemented directly\r\nin the ACP class.",
          "timestamp": "2024-02-01T09:09:52+01:00",
          "tree_id": "26290b82f17383a601874fe90264f90d785265cd",
          "url": "https://github.com/ansys-internal/pyacp/commit/1bb85ddabcb6d6623edf74249287816a8a723872"
        },
        "date": 1706775132787,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.838928040567876,
            "unit": "iter/sec",
            "range": "stddev: 0.0028207496498770745",
            "extra": "mean: 146.22174616666447 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1195.8808515020828,
            "unit": "iter/sec",
            "range": "stddev: 0.00023419482574818488",
            "extra": "mean: 836.203706033049 usec\nrounds: 1558"
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
          "id": "c40819f68eb497267993be081bfb520bea48ad73",
          "message": "Update install instructions (#365)\n\nAdd explicit install for internal dependencies to the install\r\ninstructions in `README.rst`. This can be replaced by a simple\r\ninstall from PyPI once released.",
          "timestamp": "2024-02-01T16:25:57+01:00",
          "tree_id": "fe2c22225043dbd81000d85a37578a3fe3ebb992",
          "url": "https://github.com/ansys-internal/pyacp/commit/c40819f68eb497267993be081bfb520bea48ad73"
        },
        "date": 1706801332553,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.647525952486905,
            "unit": "iter/sec",
            "range": "stddev: 0.00847411237144519",
            "extra": "mean: 215.16824439999027 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 879.0805074570835,
            "unit": "iter/sec",
            "range": "stddev: 0.0003862562618363171",
            "extra": "mean: 1.1375522395470927 msec\nrounds: 1148"
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
          "id": "775b36fb300beb9ba8cb5d8cf130e7f04c1e5649",
          "message": "Enable listing the currently loaded Models (#358)\n\nAdd a `models` property to the `ACP` class, which returns a tuple containing\r\nall currently loaded models on the server.\r\n\r\nNote that we use a tuple instead of `MutableMapping` because the backend\r\ndoes not have a concept of `id` for the `Model`. The name cannot be used to\r\nreplace it, since it is not necessarily unique.\r\n\r\nCloses #271.",
          "timestamp": "2024-02-01T16:35:19+01:00",
          "tree_id": "1172609a04ee716414fc098adf1359c60b3a6880",
          "url": "https://github.com/ansys-internal/pyacp/commit/775b36fb300beb9ba8cb5d8cf130e7f04c1e5649"
        },
        "date": 1706801880767,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.316722847661868,
            "unit": "iter/sec",
            "range": "stddev: 0.004570596166875719",
            "extra": "mean: 188.0857867999964 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1069.2296937937494,
            "unit": "iter/sec",
            "range": "stddev: 0.00025103801443333444",
            "extra": "mean: 935.2527392424779 usec\nrounds: 1162"
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
          "id": "c63008af5ddea28af8fe8f2f1fb2aa0e357f5f87",
          "message": "Use the 'direct' launcher as fallback (#367)\n\nDefine the direct launcher as fallback launch mode, to be used\r\nwhen no launch mode is configured.\r\n\r\nSee https://github.com/ansys-internal/ansys-tools-local-product-launcher/pull/126",
          "timestamp": "2024-02-02T13:50:54+01:00",
          "tree_id": "0f410f3fb6a2b7d24a0d5908028aebc5a91ef2e6",
          "url": "https://github.com/ansys-internal/pyacp/commit/c63008af5ddea28af8fe8f2f1fb2aa0e357f5f87"
        },
        "date": 1706878392980,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.404315066957067,
            "unit": "iter/sec",
            "range": "stddev: 0.006156835238427721",
            "extra": "mean: 156.14472266667198 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1191.8312748990008,
            "unit": "iter/sec",
            "range": "stddev: 0.00021919089472377596",
            "extra": "mean: 839.0449395487989 usec\nrounds: 1373"
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
          "id": "6961ca0a83406590111fb70e07ac99d849af173a",
          "message": "Add options for partial documentation builds (#368)\n\nAdd the following options to run a partial doc build, controlled\r\nvia environment variables:\r\n- `PYACP_DOC_SKIP_GALLERY=true`: do not build the examples\r\n  gallery\r\n- `PYACP_DOC_SKIP_API=true`: do not build the API reference\r\n\r\nAdd a quick variant of the documentation build in CI which only\r\nbuilds the main pages (no API / examples). This build runs in parallel\r\nwith the full documentation build, to provider quicker feedback\r\non errors.\r\n\r\nAdd docstrings to the enum classes.",
          "timestamp": "2024-02-02T13:38:50Z",
          "tree_id": "8035eeedbaf676b6fd6b0de1a9c9caea8b98dcd7",
          "url": "https://github.com/ansys-internal/pyacp/commit/6961ca0a83406590111fb70e07ac99d849af173a"
        },
        "date": 1706881316860,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.453186281670784,
            "unit": "iter/sec",
            "range": "stddev: 0.006555512399374841",
            "extra": "mean: 224.5583132499931 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 897.970234488952,
            "unit": "iter/sec",
            "range": "stddev: 0.0003563358395559134",
            "extra": "mean: 1.113622658738922 msec\nrounds: 967"
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
          "id": "d2922c7836360ac8931f420c4c826ace73210023",
          "message": "Add scaffolding for improved documentation (#373)\n\nAdd a landing page using a grid to the documentation, containing the following sections:\r\n- Getting started\r\n- How-to guides\r\n- Examples\r\n- API reference\r\n- Contributing\r\n\r\nThe individual sections are still incomplete.\r\n\r\nCloses #372, #364",
          "timestamp": "2024-02-05T09:44:51+01:00",
          "tree_id": "46fcf980558b90de8caec05f4d61f05bf57372a8",
          "url": "https://github.com/ansys-internal/pyacp/commit/d2922c7836360ac8931f420c4c826ace73210023"
        },
        "date": 1707122881642,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.925888359459489,
            "unit": "iter/sec",
            "range": "stddev: 0.009673793017557476",
            "extra": "mean: 203.0090669999936 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 970.9666675322853,
            "unit": "iter/sec",
            "range": "stddev: 0.00041645176909600257",
            "extra": "mean: 1.029901471840947 msec\nrounds: 799"
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
          "id": "dd0ed346b3b63e32c661739a5ca590c44a389435",
          "message": "Ensure all exposed classes are documented (#363)\n\nEnable the `pydocstyle` pre-commit hook, and fix / add all reported docstrings.\r\n\r\nAdd `FeFormat`, `IgnorableEntity` and `PuckMaterialType` enums to the list of\r\npublic classes.\r\n\r\nNote: there is no explicit automated check that all exposed objects are included in the \r\ndocumentation's `.rst` files.",
          "timestamp": "2024-02-05T10:02:09+01:00",
          "tree_id": "1498baa5fa4d9bfca7c268591690eeaaa96b751b",
          "url": "https://github.com/ansys-internal/pyacp/commit/dd0ed346b3b63e32c661739a5ca590c44a389435"
        },
        "date": 1707123897530,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.488340685908835,
            "unit": "iter/sec",
            "range": "stddev: 0.005102573157361824",
            "extra": "mean: 154.1226098333226 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1220.3516443632468,
            "unit": "iter/sec",
            "range": "stddev: 0.000208910831258352",
            "extra": "mean: 819.4359425981503 usec\nrounds: 1324"
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
          "id": "9b6ea413ea2aaef1b1ab41a695bdce2dcd31b887",
          "message": "Add 'usage' section to the getting started documentation (#379)\n\nExtend the getting started section by providing some usage examples.\r\n\r\nCloses #374",
          "timestamp": "2024-02-05T09:15:38Z",
          "tree_id": "d8af6bc3c309e1be10f2437359b26723e26aa397",
          "url": "https://github.com/ansys-internal/pyacp/commit/9b6ea413ea2aaef1b1ab41a695bdce2dcd31b887"
        },
        "date": 1707124703066,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.882556076870006,
            "unit": "iter/sec",
            "range": "stddev: 0.004074446259995418",
            "extra": "mean: 145.29485685713033 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1217.7773526776691,
            "unit": "iter/sec",
            "range": "stddev: 0.00023122925590295763",
            "extra": "mean: 821.1681698638782 usec\nrounds: 1460"
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
          "id": "1eb256ad9484cafd798f5ac331f00b08cc37a7af",
          "message": "Update dev notebooks (#383)\n\n- Remove the dev notebooks, except for `connection_test.ipynb`\r\n- Update to the latest API\r\n- Add a note mentioning that these notebooks may be outdated",
          "timestamp": "2024-02-05T13:00:13Z",
          "tree_id": "51f8267c1dcf3235fbd6797be3adceae14adc995",
          "url": "https://github.com/ansys-internal/pyacp/commit/1eb256ad9484cafd798f5ac331f00b08cc37a7af"
        },
        "date": 1707138151117,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.329558535477247,
            "unit": "iter/sec",
            "range": "stddev: 0.0035286363908076388",
            "extra": "mean: 157.98890150000014 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1268.4870720025908,
            "unit": "iter/sec",
            "range": "stddev: 0.00020739086356894243",
            "extra": "mean: 788.3407108132968 usec\nrounds: 1193"
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
          "id": "0d3d18c7e07bd5352d38b4a374750891ba192872",
          "message": "Add a howto for printing the model tree (#390)\n\n- Add a howto section for printing the model tree\r\n- Change ``Lookup Table`` label to ``Lookup Tables``.",
          "timestamp": "2024-02-06T13:24:20+01:00",
          "tree_id": "eb86a56ad3008401693d58ffb311c5a513ad09c4",
          "url": "https://github.com/ansys-internal/pyacp/commit/0d3d18c7e07bd5352d38b4a374750891ba192872"
        },
        "date": 1707222465795,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.327148450624998,
            "unit": "iter/sec",
            "range": "stddev: 0.017009947827554602",
            "extra": "mean: 231.0990740000065 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 810.1513318202091,
            "unit": "iter/sec",
            "range": "stddev: 0.0005289815980005683",
            "extra": "mean: 1.2343372907296815 msec\nrounds: 1111"
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
          "id": "67fbbb645e7ac7845b677052c4fa24637bc803ad",
          "message": "Add concept page, explain 'store' concept (#388)\n\n* Add a separate page for concept explanations\r\n* Add an explanation of the stored / unstored concept\r\n\r\nCloses #382",
          "timestamp": "2024-02-06T13:29:24Z",
          "tree_id": "4bc8cb4bc72abd4a1dda595b46faa8166b984cf6",
          "url": "https://github.com/ansys-internal/pyacp/commit/67fbbb645e7ac7845b677052c4fa24637bc803ad"
        },
        "date": 1707226334545,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.774164686097351,
            "unit": "iter/sec",
            "range": "stddev: 0.001594603069635418",
            "extra": "mean: 209.46072575000585 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 851.4310683097974,
            "unit": "iter/sec",
            "range": "stddev: 0.0005910237993356624",
            "extra": "mean: 1.174493200001653 msec\nrounds: 965"
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
          "id": "9b2a437dc755367c1a084b35af3bca5a9ea8c437",
          "message": "Adapt ACPWorkflow to embedded cdb file (#395)\n\n* Update the workflow so it expects either a acph5 or a cdb file as input.",
          "timestamp": "2024-02-06T15:46:33Z",
          "tree_id": "c8f830beea19c71e413c13518aaf7339de639120",
          "url": "https://github.com/ansys-internal/pyacp/commit/9b2a437dc755367c1a084b35af3bca5a9ea8c437"
        },
        "date": 1707234565927,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.287477671687147,
            "unit": "iter/sec",
            "range": "stddev: 0.01158305887728952",
            "extra": "mean: 233.2373662500018 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 902.1781022516735,
            "unit": "iter/sec",
            "range": "stddev: 0.0004904193550453345",
            "extra": "mean: 1.1084285879962956 msec\nrounds: 983"
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
          "id": "1a5c7a29e15b5d8229929b899767b568792d6371",
          "message": "Support adding cad geometry from local files and refresh  (#394)\n\n* Support adding cad geometry from local files and refresh the cad geometry",
          "timestamp": "2024-02-07T09:06:32Z",
          "tree_id": "3467faa633c64b40b55d31121452df32e72aeb83",
          "url": "https://github.com/ansys-internal/pyacp/commit/1a5c7a29e15b5d8229929b899767b568792d6371"
        },
        "date": 1707296937446,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.9064393558263815,
            "unit": "iter/sec",
            "range": "stddev: 0.0007314931381950251",
            "extra": "mean: 144.79241016666342 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1097.2749215686085,
            "unit": "iter/sec",
            "range": "stddev: 0.0002800775452417004",
            "extra": "mean: 911.3486331852465 usec\nrounds: 1802"
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
          "id": "1a5c7a29e15b5d8229929b899767b568792d6371",
          "message": "Support adding cad geometry from local files and refresh  (#394)\n\n* Support adding cad geometry from local files and refresh the cad geometry",
          "timestamp": "2024-02-07T09:06:32Z",
          "tree_id": "3467faa633c64b40b55d31121452df32e72aeb83",
          "url": "https://github.com/ansys-internal/pyacp/commit/1a5c7a29e15b5d8229929b899767b568792d6371"
        },
        "date": 1707312475516,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.390589228526884,
            "unit": "iter/sec",
            "range": "stddev: 0.002942611077747298",
            "extra": "mean: 156.48009350000316 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1257.1596078675398,
            "unit": "iter/sec",
            "range": "stddev: 0.0002094629632393532",
            "extra": "mean: 795.4439466093352 usec\nrounds: 1180"
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
          "id": "211e4d73b120739de98e3fb82913baef76a95ae3",
          "message": "Direction Plots (#371)\n\n* Add plotter function",
          "timestamp": "2024-02-07T16:23:19Z",
          "tree_id": "64e37b5922a9036aca4ea128a7db95b350abbcfc",
          "url": "https://github.com/ansys-internal/pyacp/commit/211e4d73b120739de98e3fb82913baef76a95ae3"
        },
        "date": 1707323210273,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 3.9421107579103305,
            "unit": "iter/sec",
            "range": "stddev: 0.01842360242534613",
            "extra": "mean: 253.67120850000902 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 864.5123581690141,
            "unit": "iter/sec",
            "range": "stddev: 0.0004556434361082738",
            "extra": "mean: 1.1567214633205947 msec\nrounds: 777"
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
          "id": "f2ec33099ebb923c392da135cde2897fa498a81b",
          "message": "Add limitations section (#406)\n\nAdd 'Limitations' section to landing page. Remove 'Key features', since the header blurb already contains these.\r\n\r\nCloses #375",
          "timestamp": "2024-02-08T16:24:37+01:00",
          "tree_id": "afc25b5f75cef88db3b19173f49605ab0d46d6cf",
          "url": "https://github.com/ansys-internal/pyacp/commit/f2ec33099ebb923c392da135cde2897fa498a81b"
        },
        "date": 1707406048305,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.274919432568546,
            "unit": "iter/sec",
            "range": "stddev: 0.008421085279784118",
            "extra": "mean: 189.57635520000053 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1146.728343368477,
            "unit": "iter/sec",
            "range": "stddev: 0.00033675304819828474",
            "extra": "mean: 872.0461177950243 usec\nrounds: 798"
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
          "id": "26a0427943a3253e14f563ffe95d51eab718a290",
          "message": "Handle missing mesh query data (#403)\n\nAllow for missing data in mesh queries, setting the corresponding\r\ncomponent of the ElementalData or NodalData to None.\r\n\r\nAdapt example code to check for None where necessary.\r\n\r\nAdd test for partial elemental data on a ModelingPly.\r\n\r\nCloses #272",
          "timestamp": "2024-02-08T15:54:09Z",
          "tree_id": "962a6114bb5e8d8dd9fcf8175fb8244fc28d139b",
          "url": "https://github.com/ansys-internal/pyacp/commit/26a0427943a3253e14f563ffe95d51eab718a290"
        },
        "date": 1707407823928,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.780001740765375,
            "unit": "iter/sec",
            "range": "stddev: 0.003739492164622553",
            "extra": "mean: 147.49258750000158 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1233.1113555845782,
            "unit": "iter/sec",
            "range": "stddev: 0.00022536427770333722",
            "extra": "mean: 810.9567683982056 usec\nrounds: 1386"
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
          "id": "fbcf2ec43f6c2f1fc3e6dbc56544f66ffe593025",
          "message": "Remove Fabric.locked (#417)\n\nThe `locked` attribute of the fabric is not present in the API; remove it.\r\n\r\nCloses #98",
          "timestamp": "2024-02-11T22:15:06+01:00",
          "tree_id": "26717f82ca03e48cef7e256b2c5a9b1b1d1651dd",
          "url": "https://github.com/ansys-internal/pyacp/commit/fbcf2ec43f6c2f1fc3e6dbc56544f66ffe593025"
        },
        "date": 1707686257653,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.929662896114526,
            "unit": "iter/sec",
            "range": "stddev: 0.01207357749563526",
            "extra": "mean: 168.64365100000214 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1233.7157733442039,
            "unit": "iter/sec",
            "range": "stddev: 0.00021901190107533581",
            "extra": "mean: 810.5594672663736 usec\nrounds: 1222"
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
          "id": "9dae1188245e405be2fd869a4b5bf0f44a23f706",
          "message": "Improve usability of isotropic / orthotropic material property sets (#414)\n\nImprove the usability of property sets which can be either isotropic\r\nor orthotropic in the following ways (details below)\r\n1. Improve error message on unavailable attributes\r\n2. Allow constructing isotropic property sets directly\r\n3. Add concept documentation\r\n\r\nDetails:\r\n\r\n1.\r\nWhen a material property which is currently unavailable (due to\r\nthe difference between isotropic / orthotropic material property\r\nsets) is accessed (getter or setter), raise an AttributeError with\r\na specific exception message.\r\nTo achieve this, the property helpers for material properties get\r\ntwo new keyword arguments ``available_on_pb_type`` and\r\n``unavailable_msg``. The former determines which protobuf type\r\nneeds to be present for the property to be available, and the\r\nlatter gives the error message (enhanced automatically with\r\nthe attribute name).\r\n\r\n2.\r\nAdd classmethod constructors `from_isotropic_constants` and\r\n`from_orthotropic_constants` for directly creating a property\r\nset which is either isotropic or orthotropic. Previously, directly\r\nconstructed property sets would always be orthotropic. This\r\nchange removes the ability to pass the parameters on the\r\nmain constructor (`__init__`).\r\n\r\n3.\r\nAdd a concept page for material property sets, explaining the\r\ndifference between constant / variable property sets, as well\r\nas isotropic / orthotropic. Includes the validation rules for\r\nchanging ply type or assigning property sets.\r\n\r\nCloses #398",
          "timestamp": "2024-02-12T10:07:14Z",
          "tree_id": "07fd6f242a9d7e00229d1b49d067585c8d4d2de2",
          "url": "https://github.com/ansys-internal/pyacp/commit/9dae1188245e405be2fd869a4b5bf0f44a23f706"
        },
        "date": 1707732580975,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.90628181107446,
            "unit": "iter/sec",
            "range": "stddev: 0.0038382105289549804",
            "extra": "mean: 144.7957131428471 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1172.6341263483262,
            "unit": "iter/sec",
            "range": "stddev: 0.00024792066388204883",
            "extra": "mean: 852.7809122476059 usec\nrounds: 1584"
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
          "id": "ca4339f5fc919e4f5b55f2ddd7e606050bd71fee",
          "message": "Add 'connect' launch mode (#416)\n\nAdd a launch mode which connects to an existing ACP + Filetransfer server.\r\nCurrently, it is not supported to use only an ACP server (without filetransfer, e.g. on a local machine).\r\n\r\nAdapt the documentation to mention the connect launch mode.\r\n\r\nExpose the connect mode in the test configuration via the --server-urls CLI option.\r\n\r\nThe immediate use case for the 'connect' launch mode is quick iterations on tests: connecting to an existing docker-compose setup avoids the startup time present in both 'direct' and 'docker_compose' mode due to the license checkout.\r\n\r\nOther changes:\r\n- In the main README, remove the mention of configuring the launch mode, since the default (use unified install) should be enough for the common quickstart scenario\r\n- Update poetry lockfile",
          "timestamp": "2024-02-13T10:50:42+01:00",
          "tree_id": "5fc7d6b73000644965ac5fe04bae2c2e0b02c46b",
          "url": "https://github.com/ansys-internal/pyacp/commit/ca4339f5fc919e4f5b55f2ddd7e606050bd71fee"
        },
        "date": 1707818019213,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.413357138246848,
            "unit": "iter/sec",
            "range": "stddev: 0.004769616531639138",
            "extra": "mean: 155.9245771666724 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1288.3896028115603,
            "unit": "iter/sec",
            "range": "stddev: 0.00018933169073277392",
            "extra": "mean: 776.162736658051 usec\nrounds: 1143"
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
          "id": "d6fcff87e5bd4b27255881c12d05b529e332ce44",
          "message": "Get ansys-api-tools-filetransfer from public PyPI (#422)\n\nRemove the entry in ``pyproject.toml`` to get the filetransfer\r\nAPI package from the private PyPI instance.",
          "timestamp": "2024-02-13T13:42:32+01:00",
          "tree_id": "44aa48f05e3b4639c5ec0780524fac52e0bf3654",
          "url": "https://github.com/ansys-internal/pyacp/commit/d6fcff87e5bd4b27255881c12d05b529e332ce44"
        },
        "date": 1707828328732,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.21040981733316,
            "unit": "iter/sec",
            "range": "stddev: 0.007233892814003938",
            "extra": "mean: 191.92348300000504 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 967.4152033980157,
            "unit": "iter/sec",
            "range": "stddev: 0.00030054313361589045",
            "extra": "mean: 1.0336823284227197 msec\nrounds: 1154"
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
          "id": "a1e6c98b7f18903a328c0341b4d78685b1731611",
          "message": "Enable nitpicky doc build, add internal API docs (#421)\n\nEnable nitpicky mode when building the full docs in CI / CD.\r\n\r\nAdd an 'Internal objects' page to the API documentation. A warning is displayed on these objects not to use them directly (via a custom autosummary template).",
          "timestamp": "2024-02-13T13:00:59Z",
          "tree_id": "cff8e4a3c2432d481480a6b160304248c0505d04",
          "url": "https://github.com/ansys-internal/pyacp/commit/a1e6c98b7f18903a328c0341b4d78685b1731611"
        },
        "date": 1707829411827,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.769528165365165,
            "unit": "iter/sec",
            "range": "stddev: 0.004871057060287109",
            "extra": "mean: 147.72078283332726 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1208.7116784908762,
            "unit": "iter/sec",
            "range": "stddev: 0.00023504023524151775",
            "extra": "mean: 827.327159814108 usec\nrounds: 1508"
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
          "id": "77b25bab9c7e875792739aa361b3515d2f526020",
          "message": "Add plotting how-to (#409)\n\nAdd a how-to section for plotting the model, showcasing:\r\n- plotting the mesh\r\n- directions plotter\r\n- scalar data plot\r\n- vector data plot (on its own, and with mesh)\r\n- plotting CAD geometries\r\n\r\nAdd a 'scaling_factor' parameter to 'get_pyvista_glyphs', since this was needed to reasonably show the vector data (ply offset).\r\n\r\nAdd an example data key for the race car nose `.acph5`.\r\n\r\nSince the how-to needs to execute code, it's not run when `PYACP_DOC_SKIP_GALLERY=true` is set. If we need to individually control it, we can always add a separate env var later. In any case, it shouldn't be included in the \"quick\" CI doc build.\r\n\r\nCloses #380",
          "timestamp": "2024-02-13T15:58:06Z",
          "tree_id": "2b645ddbf0210332997d93dde49b72181927e85f",
          "url": "https://github.com/ansys-internal/pyacp/commit/77b25bab9c7e875792739aa361b3515d2f526020"
        },
        "date": 1707840044221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.735424930264023,
            "unit": "iter/sec",
            "range": "stddev: 0.003134232309414982",
            "extra": "mean: 148.46873216665793 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1209.5710771645868,
            "unit": "iter/sec",
            "range": "stddev: 0.00023351721354033936",
            "extra": "mean: 826.7393449454394 usec\nrounds: 1464"
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
          "id": "86c3806d8dd353f9f5a39fe82d93387ca3f4374a",
          "message": "Ensure only a single object instance exists per tree object (#415)\n\nEnsure only a single instance refers to the same tree object or container.\r\n\r\nAdd a mixin class `ObjectCacheMixin` which adds a class attribute \r\n`_OBJECT_CACHE` to each of its subclasses. The object cache is a \r\n`WeakValueDictionary`, meaning the instances will be properly deleted\r\nonce their refcount _outside_ of the object cache goes to zero.\r\n\r\nThe `ObjectCacheMixin` subclasses need to provide a method `_cache_key_valid`; \r\nthis enables making certain cache key values disallowed. In particular, empty \r\nresource paths are not considered valid for tree objects.\r\n\r\nA decorator `constructor_with_cache` is provided to decorate constructor\r\nclassmethods s.t. they use the cache.\r\n\r\nThe arguments to the `__init__` method in the container classes `Mapping`, \r\n`MutableMapping`, `LinkedObjectList` and `EdgePropertyList` are prefixed\r\nwith underscores, to prevent accidental use of the direct constructor.\r\n\r\nTree objects which are directly instantiated are added to the cache during \r\n`.store()`.",
          "timestamp": "2024-02-14T14:13:45+01:00",
          "tree_id": "88b6a53485d2a14ff8e63c9fb2d5e581607b32b4",
          "url": "https://github.com/ansys-internal/pyacp/commit/86c3806d8dd353f9f5a39fe82d93387ca3f4374a"
        },
        "date": 1707916601067,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.3041847377573905,
            "unit": "iter/sec",
            "range": "stddev: 0.015220732032072538",
            "extra": "mean: 232.33203520001098 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 820.2250097842266,
            "unit": "iter/sec",
            "range": "stddev: 0.0005418441338572378",
            "extra": "mean: 1.2191776501219662 msec\nrounds: 1229"
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
          "id": "c1255f78f870d80388cfc154bae7fab4943d2bdb",
          "message": "Allow linking to CutoffSelectionRule from ModelingPly (#424)\n\nAdd the CutoffSelectionRule to the allowed selection rule types if the parent is not a BooleanSelectionRule.\r\n\r\nFix the docstring of LinkedSelectionRule, since CutoffSelectionRule and BooleanSelectionRule are disallowed only when the parent is a BoolenSelectionRule (not for ModelingPly).\r\n\r\nAdd a check for the operation type when linking to a CutoffSelectionRule, to avoid a hidden conversion.\r\n\r\nCloses #412",
          "timestamp": "2024-02-14T13:38:03Z",
          "tree_id": "551372b515dfb5e7f39c54f27e943c1934f31924",
          "url": "https://github.com/ansys-internal/pyacp/commit/c1255f78f870d80388cfc154bae7fab4943d2bdb"
        },
        "date": 1707918020686,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.525209868285993,
            "unit": "iter/sec",
            "range": "stddev: 0.00301342494052015",
            "extra": "mean: 153.25177583333036 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1108.2935215400441,
            "unit": "iter/sec",
            "range": "stddev: 0.0002617961475046732",
            "extra": "mean: 902.2880496589357 usec\nrounds: 1611"
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
          "id": "699f7cfe2c1fcd021b4b79720e4d5cdcb24c51e6",
          "message": "Add runtime type check for grpc_link_property (#429)\n\nAdd a runtime type check in the setter of grpc_link_property, which\r\ngives a nice error when the wrong object type is passed.\r\n\r\nAddresses the second point in #408.",
          "timestamp": "2024-02-16T08:25:53Z",
          "tree_id": "2f74072ad5cd6410c2b8628450c4919c778eb913",
          "url": "https://github.com/ansys-internal/pyacp/commit/699f7cfe2c1fcd021b4b79720e4d5cdcb24c51e6"
        },
        "date": 1708072088517,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.775791312764555,
            "unit": "iter/sec",
            "range": "stddev: 0.002741846490869992",
            "extra": "mean: 147.58423833333723 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1066.6374777260796,
            "unit": "iter/sec",
            "range": "stddev: 0.00029571498691788713",
            "extra": "mean: 937.5256550443537 usec\nrounds: 1893"
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
          "id": "a8775827e34061f8594afb5ccf0147ecb869c035",
          "message": "use latest version of ansys-tools-path to ensure that also the latest… (#430)\n\nuse latest version of ansys-tools-path to ensure that also the latest dev version of the unified installer is found",
          "timestamp": "2024-02-16T12:44:20+01:00",
          "tree_id": "b49b1710e09c25c93e536eed8dd5af059f200db3",
          "url": "https://github.com/ansys-internal/pyacp/commit/a8775827e34061f8594afb5ccf0147ecb869c035"
        },
        "date": 1708084029198,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.757041534142661,
            "unit": "iter/sec",
            "range": "stddev: 0.007218400645921581",
            "extra": "mean: 210.21468759999493 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 917.1837531522006,
            "unit": "iter/sec",
            "range": "stddev: 0.00039782444450165794",
            "extra": "mean: 1.090294062191109 msec\nrounds: 1013"
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
          "id": "4b4d4a1244e9dd6b533d3299bc47823a87684b4d",
          "message": "Sandwich and selection rule examples (#423)\n\n* Add new examples for a sandwich panel, basic and advanced selection rules.\r\n* Small improvement to the Virtual Geometries API\r\n* Add tests for the create method with non-default arguments for all the objects.",
          "timestamp": "2024-02-19T12:01:24+01:00",
          "tree_id": "bfe078d998aec95dd40d6f95234cc1048c7495c8",
          "url": "https://github.com/ansys-internal/pyacp/commit/4b4d4a1244e9dd6b533d3299bc47823a87684b4d"
        },
        "date": 1708340667379,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.714491133554726,
            "unit": "iter/sec",
            "range": "stddev: 0.005114748324784435",
            "extra": "mean: 212.1119695999937 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 890.4382059383754,
            "unit": "iter/sec",
            "range": "stddev: 0.000423666987564717",
            "extra": "mean: 1.1230425573958436 msec\nrounds: 906"
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
          "id": "1a4b36cc7700a596d494681ceab4cfc48723354c",
          "message": "Improve usability of edge property lists (#433)\n\n* Improve usability of edge property lists\r\n\r\n* Add type checks to the GenericEdgePropertyType classes (FabricWithAngle,\r\n  LinkedSelectionRule etc.), to check that the linked object is of\r\n  the right type. This avoids raising an obscure resource path\r\n  validation error.\r\n* In the EdgePropertyList, check that the linked objects are of the\r\n  correct type (e.g. FabricWithAngle), and raise a nice exception\r\n  otherwise\r\n* Add ``add_*`` methods to append a linked object, using the same\r\n  parameters as instantiating the GenericEdgePropertyType.\r\n\r\n* Update stackup.fabric test\r\n\r\n* add more unit tests\r\n\r\n* fix the new unit test of sub-laminate\r\n\r\n* run pre-commit hook\r\n\r\n---------\r\n\r\nCo-authored-by: René Roos <rene.roos@ansys.com>",
          "timestamp": "2024-02-20T13:59:30+01:00",
          "tree_id": "e79f9a843bc6180e832a97db771ed60b27feee20",
          "url": "https://github.com/ansys-internal/pyacp/commit/1a4b36cc7700a596d494681ceab4cfc48723354c"
        },
        "date": 1708434181045,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.3119344445222945,
            "unit": "iter/sec",
            "range": "stddev: 0.00992292176060049",
            "extra": "mean: 231.9144719999997 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 797.9125537096762,
            "unit": "iter/sec",
            "range": "stddev: 0.0006155822149049252",
            "extra": "mean: 1.2532701677029312 msec\nrounds: 1127"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "133802577+nshum4@users.noreply.github.com",
            "name": "Nellie Shum",
            "username": "nshum4"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "8ff834a71761b940e2f13d9334045cb74408e862",
          "message": "Changed header to lowercase (#434)\n\nchanged to lower case",
          "timestamp": "2024-02-21T10:17:39-05:00",
          "tree_id": "e1627ce958589b68fed90d1028186aedb5205666",
          "url": "https://github.com/ansys-internal/pyacp/commit/8ff834a71761b940e2f13d9334045cb74408e862"
        },
        "date": 1708528807221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.381317150614403,
            "unit": "iter/sec",
            "range": "stddev: 0.003093817854115896",
            "extra": "mean: 156.70745966664867 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1197.6395152113525,
            "unit": "iter/sec",
            "range": "stddev: 0.00021016072651389256",
            "extra": "mean: 834.975789708747 usec\nrounds: 1341"
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
          "id": "49d68449916c45a39fc6341d602cd3455e050b1a",
          "message": "rename property modeling_plies of ModelingGroup to plies because the … (#440)\n\n* rename property modeling_plies of ModelingGroup to plies because the entries of plies can be of type modeling ply, interface layer, butt-joint sequence.\r\n\r\n* update docu (plot ply data)",
          "timestamp": "2024-02-22T14:27:55+01:00",
          "tree_id": "c114c3cd012f84cf35396c50e2309e7fc7483fe8",
          "url": "https://github.com/ansys-internal/pyacp/commit/49d68449916c45a39fc6341d602cd3455e050b1a"
        },
        "date": 1708608632989,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.71098908988982,
            "unit": "iter/sec",
            "range": "stddev: 0.0039374614078341585",
            "extra": "mean: 175.10101739999868 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1040.3397121464384,
            "unit": "iter/sec",
            "range": "stddev: 0.0006373592969069215",
            "extra": "mean: 961.2244811233736 usec\nrounds: 1139"
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
          "id": "297257be55830218aa1ac953b60baeff27d3cb07",
          "message": "Complete docs for element set (#442)\n\nComplete docs for element set",
          "timestamp": "2024-02-22T14:07:49Z",
          "tree_id": "2b3c7df56c2c4d1e8665549c9be76f0ed611fdc9",
          "url": "https://github.com/ansys-internal/pyacp/commit/297257be55830218aa1ac953b60baeff27d3cb07"
        },
        "date": 1708611066305,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.5049808189675655,
            "unit": "iter/sec",
            "range": "stddev: 0.014017841708610649",
            "extra": "mean: 221.97652779999544 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 906.6716753302462,
            "unit": "iter/sec",
            "range": "stddev: 0.0003148053462238284",
            "extra": "mean: 1.1029350835689886 msec\nrounds: 1065"
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
          "id": "76f6a28e446c07099ae692aa0df9819420a9900b",
          "message": "Document creation of input files. (#446)\n\n* Document creation of input files\r\n\r\n* Disable warning is error for quick builds, because some links from doc to gallery cannot resolved",
          "timestamp": "2024-02-22T14:19:16Z",
          "tree_id": "e5d478301ad6c25d34f0086f3f808c447bc0ecff",
          "url": "https://github.com/ansys-internal/pyacp/commit/76f6a28e446c07099ae692aa0df9819420a9900b"
        },
        "date": 1708611715104,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.242794774364614,
            "unit": "iter/sec",
            "range": "stddev: 0.0031253229265014557",
            "extra": "mean: 160.18466666666598 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1192.3171665798836,
            "unit": "iter/sec",
            "range": "stddev: 0.00021949773579564048",
            "extra": "mean: 838.7030129478568 usec\nrounds: 1313"
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
          "id": "66c33a64b4a9d274bd02b6568227af299eb1d440",
          "message": "Add unit_system kwarg to Workflow.from_cdb_file (#436)\n\n* Add unit_system kwarg to Workflow\r\n\r\n* Don't mention abaqus and nastran files as input for workflow. \r\n\r\n* Make unit system mandatory iff it is not defined in the unit input file\r\n\r\n* Add tests to check unit system behaviour",
          "timestamp": "2024-02-22T14:45:17Z",
          "tree_id": "7bbb5d9a498254867ccd8cfdd77e7f565bb1c2cb",
          "url": "https://github.com/ansys-internal/pyacp/commit/66c33a64b4a9d274bd02b6568227af299eb1d440"
        },
        "date": 1708613274122,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.402209045525757,
            "unit": "iter/sec",
            "range": "stddev: 0.002623387273671273",
            "extra": "mean: 156.19608683331876 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1245.8787377693554,
            "unit": "iter/sec",
            "range": "stddev: 0.0002251154849132537",
            "extra": "mean: 802.6463328127894 usec\nrounds: 1283"
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
          "id": "5e88c1180f536941c546f7719782500ef767f403",
          "message": "Feat/thickness definition example (#439)\n\n* Add thickness definition example\r\n* Remove start from existing project examples.\r\n* Start from existing projects for more complex examples.",
          "timestamp": "2024-02-22T15:01:42Z",
          "tree_id": "7804b6bf7beec3014c09a740ff06c098b1d62a5f",
          "url": "https://github.com/ansys-internal/pyacp/commit/5e88c1180f536941c546f7719782500ef767f403"
        },
        "date": 1708614300776,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.954290531481187,
            "unit": "iter/sec",
            "range": "stddev: 0.005240697454282062",
            "extra": "mean: 201.8452477999972 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 822.5021280593986,
            "unit": "iter/sec",
            "range": "stddev: 0.00044728293980320245",
            "extra": "mean: 1.2158023254716528 msec\nrounds: 1484"
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
          "id": "913f1fb92b3995e8b9830e0035a984be35e09029",
          "message": "Block accessing root_shapes if cad geometry is out-of-date (#450)\n\n* add optional check for grpc properties that they can be accessed only if the parent object is up-to-date\r\n\r\n* patch of pre-commit run\r\n\r\n* use StatusType instead of string value.",
          "timestamp": "2024-02-26T08:55:01Z",
          "tree_id": "2a74945d32e9b6df46a631d84d2c54e66740a7df",
          "url": "https://github.com/ansys-internal/pyacp/commit/913f1fb92b3995e8b9830e0035a984be35e09029"
        },
        "date": 1708937869551,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.482290272236488,
            "unit": "iter/sec",
            "range": "stddev: 0.0037480166887044154",
            "extra": "mean: 154.26646416668177 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1311.2528012782197,
            "unit": "iter/sec",
            "range": "stddev: 0.00018687796004101907",
            "extra": "mean: 762.6294479792089 usec\nrounds: 1163"
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
          "id": "74d843a45b500cf30507c2d5230966a0ba8e5b88",
          "message": "Define _GRPC_PROPERTIES in GrpcObjectBase (#452)\n\nDefine the _GRPC_PROPERTIES class attribute as an empty tuple\r\nin the GrpcObjectBase class, instead of only declaring its type.\r\n\r\nThis makes mypy understand that the attribute is set; otherwise\r\nit does not recognize this since the attribute is set dynamically\r\nin the `mark_grpc_properties` class decorator.\r\n\r\nCloses #419.",
          "timestamp": "2024-02-26T11:58:23+01:00",
          "tree_id": "88d374e595f9b01245ca0a9c69fae1f2f04a7891",
          "url": "https://github.com/ansys-internal/pyacp/commit/74d843a45b500cf30507c2d5230966a0ba8e5b88"
        },
        "date": 1708945266311,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.631278561268666,
            "unit": "iter/sec",
            "range": "stddev: 0.0038334121704749037",
            "extra": "mean: 150.80048150000871 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1183.324645081839,
            "unit": "iter/sec",
            "range": "stddev: 0.0002474039252874205",
            "extra": "mean: 845.0766272436081 usec\nrounds: 1505"
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
          "id": "ae66fdf03067dfcc3c68f5220905dabc7d1e2e85",
          "message": "Revert renaming 'modeling_plies' to 'plies' (#456)\n\nRevert the rename of 'modeling_plies' to 'plies'. This change\r\nwas originally made to accommodate butt joint sequences and\r\ninterface layers in the collection.\r\nHowever, the current type of the collection (MutableMapping)\r\nis not well-suited to this since it is\r\n- not polymorphic\r\n- not ordered\r\n\r\nThe current plan is to add MutableMapping exposure also for\r\n``butt_joint_sequences`` and ``interface_layers``, and then\r\nadd a _different_ collection as ``plies``, which contains\r\nall different objects which are to be sorted by global ply\r\nnumber.\r\n\r\nThis reverts commit 49d68449916c45a39fc6341d602cd3455e050b1a.",
          "timestamp": "2024-02-26T22:33:23+01:00",
          "tree_id": "2d113cacff4a4a6771a9ac888cd2f297ec7be071",
          "url": "https://github.com/ansys-internal/pyacp/commit/ae66fdf03067dfcc3c68f5220905dabc7d1e2e85"
        },
        "date": 1708983417177,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.16305091894636,
            "unit": "iter/sec",
            "range": "stddev: 0.004188737470234343",
            "extra": "mean: 193.68393140001672 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1052.009680875362,
            "unit": "iter/sec",
            "range": "stddev: 0.0002580462740154326",
            "extra": "mean: 950.5615948019744 usec\nrounds: 1039"
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
          "id": "db58936e167db93697d341e68703136b11d3376a",
          "message": "Move clone definition to CreatableTreeObject (#459)\n\nOnly objects which can be created directly should be clonable,\r\nsince the 'unlinked' representation doesn't have any value\r\notherwise.\r\n\r\nCloses #454.",
          "timestamp": "2024-02-26T21:44:15Z",
          "tree_id": "bad402e2b75d5add9ea5842c144a9e4e7b4985a3",
          "url": "https://github.com/ansys-internal/pyacp/commit/db58936e167db93697d341e68703136b11d3376a"
        },
        "date": 1708984078086,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.507695430016811,
            "unit": "iter/sec",
            "range": "stddev: 0.006632982774446517",
            "extra": "mean: 221.84284975000423 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 960.2453549958573,
            "unit": "iter/sec",
            "range": "stddev: 0.0002471738105552616",
            "extra": "mean: 1.0414005074820845 msec\nrounds: 802"
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
          "id": "8cee8df84269d9fb354bd4db83bb57fa17feabf3",
          "message": "Add file management how-to (#462)\n\nAdd how-to section for file management, covering\r\n- using a workflow\r\n- using manual file up- and download\r\n\r\nfor creating a model from a ``.cdb``, and storing the ``.acph5``.\r\n\r\nCloses #381",
          "timestamp": "2024-02-26T21:59:16Z",
          "tree_id": "46fdd363c93c3ad2a469199f6dc99b09298dbde1",
          "url": "https://github.com/ansys-internal/pyacp/commit/8cee8df84269d9fb354bd4db83bb57fa17feabf3"
        },
        "date": 1708984939242,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.108142283054474,
            "unit": "iter/sec",
            "range": "stddev: 0.004907273784572324",
            "extra": "mean: 163.71589816665733 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1245.6182809106351,
            "unit": "iter/sec",
            "range": "stddev: 0.00018720944583621796",
            "extra": "mean: 802.8141649213187 usec\nrounds: 1146"
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
          "id": "da4a72a651067b433c288ff2a22f41dae1f2fc30",
          "message": "Document loading an pyACP project in the ACP gui (#447)\n\n* Document loading an pyACP project in the ACP gui. \r\n* Rename get_local_acp_h5_file to get_local_acph5_file",
          "timestamp": "2024-02-27T10:33:27Z",
          "tree_id": "ea756304fe2296006e6a56b53085a27bab7ef9f0",
          "url": "https://github.com/ansys-internal/pyacp/commit/da4a72a651067b433c288ff2a22f41dae1f2fc30"
        },
        "date": 1709030187060,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.419021934462526,
            "unit": "iter/sec",
            "range": "stddev: 0.0036678207838257947",
            "extra": "mean: 155.78697349999496 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1205.6965362164397,
            "unit": "iter/sec",
            "range": "stddev: 0.000237013679134342",
            "extra": "mean: 829.3960959181903 usec\nrounds: 1470"
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
          "id": "eba2434dabd61a9cc341f9ce4af9f0c7119c76fa",
          "message": "Reenable warning as error on quick doc build (#461)\n\nAdd back the '-W' flag to the 'quick' doc build, by manually\r\ncreating a placeholder reference for interlinked gallery examples\r\nwhich don't exist.",
          "timestamp": "2024-02-27T10:46:09Z",
          "tree_id": "fa95444fc2ac99311d20f61e517d399b881a2845",
          "url": "https://github.com/ansys-internal/pyacp/commit/eba2434dabd61a9cc341f9ce4af9f0c7119c76fa"
        },
        "date": 1709030931509,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.355288535189111,
            "unit": "iter/sec",
            "range": "stddev: 0.005319448231010199",
            "extra": "mean: 157.34926816666453 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1218.489855814717,
            "unit": "iter/sec",
            "range": "stddev: 0.0002040856970127773",
            "extra": "mean: 820.6879977112092 usec\nrounds: 1311"
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
          "id": "318a183dabbdf5abff62008680b8bbdb3c43cdca",
          "message": "Update pre-commit hooks (#465)\n\nUpdate the pre-commit hooks to the latest version. Includes the\r\n2024 style of the black formatter.",
          "timestamp": "2024-02-27T12:56:24+01:00",
          "tree_id": "b994f189828290934d5010f0683e0d2b8f2acb1b",
          "url": "https://github.com/ansys-internal/pyacp/commit/318a183dabbdf5abff62008680b8bbdb3c43cdca"
        },
        "date": 1709035188947,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.552164974610254,
            "unit": "iter/sec",
            "range": "stddev: 0.011881651725002223",
            "extra": "mean: 219.67569400000002 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 908.6788748705967,
            "unit": "iter/sec",
            "range": "stddev: 0.00034318944749410415",
            "extra": "mean: 1.1004987874758374 msec\nrounds: 974"
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
          "id": "cd188e5569ba867ef0399632f72ae27cbdfc674f",
          "message": "Add missing CI stages (#466)\n\nAdd or update the following CI stages:\r\n- `build-wheelhouse`: added, but commented-out while dependencies are private\r\n- `release`: added\r\n- `upload_docs_release`: added\r\n- `upload_docs_dev`: changed `needs` to `build` instead of `docs`\r\n- `build`: added `needs`",
          "timestamp": "2024-02-27T12:10:03Z",
          "tree_id": "1fd3952b662e22a14fcef327587cd290ce77f1bb",
          "url": "https://github.com/ansys-internal/pyacp/commit/cd188e5569ba867ef0399632f72ae27cbdfc674f"
        },
        "date": 1709035959275,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.476151130385574,
            "unit": "iter/sec",
            "range": "stddev: 0.005823377238320227",
            "extra": "mean: 154.41270283333589 msec\nrounds: 6"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1253.7735121454061,
            "unit": "iter/sec",
            "range": "stddev: 0.00022167346582783307",
            "extra": "mean: 797.5922208540206 usec\nrounds: 1381"
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
          "id": "e8945ee87338284d3d1603b985ddcbcf39dd5713",
          "message": "Add coverage upload in CI testing (#467)\n\n* Generate and upload coverage information in CI.\r\n* Add coverage configuration to ``pyproject.toml``.",
          "timestamp": "2024-02-28T08:22:16+01:00",
          "tree_id": "798417b05ba9137f25c2eed86abbdfa3c715ace4",
          "url": "https://github.com/ansys-internal/pyacp/commit/e8945ee87338284d3d1603b985ddcbcf39dd5713"
        },
        "date": 1709105136922,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.127167920540115,
            "unit": "iter/sec",
            "range": "stddev: 0.015359454909083909",
            "extra": "mean: 195.03944779999642 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1097.7580560794777,
            "unit": "iter/sec",
            "range": "stddev: 0.0002253401431633526",
            "extra": "mean: 910.9475393616242 usec\nrounds: 940"
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
          "id": "08c39db15dd5cd4160720179b6571851098110a7",
          "message": "Add CONTRIBUTORS.md file (#470)",
          "timestamp": "2024-02-28T09:30:12+01:00",
          "tree_id": "ea16ebe12b88b6c2b71fe876c5c4c952f837b066",
          "url": "https://github.com/ansys-internal/pyacp/commit/08c39db15dd5cd4160720179b6571851098110a7"
        },
        "date": 1709109207415,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 7.496678545699534,
            "unit": "iter/sec",
            "range": "stddev: 0.004212581421357301",
            "extra": "mean: 133.39240757143702 msec\nrounds: 7"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1320.9031335290429,
            "unit": "iter/sec",
            "range": "stddev: 0.00018233782858097675",
            "extra": "mean: 757.0577846448972 usec\nrounds: 1537"
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
          "id": "4fb9df91318bec1a73eb372bfc6980886f9d9ec3",
          "message": "Update documentation dependencies (#468)",
          "timestamp": "2024-02-28T09:10:52Z",
          "tree_id": "abedef0f379f311dff1d261ba07239dc4576f832",
          "url": "https://github.com/ansys-internal/pyacp/commit/4fb9df91318bec1a73eb372bfc6980886f9d9ec3"
        },
        "date": 1709111677631,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.204936830474913,
            "unit": "iter/sec",
            "range": "stddev: 0.007354181619906273",
            "extra": "mean: 237.81570099997396 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1003.2452176207578,
            "unit": "iter/sec",
            "range": "stddev: 0.00060131183378858",
            "extra": "mean: 996.7652797503945 usec\nrounds: 479"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "9f828bab7fb9668023369baa1d226741c14f7350",
          "message": "feat: tech review (#471)\n\n- Update badge on main README\r\n- Clean up of main README refs to private PyPI and tokens\r\n- Ordering contributors in alphabetical order\r\n- Use ``ansys-api-acp`` package version from public PyPI\r\n- Formatting ``pyproject.toml`` and missing classifiers\r\n- Remove private PyPI refs\r\n- Add AUTHORS file\r\n- Add year range to LICENSE file\r\n- Update to vale 3.1.0 (foreseeing change in ansys/actions v6)\r\n- Build wheel using ansys/actions v5\r\n- Change ansys-api-acp URLs\r\n- Upload benchmark tests on MAIN_PYTHON_VERSION",
          "timestamp": "2024-02-28T15:51:59+01:00",
          "tree_id": "bbdc5c8aa7f0349679ab3a4c761af3bf94bba158",
          "url": "https://github.com/ansys-internal/pyacp/commit/9f828bab7fb9668023369baa1d226741c14f7350"
        },
        "date": 1709132142614,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 3.849928819821059,
            "unit": "iter/sec",
            "range": "stddev: 0.017785110404899763",
            "extra": "mean: 259.745061999998 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 879.1896476139943,
            "unit": "iter/sec",
            "range": "stddev: 0.0003560319194097233",
            "extra": "mean: 1.1374110269767952 msec\nrounds: 1075"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b6bd26c8a4698c38c97332ded792dfd8980d8a44",
          "message": "fix: urls (#474)\n\n* fix: urls\r\n\r\n* fix: ghcr.io urls\r\n\r\n* fix: other repo URLs\r\n\r\n* update lock file",
          "timestamp": "2024-02-28T16:22:24Z",
          "tree_id": "3621c5883c9f2a284ee8b57acc7468e5e2445a9f",
          "url": "https://github.com/ansys/pyacp/commit/b6bd26c8a4698c38c97332ded792dfd8980d8a44"
        },
        "date": 1709137586985,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.790350111792092,
            "unit": "iter/sec",
            "range": "stddev: 0.00118239866703262",
            "extra": "mean: 208.75300899998214 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1239.6268295695204,
            "unit": "iter/sec",
            "range": "stddev: 0.00018442714445654148",
            "extra": "mean: 806.6943826532582 usec\nrounds: 980"
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
          "id": "fc72cd3caecdb2c0e8f864ad523c44ff2c6eaed9",
          "message": "Fix material property sets concept page (#451)\n\nClarify the difference between stress-/strain limits and engineering constants\r\nin the material property sets concept page.\r\n\r\nMake it clear that the stress-/strain limits use independent attributes in the\r\nisotropic / orthotropic cases, whereas the engineering constants are related\r\nfor the two cases and must follow the conversion and assignment rules.\r\n\r\nCloses #428.",
          "timestamp": "2024-02-29T11:19:06+01:00",
          "tree_id": "0510b5ece126674df5c3bbaf3d7b3e03a81221df",
          "url": "https://github.com/ansys/pyacp/commit/fc72cd3caecdb2c0e8f864ad523c44ff2c6eaed9"
        },
        "date": 1709202165097,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.17531454916553,
            "unit": "iter/sec",
            "range": "stddev: 0.013349482282079208",
            "extra": "mean: 239.50291366667406 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1006.9708253802836,
            "unit": "iter/sec",
            "range": "stddev: 0.0004610123625741243",
            "extra": "mean: 993.0774306418945 usec\nrounds: 966"
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
          "id": "b352381d631cd8dc32e265607981ba8129159059",
          "message": "Use released version of internal dependencies (#476)\n\n- Use the released version of ``ansys-tools-filetransfer`` and\r\n  ``ansys-tools-local-product-launcher``.\r\n- Remove now-unnecessary token injection in CI.\r\n\r\nCloses #399.",
          "timestamp": "2024-02-29T15:44:12+01:00",
          "tree_id": "1b07291bd8c4c42129e4f19027d446c510a952ae",
          "url": "https://github.com/ansys/pyacp/commit/b352381d631cd8dc32e265607981ba8129159059"
        },
        "date": 1709218058288,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 3.961120001609929,
            "unit": "iter/sec",
            "range": "stddev: 0.007737539983727772",
            "extra": "mean: 252.45385133335202 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 866.4197496270936,
            "unit": "iter/sec",
            "range": "stddev: 0.00040387274000148766",
            "extra": "mean: 1.1541749832346264 msec\nrounds: 1193"
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
          "id": "221121ab9c3469bff38dc768c5629fc869070b67",
          "message": "Improve gallery thumbnails and theme (#469)\n\nSelect gallery thumbnails by setting the \r\n``# sphinx_gallery_thumbnail_number = <nr>`` comment.\r\nTo avoid this comment showing up in the rendered example, the\r\n``remove_config_comments`` option is set to ``True``, and the\r\ncomment itself is hidden within a code block (i.e., it cannot\r\nbe on its own, otherwise the rendered example has an empty code\r\nblock).\r\n\r\nImport ``ansys.mapdl.core`` and ``ansys.dpf.core`` in ``conf.py``\r\nbefore setting the PyVista theme, otherwise these imports\r\noverride the theme.\r\nRemove the workaround of manually importing PyMAPDL in\r\nthe example, since it should anyway become obsolete with the\r\nupcoming PyMAPDL release.\r\n\r\nRemove setting the PyVista window size, otherwise text within\r\nthe plot is too small.\r\n\r\nUse the reversed ``viridis_r`` colormap (instead of the default \r\n``viridis``), so that small values are light, and large values dark.",
          "timestamp": "2024-03-04T09:39:03Z",
          "tree_id": "5b136e17c7927d3640ba00f4fb103020e6d003b2",
          "url": "https://github.com/ansys/pyacp/commit/221121ab9c3469bff38dc768c5629fc869070b67"
        },
        "date": 1709545327085,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.284050173942662,
            "unit": "iter/sec",
            "range": "stddev: 0.0057119626155935875",
            "extra": "mean: 189.24877075000524 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1168.8566175096234,
            "unit": "iter/sec",
            "range": "stddev: 0.0002300658719816166",
            "extra": "mean: 855.536928156859 usec\nrounds: 1378"
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
          "id": "eb7f1710ec0a0939b32ecf115c36d4ea82405468",
          "message": "Add rosette example (#448)\n\n* Add rosette example\r\n* Allow passing Optional VectorData objects to the plotter.\r\n* Add edge set to Rosette and Rosette example.\r\n* Update lock file",
          "timestamp": "2024-03-04T14:28:01+01:00",
          "tree_id": "1f1e98f2a205063122a5736f6ce2db960351b0da",
          "url": "https://github.com/ansys/pyacp/commit/eb7f1710ec0a0939b32ecf115c36d4ea82405468"
        },
        "date": 1709559065114,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.210123410982077,
            "unit": "iter/sec",
            "range": "stddev: 0.003838508662231823",
            "extra": "mean: 191.9340332499928 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1598.8972751390875,
            "unit": "iter/sec",
            "range": "stddev: 0.00010571168023650065",
            "extra": "mean: 625.4310489790599 usec\nrounds: 490"
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
          "id": "186eddc83abb0606c896761db9fec36492b23d50",
          "message": "Add missing newlines in launch_configuration.rst (#484)\n\nAdd missing newlines before bullet lists in the\r\n``launch_configuration.rst`` file.",
          "timestamp": "2024-03-05T10:39:39Z",
          "tree_id": "72a9cc1abf4a20d8952856a4f67d7c4f26b0d62a",
          "url": "https://github.com/ansys/pyacp/commit/186eddc83abb0606c896761db9fec36492b23d50"
        },
        "date": 1709635358509,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.101038859082055,
            "unit": "iter/sec",
            "range": "stddev: 0.0025259448864629625",
            "extra": "mean: 196.03849875002766 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1169.3747662314888,
            "unit": "iter/sec",
            "range": "stddev: 0.00020167098019902051",
            "extra": "mean: 855.1578406490435 usec\nrounds: 1230"
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
          "id": "a183fdcc36eb089adb4e6cfed91a71b87721c93e",
          "message": "Rosette example: change thumbnail (#482)\n\nUse the fourth image (radial rosette) as thumbnail for the rosette\r\nexample.",
          "timestamp": "2024-03-05T11:06:31Z",
          "tree_id": "749589d6454bd6f5fb528a423e74739231357d57",
          "url": "https://github.com/ansys/pyacp/commit/a183fdcc36eb089adb4e6cfed91a71b87721c93e"
        },
        "date": 1709637026621,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 3.822571354710033,
            "unit": "iter/sec",
            "range": "stddev: 0.014000247633908091",
            "extra": "mean: 261.6040113333232 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 786.0067129570928,
            "unit": "iter/sec",
            "range": "stddev: 0.000533161439492904",
            "extra": "mean: 1.272253765159114 msec\nrounds: 1039"
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
          "id": "d5b48fd57256f4aa70def36caa0aeb6f909d9b85",
          "message": "Add direction definition example (#449)\n\n* Add direction definition example\r\n* Add reference direction field and use it in example",
          "timestamp": "2024-03-05T11:45:48Z",
          "tree_id": "ca033407f6d79d175df8d1e9f728ef986e1e2a43",
          "url": "https://github.com/ansys/pyacp/commit/d5b48fd57256f4aa70def36caa0aeb6f909d9b85"
        },
        "date": 1709639328660,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.04369031164537,
            "unit": "iter/sec",
            "range": "stddev: 0.005551181205192892",
            "extra": "mean: 198.26752599998088 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1191.4039462902576,
            "unit": "iter/sec",
            "range": "stddev: 0.00019779174205365396",
            "extra": "mean: 839.3458852589476 usec\nrounds: 1194"
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
          "id": "bcb55bd80ca66b1e5322db27563d335db64a1aeb",
          "message": "Fix vale warnings (#479)\n\n* Fix some vale warnings\r\n\r\n* Fix more vale warnings\r\n\r\n* Update doc/source/user_guide/howto/create_input_file.rst\r\n\r\nCo-authored-by: Kathy Pippert <84872299+PipKat@users.noreply.github.com>\r\n\r\n* Update doc/source/user_guide/howto/file_management.rst\r\n\r\nCo-authored-by: Kathy Pippert <84872299+PipKat@users.noreply.github.com>\r\n\r\n---------\r\n\r\nCo-authored-by: Kathy Pippert <84872299+PipKat@users.noreply.github.com>",
          "timestamp": "2024-03-05T12:29:28Z",
          "tree_id": "7fe9f9d753f95644ca214b9354c67eac637b9832",
          "url": "https://github.com/ansys/pyacp/commit/bcb55bd80ca66b1e5322db27563d335db64a1aeb"
        },
        "date": 1709641941256,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.43599674152267,
            "unit": "iter/sec",
            "range": "stddev: 0.0037883339610546947",
            "extra": "mean: 183.95890349998467 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1167.7981533466004,
            "unit": "iter/sec",
            "range": "stddev: 0.00023900343770377535",
            "extra": "mean: 856.3123662546174 usec\nrounds: 1458"
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
          "id": "0b2db26d91dae9b530cb7f30d9f5df976a443964",
          "message": "Add optimization example (#480)\n\nAdd an example which optimizes ply angles to minize the maximum\r\nIRF, considering only maximum stress.\r\n\r\nThe optimization uses the Nelder-Mead (downhill simplex) method\r\nas implemented in scipy.optimize.minimize to find a local minimum.\r\n\r\nSince the full optimization takes too long to build as part of\r\nthe documentation (~30 min), only a single iteration is performed\r\nas part of the build.\r\n\r\n---------\r\n\r\nCo-authored-by: Kathy Pippert <84872299+PipKat@users.noreply.github.com>",
          "timestamp": "2024-03-05T15:38:13Z",
          "tree_id": "19c0f05ca3a9fc4592fcdaef5112ae392b7515b9",
          "url": "https://github.com/ansys/pyacp/commit/0b2db26d91dae9b530cb7f30d9f5df976a443964"
        },
        "date": 1709653260532,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.071452087897012,
            "unit": "iter/sec",
            "range": "stddev: 0.002456121750284102",
            "extra": "mean: 164.7052444000053 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1258.2052195625386,
            "unit": "iter/sec",
            "range": "stddev: 0.00018374592179400728",
            "extra": "mean: 794.7829054052779 usec\nrounds: 1554"
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
          "id": "a3ad63252408bb76a9e116f1ca4ac48bc104298c",
          "message": "Do not document methods on enum types (#485)\n\n* Rename the 'Other data types' API section to 'Enumeration data types'\r\n* Create an autosummary template which skips the methods section, and use\r\n  it for the enum data types\r\n* Rename \"Elemental and nodal data types\" to \"Mesh data types\"\r\n* Move non-enum classes ``MeshData`` and ``TriangleMesh`` to\r\n  \"Mesh data types\"\r\n* Rename the custom autosummary templates by adding the `.jinja2` suffix, to\r\n  make the vale style check ignore them.",
          "timestamp": "2024-03-05T16:23:19Z",
          "tree_id": "e26d42ad9946f3f4c6adccfcdc56afcd30b4409e",
          "url": "https://github.com/ansys/pyacp/commit/a3ad63252408bb76a9e116f1ca4ac48bc104298c"
        },
        "date": 1709656029347,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.439288628324289,
            "unit": "iter/sec",
            "range": "stddev: 0.003000150325753273",
            "extra": "mean: 225.26131633334975 msec\nrounds: 3"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1016.6126540589098,
            "unit": "iter/sec",
            "range": "stddev: 0.0005492868749305254",
            "extra": "mean: 983.6588163716217 usec\nrounds: 904"
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
          "id": "ecd37c0abb487e6cf43ea2028fe1166a6cc18b25",
          "message": "Update CONTRIBUTORS.md (#487)",
          "timestamp": "2024-03-05T16:47:46Z",
          "tree_id": "b10e91acd13b632683f1575db952843edadb0b49",
          "url": "https://github.com/ansys/pyacp/commit/ecd37c0abb487e6cf43ea2028fe1166a6cc18b25"
        },
        "date": 1709657451510,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.122716485572467,
            "unit": "iter/sec",
            "range": "stddev: 0.0044031848431661524",
            "extra": "mean: 195.20892925001476 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1177.7068299351463,
            "unit": "iter/sec",
            "range": "stddev: 0.00018745054905827904",
            "extra": "mean: 849.1077529499152 usec\nrounds: 1186"
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
          "id": "dd7da226426489b47524bdcd248f7cfddc04f825",
          "message": "Make intro ready for the testing session (#488)\n\n* Add temporary section for the testing session of pyACP\r\n\r\n* some unrelated cosmetic changes\r\n\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>\r\n\r\n---------\r\n\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>\r\nCo-authored-by: Kathy Pippert <84872299+PipKat@users.noreply.github.com>",
          "timestamp": "2024-03-07T14:27:17+01:00",
          "tree_id": "eafe40f038a01d97969e055056496da478fb5f18",
          "url": "https://github.com/ansys/pyacp/commit/dd7da226426489b47524bdcd248f7cfddc04f825"
        },
        "date": 1709818250256,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.147995618053151,
            "unit": "iter/sec",
            "range": "stddev: 0.004094357013144911",
            "extra": "mean: 241.08029325000757 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1009.2637457559613,
            "unit": "iter/sec",
            "range": "stddev: 0.00031147581180920566",
            "extra": "mean: 990.821283539693 usec\nrounds: 1051"
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
          "id": "1e790bb17376d580cb8e968f9da078eaed9c55eb",
          "message": "Bump the dependencies group with 4 updates (#492)\n\nBumps the dependencies group with 4 updates: [packaging](https://github.com/pypa/packaging), [mypy](https://github.com/python/mypy), [pytest-cases](https://github.com/smarie/python-pytest-cases) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `packaging` from 23.2 to 24.0\r\n- [Release notes](https://github.com/pypa/packaging/releases)\r\n- [Changelog](https://github.com/pypa/packaging/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pypa/packaging/compare/23.2...24.0)\r\n\r\nUpdates `mypy` from 1.8.0 to 1.9.0\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.8.0...1.9.0)\r\n\r\nUpdates `pytest-cases` from 3.8.2 to 3.8.3\r\n- [Release notes](https://github.com/smarie/python-pytest-cases/releases)\r\n- [Changelog](https://github.com/smarie/python-pytest-cases/blob/main/docs/changelog.md)\r\n- [Commits](https://github.com/smarie/python-pytest-cases/compare/3.8.2...3.8.3)\r\n\r\nUpdates `hypothesis` from 6.98.17 to 6.99.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.98.17...hypothesis-python-6.99.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: packaging\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n  dependency-group: dependencies\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest-cases\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-03-11T08:09:48+01:00",
          "tree_id": "2ca4645e2e88f979318bb435cf110600b834e188",
          "url": "https://github.com/ansys/pyacp/commit/1e790bb17376d580cb8e968f9da078eaed9c55eb"
        },
        "date": 1710141177385,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.825615187701294,
            "unit": "iter/sec",
            "range": "stddev: 0.007771790114750139",
            "extra": "mean: 207.22746449999363 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1247.2204552803585,
            "unit": "iter/sec",
            "range": "stddev: 0.00019144086036763193",
            "extra": "mean: 801.7828730809368 usec\nrounds: 977"
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
          "id": "66a1dedef4577dcf03e4cb8e9fa6bea47265bdf6",
          "message": "Improve install instructions (#495)\n\n* Add `examples` extra in default install instructions\r\n* Add note about token in testing session instructions",
          "timestamp": "2024-03-12T10:59:05Z",
          "tree_id": "007ef644332b4eee0a358c387fbbe52817c824a2",
          "url": "https://github.com/ansys/pyacp/commit/66a1dedef4577dcf03e4cb8e9fa6bea47265bdf6"
        },
        "date": 1710241360099,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 4.33952184588074,
            "unit": "iter/sec",
            "range": "stddev: 0.0055357469699484855",
            "extra": "mean: 230.4401349999523 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1036.5862644476467,
            "unit": "iter/sec",
            "range": "stddev: 0.00020893078761779254",
            "extra": "mean: 964.705046070486 usec\nrounds: 1107"
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
          "id": "3d62124a66279cf67e3cf9787efb9716071f877d",
          "message": "Fix syntax for specifying extras with git install (#496)",
          "timestamp": "2024-03-13T14:45:03+01:00",
          "tree_id": "19bf49ac641820749e767e8407253556628dd14e",
          "url": "https://github.com/ansys/pyacp/commit/3d62124a66279cf67e3cf9787efb9716071f877d"
        },
        "date": 1710337676903,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.063921960137607,
            "unit": "iter/sec",
            "range": "stddev: 0.005376327781876439",
            "extra": "mean: 164.90977400001157 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1223.9193075367523,
            "unit": "iter/sec",
            "range": "stddev: 0.00018472257141212002",
            "extra": "mean: 817.0473280731146 usec\nrounds: 1521"
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
          "id": "0a88ccc53c53413ad2a2fa585ce191c72afca229",
          "message": "Adapt to changes in material handling (#502)\n\nAdapt to the changes made in material handling:\r\n\r\nMaterial names are deduplicated on creation, and changing a name to an\r\nexisting one raises an error. This required changes to the material unittests.\r\n\r\nOn models which have a link to a MatML file, creating materials is no longer\r\nallowed since storing them back to the MatML file is not implemented (and they\r\nwould be lost upon save).\r\nUse a variant of the `minimal_complete_model.acph5` which does not have this\r\nlink in tests + doctests to fix this.",
          "timestamp": "2024-03-21T16:49:26Z",
          "tree_id": "0fad2cec0dceafeb0fd30c7c431aed0f0d6b94ea",
          "url": "https://github.com/ansys/pyacp/commit/0a88ccc53c53413ad2a2fa585ce191c72afca229"
        },
        "date": 1711039921936,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.3434506122448635,
            "unit": "iter/sec",
            "range": "stddev: 0.003635578418522532",
            "extra": "mean: 157.64290780000465 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1207.6305498944716,
            "unit": "iter/sec",
            "range": "stddev: 0.00019848275410895043",
            "extra": "mean: 828.0678226361404 usec\nrounds: 1714"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "65216347+jonathanzopes@users.noreply.github.com",
            "name": "Jonathan Zopes",
            "username": "jonathanzopes"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6136b42bdace6d58443051e295ef15ea435e2262",
          "message": "Minimal fix in rosettes example (#506)",
          "timestamp": "2024-03-25T09:22:10+01:00",
          "tree_id": "494d9f299bed0c01f250031728b1f1e1395a4083",
          "url": "https://github.com/ansys/pyacp/commit/6136b42bdace6d58443051e295ef15ea435e2262"
        },
        "date": 1711355101043,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.17482729742946,
            "unit": "iter/sec",
            "range": "stddev: 0.004258214562415406",
            "extra": "mean: 161.94784919997574 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1231.0329388567839,
            "unit": "iter/sec",
            "range": "stddev: 0.00020267059921144948",
            "extra": "mean: 812.325948750538 usec\nrounds: 1561"
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
          "id": "6504fa960e55dceb471f7ac0f7a07b66018e2c5a",
          "message": "Use dev version of py dpf composites (#500)",
          "timestamp": "2024-03-25T08:34:59Z",
          "tree_id": "358d0256f009c3f34665a4cc5bb07ea8326129c9",
          "url": "https://github.com/ansys/pyacp/commit/6504fa960e55dceb471f7ac0f7a07b66018e2c5a"
        },
        "date": 1711355864289,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.12148890526058,
            "unit": "iter/sec",
            "range": "stddev: 0.00289766081648776",
            "extra": "mean: 163.3589499999971 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1195.4859514039663,
            "unit": "iter/sec",
            "range": "stddev: 0.00020692845341203887",
            "extra": "mean: 836.4799258624582 usec\nrounds: 1740"
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
          "id": "984d9828878fc11f306f1ca3539cf3ae25e0df04",
          "message": "Re-add dpf core as direct dependency (#509)\n\n* Re-add dpf core as explicit dependency",
          "timestamp": "2024-03-25T11:50:40+01:00",
          "tree_id": "daefec54bdfc2b6b850e56edaf4dffd9410b52b2",
          "url": "https://github.com/ansys/pyacp/commit/984d9828878fc11f306f1ca3539cf3ae25e0df04"
        },
        "date": 1711364009437,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.052363372605397,
            "unit": "iter/sec",
            "range": "stddev: 0.006204609842113129",
            "extra": "mean: 165.2247128000056 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1211.8876753278535,
            "unit": "iter/sec",
            "range": "stddev: 0.00019872436096448525",
            "extra": "mean: 825.1589816106256 usec\nrounds: 1577"
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
          "id": "bbbddff2a669af50128b32e37bf13c1c50ae0482",
          "message": "Improve the geometry plot in thickness definition example (#510)\n\nImprove the plot of the geometry in the thickness definition example.\r\nInstead of showing the wireframe, plot the surface (with low opacity) and\r\nfeature edges.",
          "timestamp": "2024-03-27T10:59:13+01:00",
          "tree_id": "9121fd9b562059c40e9b2d487c80ffd6f8bc0b45",
          "url": "https://github.com/ansys/pyacp/commit/bbbddff2a669af50128b32e37bf13c1c50ae0482"
        },
        "date": 1711533749795,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.7891385144190926,
            "unit": "iter/sec",
            "range": "stddev: 0.00469897878237362",
            "extra": "mean: 172.73727299999564 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1297.167800884172,
            "unit": "iter/sec",
            "range": "stddev: 0.0001788095051574735",
            "extra": "mean: 770.9102857150652 usec\nrounds: 1309"
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
          "id": "6713128e3e9329cc6075f46a88c2298785f32595",
          "message": "Replace license server adress by dummy address (#511)",
          "timestamp": "2024-03-28T09:45:15+01:00",
          "tree_id": "164cd2286a1a829afc8f7c9620a9e8f680abf86d",
          "url": "https://github.com/ansys/pyacp/commit/6713128e3e9329cc6075f46a88c2298785f32595"
        },
        "date": 1711615687959,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.962628990261053,
            "unit": "iter/sec",
            "range": "stddev: 0.00371977998993603",
            "extra": "mean: 167.71125649999874 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1241.0860917504513,
            "unit": "iter/sec",
            "range": "stddev: 0.000178354171854634",
            "extra": "mean: 805.7458758478076 usec\nrounds: 1474"
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
          "id": "ccf83d73a846ba18e1a1e208446edd737c4c6cd9",
          "message": "Use docker compose by default, fallback to docker-compose (#514)\n\nThe `docker-compose` command is deprecated according to https://docs.docker.com/compose/faq/, \r\nand replaced by using a subcommand `docker compose`.\r\n\r\nThis PR adds `docker compose` as a default in the launching code, and only falls back to `docker-compose`\r\nif calling `docker compose` fails.\r\n\r\nIn the CI code, use `docker compose` consistently.",
          "timestamp": "2024-04-03T22:20:44+02:00",
          "tree_id": "f5791c166b2b6ca12b1e935390914b2b352f7bf8",
          "url": "https://github.com/ansys/pyacp/commit/ccf83d73a846ba18e1a1e208446edd737c4c6cd9"
        },
        "date": 1712175820500,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.998392910571748,
            "unit": "iter/sec",
            "range": "stddev: 0.0036043942617057802",
            "extra": "mean: 166.71131999999034 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1177.743413647803,
            "unit": "iter/sec",
            "range": "stddev: 0.00021464351527737777",
            "extra": "mean: 849.081377498617 usec\nrounds: 1751"
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
          "id": "7f6ff8139ee583f7c3ac3b774688aee0fad32ce3",
          "message": "Add server availability disclaimer (#515)\n\n* Add server availability disclaimer\r\n* Replace docker-compose with docker compose in README",
          "timestamp": "2024-04-04T09:44:17+02:00",
          "tree_id": "0ee887ba9573f989607c2edb80dd9a53c32536a7",
          "url": "https://github.com/ansys/pyacp/commit/7f6ff8139ee583f7c3ac3b774688aee0fad32ce3"
        },
        "date": 1712216830420,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.045415974711264,
            "unit": "iter/sec",
            "range": "stddev: 0.003360092006288405",
            "extra": "mean: 165.4145892000031 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1198.8154695022674,
            "unit": "iter/sec",
            "range": "stddev: 0.00020429386099115967",
            "extra": "mean: 834.1567367454702 usec\nrounds: 1641"
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
          "id": "e5d82d6a9753829695dba47910add4f93e2dea85",
          "message": "Remove testing session section from docs (#517)\n\n* Bump the dependencies group with 12 updates\r\n\r\nBumps the dependencies group with 12 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [typing-extensions](https://github.com/python/typing_extensions) | `4.10.0` | `4.11.0` |\r\n| [ansys-tools-path](https://github.com/ansys/ansys-tools-path) | `0.4.1` | `0.5.1` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.4` | `0.43.5` |\r\n| [ansys-mapdl-core](https://github.com/ansys/pymapdl) | `0.68.0` | `0.68.1` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.8` | `0.10.9` |\r\n| [matplotlib](https://github.com/matplotlib/matplotlib) | `3.8.3` | `3.8.4` |\r\n| [scipy](https://github.com/scipy/scipy) | `1.12.0` | `1.13.0` |\r\n| [numpydoc](https://github.com/numpy/numpydoc) | `1.6.0` | `1.7.0` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.14.1` | `0.15.1` |\r\n| [ipykernel](https://github.com/ipython/ipykernel) | `6.29.3` | `6.29.4` |\r\n| [pytest-cases](https://github.com/smarie/python-pytest-cases) | `3.8.4` | `3.8.5` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.99.13` | `6.100.0` |\r\n\r\n\r\nUpdates `typing-extensions` from 4.10.0 to 4.11.0\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.10.0...4.11.0)\r\n\r\nUpdates `ansys-tools-path` from 0.4.1 to 0.5.1\r\n- [Release notes](https://github.com/ansys/ansys-tools-path/releases)\r\n- [Changelog](https://github.com/ansys/ansys-tools-path/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/ansys-tools-path/compare/v0.4.1...v0.5.1)\r\n\r\nUpdates `pyvista` from 0.43.4 to 0.43.5\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.4...v0.43.5)\r\n\r\nUpdates `ansys-mapdl-core` from 0.68.0 to 0.68.1\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.68.0...v0.68.1)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.8 to 0.10.9\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.8...v0.10.9)\r\n\r\nUpdates `matplotlib` from 3.8.3 to 3.8.4\r\n- [Release notes](https://github.com/matplotlib/matplotlib/releases)\r\n- [Commits](https://github.com/matplotlib/matplotlib/compare/v3.8.3...v3.8.4)\r\n\r\nUpdates `scipy` from 1.12.0 to 1.13.0\r\n- [Release notes](https://github.com/scipy/scipy/releases)\r\n- [Commits](https://github.com/scipy/scipy/compare/v1.12.0...v1.13.0)\r\n\r\nUpdates `numpydoc` from 1.6.0 to 1.7.0\r\n- [Release notes](https://github.com/numpy/numpydoc/releases)\r\n- [Changelog](https://github.com/numpy/numpydoc/blob/main/RELEASE.rst)\r\n- [Commits](https://github.com/numpy/numpydoc/compare/v1.6.0...v1.7.0)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.14.1 to 0.15.1\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.14.1...v0.15.1)\r\n\r\nUpdates `ipykernel` from 6.29.3 to 6.29.4\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/v6.29.4/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.29.3...v6.29.4)\r\n\r\nUpdates `pytest-cases` from 3.8.4 to 3.8.5\r\n- [Release notes](https://github.com/smarie/python-pytest-cases/releases)\r\n- [Changelog](https://github.com/smarie/python-pytest-cases/blob/main/docs/changelog.md)\r\n- [Commits](https://github.com/smarie/python-pytest-cases/compare/3.8.4...3.8.5)\r\n\r\nUpdates `hypothesis` from 6.99.13 to 6.100.0\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.99.13...hypothesis-python-6.100.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-tools-path\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: matplotlib\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: scipy\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: numpydoc\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pytest-cases\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\n* Remove testing session section from intro\r\n\r\n---------\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-04-08T08:40:48+02:00",
          "tree_id": "45e8e6a940ce0d92cb50093e91d8b8a1af334b2e",
          "url": "https://github.com/ansys/pyacp/commit/e5d82d6a9753829695dba47910add4f93e2dea85"
        },
        "date": 1712558623241,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.906987650958074,
            "unit": "iter/sec",
            "range": "stddev: 0.006375163209387956",
            "extra": "mean: 169.29102599999624 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1257.7911320128792,
            "unit": "iter/sec",
            "range": "stddev: 0.00018024703815621462",
            "extra": "mean: 795.0445622872784 usec\nrounds: 1469"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "57ed691447479d23bf08b974774c1236755021e4",
          "message": "cicd: uncomment stages for releasing (#518)",
          "timestamp": "2024-04-08T07:06:10Z",
          "tree_id": "8b4cf95cf2eb3193a72a023ab9714d856226bac2",
          "url": "https://github.com/ansys/pyacp/commit/57ed691447479d23bf08b974774c1236755021e4"
        },
        "date": 1712560139107,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.04817135021002,
            "unit": "iter/sec",
            "range": "stddev: 0.0035729858011584845",
            "extra": "mean: 165.3392310000072 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1212.5811542371325,
            "unit": "iter/sec",
            "range": "stddev: 0.00019141386012596173",
            "extra": "mean: 824.6870706391004 usec\nrounds: 1628"
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
          "id": "e14b50103d29d98c54ade6fb868a4f2c43dbccd5",
          "message": "Use released ansys-dpf-core and ansys-dpf-composites (#519)",
          "timestamp": "2024-04-08T08:46:30Z",
          "tree_id": "cdf1d313986ae26e7dca63aff601f8575ee1d246",
          "url": "https://github.com/ansys/pyacp/commit/e14b50103d29d98c54ade6fb868a4f2c43dbccd5"
        },
        "date": 1712566168684,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 5.953806295379672,
            "unit": "iter/sec",
            "range": "stddev: 0.005701622212737997",
            "extra": "mean: 167.95978075001017 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1262.1433343064298,
            "unit": "iter/sec",
            "range": "stddev: 0.00017909339829567654",
            "extra": "mean: 792.3030394559092 usec\nrounds: 1470"
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
          "id": "e14b50103d29d98c54ade6fb868a4f2c43dbccd5",
          "message": "Use released ansys-dpf-core and ansys-dpf-composites (#519)",
          "timestamp": "2024-04-08T08:46:30Z",
          "tree_id": "cdf1d313986ae26e7dca63aff601f8575ee1d246",
          "url": "https://github.com/ansys/pyacp/commit/e14b50103d29d98c54ade6fb868a4f2c43dbccd5"
        },
        "date": 1712568706023,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.449266859661601,
            "unit": "iter/sec",
            "range": "stddev: 0.004372646794961155",
            "extra": "mean: 155.0563841999974 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1250.9427042970008,
            "unit": "iter/sec",
            "range": "stddev: 0.00023233991608398067",
            "extra": "mean: 799.3971239170187 usec\nrounds: 1848"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a508d4a94a1a4e49a700af3656f42a7100f7c37e",
          "message": "fix: use PYANSYS_CI_BOT_USERNAME (#523)\n\n* fix: use PYANSYS_CI_BOT_TOKEN\r\n\r\n* Update ci_cd.yml",
          "timestamp": "2024-04-08T12:02:18+02:00",
          "tree_id": "940d6427a1df13b1dda61392161e8d26f0987d86",
          "url": "https://github.com/ansys/pyacp/commit/a508d4a94a1a4e49a700af3656f42a7100f7c37e"
        },
        "date": 1712570687978,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.570907931733995,
            "unit": "iter/sec",
            "range": "stddev: 0.0036223010624424536",
            "extra": "mean: 152.18597040000077 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1263.417100036582,
            "unit": "iter/sec",
            "range": "stddev: 0.00020920820841325248",
            "extra": "mean: 791.5042466743922 usec\nrounds: 1804"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6542d2227380c9eb6b2dad066c00579ff12ad9c1",
          "message": "fix: badges (#522)",
          "timestamp": "2024-04-08T10:12:42Z",
          "tree_id": "f1b6e90c943794b0613a718d55c0b55950139555",
          "url": "https://github.com/ansys/pyacp/commit/6542d2227380c9eb6b2dad066c00579ff12ad9c1"
        },
        "date": 1712571325115,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.2290385688765095,
            "unit": "iter/sec",
            "range": "stddev: 0.006764680354961492",
            "extra": "mean: 160.5384183999945 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1355.5615153080155,
            "unit": "iter/sec",
            "range": "stddev: 0.00018022408876668862",
            "extra": "mean: 737.7016746988252 usec\nrounds: 1494"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "37798125+RobPasMue@users.noreply.github.com",
            "name": "Roberto Pastor Muela",
            "username": "RobPasMue"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e7cd51e7d0b47639441e19a1df5b4ae8c74cd014",
          "message": "feat: allow local-product-launcher and filetransfer new versions (#524)\n\n* feat: allow local-product-launcher and filetransfer new versions\r\n\r\n* Update pyproject.toml\r\n\r\n* feat: update lock file\r\n\r\n---------\r\n\r\nCo-authored-by: Dominik Gresch <greschd@users.noreply.github.com>",
          "timestamp": "2024-04-08T13:01:08Z",
          "tree_id": "d38693e1541c5d7b2ca98538114a962c1b8af7cb",
          "url": "https://github.com/ansys/pyacp/commit/e7cd51e7d0b47639441e19a1df5b4ae8c74cd014"
        },
        "date": 1712581431627,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.491335554848738,
            "unit": "iter/sec",
            "range": "stddev: 0.0042255113524504225",
            "extra": "mean: 154.05150319999166 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1269.4797493501312,
            "unit": "iter/sec",
            "range": "stddev: 0.00020481172477914328",
            "extra": "mean: 787.7242630391839 usec\nrounds: 1783"
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
          "id": "1f71c0c052c42e6d171009d7be8dc42a4fbc9e7d",
          "message": "Update pre-commit and dev dependencies (#525)\n\nExtend the allowable range for `black` to `^24` to allow minor release bumps.\r\n\r\nRun pre-commit autoupdate, and adapt the indirect dependency on black \r\nspecified in the blacken-docs hook.",
          "timestamp": "2024-04-09T11:54:24+02:00",
          "tree_id": "6b981d644076ae23f54faa95be21c4460a71d8ab",
          "url": "https://github.com/ansys/pyacp/commit/1f71c0c052c42e6d171009d7be8dc42a4fbc9e7d"
        },
        "date": 1712656631987,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.469615129065881,
            "unit": "iter/sec",
            "range": "stddev: 0.0028913032530803367",
            "extra": "mean: 154.568699999993 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1357.147808914228,
            "unit": "iter/sec",
            "range": "stddev: 0.00017681174674944404",
            "extra": "mean: 736.8394167765997 usec\nrounds: 1526"
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
          "id": "c2bccc660b1231767357dd986e7f850466fce083",
          "message": "Bump the dependencies group with 4 updates (#526)\n\nBumps the dependencies group with 4 updates: [ansys-dpf-core](https://github.com/ansys/pydpf-core), [black](https://github.com/psf/black), [types-protobuf](https://github.com/python/typeshed) and [sphinx-autodoc-typehints](https://github.com/tox-dev/sphinx-autodoc-typehints).\r\n\r\n\r\nUpdates `ansys-dpf-core` from 0.11.0 to 0.12.0\r\n- [Release notes](https://github.com/ansys/pydpf-core/releases)\r\n- [Commits](https://github.com/ansys/pydpf-core/compare/v0.11.0...v0.12.0)\r\n\r\nUpdates `black` from 24.3.0 to 24.4.0\r\n- [Release notes](https://github.com/psf/black/releases)\r\n- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)\r\n- [Commits](https://github.com/psf/black/compare/24.3.0...24.4.0)\r\n\r\nUpdates `types-protobuf` from 4.24.0.20240408 to 4.25.0.20240410\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\nUpdates `sphinx-autodoc-typehints` from 2.0.0 to 2.0.1\r\n- [Release notes](https://github.com/tox-dev/sphinx-autodoc-typehints/releases)\r\n- [Changelog](https://github.com/tox-dev/sphinx-autodoc-typehints/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/tox-dev/sphinx-autodoc-typehints/compare/2.0.0...2.0.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-dpf-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: black\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-autodoc-typehints\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-04-17T11:55:21+02:00",
          "tree_id": "c488663def3e79f6e6aae7b7a7319f2145ecfda0",
          "url": "https://github.com/ansys/pyacp/commit/c2bccc660b1231767357dd986e7f850466fce083"
        },
        "date": 1713347885369,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.451465659968339,
            "unit": "iter/sec",
            "range": "stddev: 0.00355764746001164",
            "extra": "mean: 155.00353759999825 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1226.2100764018187,
            "unit": "iter/sec",
            "range": "stddev: 0.0002143054112994734",
            "extra": "mean: 815.5209447751336 usec\nrounds: 1847"
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
          "id": "40ebaeeb8750474571fc13483712b2488515b66f",
          "message": "Bump ansys/actions from 5 to 6 (#530)\n\n* Bump ansys/actions from 5 to 6\r\n\r\nBumps [ansys/actions](https://github.com/ansys/actions) from 5 to 6.\r\n- [Release notes](https://github.com/ansys/actions/releases)\r\n- [Commits](https://github.com/ansys/actions/compare/v5...v6)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys/actions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\n\r\n* Remove pinned vale version\r\n\r\n---------\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>\r\nCo-authored-by: Dominik Gresch <dominik.gresch@ansys.com>",
          "timestamp": "2024-04-22T16:56:23+02:00",
          "tree_id": "b29b3d643a93a47fed71a8587b2c0b6886d5f64b",
          "url": "https://github.com/ansys/pyacp/commit/40ebaeeb8750474571fc13483712b2488515b66f"
        },
        "date": 1713797940981,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.458185986590386,
            "unit": "iter/sec",
            "range": "stddev: 0.004610289717990175",
            "extra": "mean: 154.84224240001367 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1311.3179329165655,
            "unit": "iter/sec",
            "range": "stddev: 0.000190969290268932",
            "extra": "mean: 762.5915690604884 usec\nrounds: 1629"
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
          "id": "a2c52d743b52e084b591bdcd811c916c48980ab3",
          "message": "Remove upper bounds on dependencies (#531)\n\nRemove upper limits on dependencies. For context, see e.g. the discussion in\r\nhttps://iscinumpy.dev/post/bound-version-constraints/\r\n\r\nIn short: downstream projects have no way to remove an artificial (wrong)\r\nupper bound, but adding a missing one is easy. Since it's unknowable\r\nwhich future versions will be compatible, it's better to err on the side of\r\nallowing them, for the context of libraries.\r\n\r\nIn addition, we continuously check the newest dependency versions via\r\ndependabot, and our CI is using pinned dependencies. As such, I believe we\r\ncan afford to leave out the upper limit.\r\n\r\nOther changes:\r\n- Ignore a new warning generated by sphinx, indicating that its caching does\r\n  not work as intended. This can be removed once https://github.com/sphinx-gallery/sphinx-gallery/issues/1286\r\n  is resolved.\r\n\r\n---------\r\n\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-04-25T08:35:26+02:00",
          "tree_id": "a22f3686e899501ff8e6fac4a8ca1cb37345cae6",
          "url": "https://github.com/ansys/pyacp/commit/a2c52d743b52e084b591bdcd811c916c48980ab3"
        },
        "date": 1714027099122,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.536442226314461,
            "unit": "iter/sec",
            "range": "stddev: 0.004407986946960121",
            "extra": "mean: 152.98842479999166 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1263.0438757805734,
            "unit": "iter/sec",
            "range": "stddev: 0.0002194296605509183",
            "extra": "mean: 791.7381329148128 usec\nrounds: 1753"
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
          "id": "b47eb84ccd3b7e666933f9caa444b1d4756c9ebf",
          "message": "Bump the dependencies group with 7 updates (#532)\n\nBumps the dependencies group with 7 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.5` | `0.43.6` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.9` | `0.10.10` |\r\n| [black](https://github.com/psf/black) | `24.4.0` | `24.4.2` |\r\n| [mypy](https://github.com/python/mypy) | `1.9.0` | `1.10.0` |\r\n| [sphinx-gallery](https://github.com/sphinx-gallery/sphinx-gallery) | `0.15.0` | `0.16.0` |\r\n| [pytest](https://github.com/pytest-dev/pytest) | `8.1.1` | `8.2.0` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.100.1` | `6.100.2` |\r\n\r\n\r\nUpdates `pyvista` from 0.43.5 to 0.43.6\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.5...v0.43.6)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.9 to 0.10.10\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.9...v0.10.10)\r\n\r\nUpdates `black` from 24.4.0 to 24.4.2\r\n- [Release notes](https://github.com/psf/black/releases)\r\n- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)\r\n- [Commits](https://github.com/psf/black/compare/24.4.0...24.4.2)\r\n\r\nUpdates `mypy` from 1.9.0 to 1.10.0\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/1.9.0...v1.10.0)\r\n\r\nUpdates `sphinx-gallery` from 0.15.0 to 0.16.0\r\n- [Release notes](https://github.com/sphinx-gallery/sphinx-gallery/releases)\r\n- [Changelog](https://github.com/sphinx-gallery/sphinx-gallery/blob/master/.github_changelog_generator)\r\n- [Commits](https://github.com/sphinx-gallery/sphinx-gallery/compare/v0.15.0...v0.16.0)\r\n\r\nUpdates `pytest` from 8.1.1 to 8.2.0\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/8.1.1...8.2.0)\r\n\r\nUpdates `hypothesis` from 6.100.1 to 6.100.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.100.1...hypothesis-python-6.100.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: black\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-gallery\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-04-29T08:00:12+02:00",
          "tree_id": "c516ba38ab63965c3d64fb61f9b3159755144402",
          "url": "https://github.com/ansys/pyacp/commit/b47eb84ccd3b7e666933f9caa444b1d4756c9ebf"
        },
        "date": 1714370577996,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.470116233464529,
            "unit": "iter/sec",
            "range": "stddev: 0.005802204160502707",
            "extra": "mean: 154.55672879999156 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1403.3120880505476,
            "unit": "iter/sec",
            "range": "stddev: 0.00016297202445843614",
            "extra": "mean: 712.5998617949479 usec\nrounds: 1382"
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
          "id": "069645ab45fd6bb7bffe89635fe14e094a4c8e46",
          "message": "Bump the dependencies group with 2 updates (#534)\n\nBumps the dependencies group with 2 updates: [pyvista](https://github.com/pyvista/pyvista) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `pyvista` from 0.43.6 to 0.43.7\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.6...v0.43.7)\r\n\r\nUpdates `hypothesis` from 6.100.2 to 6.100.4\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.100.2...hypothesis-python-6.100.4)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-05-06T07:59:14+02:00",
          "tree_id": "b440a6ec9bd4d236ba0653136e5498b74b34cb54",
          "url": "https://github.com/ansys/pyacp/commit/069645ab45fd6bb7bffe89635fe14e094a4c8e46"
        },
        "date": 1714975313912,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.598119419839214,
            "unit": "iter/sec",
            "range": "stddev: 0.005723924599627199",
            "extra": "mean: 151.55833599998232 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1226.4117164291883,
            "unit": "iter/sec",
            "range": "stddev: 0.00022786374951137852",
            "extra": "mean: 815.3868612015489 usec\nrounds: 1830"
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
          "id": "7c5ea14ebbf71b08430e4de5312c2f0d4a78fdb6",
          "message": "Remove workaround for sphinx cache warning (#533)\n\nRemove the suppression of the sphinx 'config.cache' warning, by\r\nusing the string representation of the sphinx-gallery\r\n'FileNameSortKey' instead of directly passing the class.\r\n\r\nSee https://sphinx-gallery.github.io/dev/configuration.html#importing-callables",
          "timestamp": "2024-05-06T11:17:49Z",
          "tree_id": "74467cc346ec4076e10c01ce0c5babcdf03cf435",
          "url": "https://github.com/ansys/pyacp/commit/7c5ea14ebbf71b08430e4de5312c2f0d4a78fdb6"
        },
        "date": 1714994420058,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.446764528698434,
            "unit": "iter/sec",
            "range": "stddev: 0.0035997846615532427",
            "extra": "mean: 155.1165697999977 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1355.5131584750952,
            "unit": "iter/sec",
            "range": "stddev: 0.00018015665467164245",
            "extra": "mean: 737.7279916079642 usec\nrounds: 1549"
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
          "id": "5141ff186ed150092e085b0e21eb3c559c402459",
          "message": "Skip inherited members for enums (#535)\n\n* Skip inherited members for enums",
          "timestamp": "2024-05-13T10:27:59+02:00",
          "tree_id": "8a24f00dd2a0be3ff2d7f836d028f2573f47518a",
          "url": "https://github.com/ansys/pyacp/commit/5141ff186ed150092e085b0e21eb3c559c402459"
        },
        "date": 1715589046685,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.445607144312869,
            "unit": "iter/sec",
            "range": "stddev: 0.004317923610965458",
            "extra": "mean: 155.14442280000367 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1281.5589987126825,
            "unit": "iter/sec",
            "range": "stddev: 0.00020363010659214524",
            "extra": "mean: 780.2996202316814 usec\nrounds: 1730"
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
          "id": "a8b002f5fc03f1d3bdf5e6d917a34a3529b2f84d",
          "message": "Bump the dependencies group across 1 directory with 13 updates (#539)\n\nBumps the dependencies group with 13 updates in the / directory:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [typing-extensions](https://github.com/python/typing_extensions) | `4.11.0` | `4.12.1` |\r\n| [ansys-tools-path](https://github.com/ansys/ansys-tools-path) | `0.5.2` | `0.6.0` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.7` | `0.43.8` |\r\n| [ansys-dpf-core](https://github.com/ansys/pydpf-core) | `0.12.0` | `0.12.1` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.10` | `0.10.11` |\r\n| [matplotlib](https://github.com/matplotlib/matplotlib) | `3.8.4` | `3.9.0` |\r\n| [scipy](https://github.com/scipy/scipy) | `1.13.0` | `1.13.1` |\r\n| [pre-commit](https://github.com/pre-commit/pre-commit) | `3.7.0` | `3.7.1` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.15.2` | `0.16.5` |\r\n| [sphinx-design](https://github.com/executablebooks/sphinx-design) | `0.5.0` | `0.6.0` |\r\n| [pytest](https://github.com/pytest-dev/pytest) | `8.2.0` | `8.2.1` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.100.4` | `6.103.0` |\r\n| [docker](https://github.com/docker/docker-py) | `7.0.0` | `7.1.0` |\r\n\r\n\r\n\r\nUpdates `typing-extensions` from 4.11.0 to 4.12.1\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.11.0...4.12.1)\r\n\r\nUpdates `ansys-tools-path` from 0.5.2 to 0.6.0\r\n- [Release notes](https://github.com/ansys/ansys-tools-path/releases)\r\n- [Changelog](https://github.com/ansys/ansys-tools-path/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/ansys-tools-path/compare/v0.5.2...v0.6.0)\r\n\r\nUpdates `pyvista` from 0.43.7 to 0.43.8\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.7...v0.43.8)\r\n\r\nUpdates `ansys-dpf-core` from 0.12.0 to 0.12.1\r\n- [Release notes](https://github.com/ansys/pydpf-core/releases)\r\n- [Commits](https://github.com/ansys/pydpf-core/compare/v0.12.0...v0.12.1)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.10 to 0.10.11\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.10...v0.10.11)\r\n\r\nUpdates `matplotlib` from 3.8.4 to 3.9.0\r\n- [Release notes](https://github.com/matplotlib/matplotlib/releases)\r\n- [Commits](https://github.com/matplotlib/matplotlib/compare/v3.8.4...v3.9.0)\r\n\r\nUpdates `scipy` from 1.13.0 to 1.13.1\r\n- [Release notes](https://github.com/scipy/scipy/releases)\r\n- [Commits](https://github.com/scipy/scipy/compare/v1.13.0...v1.13.1)\r\n\r\nUpdates `pre-commit` from 3.7.0 to 3.7.1\r\n- [Release notes](https://github.com/pre-commit/pre-commit/releases)\r\n- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.7.0...v3.7.1)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.15.2 to 0.16.5\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.15.2...v0.16.5)\r\n\r\nUpdates `sphinx-design` from 0.5.0 to 0.6.0\r\n- [Release notes](https://github.com/executablebooks/sphinx-design/releases)\r\n- [Changelog](https://github.com/executablebooks/sphinx-design/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/executablebooks/sphinx-design/compare/v0.5.0...v0.6.0)\r\n\r\nUpdates `pytest` from 8.2.0 to 8.2.1\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/8.2.0...8.2.1)\r\n\r\nUpdates `hypothesis` from 6.100.4 to 6.103.0\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.100.4...hypothesis-python-6.103.0)\r\n\r\nUpdates `docker` from 7.0.0 to 7.1.0\r\n- [Release notes](https://github.com/docker/docker-py/releases)\r\n- [Commits](https://github.com/docker/docker-py/compare/7.0.0...7.1.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-tools-path\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-dpf-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: matplotlib\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: scipy\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pre-commit\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-design\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: docker\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-06-03T13:40:59+02:00",
          "tree_id": "2e8d50417099bc982958abf2ca6cd22e5a728667",
          "url": "https://github.com/ansys/pyacp/commit/a8b002f5fc03f1d3bdf5e6d917a34a3529b2f84d"
        },
        "date": 1717415029844,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.536386496198913,
            "unit": "iter/sec",
            "range": "stddev: 0.0029933329359878498",
            "extra": "mean: 152.9897291999987 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1318.6382141387462,
            "unit": "iter/sec",
            "range": "stddev: 0.00019382785302885243",
            "extra": "mean: 758.3581222489739 usec\nrounds: 1636"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "dependabot[bot]",
            "username": "dependabot[bot]",
            "email": "49699333+dependabot[bot]@users.noreply.github.com"
          },
          "committer": {
            "name": "GitHub",
            "username": "web-flow",
            "email": "noreply@github.com"
          },
          "id": "a8b002f5fc03f1d3bdf5e6d917a34a3529b2f84d",
          "message": "Bump the dependencies group across 1 directory with 13 updates (#539)\n\nBumps the dependencies group with 13 updates in the / directory:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [typing-extensions](https://github.com/python/typing_extensions) | `4.11.0` | `4.12.1` |\r\n| [ansys-tools-path](https://github.com/ansys/ansys-tools-path) | `0.5.2` | `0.6.0` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.7` | `0.43.8` |\r\n| [ansys-dpf-core](https://github.com/ansys/pydpf-core) | `0.12.0` | `0.12.1` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.10` | `0.10.11` |\r\n| [matplotlib](https://github.com/matplotlib/matplotlib) | `3.8.4` | `3.9.0` |\r\n| [scipy](https://github.com/scipy/scipy) | `1.13.0` | `1.13.1` |\r\n| [pre-commit](https://github.com/pre-commit/pre-commit) | `3.7.0` | `3.7.1` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.15.2` | `0.16.5` |\r\n| [sphinx-design](https://github.com/executablebooks/sphinx-design) | `0.5.0` | `0.6.0` |\r\n| [pytest](https://github.com/pytest-dev/pytest) | `8.2.0` | `8.2.1` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.100.4` | `6.103.0` |\r\n| [docker](https://github.com/docker/docker-py) | `7.0.0` | `7.1.0` |\r\n\r\n\r\n\r\nUpdates `typing-extensions` from 4.11.0 to 4.12.1\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.11.0...4.12.1)\r\n\r\nUpdates `ansys-tools-path` from 0.5.2 to 0.6.0\r\n- [Release notes](https://github.com/ansys/ansys-tools-path/releases)\r\n- [Changelog](https://github.com/ansys/ansys-tools-path/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/ansys-tools-path/compare/v0.5.2...v0.6.0)\r\n\r\nUpdates `pyvista` from 0.43.7 to 0.43.8\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.7...v0.43.8)\r\n\r\nUpdates `ansys-dpf-core` from 0.12.0 to 0.12.1\r\n- [Release notes](https://github.com/ansys/pydpf-core/releases)\r\n- [Commits](https://github.com/ansys/pydpf-core/compare/v0.12.0...v0.12.1)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.10 to 0.10.11\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.10...v0.10.11)\r\n\r\nUpdates `matplotlib` from 3.8.4 to 3.9.0\r\n- [Release notes](https://github.com/matplotlib/matplotlib/releases)\r\n- [Commits](https://github.com/matplotlib/matplotlib/compare/v3.8.4...v3.9.0)\r\n\r\nUpdates `scipy` from 1.13.0 to 1.13.1\r\n- [Release notes](https://github.com/scipy/scipy/releases)\r\n- [Commits](https://github.com/scipy/scipy/compare/v1.13.0...v1.13.1)\r\n\r\nUpdates `pre-commit` from 3.7.0 to 3.7.1\r\n- [Release notes](https://github.com/pre-commit/pre-commit/releases)\r\n- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.7.0...v3.7.1)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.15.2 to 0.16.5\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.15.2...v0.16.5)\r\n\r\nUpdates `sphinx-design` from 0.5.0 to 0.6.0\r\n- [Release notes](https://github.com/executablebooks/sphinx-design/releases)\r\n- [Changelog](https://github.com/executablebooks/sphinx-design/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/executablebooks/sphinx-design/compare/v0.5.0...v0.6.0)\r\n\r\nUpdates `pytest` from 8.2.0 to 8.2.1\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/8.2.0...8.2.1)\r\n\r\nUpdates `hypothesis` from 6.100.4 to 6.103.0\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.100.4...hypothesis-python-6.103.0)\r\n\r\nUpdates `docker` from 7.0.0 to 7.1.0\r\n- [Release notes](https://github.com/docker/docker-py/releases)\r\n- [Commits](https://github.com/docker/docker-py/compare/7.0.0...7.1.0)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-tools-path\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-dpf-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: matplotlib\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: scipy\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pre-commit\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-design\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: docker\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-06-03T11:40:59Z",
          "url": "https://github.com/ansys/pyacp/commit/a8b002f5fc03f1d3bdf5e6d917a34a3529b2f84d"
        },
        "date": 1717570485814,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.5399642849151105,
            "unit": "iter/sec",
            "range": "stddev: 0.007196069091736222",
            "extra": "mean: 152.90603379999652 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1236.2217281507574,
            "unit": "iter/sec",
            "range": "stddev: 0.0002217735869664541",
            "extra": "mean: 808.9163757830746 usec\nrounds: 1916"
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
          "id": "15fbd57bb086397b809d8de5817268aadecb6f09",
          "message": "Bump the dependencies group with 7 updates (#541)\n\nBumps the dependencies group with 7 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [packaging](https://github.com/pypa/packaging) | `24.0` | `24.1` |\r\n| [typing-extensions](https://github.com/python/typing_extensions) | `4.12.1` | `4.12.2` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.8` | `0.43.9` |\r\n| [ansys-dpf-core](https://github.com/ansys/pydpf-core) | `0.12.1` | `0.12.2` |\r\n| [sphinx-autodoc-typehints](https://github.com/tox-dev/sphinx-autodoc-typehints) | `2.1.0` | `2.1.1` |\r\n| [pytest](https://github.com/pytest-dev/pytest) | `8.2.1` | `8.2.2` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.103.0` | `6.103.1` |\r\n\r\n\r\nUpdates `packaging` from 24.0 to 24.1\r\n- [Release notes](https://github.com/pypa/packaging/releases)\r\n- [Changelog](https://github.com/pypa/packaging/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pypa/packaging/compare/24.0...24.1)\r\n\r\nUpdates `typing-extensions` from 4.12.1 to 4.12.2\r\n- [Release notes](https://github.com/python/typing_extensions/releases)\r\n- [Changelog](https://github.com/python/typing_extensions/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/python/typing_extensions/compare/4.12.1...4.12.2)\r\n\r\nUpdates `pyvista` from 0.43.8 to 0.43.9\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.8...v0.43.9)\r\n\r\nUpdates `ansys-dpf-core` from 0.12.1 to 0.12.2\r\n- [Release notes](https://github.com/ansys/pydpf-core/releases)\r\n- [Commits](https://github.com/ansys/pydpf-core/compare/v0.12.1...v0.12.2)\r\n\r\nUpdates `sphinx-autodoc-typehints` from 2.1.0 to 2.1.1\r\n- [Release notes](https://github.com/tox-dev/sphinx-autodoc-typehints/releases)\r\n- [Changelog](https://github.com/tox-dev/sphinx-autodoc-typehints/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/tox-dev/sphinx-autodoc-typehints/compare/2.1.0...2.1.1)\r\n\r\nUpdates `pytest` from 8.2.1 to 8.2.2\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/8.2.1...8.2.2)\r\n\r\nUpdates `hypothesis` from 6.103.0 to 6.103.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.103.0...hypothesis-python-6.103.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: packaging\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: typing-extensions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-dpf-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-autodoc-typehints\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-06-10T08:05:34+02:00",
          "tree_id": "7fb528302d9d81bba8d7cac3bccdb02c8b742226",
          "url": "https://github.com/ansys/pyacp/commit/15fbd57bb086397b809d8de5817268aadecb6f09"
        },
        "date": 1717999690988,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.438634211774323,
            "unit": "iter/sec",
            "range": "stddev: 0.0037280955966475784",
            "extra": "mean: 155.31244160000597 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1321.659004228315,
            "unit": "iter/sec",
            "range": "stddev: 0.00019036913204074137",
            "extra": "mean: 756.6248153273665 usec\nrounds: 1592"
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
          "id": "ad8fb069c5bb6268024b8caf43ec45242d539452",
          "message": "Bump the dependencies group across 1 directory with 9 updates (#544)\n\nBumps the dependencies group with 9 updates in the / directory:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.9` | `0.43.10` |\r\n| [ansys-mapdl-core](https://github.com/ansys/pymapdl) | `0.68.1` | `0.68.3` |\r\n| [ansys-dpf-composites](https://github.com/ansys/pydpf-composites) | `0.4.1` | `0.5.0` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.11` | `0.11.1` |\r\n| [mypy](https://github.com/python/mypy) | `1.10.0` | `1.10.1` |\r\n| [types-protobuf](https://github.com/python/typeshed) | `5.26.0.20240422` | `5.27.0.20240626` |\r\n| [sphinx-autodoc-typehints](https://github.com/tox-dev/sphinx-autodoc-typehints) | `2.1.1` | `2.2.2` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.16.5` | `0.16.6` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.103.1` | `6.104.2` |\r\n\r\n\r\n\r\nUpdates `pyvista` from 0.43.9 to 0.43.10\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.9...v0.43.10)\r\n\r\nUpdates `ansys-mapdl-core` from 0.68.1 to 0.68.3\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Changelog](https://github.com/ansys/pymapdl/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.68.1...v0.68.3)\r\n\r\nUpdates `ansys-dpf-composites` from 0.4.1 to 0.5.0\r\n- [Release notes](https://github.com/ansys/pydpf-composites/releases)\r\n- [Changelog](https://github.com/ansys/pydpf-composites/blob/main/release_checklist.rst)\r\n- [Commits](https://github.com/ansys/pydpf-composites/compare/v0.4.1...v0.5.0)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.11 to 0.11.1\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.11...v0.11.1)\r\n\r\nUpdates `mypy` from 1.10.0 to 1.10.1\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.10.0...v1.10.1)\r\n\r\nUpdates `types-protobuf` from 5.26.0.20240422 to 5.27.0.20240626\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\nUpdates `sphinx-autodoc-typehints` from 2.1.1 to 2.2.2\r\n- [Release notes](https://github.com/tox-dev/sphinx-autodoc-typehints/releases)\r\n- [Changelog](https://github.com/tox-dev/sphinx-autodoc-typehints/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/tox-dev/sphinx-autodoc-typehints/compare/2.1.1...2.2.2)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.16.5 to 0.16.6\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.16.5...v0.16.6)\r\n\r\nUpdates `hypothesis` from 6.103.1 to 6.104.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.103.1...hypothesis-python-6.104.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-dpf-composites\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-autodoc-typehints\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-07-01T07:03:18Z",
          "tree_id": "7f6bde639da83b13fc6de2da77043c5f22852810",
          "url": "https://github.com/ansys/pyacp/commit/ad8fb069c5bb6268024b8caf43ec45242d539452"
        },
        "date": 1719817553362,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.598592038950313,
            "unit": "iter/sec",
            "range": "stddev: 0.005167200210255873",
            "extra": "mean: 151.54748075001123 msec\nrounds: 4"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1270.4743865729963,
            "unit": "iter/sec",
            "range": "stddev: 0.0002085083807907693",
            "extra": "mean: 787.1075643621755 usec\nrounds: 1779"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "dependabot[bot]",
            "username": "dependabot[bot]",
            "email": "49699333+dependabot[bot]@users.noreply.github.com"
          },
          "committer": {
            "name": "GitHub",
            "username": "web-flow",
            "email": "noreply@github.com"
          },
          "id": "ad8fb069c5bb6268024b8caf43ec45242d539452",
          "message": "Bump the dependencies group across 1 directory with 9 updates (#544)\n\nBumps the dependencies group with 9 updates in the / directory:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.9` | `0.43.10` |\r\n| [ansys-mapdl-core](https://github.com/ansys/pymapdl) | `0.68.1` | `0.68.3` |\r\n| [ansys-dpf-composites](https://github.com/ansys/pydpf-composites) | `0.4.1` | `0.5.0` |\r\n| [ansys-mechanical-core](https://github.com/ansys/pymechanical) | `0.10.11` | `0.11.1` |\r\n| [mypy](https://github.com/python/mypy) | `1.10.0` | `1.10.1` |\r\n| [types-protobuf](https://github.com/python/typeshed) | `5.26.0.20240422` | `5.27.0.20240626` |\r\n| [sphinx-autodoc-typehints](https://github.com/tox-dev/sphinx-autodoc-typehints) | `2.1.1` | `2.2.2` |\r\n| [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) | `0.16.5` | `0.16.6` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.103.1` | `6.104.2` |\r\n\r\n\r\n\r\nUpdates `pyvista` from 0.43.9 to 0.43.10\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.9...v0.43.10)\r\n\r\nUpdates `ansys-mapdl-core` from 0.68.1 to 0.68.3\r\n- [Release notes](https://github.com/ansys/pymapdl/releases)\r\n- [Changelog](https://github.com/ansys/pymapdl/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymapdl/compare/v0.68.1...v0.68.3)\r\n\r\nUpdates `ansys-dpf-composites` from 0.4.1 to 0.5.0\r\n- [Release notes](https://github.com/ansys/pydpf-composites/releases)\r\n- [Changelog](https://github.com/ansys/pydpf-composites/blob/main/release_checklist.rst)\r\n- [Commits](https://github.com/ansys/pydpf-composites/compare/v0.4.1...v0.5.0)\r\n\r\nUpdates `ansys-mechanical-core` from 0.10.11 to 0.11.1\r\n- [Release notes](https://github.com/ansys/pymechanical/releases)\r\n- [Changelog](https://github.com/ansys/pymechanical/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/ansys/pymechanical/compare/v0.10.11...v0.11.1)\r\n\r\nUpdates `mypy` from 1.10.0 to 1.10.1\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.10.0...v1.10.1)\r\n\r\nUpdates `types-protobuf` from 5.26.0.20240422 to 5.27.0.20240626\r\n- [Commits](https://github.com/python/typeshed/commits)\r\n\r\nUpdates `sphinx-autodoc-typehints` from 2.1.1 to 2.2.2\r\n- [Release notes](https://github.com/tox-dev/sphinx-autodoc-typehints/releases)\r\n- [Changelog](https://github.com/tox-dev/sphinx-autodoc-typehints/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/tox-dev/sphinx-autodoc-typehints/compare/2.1.1...2.2.2)\r\n\r\nUpdates `ansys-sphinx-theme` from 0.16.5 to 0.16.6\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v0.16.5...v0.16.6)\r\n\r\nUpdates `hypothesis` from 6.103.1 to 6.104.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.103.1...hypothesis-python-6.104.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mapdl-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-dpf-composites\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-mechanical-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: types-protobuf\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-autodoc-typehints\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-07-01T07:03:18Z",
          "url": "https://github.com/ansys/pyacp/commit/ad8fb069c5bb6268024b8caf43ec45242d539452"
        },
        "date": 1719947457596,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.605000282410664,
            "unit": "iter/sec",
            "range": "stddev: 0.01419903998269253",
            "extra": "mean: 116.2115011250009 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1383.5151458423886,
            "unit": "iter/sec",
            "range": "stddev: 0.00021432944804757425",
            "extra": "mean: 722.7965685848161 usec\nrounds: 1859"
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
          "id": "93ce405cb4819a9ef1542db8d7b52ab9dd62bf3b",
          "message": "CI: Fix custom API branch install (#546)\n\nFix installing a custom API branch in the CI pipeline:\r\n- build the API repository in a separate step, using Python3.10, since\r\n  newer Python versions are not supported by the necessary `protobuf` version\r\n- install the API package without dependencies, to avoid accidentally installing\r\n  a transitive dependency which is incompatible with some other dependency\r\n\r\nOther changes:\r\n- Simplify the pipeline logic by using `env` to process the `workflow_dispatch` inputs.\r\n  This also allows setting a default value in the CI `.yml`, for example for a feature branch.\r\n- Update the poetry lockfile. This is done to update transitive dependencies, as dependabot\r\n  only manages direct ones.",
          "timestamp": "2024-07-03T06:26:44+02:00",
          "tree_id": "dcbf240decf5a110fe3c4528e6d38f41884c79aa",
          "url": "https://github.com/ansys/pyacp/commit/93ce405cb4819a9ef1542db8d7b52ab9dd62bf3b"
        },
        "date": 1719980967701,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.629497680772692,
            "unit": "iter/sec",
            "range": "stddev: 0.003917032624577211",
            "extra": "mean: 150.84099100000685 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1299.2345471082347,
            "unit": "iter/sec",
            "range": "stddev: 0.00020098894170571054",
            "extra": "mean: 769.683966783169 usec\nrounds: 1716"
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
          "id": "45a364d22ca048cfa91f7b21e04afef311aad8aa",
          "message": "Bump the dependencies group with 5 updates (#547)\n\nBumps the dependencies group with 5 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [ansys-api-acp](https://github.com/ansys/ansys-api-acp) | `0.1.0.dev8` | `0.1.0.dev9` |\r\n| [pyvista](https://github.com/pyvista/pyvista) | `0.43.10` | `0.44.0` |\r\n| [matplotlib](https://github.com/matplotlib/matplotlib) | `3.9.0` | `3.9.1` |\r\n| [ipykernel](https://github.com/ipython/ipykernel) | `6.29.4` | `6.29.5` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.104.2` | `6.105.1` |\r\n\r\n\r\nUpdates `ansys-api-acp` from 0.1.0.dev8 to 0.1.0.dev9\r\n- [Release notes](https://github.com/ansys/ansys-api-acp/releases)\r\n- [Commits](https://github.com/ansys/ansys-api-acp/compare/v0.1.0.dev8...v0.1.0.dev9)\r\n\r\nUpdates `pyvista` from 0.43.10 to 0.44.0\r\n- [Release notes](https://github.com/pyvista/pyvista/releases)\r\n- [Commits](https://github.com/pyvista/pyvista/compare/v0.43.10...v0.44.0)\r\n\r\nUpdates `matplotlib` from 3.9.0 to 3.9.1\r\n- [Release notes](https://github.com/matplotlib/matplotlib/releases)\r\n- [Commits](https://github.com/matplotlib/matplotlib/compare/v3.9.0...v3.9.1)\r\n\r\nUpdates `ipykernel` from 6.29.4 to 6.29.5\r\n- [Release notes](https://github.com/ipython/ipykernel/releases)\r\n- [Changelog](https://github.com/ipython/ipykernel/blob/v6.29.5/CHANGELOG.md)\r\n- [Commits](https://github.com/ipython/ipykernel/compare/v6.29.4...v6.29.5)\r\n\r\nUpdates `hypothesis` from 6.104.2 to 6.105.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.104.2...hypothesis-python-6.105.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-api-acp\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: pyvista\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: matplotlib\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ipykernel\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-07-08T08:26:39+02:00",
          "tree_id": "7a009d2d947002b8b657a9f1990931cb75353101",
          "url": "https://github.com/ansys/pyacp/commit/45a364d22ca048cfa91f7b21e04afef311aad8aa"
        },
        "date": 1720420148297,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 7.00591244223932,
            "unit": "iter/sec",
            "range": "stddev: 0.004604863671571229",
            "extra": "mean: 142.73658259999138 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1255.732334948518,
            "unit": "iter/sec",
            "range": "stddev: 0.00022906550067716835",
            "extra": "mean: 796.3480529797758 usec\nrounds: 2114"
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
          "id": "d893c29615d9607564fe254322faa01896087aea",
          "message": "Bump hypothesis from 6.105.1 to 6.108.1 in the dependencies group (#549)\n\nBumps the dependencies group with 1 update: [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `hypothesis` from 6.105.1 to 6.108.1\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.105.1...hypothesis-python-6.108.1)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-07-15T07:38:15+02:00",
          "tree_id": "3316a45f6a2d8e6618fc777cf31bf83ac92da13d",
          "url": "https://github.com/ansys/pyacp/commit/d893c29615d9607564fe254322faa01896087aea"
        },
        "date": 1721022072619,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.713782262907848,
            "unit": "iter/sec",
            "range": "stddev: 0.0031603216392314323",
            "extra": "mean: 148.9473385999986 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1238.1900240077578,
            "unit": "iter/sec",
            "range": "stddev: 0.0002206119918917137",
            "extra": "mean: 807.6304772374217 usec\nrounds: 1911"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "dominik.gresch@ansys.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "committer": {
            "email": "greschd@users.noreply.github.com",
            "name": "Dominik Gresch",
            "username": "greschd"
          },
          "distinct": true,
          "id": "dba9c86956eb5763117fac7dec38ea51c0b578a1",
          "message": "Remove now-redundant type cast",
          "timestamp": "2024-07-22T08:57:15+02:00",
          "tree_id": "3fb6d938b66a5669310cafeb444b459f7731b6d6",
          "url": "https://github.com/ansys/pyacp/commit/dba9c86956eb5763117fac7dec38ea51c0b578a1"
        },
        "date": 1721631585991,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 6.356905009183006,
            "unit": "iter/sec",
            "range": "stddev: 0.005543953668913171",
            "extra": "mean: 157.30925639999782 msec\nrounds: 5"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1284.0377045492414,
            "unit": "iter/sec",
            "range": "stddev: 0.00019792499954224139",
            "extra": "mean: 778.7933301779856 usec\nrounds: 1690"
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
          "id": "2800e91dbfe767623483b9322b260b665c12f72f",
          "message": "Bump the dependencies group with 4 updates (#551)\n\nBumps the dependencies group with 4 updates: [grpcio-health-checking](https://grpc.io), [pre-commit](https://github.com/pre-commit/pre-commit), [pytest](https://github.com/pytest-dev/pytest) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `grpcio-health-checking` from 1.48.2 to 1.62.2\r\n\r\nUpdates `pre-commit` from 3.7.1 to 3.8.0\r\n- [Release notes](https://github.com/pre-commit/pre-commit/releases)\r\n- [Changelog](https://github.com/pre-commit/pre-commit/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/pre-commit/pre-commit/compare/v3.7.1...v3.8.0)\r\n\r\nUpdates `pytest` from 8.3.1 to 8.3.2\r\n- [Release notes](https://github.com/pytest-dev/pytest/releases)\r\n- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)\r\n- [Commits](https://github.com/pytest-dev/pytest/compare/8.3.1...8.3.2)\r\n\r\nUpdates `hypothesis` from 6.108.2 to 6.108.5\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.108.2...hypothesis-python-6.108.5)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: grpcio-health-checking\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pre-commit\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: pytest\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-07-29T08:11:02+02:00",
          "tree_id": "1e0f79ff0b2ca03a0cef3460a544a0b8efd5b660",
          "url": "https://github.com/ansys/pyacp/commit/2800e91dbfe767623483b9322b260b665c12f72f"
        },
        "date": 1722233608150,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.78482072057511,
            "unit": "iter/sec",
            "range": "stddev: 0.015450118458565608",
            "extra": "mean: 113.8327157500072 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1338.625038871985,
            "unit": "iter/sec",
            "range": "stddev: 0.00022254373961537064",
            "extra": "mean: 747.0351823410288 usec\nrounds: 1914"
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
          "id": "2d5db9d654aa2945f79615857005e95a43104179",
          "message": "Bump the dependencies group with 5 updates (#553)\n\nBumps the dependencies group with 5 updates:\r\n\r\n| Package | From | To |\r\n| --- | --- | --- |\r\n| [ansys-dpf-core](https://github.com/ansys/pydpf-core) | `0.12.2` | `0.13.0` |\r\n| [black](https://github.com/psf/black) | `24.4.2` | `24.8.0` |\r\n| [mypy](https://github.com/python/mypy) | `1.11.0` | `1.11.1` |\r\n| [sphinx-design](https://github.com/executablebooks/sphinx-design) | `0.6.0` | `0.6.1` |\r\n| [hypothesis](https://github.com/HypothesisWorks/hypothesis) | `6.108.5` | `6.108.8` |\r\n\r\n\r\nUpdates `ansys-dpf-core` from 0.12.2 to 0.13.0\r\n- [Release notes](https://github.com/ansys/pydpf-core/releases)\r\n- [Commits](https://github.com/ansys/pydpf-core/compare/v0.12.2...v0.13.0)\r\n\r\nUpdates `black` from 24.4.2 to 24.8.0\r\n- [Release notes](https://github.com/psf/black/releases)\r\n- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)\r\n- [Commits](https://github.com/psf/black/compare/24.4.2...24.8.0)\r\n\r\nUpdates `mypy` from 1.11.0 to 1.11.1\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.11...v1.11.1)\r\n\r\nUpdates `sphinx-design` from 0.6.0 to 0.6.1\r\n- [Release notes](https://github.com/executablebooks/sphinx-design/releases)\r\n- [Changelog](https://github.com/executablebooks/sphinx-design/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/executablebooks/sphinx-design/compare/v0.6.0...v0.6.1)\r\n\r\nUpdates `hypothesis` from 6.108.5 to 6.108.8\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.108.5...hypothesis-python-6.108.8)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys-dpf-core\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: black\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-minor\r\n  dependency-group: dependencies\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: sphinx-design\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-08-05T08:22:05+02:00",
          "tree_id": "90e3835bf1c1ed97a7f6b50424e8c382f9fb1f42",
          "url": "https://github.com/ansys/pyacp/commit/2d5db9d654aa2945f79615857005e95a43104179"
        },
        "date": 1722839090894,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.511456149205078,
            "unit": "iter/sec",
            "range": "stddev: 0.016708233710771063",
            "extra": "mean: 117.48870962501456 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1364.9571088767257,
            "unit": "iter/sec",
            "range": "stddev: 0.00021717270723922225",
            "extra": "mean: 732.6237531543665 usec\nrounds: 1823"
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
          "id": "bda68366c1c5deb016bbf3dbb6ccfda06cd27d46",
          "message": "Bump ansys/actions from 6 to 7 (#555)\n\nBumps [ansys/actions](https://github.com/ansys/actions) from 6 to 7.\r\n- [Release notes](https://github.com/ansys/actions/releases)\r\n- [Commits](https://github.com/ansys/actions/compare/v6...v7)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: ansys/actions\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-08-14T11:26:41+02:00",
          "tree_id": "67960e5a1547900067ac1873a64694b386515b42",
          "url": "https://github.com/ansys/pyacp/commit/bda68366c1c5deb016bbf3dbb6ccfda06cd27d46"
        },
        "date": 1723627740594,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.672786325630417,
            "unit": "iter/sec",
            "range": "stddev: 0.015553734295004683",
            "extra": "mean: 115.30319812500522 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1296.9784344888833,
            "unit": "iter/sec",
            "range": "stddev: 0.00023900283227426777",
            "extra": "mean: 771.0228431007665 usec\nrounds: 2116"
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
          "id": "bb2d70e217a20b03e0f63455143b0169fde8953e",
          "message": "Remove note about 2024R2 server not being released (#552)",
          "timestamp": "2024-08-18T21:33:30+02:00",
          "tree_id": "e3ab7a862aa1df80e0388167aa7268b0adee2991",
          "url": "https://github.com/ansys/pyacp/commit/bb2d70e217a20b03e0f63455143b0169fde8953e"
        },
        "date": 1724009762096,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.900762010924558,
            "unit": "iter/sec",
            "range": "stddev: 0.014848842681326411",
            "extra": "mean: 112.34993125000159 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1282.467038713375,
            "unit": "iter/sec",
            "range": "stddev: 0.0002460003108671497",
            "extra": "mean: 779.7471356482131 usec\nrounds: 2160"
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
          "id": "eb5056ca886e76366197d491047c1da64ee7a03c",
          "message": "Update to ansys-sphinx-theme 1.x (#558)\n\nCo-authored-by: René Roos <105842014+roosre@users.noreply.github.com>",
          "timestamp": "2024-08-19T00:02:54+02:00",
          "tree_id": "87ee84e046afa8baaed6d0faad0e895e04fbd017",
          "url": "https://github.com/ansys/pyacp/commit/eb5056ca886e76366197d491047c1da64ee7a03c"
        },
        "date": 1724018719494,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.87401875482209,
            "unit": "iter/sec",
            "range": "stddev: 0.013606663966749453",
            "extra": "mean: 112.68851549999326 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1268.0382028271993,
            "unit": "iter/sec",
            "range": "stddev: 0.0002472626335859284",
            "extra": "mean: 788.6197732611012 usec\nrounds: 2214"
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
          "id": "a2feb2ce1ab8e60cf2267c0bda60c713f9807bd6",
          "message": "Implement ply geometry export for modeling plies (#557)\n\nMerging the changes from #545 onto `main`.\r\n\r\nAdd an `export_modeling_ply_geometries` method to the `Model`, which the geometry of all modeling plies\r\n\r\nOther changes:\r\n- Add a helper function for managing the version of the server which supports a particular feature.\r\n- Since that required knowing the server version at the `TreeObject` level, convert the `channel` member into a `ServerWrapper` which contains both the channel and version.\r\n- Force newer version of `ansys-mapdl-core`, to avoid poetry resolving numpy to version 2.0 and downgrading `ansys-mapdl-core`, since older versions do not declare their incompatibility with numpy 2.0.",
          "timestamp": "2024-08-20T17:15:17+02:00",
          "tree_id": "fdb0ff54f661ad8fe3ae4fbc190b5e47659ace96",
          "url": "https://github.com/ansys/pyacp/commit/a2feb2ce1ab8e60cf2267c0bda60c713f9807bd6"
        },
        "date": 1724167065524,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.851324996606074,
            "unit": "iter/sec",
            "range": "stddev: 0.014189443479757131",
            "extra": "mean: 112.97743562499818 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1269.0681546116514,
            "unit": "iter/sec",
            "range": "stddev: 0.00024611884216132736",
            "extra": "mean: 787.9797443235119 usec\nrounds: 2202"
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
          "id": "31a3798febb2c1750afa4f4d19ba57e214f23814",
          "message": "Fix EdgePropertyList construction via _from_object_info (#562)\n\nFixes #561\r\n\r\nThe `EdgePropertyList` retains the _same_ list instance during its lifetime \r\nfor containing the edge property wrappers. This is done so that references\r\nuser code might hold to its items to correctly update its contents.\r\n\r\nIn contrast to other types, it means that the state is not re-fetched from\r\nthe `_pb_object` if it were to change outside of the `EdgePropertyList`'s\r\ncontrol.\r\nThis led to a bug when constructing objects via `_from_object_info`, which\r\nfirst default-constructs the object (in the process creating the `EdgePropertyList`)\r\nand then modifies the `_pb_object`.\r\n\r\nTo fix this, the `EdgePropertyList` now stores whether its parent object was\r\nstored when this list was last accessed. If it changes from unstored to stored,\r\nthe following logic is applied:\r\n- If the current list is already populated (the \"regular\" case), only a sanity check\r\n  for matching length is performed\r\n- If the current list is empty, it is re-fetched from the parent object. This is the\r\n  case which occurs during construction with `_from_object_info`\r\n\r\nSince the edge property list can be in an inconsistent state (empty when it shouldn't \r\nbe) while the parent is unstored, we disallow accessing it in this state. It is still\r\nallowed however to fully replace the contents.\r\n\r\nThis PR also fixes a bug in `tree_object_from_resource_path`, where the `channel`\r\nargument was still used instead of `server_wrapper`.",
          "timestamp": "2024-08-24T00:32:39+02:00",
          "tree_id": "71c249cfd3828936fe32d7c0076334b211adfa73",
          "url": "https://github.com/ansys/pyacp/commit/31a3798febb2c1750afa4f4d19ba57e214f23814"
        },
        "date": 1724452517836,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 9.404657617185421,
            "unit": "iter/sec",
            "range": "stddev: 0.002932324596295923",
            "extra": "mean: 106.33029299999919 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1261.995932342557,
            "unit": "iter/sec",
            "range": "stddev: 0.0002526745779919674",
            "extra": "mean: 792.3955809776409 usec\nrounds: 2229"
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
          "id": "acee20f5614ddd233096561f29515695d766d47b",
          "message": "Bump the dependencies group across 1 directory with 3 updates (#568)\n\nBumps the dependencies group with 3 updates in the / directory: [mypy](https://github.com/python/mypy), [ansys-sphinx-theme](https://github.com/ansys/ansys-sphinx-theme) and [hypothesis](https://github.com/HypothesisWorks/hypothesis).\r\n\r\n\r\nUpdates `mypy` from 1.11.1 to 1.11.2\r\n- [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md)\r\n- [Commits](https://github.com/python/mypy/compare/v1.11.1...v1.11.2)\r\n\r\nUpdates `ansys-sphinx-theme` from 1.0.4 to 1.0.7\r\n- [Release notes](https://github.com/ansys/ansys-sphinx-theme/releases)\r\n- [Commits](https://github.com/ansys/ansys-sphinx-theme/compare/v1.0.4...v1.0.7)\r\n\r\nUpdates `hypothesis` from 6.111.1 to 6.111.2\r\n- [Release notes](https://github.com/HypothesisWorks/hypothesis/releases)\r\n- [Commits](https://github.com/HypothesisWorks/hypothesis/compare/hypothesis-python-6.111.1...hypothesis-python-6.111.2)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: mypy\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: ansys-sphinx-theme\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n- dependency-name: hypothesis\r\n  dependency-type: direct:development\r\n  update-type: version-update:semver-patch\r\n  dependency-group: dependencies\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>",
          "timestamp": "2024-08-26T08:09:28+02:00",
          "tree_id": "24d81d122c157e00d7b6e10e083926ce00cbb6f1",
          "url": "https://github.com/ansys/pyacp/commit/acee20f5614ddd233096561f29515695d766d47b"
        },
        "date": 1724652710729,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 9.47594711283057,
            "unit": "iter/sec",
            "range": "stddev: 0.0022929029948249476",
            "extra": "mean: 105.53034837499098 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1225.7058633068418,
            "unit": "iter/sec",
            "range": "stddev: 0.0002617695032811329",
            "extra": "mean: 815.856421949465 usec\nrounds: 2287"
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
          "id": "b4bba3041c2dba45bc8bb75a5098105bb889b7b3",
          "message": "Accept empty resource paths in linked objects when storing (#569)\n\nThe `.store()` method contains a check that all linked objects are\r\nwithin the same model. However, this check falsely raised when\r\ngiven an empty resource path. This is now fixed by filtering out\r\nthe empty resource paths in the check.",
          "timestamp": "2024-08-26T06:27:57Z",
          "tree_id": "64bd3c961433db2bf5ca7943b57a6dd8387b3bb3",
          "url": "https://github.com/ansys/pyacp/commit/b4bba3041c2dba45bc8bb75a5098105bb889b7b3"
        },
        "date": 1724653820964,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 9.383849090656735,
            "unit": "iter/sec",
            "range": "stddev: 0.003408567928273312",
            "extra": "mean: 106.56607862499357 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1250.7764546441347,
            "unit": "iter/sec",
            "range": "stddev: 0.00025756993824539145",
            "extra": "mean: 799.5033775116237 usec\nrounds: 2090"
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
          "id": "9a8bb9bea4240de6ef7ccaabceaa7192fe3ac7e5",
          "message": "Add step for testing on the released server (#573)\n\nAdd a step to the tests on Python 3.12 for testing with the 2024R2 server version.\r\n\r\nExpected test failures (new features) are marked with the new `xfail_before` fixture. The\r\nonly current expected failure is the modeling ply geometry export test (added in 25.1).\r\n\r\nAlso fixes an issue with the `clone` method when `unlink=True` is specified: Any \r\nfields unknown to the current client were retained. This caused an error on storing,\r\nsince those may be unknown linked objects. In the current case, the newly added \r\nlinks to the `Fabric` caused this.\r\nCalling `DiscardUnknownFields()` on the protobuf message fixes this.",
          "timestamp": "2024-09-03T11:27:27+02:00",
          "tree_id": "664dc57cadada66e226ab65a7ba5e869c512d11d",
          "url": "https://github.com/ansys/pyacp/commit/9a8bb9bea4240de6ef7ccaabceaa7192fe3ac7e5"
        },
        "date": 1725355903103,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 9.355968024061362,
            "unit": "iter/sec",
            "range": "stddev: 0.0028730502128676886",
            "extra": "mean: 106.88364874999934 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1294.3554120502777,
            "unit": "iter/sec",
            "range": "stddev: 0.00022950214368226704",
            "extra": "mean: 772.585327561605 usec\nrounds: 2079"
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
          "id": "b9c40d3d2cbd21a367dae139a8705035ca1808eb",
          "message": "Merge pull request #576 from ansys/dependabot/pip/dependencies-d2235673a0\n\nBump the dependencies group across 1 directory with 5 updates",
          "timestamp": "2024-09-09T09:18:18+02:00",
          "tree_id": "00d30409bd6023dde07ee692a5df0f067dee3c4f",
          "url": "https://github.com/ansys/pyacp/commit/b9c40d3d2cbd21a367dae139a8705035ca1808eb"
        },
        "date": 1725866542038,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/benchmarks/test_class40.py::test_class40",
            "value": 8.844504238109343,
            "unit": "iter/sec",
            "range": "stddev: 0.0035821919131723903",
            "extra": "mean: 113.0645622499884 msec\nrounds: 8"
          },
          {
            "name": "tests/benchmarks/test_create.py::test_create_modeling_group",
            "value": 1463.5036673117063,
            "unit": "iter/sec",
            "range": "stddev: 0.00018823525653927805",
            "extra": "mean: 683.2917623205476 usec\nrounds: 1603"
          }
        ]
      }
    ]
  }
}