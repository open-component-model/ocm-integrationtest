[![REUSE status](https://api.reuse.software/badge/github.com/open-component-model/ocm-integrationtest)](https://api.reuse.software/info/github.com/open-component-model/ocm-integrationtest) [![OCM Integration Tests](https://github.com/open-component-model/ocm-integrationtest/actions/workflows/integrationtest.yaml/badge.svg?branch=main)](https://open-component-model.github.io/ocm-integrationtest/report.html)

# Open-Component-Model Integration Test

## About this project

This repository runs the OCM integration tests. It installs a local OCI registry, performs various OCM commands and checks for the expected results.

## Requirements and Setup

This project uses Python 3.9+ to run the tests against the [OCM CLI](https://github.com/open-component-model/ocm). It is targeted to be executed in a Github action workflow. You can also run the tests locally:

* Install Python 3.9+
* Create a virtual environment, e.g `python -m venv <path-to-your-env>/ocmtest`
* Install pip: `python -m pip install --upgrade pip`
* Activate environment: `. <path-to-your-env>/ocmtest/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Install docker
* Install htpasswd
* Install [crane](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)
* Create SSL certificates and store them in `./certs` directory (see `create-cert.sh` for instructions [Link](create-cert.sh) (be sure to have a hostname with a fully qualified domain name)
* Create a user for the OCI registry and passwd file: `htpasswd -b -v certs/htpasswd ocmuser <my-secret-password>`
* Set environment variables: `export FDQN_NAME=<Your fully qualified host-name>:4430; export USER_NAME=ocmuser; export PASSWD=<my-secret-password>`
* If you user alternative container runtimes to docker (like e.g. colima) you may need to set DOCKER_HOST env var. e.g.: `export DOCKER_HOST=unix:///Users/<my-user>/.colima/default/docker.sock`
* Run local OCI registry in docker: `./start_docker.sh`
* Build local test binaries: `./build.sh`
* Run tests: `pytest tests`
* Stop and remove container: `./stop_docker.sh`

## Support, Feedback, Contributing

This project is open to feature requests/suggestions, bug reports etc. via [GitHub issues](https://github.com/open-component-model/ocm-integrationtest/issues). Contribution and feedback are encouraged and always welcome. For more information about how to contribute, the project structure, as well as additional contribution information, see our [Contribution Guidelines](CONTRIBUTING.md).

## Code of Conduct

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone. By participating in this project, you agree to abide by its [Code of Conduct](CODE_OF_CONDUCT.md) at all times.

## Licensing

Copyright 2022-2023 SAP SE or an SAP affiliate company and open-component-model contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information including third-party components and their licensing/copyright information is available [via the REUSE tool](https://api.reuse.software/info/github.com/open-component-model/ocm-integrationtest).

## Test Report

[Latest Test Report](https://open-component-model.github.io/ocm-integrationtest/report.html)

## Statistics

Statistics of the latest [test runs](https://github.com/open-component-model/ocm-integrationtest/actions/workflows/integrationtest.yaml):

Date + Time | OCM Version | Result
------------|-------------|-------
2023-05-11 13:23:21+0000 | ocm version 0.3.0-rc.2 | &#9989; (passed)
2023-05-12 02:18:54+0000 | ocm version 0.3.0-rc.2 | &#9989; (passed)
2023-05-12 08:15:11+0000 | ocm version 0.3.0-dev+8b33f961e20e1bd646fec5b26352cf3fab2d5569 | &#9989; (passed)
2023-05-12 08:18:09+0000 | ocm version 0.3.0-rc.2 | &#9989; (passed)
2023-05-14 02:23:08+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-15 02:24:50+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-16 02:22:40+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-17 02:22:48+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-18 02:21:51+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-19 02:22:49+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-21 02:26:48+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-22 02:26:39+0000 | ocm version 0.3.0-dev+f2903dd6e7fb6c6ef385d72a198d6819c95b91f2 | &#9989; (passed)
2023-05-24 06:07:05+0000 | ocm version 0.3.0-dev+902e7427c9aa9c2b4bf8b41d5c87882f7e899f15 | &#9989; (passed)
2023-05-25 02:23:06+0000 | ocm version 0.3.0-dev+902e7427c9aa9c2b4bf8b41d5c87882f7e899f15 | &#9989; (passed)
2023-05-26 02:23:05+0000 | ocm version 0.3.0-dev+903326e10fa34a674c493cf73826345d17cf3a3a | &#9989; (passed)
2023-05-27 02:21:57+0000 | ocm version 0.3.0-dev+130abc3db2d7884191ab69c0b08da480063c99ba | &#9989; (passed)
2023-05-28 02:30:48+0000 | ocm version 0.3.0-dev+130abc3db2d7884191ab69c0b08da480063c99ba | &#9989; (passed)
2023-05-29 02:26:36+0000 | ocm version 0.3.0-dev+130abc3db2d7884191ab69c0b08da480063c99ba | &#9989; (passed)
2023-05-30 02:26:16+0000 | ocm version 0.3.0-dev+130abc3db2d7884191ab69c0b08da480063c99ba | &#9989; (passed)
2023-05-31 02:35:10+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-01 02:43:05+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-02 02:33:21+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-03 02:31:45+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-04 02:40:43+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-05 02:35:02+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-06 02:37:06+0000 | ocm version 0.3.0-dev+4b053e6ddd15485b58e9808c3cf33a5034cff541 | &#9989; (passed)
2023-06-07 02:35:57+0000 | ocm version 0.3.0-dev+94f146bdbbeadf9a81472c479c9b2710a18aaa9d | &#9989; (passed)
2023-06-08 02:36:02+0000 | ocm version 0.3.0-dev+8d3b8aa59b922bd66c061b3f1cc3187d1d5e694e | &#9989; (passed)
2023-06-09 02:36:08+0000 | ocm version 0.3.0-dev+8d3b8aa59b922bd66c061b3f1cc3187d1d5e694e | &#9989; (passed)
2023-06-10 02:31:26+0000 | ocm version 0.3.0-dev+0c00a88ddb3da53f507a879f5d62bda7aff49fff | &#9989; (passed)
2023-06-11 02:38:23+0000 | ocm version 0.3.0-dev+0c00a88ddb3da53f507a879f5d62bda7aff49fff | &#9989; (passed)
2023-06-12 02:36:12+0000 | ocm version 0.3.0-dev+0c00a88ddb3da53f507a879f5d62bda7aff49fff | &#9989; (passed)
2023-06-13 02:31:12+0000 | ocm version 0.3.0-dev+0c00a88ddb3da53f507a879f5d62bda7aff49fff | &#9989; (passed)
2023-06-14 02:30:01+0000 | ocm version 0.3.0-dev+0c00a88ddb3da53f507a879f5d62bda7aff49fff | &#9989; (passed)
2023-06-15 02:27:55+0000 | ocm version 0.3.0-dev+c0714531a198f641d176d7e2b0cf47a1a69a7db6 | &#9989; (passed)
2023-06-16 02:28:44+0000 | ocm version 0.3.0-dev+c0714531a198f641d176d7e2b0cf47a1a69a7db6 | &#9989; (passed)
2023-06-17 02:25:11+0000 | ocm version 0.3.0-dev+b49c149a0a476c560ee3eb8eec4b5ba2a77e8606 | &#9989; (passed)
2023-06-18 02:35:45+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-19 02:30:04+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-20 02:25:25+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-21 02:25:44+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-22 02:30:00+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-23 02:36:23+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-23 09:33:09+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-24 02:36:09+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-25 02:43:09+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-26 02:39:55+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-27 02:36:58+0000 | ocm version 0.3.0-dev+70faf42c7d0bce4d1b745b5d6e1ceb221b2798a8 | &#9989; (passed)
2023-06-28 02:36:28+0000 | ocm version 0.3.0-dev+e31420347afdb42398e468113054cafb3b31848e | &#9989; (passed)
2023-06-29 02:35:24+0000 | ocm version 0.3.0-dev+e31420347afdb42398e468113054cafb3b31848e | &#9989; (passed)
2023-06-30 02:35:16+0000 | ocm version 0.3.0-dev+67c2c0a378be15dd44f2188d7ff20280bae4c8a0 | &#9989; (passed)
2023-07-01 02:41:37+0000 | ocm version 0.3.0-dev+b581bb4c1b39ee72186aff0a4f64ba6dca8c1dd4 | &#9989; (passed)
2023-07-02 02:41:03+0000 | ocm version 0.3.0-dev+b581bb4c1b39ee72186aff0a4f64ba6dca8c1dd4 | &#9989; (passed)
2023-07-03 02:37:19+0000 | ocm version 0.3.0-dev+b581bb4c1b39ee72186aff0a4f64ba6dca8c1dd4 | &#9989; (passed)
2023-07-04 02:38:52+0000 | ocm version 0.3.0-dev+b581bb4c1b39ee72186aff0a4f64ba6dca8c1dd4 | &#9989; (passed)
2023-07-05 02:37:27+0000 | ocm version 0.3.0-dev+b581bb4c1b39ee72186aff0a4f64ba6dca8c1dd4 | &#9989; (passed)
2023-07-07 02:37:19+0000 | ocm version 0.3.0-dev+8c6e9cf219e78357d0b4273c3c3d87ddb33cca9b | &#9989; (passed)
2023-07-08 02:37:11+0000 | ocm version 0.3.0-dev+8c6e9cf219e78357d0b4273c3c3d87ddb33cca9b | &#9989; (passed)
2023-07-09 02:39:51+0000 | ocm version 0.3.0-dev+8c6e9cf219e78357d0b4273c3c3d87ddb33cca9b | &#9989; (passed)
2023-07-10 02:38:35+0000 | ocm version 0.3.0-dev+8c6e9cf219e78357d0b4273c3c3d87ddb33cca9b | &#9989; (passed)
2023-07-11 02:35:08+0000 | ocm version 0.3.0-dev+8c6e9cf219e78357d0b4273c3c3d87ddb33cca9b | &#9989; (passed)
2023-07-12 02:37:51+0000 | ocm version 0.3.0-dev+289710cc81cdfe9277fc702b98099c55eb2e5286 | &#9989; (passed)
2023-07-13 02:39:36+0000 | ocm version 0.3.0-dev+8abfefa3ca26237759f8299fec846bc3898bcfbb | &#9989; (passed)
2023-07-14 02:37:36+0000 | ocm version 0.3.0-dev+6e9c826c5a5c06528cb250131041c3c371ee8d25 | &#9989; (passed)
2023-07-15 02:38:32+0000 | ocm version 0.3.0-dev+6d7c21618cf9455478316eff18ae744bd83a9b78 | &#9989; (passed)
2023-07-16 02:43:56+0000 | ocm version 0.3.0-dev+6d7c21618cf9455478316eff18ae744bd83a9b78 | &#9989; (passed)
2023-07-17 02:40:10+0000 | ocm version 0.3.0-dev+6d7c21618cf9455478316eff18ae744bd83a9b78 | &#9989; (passed)
2023-07-18 02:40:09+0000 | ocm version 0.3.0-dev+6d7c21618cf9455478316eff18ae744bd83a9b78 | &#9989; (passed)
2023-07-19 03:07:15+0000 | ocm version 0.3.0-dev+6d7c21618cf9455478316eff18ae744bd83a9b78 | &#9989; (passed)
2023-07-20 02:25:00+0000 | ocm version 0.3.0-dev+6ef647ffb0317e0651ba4f90255bdab6f55e78f1 | &#9989; (passed)
2023-07-21 02:25:30+0000 | ocm version 0.3.0-dev+6ef647ffb0317e0651ba4f90255bdab6f55e78f1 | &#9989; (passed)
2023-07-24 07:57:39+0000 | ocm version 0.4.0-dev+c3d77cc04d81e706fc31781ad4e679acec40837d | &#9989; (passed)
2023-07-25 02:33:32+0000 | ocm version 0.4.0-dev+c3d77cc04d81e706fc31781ad4e679acec40837d | &#9989; (passed)
2023-07-26 02:27:36+0000 | ocm version 0.4.0-dev+c321dc869dfebf4c61eddd9919811c641b19a237 | &#9989; (passed)
2023-07-27 02:21:55+0000 | ocm version 0.4.0-dev+25878a816c01347e3ff514f9f27e79b2b4c57d5c | &#9989; (passed)
2023-07-28 02:22:53+0000 | ocm version 0.4.0-dev+f2f0fef26bb2424e2fe3c61b6885a50a78bd9f9f | &#9989; (passed)
2023-07-29 02:20:06+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-07-30 02:22:14+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-07-31 02:23:31+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-08-01 02:28:09+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-08-02 02:20:03+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-08-03 02:21:38+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-08-04 02:23:45+0000 | ocm version 0.4.0-dev+6efa6b7fc47ef3567fd0d16b2c413f58921bee10 | &#9989; (passed)
2023-08-05 02:20:45+0000 | ocm version 0.4.0-dev+b2d2656e1cada41aa09d0eaaf437d01ebc6eb2ae | &#9989; (passed)
2023-08-06 02:16:30+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-07 02:22:16+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-08 02:23:29+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-09 02:22:23+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-10 02:24:42+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-11 02:13:11+0000 | ocm version 0.4.0-dev+a93e07911c38f694859d74e7015f07227150a565 | &#9989; (passed)
2023-08-12 02:11:46+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-13 02:14:37+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-14 02:15:18+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-15 02:13:39+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 02:13:24+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 13:03:45+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 13:20:02+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 13:43:00+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 14:19:28+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-16 14:39:43+0000 | ocm version 0.4.0-dev+26f41d763635e54bc2ee7ed22c30af02c8bbe947 | &#9989; (passed)
2023-08-17 02:14:14+0000 | ocm version 0.4.0-dev+b860b8bc15a38b7a7c7e3820672c812e0ff0f446 | &#9989; (passed)
2023-08-17 06:22:23+0000 | ocm version 0.4.0-dev+ded445a0f27cb42cf1a84e34f56c45d1544526a1 | &#9989; (passed)
