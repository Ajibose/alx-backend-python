#!/usr/bin/env python3
"""
    ./1-concurrent_coroutines.py
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = task
        delays.append(delay)

    return delays
