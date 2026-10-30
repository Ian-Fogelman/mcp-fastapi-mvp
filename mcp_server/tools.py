# MCP concept: Tools.
# A tool is a Python function the AI can CALL to take an action or get data.
# The AI sees the name, docstring, and parameter types — write them clearly.
# Compare to api/routes.py: same idea, different caller (AI vs HTTP client).

from mcp_server.server import mcp
from shared.data import items_db


@mcp.tool()
def get_stock(item: str) -> str:
    """Check how many of an item are in stock"""
    count = items_db.get(item.lower())
    return f"{count} in stock" if count is not None else "Item not found"


@mcp.tool()
def update_stock(item: str, count: int) -> str:
    """Set the stock count for an item"""
    items_db[item.lower()] = count
    return f"Updated {item} to {count} units"
