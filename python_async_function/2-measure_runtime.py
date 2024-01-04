#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay"""

from typing import List
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    before: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total: float = time.time() - before
    return total / n
