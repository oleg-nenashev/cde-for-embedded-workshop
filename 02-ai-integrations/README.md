# 02 - AI Integrations

This section explores how AI tools and assistants can be used inside container-based development environments.

## Goals

- Understand the role of AI in modern development workflows
- See how AI assistants can help with coding, debugging, and documentation
- Learn how to combine local development environments with AI-powered tools

## Suggested activities

1. Review the available AI-related tooling and extensions.
2. Try a simple coding or explanation task with an AI assistant.
3. Observe how the same environment can support both human developers and AI workflows.

## Expected outcome

By the end of this section, you should have a basic understanding of how AI integrations can fit into a devcontainer-based workflow.


## Steps

### Step 1. GitHub Copilot

1. Ensure GitHub Copilot is connected
2. Start a Dev Container from the previous step
3. Just use it and see the results!

### Step 2. MCPs

Model Context Protocol (MCP) servers let Copilot Chat call out to external tools,
for example to fetch up-to-date documentation instead of relying only on its
training data.
Common MCP features like `mcp.json` apply here

1. Go to [02-mcp](./02-mcp/) and open it in a Dev Container.
2. Follow the steps in the [project README](./project/README.md) to enable the
   [Context7](https://context7.com/) MCP server and use it from Copilot Chat
   to look up Python documentation while implementing a small task.


### Step 3. LLMs/SLMs

You can also connect SLMs or external providers directly in the container,
using resources available to the Docker engine.
For the demo, we will use a tiny [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) model.

1. Create a new project. [03-slm](./03-slm/) is provided for a reference

2. Install the [Ollama feature](https://github.com/prulloac/devcontainer-features/tree/main/src/ollama) to the project.

```json
"features": {
    "ghcr.io/prulloac/devcontainer-features/ollama:1": {
      "pull": "Qwen2.5-0.5B"
    }
}
```

2. 

## When completed

Return to the [main workshop README](../README.md).

## Notes

### Other coding agents

GitHub Copilot has a native integration with Dev Containers when using Visual Studio Code.
Your mileage may vary for other local and remote coding agents.
Below, there are some tips for other coding agents you can explore after the workshop.

