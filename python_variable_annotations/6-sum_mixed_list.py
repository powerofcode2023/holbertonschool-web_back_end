#!/usr/bin/env python3
"""function sum_mixed_list which takes a list mxd_lst of integers and floats"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns sum as a float"""
    return (sum(mxd_list))
