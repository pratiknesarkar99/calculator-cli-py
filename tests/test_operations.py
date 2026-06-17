import pytest
from calculator.operations import (
    add, subtract, multiply, divide,
    power, square_root, filter_even, filter_odd
)


# --- add ---
def test_add_integers():
    assert add([1, 2, 3]) == 6

def test_add_floats():
    assert add([1.5, 2.5]) == pytest.approx(4.0)

def test_add_single():
    assert add([5]) == 5


# --- subtract ---
def test_subtract_basic():
    assert subtract([10, 3, 2]) == 5

def test_subtract_single():
    assert subtract([7]) == 7


# --- multiply ---
def test_multiply_basic():
    assert multiply([2, 3, 4]) == 24

def test_multiply_by_zero():
    assert multiply([5, 0]) == 0


# --- divide ---
def test_divide_basic():
    assert divide([20, 4]) == pytest.approx(5.0)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        divide([10, 0])


# --- power ---
def test_power_basic():
    assert power(2, 10) == 1024

def test_power_zero_exponent():
    assert power(5, 0) == 1


# --- square_root ---
def test_sqrt_basic():
    assert square_root(9) == pytest.approx(3.0)

def test_sqrt_negative():
    with pytest.raises(ValueError, match="negative"):
        square_root(-1)


# --- filter_even ---

def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]

def test_filter_even_whole_float():
    assert filter_even([1.0, 2.0, 3.0]) == [2.0]

def test_filter_even_rejects_non_whole_float():
    with pytest.raises(ValueError, match="whole number"):
        filter_even([1.5, 2.5])

# --- filter_odd ---

def test_filter_odd():
    assert filter_odd([1, 2, 3, 4, 5]) == [1, 3, 5]

def test_filter_odd_rejects_non_whole_float():
    with pytest.raises(ValueError, match="whole number"):
        filter_odd([1.5, 3.5])