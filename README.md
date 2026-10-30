# MCP + FastAPI MVP

Two interfaces to the same data — REST for humans/apps, MCP for AI models.

## Project layout

```
mcp/
├── main.py              # entry point — mounts MCP inside FastAPI
├── shared/
│   └── data.py          # items_db dict — single source of truth
├── api/
│   ├── app.py           # FastAPI instance
│   └── routes.py        # REST endpoints
└── mcp_server/
    ├── server.py        # FastMCP instance
    ├── tools.py         # things the AI can call
    ├── resources.py     # data the AI can read
    └── prompts.py       # reusable prompt templates
```

## Setup

```bash
pip install -r requirements.txt
python main.py
```

Server starts at `http://localhost:8000`.

## REST endpoints

```bash
# list all stock
curl http://localhost:8000/items

# get one item
curl http://localhost:8000/items/apple

# set stock (visible to MCP tools immediately)
curl -X POST http://localhost:8000/items/apple/20

# swagger UI
open http://localhost:8000/docs
```

## MCP endpoints

The MCP server is mounted at `/mcp/sse` using SSE (Server-Sent Events) transport.

**Connect Claude Desktop** — add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "inventory": {
      "url": "http://localhost:8000/mcp/sse"
    }
  }
}
```

Once connected, Claude has access to:

| Type | Name | What it does |
|---|---|---|
| Tool | `get_stock` | Ask "how many apples?" → calls this |
| Tool | `update_stock` | Ask "set apple to 20" → calls this |
| Resource | `inventory://all` | Full snapshot of items_db |
| Prompt | `reorder_prompt` | Pre-built reorder analysis message |

## How it works

`main.py` creates both servers, imports the route/handler modules to trigger their decorator registrations, then mounts the MCP server inside FastAPI:

```python
app.mount("/mcp", mcp.sse_app())
```

FastAPI and FastMCP are both Starlette ASGI apps, so one can host the other at a path prefix. Requests to `/mcp/*` go to MCP; everything else goes to FastAPI. Both read and write the same `items_db` dict in memory.
