# 01 - Devcontainer Basics

This section introduces the core concepts behind Dev Containers and how they simplify onboarding for software projects.

In this chapter, we will basically rebuild the demo from [00-setup-and-hello-world/hello-world/](../00-setup-and-hello-world/hello-world/),
with a few extra modifications for demo purposes.

## Goals

- Understand what a devcontainer is and why it is useful
- Learn how a container-based development environment is defined
- Explore the relationship between VS Code, Docker, and devcontainer configuration
- Understand basic concepts of Dev Containers, e.g. features and templates

## Theory

1. Take a look at the _01 - Dev Containers 101_ part of the presentation,
   independently or together with the instructor.

2. Learn about key features of Dev Containers from the presentation.
   They will be explained and tested during the tutorial.

## Practice - Your first Dev Containers project

Here, you will create a new project from scratch, using a sample project in [project](./project/) as an example.
A target state after all the listed changes in shown in [project-final](./project-final/).

## 1. Initializing Dev Containers with a template

0. If you have not done it already, fork the [workshop repository](https://github.com/oleg-nenashev/cde-for-embedded-workshop) on GitHub
   and clone it to your machine.
1. Create a new project directory and open it as a project in VS Code.
2. Create a new Python project, add a minimum Dev Container using the [Python template](https://github.com/devcontainers/templates/blob/main/src/python/devcontainer-template.json).
   For that, click the _Dev Container_ icon, choose "New Dev Container..." and select Python 3
3. Open the project in the Dev Container.
   Observe how the environment is built and exposed to the editor.
6. Run the sample `hello.py` application.
7. Follow the slides for a deeper dive into the Dev Container features. We will try them one by one

## 2. Dev Containers Features

[Dev Container Features](https://containers.dev/features) is an established way of adding add-ons to the Dev Containers, without modifying the base images. 
In many cases, it helps to avoid custom configurations and custom images if you need a simple modification of the image.

Specifically for Python tools, where most of tools are available through PIP, it has marginal value.
However, you can still use it to install external tools.
For example, for Debian based images you can use [apt packages](https://github.com/devcontainers-extra/features/tree/main/src/apt-packages).
There are also [Nix](../12-nix-in-devcontainers/) integrations.

1. Review [Dev Container Features](https://containers.dev/features) and explore the features available for Python projects.

2. Add the [apt packages](https://github.com/devcontainers-extra/features/tree/main/src/apt-packages) feature to your Dev Containers definition.

```json
"features": {
    "ghcr.io/devcontainers-extra/features/apt-packages:1": {}
}
```

3. Review the package management and security/performance optimization  options offered by the package.

4. Add the `curl` package to the image

```json
"features": {
    "ghcr.io/devcontainers-extra/features/apt-packages:1": {
        "packages": "curl"
    }
}
```

5. Rebuild the Dev Container and see how `curl` is installed from apt-get. 
   Once the Dev Container restarts, try using curl in the CLI. 

### 3. IDE Plugins

You can install and configure IDE plugins directly from your Dev Containers configuration,
hence making the installation portable.

To test it out, configure the Python environment by adding the following block to your configuration:

```json
	"customizations": {
		"vscode": {
			"extensions": [
                "ms-python.python",
            ],
			"settings": {
				"python.defaultInterpreterPath": "/usr/local/bin/python3",
            }
        }
    }
```

After the setting, rebuild the Dev Container and confirm that you actually get syntax highlighting and other features
of the stock Python plugin for VS Code.

### 4. Post-initialization

1. Add `requirements.txt` to the Dev Container directory

```
pytest==8.3.3
```

2. Add the installation hook to `devcontainer.json`

```json
"postCreateCommand": "pip install -r .devcontainer/requirements.txt"
```

3. Rebuild the Dev Container and ensure the file was picked up

```shell
pytest
```

## Expected outcome

You should be able to explain the purpose of a Dev Containers and 
get hands-on experience with its core features.

## Tips - Dev Containers Tools

Here, we will use [Dev Containers CLI](https://github.com/devcontainers/cli) to 
build the image from the previous step.
This is the tool you can use


## When completed

Return to the [main workshop README](../README.md).
