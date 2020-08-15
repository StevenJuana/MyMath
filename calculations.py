# calculations.py

# This file contains functions that calculate answers for various
# problems across our project

from math import prod, sqrt
from itertools import count, islice


def subtract_list(lst: list) -> int:
    """Returns the result of subtracting all of the values in
    the given list"""
    return lst[0] - sum(lst[1:])


def add_sub_mult_calc(values: list, problem_type: str) -> int:
    """Returns the answer for an addition, subtraction or multiplication problem"""
    if problem_type == "Addition":
        return sum(values)
    elif problem_type == "Subtraction":
        return subtract_list(values)
    else:
        return prod(values)


def is_prime(n):
    """Returns if a number is a prime number or not"""
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))