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
2024-11-07 11:27:07+0000 | ocm version 0.17.0-dev+2188c1ce78e3cf6aaede3d458388fa947891c581 | &#9989; (passed)
2024-11-08 06:11:31+0000 | ocm version 0.17.0-dev+3577e7e9d72f25a84037aa34818a18c735e95d0a | &#9989; (passed)
2024-11-08 09:51:21+0000 | ocm version 0.17.0-dev+3577e7e9d72f25a84037aa34818a18c735e95d0a | &#9989; (passed)
2024-11-08 11:22:46+0000 | ocm version 0.18.0-dev+beabf65653edb08fff31c056e8645a4fdba75c72 | &#9989; (passed)
2024-11-08 13:38:35+0000 | ocm version 0.18.0-dev+2ea69c7ecca1e8be7e9d9f94dfdcac6090f1c69d | &#9989; (passed)
2024-11-08 18:53:47+0000 | ocm version 0.18.0-dev+2ea69c7ecca1e8be7e9d9f94dfdcac6090f1c69d | &#9989; (passed)
2024-11-08 19:39:22+0000 | ocm version 0.18.0-dev+2ea69c7ecca1e8be7e9d9f94dfdcac6090f1c69d | &#9989; (passed)
