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
2023-08-18 02:13:40+0000 | ocm version 0.4.0-dev+8e2da85eef2db13cb3273776be06c5832058184b | &#9989; (passed)
2023-08-19 02:11:14+0000 | ocm version 0.4.0-dev+8e2da85eef2db13cb3273776be06c5832058184b | &#9989; (passed)
2023-08-20 02:14:26+0000 | ocm version 0.4.0-dev+8e2da85eef2db13cb3273776be06c5832058184b | &#9989; (passed)
2023-08-21 02:13:24+0000 | ocm version 0.4.0-dev+8e2da85eef2db13cb3273776be06c5832058184b | &#9989; (passed)
2023-08-22 02:16:00+0000 | ocm version 0.4.0-dev+8e2da85eef2db13cb3273776be06c5832058184b | &#9989; (passed)
2023-08-22 13:04:11+0000 | ocm version 0.4.0-dev+506aa276f05ac2f430e67c086b89ed686378ccd9 | &#9989; (passed)
2023-08-23 02:13:14+0000 | ocm version 0.4.0-dev+3762bdcb52e9ae03050e27dd76d13ffd102078cf | &#9989; (passed)
2023-08-23 06:25:20+0000 | ocm version 0.4.0-dev+fa6bff2f83a6fc486de45bde113021714550d7b5 | &#9989; (passed)
2023-08-23 12:32:43+0000 | ocm version 0.4.0-dev+2930b4443d1bf30ed0347d04681bb2d48819f6e4 | &#9989; (passed)
2023-08-24 02:13:30+0000 | ocm version 0.4.0-dev+101df6e33e1efb1ec7279c8714de625b5d44430d | &#9989; (passed)
2023-08-24 07:59:47+0000 | ocm version 0.4.0-dev+9422cc911b694acacd2bb793406ab204dc26f9ec | &#9989; (passed)
2023-08-25 02:14:55+0000 | ocm version 0.4.0-dev+101df6e33e1efb1ec7279c8714de625b5d44430d | &#9989; (passed)
2023-08-25 12:55:33+0000 | ocm version 0.4.0-dev+e480adbc141be6c1a86ea05b53f5f6292ff91a45 | &#9989; (passed)
2023-08-25 14:30:31+0000 | ocm version 0.4.0-dev+b65413e84dfcbf1fff917ee23b28fb5e589c9a59 | &#9989; (passed)
2023-08-25 14:53:47+0000 | ocm version 0.4.0-dev+470c2c276b527cac47990a7a2d983a46174d3764 | &#9989; (passed)
2023-08-26 02:14:01+0000 | ocm version 0.4.0-dev+3200204926d6e97c6cf78b78b6a0910e6589aa1e | &#9989; (passed)
2023-08-27 02:15:03+0000 | ocm version 0.4.0-dev+3200204926d6e97c6cf78b78b6a0910e6589aa1e | &#9989; (passed)
2023-08-28 02:15:04+0000 | ocm version 0.4.0-dev+3200204926d6e97c6cf78b78b6a0910e6589aa1e | &#9989; (passed)
2023-08-29 02:43:14+0000 | ocm version 0.4.0-dev+7950357e4650bf898e03298962b8e4ff55debd9c | &#9989; (passed)
2023-08-30 02:14:24+0000 | ocm version 0.4.0-dev+300b0f80b9cc347aa91ca601fab34a23a851f780 | &#9989; (passed)
2023-08-31 02:14:52+0000 | ocm version 0.4.0-dev+300b0f80b9cc347aa91ca601fab34a23a851f780 | &#9989; (passed)
2023-09-01 02:17:47+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-02 02:12:25+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-03 02:15:09+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-04 02:15:10+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-05 02:15:26+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-06 02:15:42+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-07 02:15:33+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-08 02:15:40+0000 | ocm version 0.4.0-dev+9b7263044617bfa85ef0f2601a3af0adcba9f352 | &#9989; (passed)
2023-09-08 08:03:30+0000 | ocm version 0.4.0-dev+b1fb6656172f72dd63e5cac561c04f0e5a3dfab0 | &#9989; (passed)
2023-09-09 02:12:44+0000 | ocm version 0.4.0-dev+b9f08d4a19ddcc8bacebf1a74538e328efd62888 | &#9989; (passed)
2023-09-10 02:16:59+0000 | ocm version 0.4.0-dev+b9f08d4a19ddcc8bacebf1a74538e328efd62888 | &#9989; (passed)
2023-09-11 02:15:19+0000 | ocm version 0.4.0-dev+b9f08d4a19ddcc8bacebf1a74538e328efd62888 | &#9989; (passed)
2023-09-12 02:14:43+0000 | ocm version 0.4.0-dev+b9f08d4a19ddcc8bacebf1a74538e328efd62888 | &#9989; (passed)
2023-09-12 10:55:50+0000 | ocm version 0.4.0-dev+a40ebc3513f9b74c275f9a51b0211c98ba2ae66e | &#9989; (passed)
2023-09-12 13:20:49+0000 | ocm version 0.4.0-dev+d54ccbfca381a869e28118d0f34efb0bbe3563e1 | &#9989; (passed)
2023-09-12 13:26:32+0000 | ocm version 0.4.0-dev+dcc352d01e245d4b117f15d48e1f1626bb134e4d | &#9989; (passed)
2023-09-12 14:50:42+0000 | ocm version 0.4.0-dev+b385d0f47378a465b75da73a0480cb5f2d5916cc | &#9989; (passed)
2023-09-13 02:16:21+0000 | ocm version 0.4.0-dev+53d94beeac09abb4d35c3780b3f21636296b4224 | &#9989; (passed)
2023-09-14 02:15:10+0000 | ocm version 0.4.0-dev+53d94beeac09abb4d35c3780b3f21636296b4224 | &#9989; (passed)
2023-09-14 07:52:46+0000 | ocm version 0.4.0-dev+bcf7d444e929c0b5c03092351c6b1d5db07e7ca5 | &#9989; (passed)
2023-09-14 07:58:32+0000 | ocm version 0.4.0-dev+c5baa4d6c1d817240566aa74f1ed799b8ea1fa88 | &#9989; (passed)
2023-09-14 08:07:16+0000 | ocm version 0.4.0-dev+b31d9036a0466950b4030b2b4395a299556a032d | &#9989; (passed)
2023-09-15 02:16:52+0000 | ocm version 0.5.0-dev+10bb76fffc4bf52348e5d03bf5ae397c90b5b401 | &#9989; (passed)
2023-09-16 02:13:21+0000 | ocm version 0.5.0-dev+10bb76fffc4bf52348e5d03bf5ae397c90b5b401 | &#9989; (passed)
2023-09-17 02:15:46+0000 | ocm version 0.5.0-dev+10bb76fffc4bf52348e5d03bf5ae397c90b5b401 | &#9989; (passed)
2023-09-18 02:15:52+0000 | ocm version 0.5.0-dev+10bb76fffc4bf52348e5d03bf5ae397c90b5b401 | &#9989; (passed)
2023-09-18 09:58:40+0000 | ocm version 0.5.0-dev+e72134e2bb9fd26e48a33d743eca0169324f318c | &#9989; (passed)
2023-09-19 02:18:07+0000 | ocm version 0.5.0-dev+3ba87f76ba9fcb07ffab7408b16e74ab8bc76953 | &#9989; (passed)
2023-09-20 02:16:52+0000 | ocm version 0.5.0-dev+3ba87f76ba9fcb07ffab7408b16e74ab8bc76953 | &#9989; (passed)
2023-09-22 14:26:14+0000 | ocm version 0.5.0-dev+47a240f99359dd53d7c5b6b04b3fedb67ba819fe | &#9989; (passed)
2023-09-23 02:15:42+0000 | ocm version 0.5.0-dev+8abf0ec48b767396a8454d5ff1de2cc71f3451a2 | &#9989; (passed)
2023-09-24 02:16:42+0000 | ocm version 0.5.0-dev+965d22959e0568fd0d8402fc22aeb220ec60ed14 | &#9989; (passed)
2023-09-25 02:28:46+0000 | ocm version 0.5.0-dev+965d22959e0568fd0d8402fc22aeb220ec60ed14 | &#9989; (passed)
2023-09-25 10:07:34+0000 | ocm version 0.5.0-dev+c8a7d65b577f1778a88cd5f233841a7d2205fdcc | &#9989; (passed)
2023-09-25 11:40:11+0000 | ocm version 0.5.0-dev+dbd26af1c808bef8a69de5affd9be7bbf2e4a3f3 | &#9989; (passed)
2023-09-26 02:15:55+0000 | ocm version 0.5.0-dev+74c568235579e97cb5ebf65d6d5b59d4accf7a51 | &#9989; (passed)
2023-09-27 02:16:30+0000 | ocm version 0.5.0-dev+541f91b282264c2d7195fcd3bdfcbe35beb283a0 | &#9989; (passed)
2023-09-28 02:16:18+0000 | ocm version 0.5.0-dev+541f91b282264c2d7195fcd3bdfcbe35beb283a0 | &#9989; (passed)
2023-09-29 02:17:35+0000 | ocm version 0.5.0-dev+a68b9c4dfabc4f9201b07ad2b6bee44f6b96aa22 | &#9989; (passed)
2023-09-29 11:16:12+0000 | ocm version 0.5.0-dev+0e44559ead2e9db649af8200bd782a8b002f094d | &#9989; (passed)
2023-09-29 13:16:04+0000 | ocm version 0.5.0-dev+cc58def255077bde93f99bae4739b8e3e120baf4 | &#9989; (passed)
2023-09-29 15:08:55+0000 | ocm version 0.5.0-dev+42808568223087767a017e39f18467c666d7d83c | &#9989; (passed)
2023-09-30 02:15:10+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-01 02:21:27+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-02 02:17:12+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-03 02:16:11+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-04 02:17:33+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-05 02:17:48+0000 | ocm version 0.5.0-dev+da41d204becc4d43cc8c96f5800ea9050199db15 | &#9989; (passed)
2023-10-06 02:16:15+0000 | ocm version 0.5.0-dev+72b80b0b271223036b157cb5e18828ae15c2d367 | &#9989; (passed)
2023-10-07 02:15:01+0000 | ocm version 0.5.0-dev+72b80b0b271223036b157cb5e18828ae15c2d367 | &#9989; (passed)
2023-10-08 02:17:27+0000 | ocm version 0.5.0-dev+72b80b0b271223036b157cb5e18828ae15c2d367 | &#9989; (passed)
2023-10-09 02:19:25+0000 | ocm version 0.5.0-dev+72b80b0b271223036b157cb5e18828ae15c2d367 | &#9989; (passed)
2023-10-09 13:44:14+0000 | ocm version 0.5.0-dev+58d11622321d0d7ec715f3cf525f43b8f4f8068a | &#9989; (passed)
2023-10-10 02:16:18+0000 | ocm version 0.5.0-dev+a5e201209b68e5aab2f96d8848fc74da18ac0973 | &#9989; (passed)
2023-10-10 08:42:29+0000 | ocm version 0.5.0-dev+d649e186744db352b0c1af5124f6cc9bba05927b | &#9989; (passed)
2023-10-10 09:39:20+0000 | ocm version 0.5.0-dev+9c2a1ca272495249e901d7677e9e832829bc7f9c | &#9989; (passed)
2023-10-10 09:45:47+0000 | ocm version 0.5.0-dev+107290a83abde4ec456284f52e2a02a7d3ea70c1 | &#9989; (passed)
2023-10-10 11:46:38+0000 | ocm version 0.5.0-dev+ecf85230d8bab25d61ff31c2a559b33d7126ea84 | &#9989; (passed)
2023-10-10 11:54:57+0000 | ocm version 0.5.0-dev+44934a6659f378a7944eedc16c11c95778d7835f | &#9989; (passed)
2023-10-10 14:56:17+0000 | ocm version 0.5.0-dev+13240e2fc2a379c7de3fd63fda346217965086bd | &#9989; (passed)
2023-10-10 15:03:07+0000 | ocm version 0.5.0-dev+0907e70bdd7b8acc4c6cafa139f966815ea55872 | &#9989; (passed)
2023-10-10 15:40:03+0000 | ocm version 0.5.0-dev+6a7f52614904bfc6ea5a7bef69fbffa4bcb17fd6 | &#9989; (passed)
2023-10-11 02:16:05+0000 | ocm version 0.5.0-dev+a5e201209b68e5aab2f96d8848fc74da18ac0973 | &#9989; (passed)
2023-10-11 12:12:01+0000 | ocm version 0.5.0-dev+b8e0ead4006befe313b4bf678ec3891dda7d6a5b | &#9989; (passed)
2023-10-11 13:18:45+0000 | ocm version 0.5.0-dev+12d0d7aca80161a07cc3e8ae43027636455004db | &#9989; (passed)
2023-10-11 13:24:56+0000 | ocm version 0.5.0-dev+ba6ecda6352e41dc958281640f359e90c54ab545 | &#9989; (passed)
2023-10-11 13:35:20+0000 | ocm version 0.5.0-dev+3c5e21188acd15021feec075a12b8ba6553401f6 | &#9989; (passed)
2023-10-11 14:10:21+0000 | ocm version 0.5.0-dev+f604819fedd733c428b422614e2e7e2d50646e41 | &#9989; (passed)
2023-10-11 14:22:28+0000 | ocm version 0.5.0-dev+fbbd4c48e46896c9156400facdcb9066d0bbf127 | &#9989; (passed)
2023-10-11 14:27:56+0000 | ocm version 0.5.0-dev+19c5e95a629b01e88b33a1833b90f344414ae229 | &#9989; (passed)
2023-10-11 14:39:51+0000 | ocm version 0.5.0-dev+1ddff0a620ba45bad0958c0812bdc99f56e7526e | &#9989; (passed)
2023-10-12 02:14:51+0000 | ocm version 0.5.0-dev+9cfa58a8cdd1cea8f9af6ccf4da74438cd4fbca5 | &#9989; (passed)
2023-10-13 02:19:20+0000 | ocm version 0.5.0-dev+9cfa58a8cdd1cea8f9af6ccf4da74438cd4fbca5 | &#9989; (passed)
2023-10-14 02:13:58+0000 | ocm version 0.5.0-dev+9cfa58a8cdd1cea8f9af6ccf4da74438cd4fbca5 | &#9989; (passed)
2023-10-15 02:17:49+0000 | ocm version 0.5.0-dev+241c6166f4ee934208b05e03d44c8e3af6be9ada | &#9989; (passed)
2023-10-16 02:17:38+0000 | ocm version 0.5.0-dev+241c6166f4ee934208b05e03d44c8e3af6be9ada | &#9989; (passed)
2023-10-16 09:24:51+0000 | ocm version 0.5.0-dev+e1609ebe2f1f81c8830c72c9f1952c36516060e1 | &#9989; (passed)
2023-10-16 09:41:52+0000 | ocm version 0.5.0-dev+53e99864de29aa89b6ae2bffbaaa333989e26f57 | &#9989; (passed)
2023-10-16 10:23:46+0000 | ocm version 0.5.0-dev+1e94e5e4e1c87e0c115b1ea9e09468147776b508 | &#9989; (passed)
2023-10-16 10:31:50+0000 | ocm version 0.5.0-dev+1338d7c52a94e53f9daa6d2206c8fd3ef842846c | &#9989; (passed)
2023-10-16 12:59:23+0000 | ocm version 0.5.0-dev+7044129c1685c2ece23e93bb5550deb112fa5f47 | &#9989; (passed)
2023-10-16 13:09:37+0000 | ocm version 0.5.0-dev+802c2e78843453edca220c6273c82b4aec236043 | &#9989; (passed)
2023-10-17 02:17:17+0000 | ocm version 0.5.0-dev+8b50769dec68a0bb063854d24c923a71e4c990f7 | &#9989; (passed)
2023-10-17 08:59:13+0000 | ocm version 0.5.0-dev+8b50769dec68a0bb063854d24c923a71e4c990f7 | &#9989; (passed)
2023-10-18 02:16:24+0000 | ocm version 0.5.0-dev+8b50769dec68a0bb063854d24c923a71e4c990f7 | &#9989; (passed)
2023-10-18 13:26:05+0000 | ocm version 0.5.0-dev+8b50769dec68a0bb063854d24c923a71e4c990f7 | &#9989; (passed)
2023-10-19 06:11:17+0000 | ocm version 0.5.0-dev+e9f696b8f5dd3e1032e3d4faf01dd7aab1d7c6c4 | &#9989; (passed)
2023-10-20 06:11:12+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-21 06:12:09+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-22 06:11:50+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-23 06:11:09+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-24 06:11:50+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-24 08:10:16+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-24 08:17:33+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-24 08:27:34+0000 | ocm version 0.5.0-dev+0340a0b9664966f4c3e89ab58d234c6142c9df7d | &#9989; (passed)
2023-10-25 06:13:28+0000 | ocm version 0.5.0-dev+7af2f40cebdc80c7cfb0e7857a9351abd8ac5377 | &#9989; (passed)
2023-10-25 22:53:47+0000 | ocm version 0.5.0-dev+7af2f40cebdc80c7cfb0e7857a9351abd8ac5377 | &#9989; (passed)
2023-10-26 06:11:11+0000 | ocm version 0.5.0-dev+7af2f40cebdc80c7cfb0e7857a9351abd8ac5377 | &#9989; (passed)
2023-10-27 06:11:35+0000 | ocm version 0.5.0-dev+f29de6f8c5399729392f4efc4648de89484cde7a | &#9989; (passed)
2023-10-28 06:10:28+0000 | ocm version 0.5.0-dev+b55ecc36c927b03667a5d14134166f46736f306a | &#9989; (passed)
2023-10-29 06:11:04+0000 | ocm version 0.5.0-dev+b55ecc36c927b03667a5d14134166f46736f306a | &#9989; (passed)
2023-10-30 06:11:06+0000 | ocm version 0.5.0-dev+b55ecc36c927b03667a5d14134166f46736f306a | &#9989; (passed)
2023-10-30 15:50:40+0000 | ocm version 0.5.0-dev+b55ecc36c927b03667a5d14134166f46736f306a | &#9989; (passed)
2023-10-31 06:11:48+0000 | ocm version 0.5.0-dev+b55ecc36c927b03667a5d14134166f46736f306a | &#9989; (passed)
2023-11-01 06:11:53+0000 | ocm version 0.5.0-dev+c9994ca3966fd29c2c62ce441280786664c17697 | &#9989; (passed)
2023-11-02 06:09:29+0000 | ocm version 0.5.0-dev+c9994ca3966fd29c2c62ce441280786664c17697 | &#9989; (passed)
2023-11-03 06:10:45+0000 | ocm version 0.5.0-dev+c9994ca3966fd29c2c62ce441280786664c17697 | &#9989; (passed)
2023-12-18 19:25:52+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-18 23:42:57+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-19 06:09:36+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-19 21:27:32+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-20 06:08:40+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-21 06:09:45+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-22 06:09:15+0000 | ocm version 0.6.0-dev+f3d9e9da227f1e1737d5e04f44caa9b277957559 | &#9989; (passed)
2023-12-22 14:23:04+0000 | ocm version 0.6.0-dev+8fb075d6282f2886586a40880f1620365f605fd5 | &#9989; (passed)
2023-12-22 15:15:08+0000 | ocm version 0.6.0-dev+35e332bf2bc8c885c5ec84abab978a7f71fe61e3 | &#9989; (passed)
2023-12-22 15:39:45+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-22 15:44:21+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-23 06:08:44+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-24 06:08:30+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-24 09:03:56+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-25 06:09:53+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-26 06:09:30+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-27 06:09:40+0000 | ocm version 0.6.0-dev+708d2c34ff65f0d9db14cf1c9215c6f65455bbff | &#9989; (passed)
2023-12-28 06:09:01+0000 | ocm version 0.6.0-dev+fade9c4444417bf36bb9ff630891f261b6cc1387 | &#9989; (passed)
2023-12-29 06:09:42+0000 | ocm version 0.6.0-dev+fade9c4444417bf36bb9ff630891f261b6cc1387 | &#9989; (passed)
2023-12-29 11:04:13+0000 | ocm version 0.6.0-dev+dce53f2188c91c354433eee77455b8ec14d598f7 | &#9989; (passed)
2023-12-29 11:16:45+0000 | ocm version 0.6.0-dev+dce53f2188c91c354433eee77455b8ec14d598f7 | &#9989; (passed)
2024-01-16 08:37:26+0000 | ocm version 0.7.0-dev+e4923005ee885ff205b77e11a829ae66fe39683f | &#9989; (passed)
2024-02-01 12:33:04+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-02 06:09:35+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-03 06:09:11+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-04 06:09:07+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-04 08:14:09+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-04 09:00:39+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-05 06:09:13+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-06 06:09:41+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-07 06:09:12+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-08 06:09:52+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-09 06:09:36+0000 | ocm version 0.7.0-dev+1004c32765ee35550f77dfacc62bf50e67fded4a | &#9989; (passed)
2024-02-10 06:08:43+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-11 06:09:24+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-11 08:07:58+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-11 08:47:51+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-12 06:09:05+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-12 13:12:52+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-13 06:09:17+0000 | ocm version 0.7.0-dev+1e39e53ebd5b6c9e06636ae35fe2f38c7bb0c4cc | &#9989; (passed)
2024-02-13 11:26:35+0000 | ocm version 0.7.0-dev+1d2822df007fbfba9f46e9711089999e58fa3f11 | &#9989; (passed)
2024-02-13 14:52:12+0000 | ocm version 0.7.0-dev+f111a7b6be2627823e67f37de488e97960527af5 | &#9989; (passed)
2024-02-13 16:06:44+0000 | ocm version 0.7.0-dev+f111a7b6be2627823e67f37de488e97960527af5 | &#9989; (passed)
2024-02-13 16:25:46+0000 | ocm version 0.7.0-dev+f111a7b6be2627823e67f37de488e97960527af5 | &#9989; (passed)
2024-02-14 06:10:07+0000 | ocm version 0.7.0-dev+ff2691f8ee76aa5cf4c920909a70f33a4d8302f7 | &#9989; (passed)
2024-02-14 07:28:43+0000 | ocm version 0.7.0-dev+ff2691f8ee76aa5cf4c920909a70f33a4d8302f7 | &#9989; (passed)
2024-02-14 15:24:48+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-14 15:44:53+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-15 06:09:53+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-15 15:44:08+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-16 06:09:46+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-16 08:08:31+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-16 10:54:53+0000 | ocm version 0.7.0-dev+d47f376d0f5a2a7fbe41078db7684b6a8ddd478d | &#9989; (passed)
2024-02-16 11:27:32+0000 | ocm version 0.7.0-dev+416964601d91839c0d44ca5941e7ab2e7632a398 | &#9989; (passed)
2024-02-16 14:03:13+0000 | ocm version 0.7.0-dev+ed906a3f1e720679ccf850ad39f595fe752f9ccf | &#9989; (passed)
2024-02-16 14:24:57+0000 | ocm version 0.7.0-dev+ed906a3f1e720679ccf850ad39f595fe752f9ccf | &#9989; (passed)
2024-02-16 14:47:57+0000 | ocm version 0.7.0-dev+ed906a3f1e720679ccf850ad39f595fe752f9ccf | &#9989; (passed)
2024-02-16 21:39:03+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-16 21:43:37+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-16 22:34:18+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-17 06:08:48+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-18 06:09:53+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-18 08:53:20+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-18 09:19:58+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 06:09:30+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 08:37:30+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 09:15:51+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 12:18:11+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 13:01:28+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 13:20:58+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-19 15:09:29+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 06:09:43+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 09:33:10+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 10:06:18+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 12:24:33+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 12:39:58+0000 | ocm version 0.7.0-dev+34e6d2251df6585117b3ae93ad30b707c0c1f5d9 | &#9989; (passed)
2024-02-20 13:05:26+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-20 13:14:44+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-20 13:30:36+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-20 15:16:34+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-21 06:09:26+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-21 09:19:12+0000 | ocm version 0.7.0-dev+2ddf3fea1d80d4f45abc9859e3005940cfd5e84e | &#9989; (passed)
2024-02-21 09:23:26+0000 | ocm version 0.7.0-dev+e73ce3a43ecca3b65bdd192528822ef9ffc25d9b | &#9989; (passed)
2024-02-21 09:32:43+0000 | ocm version 0.7.0-dev+944ddecf1b9ef205b3b3287c56f56e44be7f26c4 | &#9989; (passed)
2024-02-22 06:09:19+0000 | ocm version 0.7.0-dev+944ddecf1b9ef205b3b3287c56f56e44be7f26c4 | &#9989; (passed)
2024-02-22 08:46:52+0000 | ocm version 0.7.0-dev+b60bac1e7323187fc43f2aa3776b2685338a33cd | &#9989; (passed)
2024-02-22 08:55:15+0000 | ocm version 0.7.0-dev+b60bac1e7323187fc43f2aa3776b2685338a33cd | &#9989; (passed)
2024-02-22 09:23:16+0000 | ocm version 0.7.0-dev+137c7966572c8c92be34e859f98de0d869a424b0 | &#9989; (passed)
2024-02-22 13:10:11+0000 | ocm version 0.7.0-dev+137c7966572c8c92be34e859f98de0d869a424b0 | &#9989; (passed)
2024-02-22 16:16:56+0000 | ocm version 0.7.0-dev+137c7966572c8c92be34e859f98de0d869a424b0 | &#9989; (passed)
2024-02-23 06:09:29+0000 | ocm version 0.7.0-dev+137c7966572c8c92be34e859f98de0d869a424b0 | &#9989; (passed)
2024-02-23 11:54:20+0000 | ocm version 0.7.0-dev+137c7966572c8c92be34e859f98de0d869a424b0 | &#9989; (passed)
2024-02-23 14:54:48+0000 | ocm version 0.7.0-dev+929d0ea757c4fba3ac1f2b93f16519b3d51ae421 | &#9989; (passed)
2024-02-23 15:11:29+0000 | ocm version 0.7.0-dev+929d0ea757c4fba3ac1f2b93f16519b3d51ae421 | &#9989; (passed)
2024-02-23 15:28:29+0000 | ocm version 0.7.0-dev+929d0ea757c4fba3ac1f2b93f16519b3d51ae421 | &#9989; (passed)
2024-02-23 16:22:47+0000 | ocm version 0.7.0-dev+cb203c0c28541946cce09b95316401bde7b6f20a | &#9989; (passed)
2024-02-24 06:09:10+0000 | ocm version 0.8.0-dev+fb513e3873d34a2238d11f9c4a83be9fb08a4ed4 | &#9989; (passed)
2024-02-25 06:09:07+0000 | ocm version 0.8.0-dev+fb513e3873d34a2238d11f9c4a83be9fb08a4ed4 | &#9989; (passed)
2024-02-25 09:49:47+0000 | ocm version 0.8.0-dev+fb513e3873d34a2238d11f9c4a83be9fb08a4ed4 | &#9989; (passed)
2024-02-26 06:09:33+0000 | ocm version 0.8.0-dev+fb513e3873d34a2238d11f9c4a83be9fb08a4ed4 | &#9989; (passed)
2024-02-27 06:09:05+0000 | ocm version 0.8.0-dev+2c12eb2de55828cb78566fc90fd40edec3a3d831 | &#9989; (passed)
2024-02-28 06:09:49+0000 | ocm version 0.8.0-dev+2c12eb2de55828cb78566fc90fd40edec3a3d831 | &#9989; (passed)
2024-02-29 06:10:03+0000 | ocm version 0.8.0-dev+2c12eb2de55828cb78566fc90fd40edec3a3d831 | &#9989; (passed)
