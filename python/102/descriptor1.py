class PositiveNumber:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Wartość musi być liczbą dodatnią!")
        instance._value = value

    def __delete__(self, instance):
        del instance._value


class BankAccount:
    balance = PositiveNumber()  # Deskryptor dla 'balance'

    def __init__(self, balance):
        self.balance = balance  # Przypisanie wykorzystuje __set__


account = BankAccount(100)  # Poprawne przypisanie
print(account.balance)  # Wywołuje __get__

account.balance = 200  # Aktualizacja wartości
print(account.balance)

try:
    account.balance = -50  # Błąd: wartość ujemna
except ValueError as e:
    print(e)