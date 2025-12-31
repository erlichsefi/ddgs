#!/usr/bin/env python3
"""Start the DDGS API server."""

import logging
import os
import sys

import uvicorn
from fastapi_mcp import FastApiMCP  # type: ignore[import-untyped]

from api.main import app

logger = logging.getLogger(__name__)

# Add current directory to Python path
sys.path.insert(0, ".")

if __name__ == "__main__":
    # Get number of workers from environment variable, default to 4 for better concurrency
    workers = int(os.environ.get("DDGS_WORKERS", "1"))

    mcp = FastApiMCP(app, name="ddgs-search", description="DDGS (Dux Distributed Global Search) MCP Server")
    mcp.mount_http()
    logger.info("✅ MCP server enabled at /mcp")
    mcp.mount_sse()
    logger.info("✅ MCP server enabled at /sse")

    logger.info("🚀 Starting DDGS API server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=workers)  # noqa: S104