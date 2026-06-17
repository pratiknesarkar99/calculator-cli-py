import math
from typing import Union

Number = Union[int, float]


def add(numbers: list[Number]) -> Number:
    return sum(numbers)


def subtract(numbers: list[Number]) -> Number:
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result


def multiply(numbers: list[Number]) -> Number:
    result = numbers[0]
    for n in numbers[1:]:
        result *= n
    return result


def divide(numbers: list[Number]) -> Number:
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            raise ValueError("Division by zero is not allowed.")
        result /= n
    return result


def power(base: Number, exponent: Number) -> Number:
    return base ** exponent


def square_root(n: Number) -> float:
    if n < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(n)


def filter_even(numbers: list[Number]) -> list[Number]:
    return [n for n in numbers if int(n) % 2 == 0]


def filter_odd(numbers: list[Number]) -> list[Number]:
    return [n for n in numbers if int(n) % 2 != 0]