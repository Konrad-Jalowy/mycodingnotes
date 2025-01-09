class EventEmitter:
    def __init__(self):
        self._events = {}

    # Subskrybowanie eventu
    def on(self, event_name, listener):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(listener)

    # Usunięcie subskrybenta
    def off(self, event_name, listener):
        if event_name in self._events:
            self._events[event_name] = [
                l for l in self._events[event_name] if l != listener
            ]

    # Emitowanie eventu
    def emit(self, event_name, data=None):
        if event_name in self._events:
            for listener in self._events[event_name]:
                listener(data)


# Przykład użycia
emitter = EventEmitter()

# Subskrybenci
def on_user_login(user):
    print(f"Zalogowano użytkownika: {user['name']}")

def on_user_logout(_):
    print("Użytkownik się wylogował")

# Subskrypcje
emitter.on("login", on_user_login)
emitter.on("logout", on_user_logout)

# Emitowanie eventów
emitter.emit("login", {"name": "Jan Kowalski"})  # Zalogowano użytkownika: Jan Kowalski
emitter.emit("logout")  # Użytkownik się wylogował

# Usunięcie subskrybenta
emitter.off("login", on_user_login)

# Kolejne emitowanie eventu (już bez subskrybenta login)
emitter.emit("login", {"name": "Anna Nowak"})  # Brak reakcji