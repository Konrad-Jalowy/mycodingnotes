from functools import total_ordering

@total_ordering  # Automatycznie generuje brakujące metody porównawcze
class Money:
    def __init__(self, amount: float, currency: str):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if not currency or len(currency) != 3:
            raise ValueError("Currency must be a valid 3-letter code.")
        self._amount = round(amount, 2)
        self._currency = currency

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    # Dodawanie
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add money with different currencies.")
        return Money(self.amount + other.amount, self.currency)

    # Odejmowanie
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot subtract money with different currencies.")
        return Money(self.amount - other.amount, self.currency)

    # Mnożenie (np. rabaty, zyski)
    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Money(self.amount * factor, self.currency)

    def __rmul__(self, factor):
        return self.__mul__(factor)

    # Porównanie
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot compare money with different currencies.")
        return self.amount < other.amount

    # Reprezentacja tekstowa
    def __repr__(self):
        return f"Money(amount={self.amount:.2f}, currency='{self.currency}')"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    # Hashowanie (np. użycie w zbiorach lub kluczach słownika)
    def __hash__(self):
        return hash((self.amount, self.currency))

    # Konwersja na słownik
    def to_dict(self):
        return {"amount": self.amount, "currency": self.currency}

    # Statyczna metoda do tworzenia z JSON/dict
    @staticmethod
    def from_dict(data):
        return Money(data["amount"], data["currency"])
# Tworzenie obiektów
money1 = Money(100.00, "USD")
money2 = Money(50.25, "USD")
money3 = Money(100.00, "EUR")

# Operacje matematyczne
print(money1 + money2)  # Output: 150.25 USD
print(money1 - money2)  # Output: 49.75 USD
print(money1 * 2)       # Output: 200.00 USD
print(3 * money2)       # Output: 150.75 USD

# Porównania
print(money1 == money3)        # Output: False
print(money1 > money2)         # Output: True

# Hashowanie (np. użycie w zbiorze)
unique_moneys = {money1, money2, money3}
print(unique_moneys)

# Serializacja i deserializacja
money_dict = money1.to_dict()
print(money_dict)  # Output: {'amount': 100.0, 'currency': 'USD'}
money_from_dict = Money.from_dict(money_dict)
print(money_from_dict)  # Output: Money(amount=100.00, currency='USD')
