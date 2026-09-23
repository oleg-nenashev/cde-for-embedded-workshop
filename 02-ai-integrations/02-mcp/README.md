# MCP Demo: Context7 in a Dev Container

This is a minimal project showing how to use a **Model Context Protocol (MCP)**
server inside a Dev Container. It connects GitHub Copilot Chat to
[Context7](https://context7.com/), which fetches up-to-date, version-specific
documentation (in this demo, for the Python standard library) directly into
your chat context.

## What's in here

- `.devcontainer/devcontainer.json` - a plain Python 3.12 Dev Container.
- `.vscode/mcp.json` - registers the Context7 MCP server (remote, hosted at
  `https://mcp.context7.com/mcp`, no local install required).
- `task.py` - a small starter file for the demo task.

## Steps

1. Open this `project` folder in a Dev Container (reopen in container).
2. Open the Command Palette and run **MCP: List Servers** to confirm
   `context7` is discovered. Start it if it isn't already running.
   You may be prompted to sign in / allow the server - accept it.
3. Open Copilot Chat in **Agent mode** and confirm the Context7 tools
   (`resolve-library-id`, `query-docs`) are available (check the tools picker).
4. Open [task.py](./task.py) and ask Copilot Chat something like:

   ```
   Implement main() using argparse with a --name option that defaults to
   "World" and prints a greeting. use context7
   ```

5. Watch Copilot call the Context7 tools to pull current `argparse`
   documentation before generating the code.
6. Run the result:

   ```bash
   python task.py --name Ada
   ```

## Expected outcome

You should see Copilot Chat invoke the Context7 MCP tools (visible in the tool
call output) before answering, and produce code based on fetched
documentation rather than solely on its training data.

## Notes

- Context7 also works without an API key for light/demo use; add one via the
  `Authorization: Bearer <key>` header in `.vscode/mcp.json` for higher rate
  limits (see [context7.com/dashboard](https://context7.com/dashboard)).
- Because the server is remote (`type: http`), no extra packages need to be
  installed in the Dev Container image for this demo.
