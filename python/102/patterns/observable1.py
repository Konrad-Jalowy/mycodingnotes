class Observable:
    def __init__(self):
        self._subscribers = []

    # Dodanie subskrybenta
    def subscribe(self, observer):
        self._subscribers.append(observer)

    # Usunięcie subskrybenta
    def unsubscribe(self, observer):
        self._subscribers = [sub for sub in self._subscribers if sub != observer]

    # Powiadomienie subskrybentów
    def notify(self, data):
        for observer in self._subscribers:
            observer(data)


# Przykład użycia
observable = Observable()

# Subskrybenci
def observer1(data):
    print(f"Subskrybent 1 otrzymał dane: {data}")

def observer2(data):
    print(f"Subskrybent 2 otrzymał dane: {data}")

# Dodanie subskrybentów
observable.subscribe(observer1)
observable.subscribe(observer2)

# Powiadomienie subskrybentów
observable.notify("Pierwsza wiadomość")

# Usunięcie jednego subskrybenta
observable.unsubscribe(observer1)

# Kolejne powiadomienie
observable.notify("Druga wiadomość")