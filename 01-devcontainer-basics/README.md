# 01 - Devcontainer Basics

This section introduces the core concepts behind Dev Containers and how they simplify onboarding for software projects.

## Goals

- Understand what a devcontainer is and why it is useful
- Learn how a container-based development environment is defined
- Explore the relationship between VS Code, Docker, and devcontainer configuration
- Understand basic concepts of Dev Containers, e.g. features and templates

## Steps

### 1. Theory

1. Take a look at the _01 - Dev Containers 101_ part of the presentation,
   independently or together with the instructor

### 2. Your first Dev Containers project with a template

1. Create a new project directory and open it as a project in VS Code.
2. Create a new Python project, add a minimum Dev Container using the [Python template](https://github.com/devcontainers/templates/blob/main/src/python/devcontainer-template.json).
   For that, click the "Dev COntainer" icon, choose "New Dev Container..." and select Python 3
3. Open the project in the Dev Container.
   Observe how the environment is built and exposed to the editor.
6. Run the sample `hello.py` application.
7. Follow the slides for a deeper dive into the Dev Container features. We will try them one by one

### 3. Dev Containers Features

[Dev Container Features](https://containers.dev/features) is an established way of adding add-ons to the Dev Containers, without modifying the base images. 
In many cases, it helps to avoid custom configurations.

Specifically for Python tools, where most of tools are available through PIP, it has marginal value.
However, you can still use it to install external tools.

1. Review [Dev Container Features](https://containers.dev/features) and explore the features available for Python projects

2. Add the Nix package manager to your project, by adding a new feature to the template 

```json
"features": {
    "ghcr.io/devcontainers/features/nix:1": {}
}
```

3. Now, configure the package by adding a version and a package from Nix to install

```json
"features": {
    "ghcr.io/devcontainers/features/nix:1": {
        "version": "latest",
        "packages": "fastapi-cli"
    }
}
```

4. Rebuild the Dev container and then `nix version` to check whether the installation passed.

5. Run some demo packages, e.g. `nix-shell --packages cowsay lolcat` and then `cowsay Hello, Nix!`

### 4. IDE Plugins

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

### 5. Post-initialization

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

You should be able to explain the purpose of a devcontainer and use one to start a consistent development environment.

## When completed

Return to the [main workshop README](../README.md).
