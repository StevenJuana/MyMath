from math import prod


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
