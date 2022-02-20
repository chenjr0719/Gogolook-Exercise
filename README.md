# Gogolook-Exercise

[![Python application](https://github.com/chenjr0719/Gogolook-Exercise/actions/workflows/python-app.yml/badge.svg)](https://github.com/chenjr0719/Gogolook-Exercise/actions/workflows/python-app.yml)
[![Docker Image](https://github.com/chenjr0719/Gogolook-Exercise/actions/workflows/docker-test.yml/badge.svg)](https://github.com/chenjr0719/Gogolook-Exercise/actions/workflows/docker-test.yml)
[![codecov](https://codecov.io/gh/chenjr0719/Gogolook-Exercise/branch/main/graph/badge.svg?token=AJLZJGWDC2)](https://codecov.io/gh/chenjr0719/Gogolook-Exercise)

A RESTful task list API

## How to use it?

To run the whole system with less setup, please run it with [docker-compose](https://docs.docker.com/compose/). Simply run the script:

```shell
./scripts/docker_compose_up.sh
```

And if you need to showdown the system, use another script to shut it down:

```shell
./scripts/docker_compose_down.sh
```

When you need to remove the whole system, including all the persist data (ex: DB), use the purge script:

```shell
./scripts/docker_compose_purge.sh
```

## How to contribute to this project?

Please check the [Contributing guide](CONTRIBUTING.md) for more information.
