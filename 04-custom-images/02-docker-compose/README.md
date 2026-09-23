# Docker Compose - App + PostgreSQL

This example uses `docker-compose` to run the devcontainer alongside a PostgreSQL
sidecar container, and includes a small Python app that reads/writes data in it.

## Goals

- Understand how `dockerComposeFile` wires multiple services into one devcontainer
- See how a `devcontainer` service can reach another service (`db`) over the network
- Run a small app and its tests against a real PostgreSQL instance

## Getting started

1. Open this folder in VS Code and choose **Reopen in Container**.
   This starts both the `devcontainer` and `db` services defined in
   [docker-compose.yml](.devcontainer/docker-compose.yml).

2. Wait until the completion of the container build, open a new terminal.

## Run the app

```shell
python app.py add "new item"
python app.py list
python app.py help
```

`add` stores an item, `list` prints all stored items, and `help` shows the
available commands.

## Run the tests

```shell
pytest
```

The tests connect to the `db` service (reachable as `localhost:5432` because the
devcontainer shares the `db` container's network namespace) and clear the
`items` table before each test.

## When completed

Return to the [custom images README](../README.md).
