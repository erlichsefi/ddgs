#!/usr/bin/env python3
"""Start the DDGS API server."""

import logging
import os
import sys

import uvicorn

logger = logging.getLogger(__name__)

# Add current directory to Python path
sys.path.insert(0, ".")

if __name__ == "__main__":
    # Get number of workers from environment variable, default to 4 for better concurrency
    workers = int(os.environ.get("DDGS_WORKERS", "1"))

    logger.info("🚀 Starting DDGS API server on http://0.0.0.0:8000 with %d workers", workers)
    # Use import string format to support multiple workers
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, workers=workers)  # noqa: S104
