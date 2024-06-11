#!/usr/bin/env python3
"""
    0-async_generator.py
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously wait and Yield a number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
