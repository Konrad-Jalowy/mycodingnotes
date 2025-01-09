from abc import ABC, abstractmethod

# Definicja interfejsu strategii
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Konkretne strategie
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card {self.card_number}.")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal account {self.email}.")

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid {amount} using Crypto wallet {self.wallet_address}.")

# Klasa kontekstowa, która korzysta z różnych strategii
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy strategie
    credit_card = CreditCardPayment("1234-5678-9012-3456")
    paypal = PayPalPayment("user@example.com")
    crypto = CryptoPayment("1A2B3C4D5E6F7G8H9I0J")

    # Kontekst płatności
    payment = PaymentContext(credit_card)
    payment.execute_payment(100)  # Paid 100 using Credit Card 1234-5678-9012-3456.

    # Zmiana strategii
    payment.set_strategy(paypal)
    payment.execute_payment(200)  # Paid 200 using PayPal account user@example.com.

    # Zmiana strategii
    payment.set_strategy(crypto)
    payment.execute_payment(300)  # Paid 300 using Crypto wallet 1A2B3C4D5E6F7G8H9I0J.