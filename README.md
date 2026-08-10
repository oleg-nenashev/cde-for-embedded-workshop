# Workshop - Container Developer Environments. Virtualizing your IDEs for embedded projects

## Abstract

Embedded development and QA are entering a new era, enabled by Cloud Development Environments (CDEs) such as GitHub Codespaces or Devcontainers, which allow fully configured workspaces to run on laptops, Kubernetes clusters, or public clouds.
Containers and VMs, often managed with tools like KubeVirt and QEMU, and wrapped by frameworks like Testcontainers, enable scalable, hardware-aware test setups that support HIL testing, firmware validation, and system modeling.
It might sound like a miracle, but it’s actually possible with modern tech stacks!

During this workshop, we will go through building a containerized developer environment for a robotics project using the open-source ROS2 stack (C++/Python, CMake, custom build tools, Gazebo, etc.), or by using another example nominated by the audience.
Step by step, you will learn to define and customize [Dev Containers](https://devcontainers.github.io/) for their technology stacks, 
adapt IDEs for embedded workflows, and package the full environment for sharing across teams and reuse in CI/CD pipelines.

We will also explore how these same environments can be moved beyond the laptop and executed in cloud-based development platforms such as GitHub Codespaces and similar providers.
In addition, the workshop will demonstrate how tools such as Testcontainers and API-mocking frameworks can support integration testing even in embedded projects, where external services, simulated devices, and distributed components increasingly play an important role.
Last but not least, we will look into leveraging the local AI capabilities of Large and Small Language Models in our developer environments and tests, with Dev Containers features and Testcontainers extensions.

By the end of the session, participants will have a clear understanding of how to virtualize their IDEs, standardize developer onboarding, and create reusable development environments that connect local workstations, cloud platforms, and automated pipelines.

## Prerequisites

* Bring-your-own laptop: Linux, MacOS or Windows
* Pre-installed tools
  * Installed Docker engine: Docker Desktop or Podman
  * Git
  * Visual Studio Code
* A GitHub Account
* Good internet connection

## Workshop Structure

* [Environment Setup](./00-setup-and-hello-world/README.md)
* [Devcontainer Basics](./01-devcontainer-basics/README.md)
* [Using AI and agents in Devcontainers](./02-ai-integrations/README.md)
* [Python tooling in a Devcontainer](./03-python-tooling-basics/README.md)
* [C/C++ tooling in a Devcontainer](./04-cpp-tooling-basics/README.md)
* [ROS and Gazebo in a Devcontainer](./05-ros-gazebo/README.md)
* [Using Devcontainers in CI](./06-ci-integrations/README.md)
* Optional - [Integration Testing with Testcontainers](./07-integration-testing/README.md)
* Optional - [Connecting hardware to a Devcontainer](./08-external-hardware/README.md)
* [Moving to a Cloud Developer Environment](./09-devcontainer-in-a-cde/README.md)

## Before the workshop starts

The workshop is quite heavy about the network traffic due to image pulls and
dependency installations from package managers.
To make it faster, run the following commands:

```shell
docker pull hello-world
docker pull debian:bookworm-20250317
docker pull ros:kilted-ros-base-noble
```

## References

- [Full project](./full-project/) - something you can start without going through the workshop stages. It can be opened in an IDE and you can follow it
- [Slides: 
Cloud and Hybrid Developer Environments - how virtualization transforms your IDEs for embedded projects](https://speakerdeck.com/onenashev/cloud-and-hybrid-developer-environments-how-virtualization-transforms-your-ides-for-embedded-projects) - my original presentation on Dev Containers from QA&Test 2025

## License

All code is licensed under the [Apache License v2.0](./LICENSE).


