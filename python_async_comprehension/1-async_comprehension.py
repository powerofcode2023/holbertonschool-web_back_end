#!/usr/bin/env python3
"""a coroutine called async_comprehension that takes no arguments"""
from typing import List
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """collect 10 random numbers using an async comprehensing"""
    result = [i async for i in async_generator()]
    return result
