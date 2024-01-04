#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay"""
    wait_time: float = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time

asyncio.run(wait_random())
