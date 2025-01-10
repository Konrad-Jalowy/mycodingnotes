from abc import ABC, abstractmethod

# Interfejs dla stanów
class OrderState(ABC):
    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def pick_up(self):
        pass

# Konkretne stany
class PlacedState(OrderState):
    def next_state(self):
        print("Przechodzę do stanu: W trakcie przygotowania.")
        return PreparingState()

    def cancel(self):
        print("Zamówienie zostało anulowane.")
        return None

    def pick_up(self):
        print("Nie można odebrać zamówienia, które jeszcze nie zostało przygotowane.")
        return self

class PreparingState(OrderState):
    def next_state(self):
        print("Przechodzę do stanu: Gotowe do odbioru.")
        return ReadyState()

    def cancel(self):
        print("Zamówienie zostało anulowane podczas przygotowania.")
        return None

    def pick_up(self):
        print("Nie można odebrać zamówienia, które jeszcze nie zostało przygotowane.")
        return self

class ReadyState(OrderState):
    def next_state(self):
        print("Zamówienie zostało odebrane i zakończone.")
        return CompletedState()

    def cancel(self):
        print("Nie można anulować zamówienia, które jest gotowe do odbioru.")
        return self

    def pick_up(self):
        print("Zamówienie odebrane przez klienta.")
        return CompletedState()

class CompletedState(OrderState):
    def next_state(self):
        print("Zamówienie już zakończone. Nie można zmienić stanu.")
        return self

    def cancel(self):
        print("Nie można anulować zakończonego zamówienia.")
        return self

    def pick_up(self):
        print("Zamówienie już zostało odebrane.")
        return self

# Kontekst
class Order:
    def __init__(self):
        self.state = PlacedState()  # Stan początkowy

    def next_state(self):
        if self.state:
            self.state = self.state.next_state()

    def cancel(self):
        if self.state:
            self.state = self.state.cancel()

    def pick_up(self):
        if self.state:
            self.state = self.state.pick_up()

# Testowanie
order = Order()

print("\n1. Złożenie zamówienia:")
order.next_state()  # Przechodzimy do przygotowania

print("\n2. W trakcie przygotowania:")
order.next_state()  # Zamówienie gotowe do odbioru

print("\n3. Odbiór zamówienia:")
order.pick_up()  # Zamówienie zakończone

print("\n4. Próba anulowania zakończonego zamówienia:")
order.cancel()
