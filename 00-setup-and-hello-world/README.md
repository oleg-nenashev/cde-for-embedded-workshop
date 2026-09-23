# 00 - Setup and Hello World

This first section helps you setup the workshop environment and introduces the basic tooling used throughout the course.


## Goals

- Confirm that the prerequisites are installed
- Configuring your IDE to work with Dev Containers
- Open the repository in a Dev Container
- Run a simple containerized "hello world" example

## Step 1. Confirming the prerequisites

Check out the prerequisites in the [main README](../README.md) and confirm that you have the mentioned tools in place.
For the first steps, you will need only Visual Studio Code (VS Code), 
and a container engine (Docker Desktop or Podman).

If you have not done it already, pull the following images so that they get cached
while you follow the steps below.
The examples state `docker` but the same can be done with `podman`.

```shell
docker pull hello-world
docker pull mcr.microsoft.com/devcontainers/base:ubuntu
docker pull mcr.microsoft.com/devcontainers/python:3-3.14-trixie
docker pull debian:bookworm-20250317
docker pull ros:kilted-ros-base-noble
docker pull postgres:latest
```

To test whether Docker or Podman run properly, 
using one of the following commands:

```shell
docker run --rm hello-world
podman run --rm hello-world
```

## Step 2. Configure the environment

1. Open Visual Studio Code (VS Code). 
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.
3. Open this directory in VS Code as a project.

### Podman specifics

When using Podman for the workshop, you will need to modify the executables for the commands to be used in Visual Studio Code.
Most recent of Podman should not require any other configuration when running with Podman.

```json
{
  "dev.containers.dockerPath": "podman",
  "dev.containers.dockerComposePath": "podman-compose"
}
```


### Windows specifics

You can get the workshop running on Windows,
It is tested on the WSL2 + Podman configuration.
However, there may be additional complications, and assistance from the tutor may be required.

TODO: add VS Code configuration

## Step 3. Explore Dev Containers

In this step, we will get a sample project running.
The goal is to make sure the environment is configured correctly
and that Dev Containers run well.
We will not be modifying the project for this phase.

1. Open the [hello-world](./hello-world/) directory as a project in a separate VS Code window.
2. Run the _Reopen in a Container_ task.  
3. Run the Hello World project
4. Explore the [hello-world](./hello-world/) directory, especially the Dev Containers file

A deeper dive will take place at the next step.

## Step 4. Create a project for the next phases

The next phases of the course will incrementally build the project which is provided in [full-project](../full-project/).

To get started:

1. Go to the TODO repository.
2. Clone the repository to your personal GitHub account.
3. Open the repository in VS Code as a project.

## Expected outcome

By the end of this section, you should be able to start the workshop environment and run a basic containerized command from the Dev Container CLI successfully.

Return to the [main workshop README](../README.md).
