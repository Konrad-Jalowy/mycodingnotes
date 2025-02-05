# test_exceptions.py

import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    with pytest.raises(ValueError):
        divide(5, 0)  # To powinno rzucić wyjątek
