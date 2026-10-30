# MCP concept: the server instance.
# tools.py, resources.py, and prompts.py all import this object
# to register their handlers onto it (same pattern as api/app.py).

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("inventory")
