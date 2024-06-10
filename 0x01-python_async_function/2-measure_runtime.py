#!/usr/bin/env python3
"""
    2-measure_runtime.py
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time for wait_n to execute"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    exec_time = time.perf_counter() - start
    return exec_time / n
