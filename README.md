[![OCM Integration Tests](https://github.com/open-component-model/ocm-integrationtest/actions/workflows/integrationtest.yaml/badge.svg?branch=main)](https://open-component-model.github.io/ocm-integrationtest/report.html)

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
