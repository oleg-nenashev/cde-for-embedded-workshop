# Using Nix in Devcontainers

Yes, you can use [Nix](https://nix.dev/index.html) in Dev Containers, too!
It can work as a both environment and package manager.

## Nix feature

1. Add the Nix package manager to your project, by adding a new feature to the template 

```json
"features": {
    "ghcr.io/devcontainers/features/nix:1": {}
}
```

2. Now, configure the package by adding a version and a package from Nix to install

```json
"features": {
    "ghcr.io/devcontainers/features/nix:1": {
        "version": "latest",
        "packages": "fastapi-cli"
    }
}
```

3. Rebuild the Dev container and then `nix version` to check whether the installation passed.

4. Run some demo packages, e.g. `nix-shell --packages cowsay lolcat` and then `cowsay Hello, Nix!`
