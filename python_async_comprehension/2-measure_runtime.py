#!/usr/bin/env python3
"""a measure_runtime coroutine that will execute async_comprehension"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times using asyncio.gather"""
    start = time.time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end = time.time() - start
    return end
