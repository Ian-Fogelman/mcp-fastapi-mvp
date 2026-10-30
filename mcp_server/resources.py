# MCP concept: Resources.
# A resource is data the AI can READ, addressed by a URI (like a file or URL).
# The AI fetches it for context, but cannot call it like a tool.
# URI scheme is arbitrary — "inventory://" is just a namespace we invented.

from mcp_server.server import mcp
from shared.data import items_db


@mcp.resource("inventory://all")
def all_items() -> str:
    """Full inventory snapshot — all items and their stock counts"""
    return "\n".join(f"{k}: {v}" for k, v in items_db.items())
