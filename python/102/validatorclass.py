from typing import Callable, List

# Klasa reguł walidacji
class Validator:
    def __init__(self):
        self.rules: List[Callable[[str], bool]] = []

    def add_rule(self, rule: Callable[[str], bool]) -> None:
        self.rules.append(rule)

    def validate(self, data: str) -> bool:
        return all(rule(data) for rule in self.rules)

# Reguły walidacji
def not_empty(data: str) -> bool:
    return bool(data.strip())

def min_length(min_len: int) -> Callable[[str], bool]:
    return lambda data: len(data) >= min_len

def max_length(max_len: int) -> Callable[[str], bool]:
    return lambda data: len(data) <= max_len

def contains_digit(data: str) -> bool:
    return any(char.isdigit() for char in data)

# Tworzenie walidatora
validator = Validator()
validator.add_rule(not_empty)
validator.add_rule(min_length(5))
validator.add_rule(max_length(10))
validator.add_rule(contains_digit)

# Testy
print(validator.validate("12345"))  # True
print(validator.validate("12"))     # False (za krótkie)
print(validator.validate("12345678901"))  # False (za długie)
print(validator.validate("abcde"))  # False (brak cyfry)