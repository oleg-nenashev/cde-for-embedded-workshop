# 03 - Custom Images

Ability to add custom Docker images is one of the best capability of Dev Containers.
In previous sections, we used the default images and only used features to customize them.
Now, we will customize the images.

## Goals

- Set up a Python development environment inside the container
- Use common tooling such as virtual environments and package managers
- Run simple checks and tests from the workspace

## Steps

### 1. Custom Images



### 2. Docker Compose

In addition to single images, you can have a full-fledged Docker Compose configuration.
This might be useful if you bring in additional images, e.g. a database.
In the workshop we will not be creating such a Dev Container on our own.
Instead, we will just use a sample project from the official [Dev Containers Guide](https://containers.dev/guide/dockerfile#docker-compose).

1. Go to [06-docker-compose](./02-docker-compose/)
2. Follow the instructions in the demo

## Expected outcome

You should be able to work with Python in a repeatable, container-based setup and understand the value of consistent tooling.

Return to the [main workshop README](../README.md).
