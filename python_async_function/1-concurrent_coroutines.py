#!/usr/bin/env python3
"""an async routine called wait_n that takes in 2 int arguments """

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    values_lsit: List[float] = []
    for x in range(n):
        values_lsit.append(await (wait_random(max_delay)))
    return sorted(values_lsit)
