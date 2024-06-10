#!/usr/bin/env python3
"""
    Define a function
"""
import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a  random delay"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
