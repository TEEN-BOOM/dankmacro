"""Top-level script to invoke dankmacro implementation."""

import asyncio
import sys

import dankmacro.main

if __name__ == '__main__':
    sys.exit(asyncio.run(dankmacro.main.main()))

