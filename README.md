# Simple MCP server

container image for testing/debugging
stdio or HTTP Streamable transport

Echo server from [FastMCP example](https://github.com/jlowin/fastmcp/blob/main/examples/echo.py)
Dockerfile from [Astral example](https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile)

### Streamable-HTTP transport
```
$ podman run -it --rm -p 8000:8000 ghcr.io/djoreilly/mcp-echo-server:main --transport http --host 0.0.0.0 --port 8000

```
