# test_parametrize.py

import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("num, expected", [(2, True), (3, False), (10, True), (7, False)])
def test_is_even(num, expected):
    assert is_even(num) == expected
