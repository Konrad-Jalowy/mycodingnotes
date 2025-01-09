class PositiveNumber:
    def __get__(self, instance, owner):
        if instance is None:
            return f"Deskryptor należy do klasy {owner.__name__}"
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive!")
        instance._value = value


class BankAccount:
    balance = PositiveNumber()


# Na poziomie instancji
account = BankAccount()
account.balance = 100  # Przypisanie wywołuje __set__
print(account.balance)  # Odczyt wywołuje __get__

# Na poziomie klasy
print(BankAccount.balance)  # Wywołuje __get__, gdzie instance=None