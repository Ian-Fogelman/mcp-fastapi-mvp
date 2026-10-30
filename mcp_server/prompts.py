# MCP concept: Prompts.
# A prompt is a reusable template the AI (or a UI) can call to get a pre-built message.
# Useful for standardising how the AI is asked to reason about something.
# Unlike tools, prompts return a message string, not an action result.

from mcp_server.server import mcp
from shared.data import items_db


@mcp.prompt()
def reorder_prompt(item: str) -> str:
    """Should we reorder this item?"""
    count = items_db.get(item.lower(), 0)
    return f"Item '{item}' has {count} units. Should we reorder? Under 5 is low stock."
