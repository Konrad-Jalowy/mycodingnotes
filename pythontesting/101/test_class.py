# test_class.py

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

def test_calculator():
    calc = Calculator()
    assert calc.add(3, 2) == 5
    assert calc.multiply(3, 2) == 6
