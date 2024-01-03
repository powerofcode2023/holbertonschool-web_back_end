#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def mult(n: float) -> float:
        return n * multiplier
    return mult
