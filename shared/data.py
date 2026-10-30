# The single source of truth.
# Both REST (api/) and MCP (mcp_server/) import this directly.
# A write from either side is immediately visible on the other.

items_db: dict[str, int] = {
    "apple": 5,
    "banana": 3,
    "cherry": 12,
}
