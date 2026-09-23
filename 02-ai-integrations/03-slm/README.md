# SLM in a Dev Container

In this demo, we will show how to use an SLM in a Dev Container,
using the [Ollama](https://ollama.com/) feature.

## Steps

### 1. Using built-in executable

1. Run the dev container
2. Run `ollama list` to list the preinstalled models
3. Run `ollama run qwen2.5:0.5b` to get the sample running. **IT WILL BE VERY SLOW**
4. Try out a few queries, e.g. :Generate a sample dev container configuration for Python development"

### 2. External provider (OPTIONAL)

Here, we will connect the Ollama from the host instance.
To do that, you will need to install Ollama locally on the host machine and prepare the image..

1. Run `ollama pull qwen2.5:0.5b`
2. Configure Ollama on your host machine to expose service on `0.0.0.0` (e.g. via `OLLAMA_HOST=0.0.0.0 ollama serve`)
3. Add the `OLLAMA_HOST=http://host.docker.internal:11434` environment veriable to the Dev Container (commented in the repo)
4. Rebuild the container and try the steps again

## Disclaimer

Running Ollama on Docker for Mac is possible, but not recommended because Docker on macOS cannot access Apple Silicon GPU acceleration (Metal), 
forcing models to run slowly on CPU only.
For any production use, connect to external Ollama instance (as in Step 2) or instrument Docker to support GPUs.

For GPU binding, see [Mandoa-Labs/Ollama-Devcontainer](https://github.com/Mandoa-Labs/Ollama-Devcontainer) for an example.
