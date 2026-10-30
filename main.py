# main.py — the only file that knows about both servers.
# It imports each module to trigger their decorator registrations,
# then mounts the MCP server inside FastAPI at /mcp.
#
# Request routing after mount:
#   /health, /items, ...  →  FastAPI handles it
#   /mcp/sse, /mcp/...    →  MCP server handles it (SSE transport)

import uvicorn

from api.app import app
import api.routes           # registers @app.get / @app.post decorators

from mcp_server.server import mcp
import mcp_server.tools     # registers @mcp.tool decorators
import mcp_server.resources # registers @mcp.resource decorators
import mcp_server.prompts   # registers @mcp.prompt decorators

# The one line that connects them.
# FastAPI and FastMCP are both Starlette ASGI apps, so one can mount the other.
app.mount("/mcp", mcp.sse_app())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
