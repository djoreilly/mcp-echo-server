from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers
from fastmcp.utilities.logging import get_logger, configure_logging

logger = get_logger(__name__)
configure_logging("DEBUG", logger)

mcp = FastMCP("Echo Server")

@mcp.tool
def echo_tool(text: str) -> str:
    """Echo the input text"""
    logger.debug(get_http_headers())
    return text
