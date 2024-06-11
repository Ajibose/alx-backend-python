#!/usr/bin/env python3
"""
    2-measure_runtime.py
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the parallel runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return (time.perf_counter() - start)
