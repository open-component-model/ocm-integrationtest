[![OCM Integration Tests](https://github.com/jensh007/testocm/actions/workflows/integrationtest.yaml/badge.svg?branch=main)](https://jensh007.github.io/testocm/report.html)

[![REUSE status](https://api.reuse.software/badge/github.com/open-component-model/ocm-integrationtest)](https://api.reuse.software/info/github.com/open-component-model/ocm-integrationtest)

# Open-Component-Model Integration Test

## About this project

This repository runs the OCM integration tests. It installs a local OCI registry, performs various OCM commands and checks for the expected results.

## Requirements and Setup

This project uses Python 3.9+ to run the tests against the OCM CLI. It is targeted to be executed in
a Github action workflow. You also can run the tests locally:

* Install Python 3.9+
* Create a virtual environment, e.g `python -m venv <path-to-your-env>/ocmtest`
* Install pip: `python -m pip install --upgrade pip`
* Activate environment: `. <path-to-your-env>/ocmtest/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Install docker
* Install htpasswd
* Create SSL certificates and store them in `./certs` directory (see `create-cert.sh` for instructions [Link](create-cert.sh) (be sure to have a hostname with a fully qualified domain name)
* Create a user for the OCI registry and passwd file: `htpasswd -b -v certs/htpasswd ocmuser <my-secret-password>`
* Set environment variables: `export FDQN_NAME=<Your fully qualified host-name>:4430; export USER_NAME=ocmuser; export PASSWD=<my-secret-password>`
* If you user alternative container runtimes to docker (like e.g. colima) you may need to set DOCKER_HOST env var. e.g.: `export DOCKER_HOST=unix:///Users/<my-user>/.colima/default/docker.sock`
* Run local OCI registry in docker: `./start_docker.sh`
* Run tests: `pytest tests`
* Stop and remove container: `./stop_docker.sh`

## Support, Feedback, Contributing

This project is open to feature requests/suggestions, bug reports etc. via [GitHub issues](https://github.com/SAP/<your-project>/issues). Contribution and feedback are encouraged and always welcome. For more information about how to contribute, the project structure, as well as additional contribution information, see our [Contribution Guidelines](CONTRIBUTING.md).

## Code of Conduct

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone. By participating in this project, you agree to abide by its [Code of Conduct](CODE_OF_CONDUCT.md) at all times.

## Licensing

Copyright 2022-2023 SAP SE or an SAP affiliate company and <your-project> contributors. Please see our [LICENSE](LICENSE) for copyright and license information. Detailed information including third-party components and their licensing/copyright information is available [via the REUSE tool](https://api.reuse.software/info/github.com/SAP/<your-project>).

