import os

class KeyValueStore:
    def __init__(self, filename="store.db"):
        self.filename = filename
        if not os.path.exists(filename):
            open(filename, 'w').close()

    def set(self, key, value):
        """Zapisuje wartość dla danego klucza"""
        with open(self.filename, "a") as f:
            f.write(f"{key}:{value}\n")

    def get(self, key):
        """Odczytuje wartość klucza"""
        with open(self.filename, "r") as f:
            for line in f:
                stored_key, stored_value = line.strip().split(":", 1)
                if stored_key == key:
                    return stored_value
        return None  # Klucz nie istnieje

    def delete(self, key):
        """Usuwa klucz"""
        lines = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            for line in lines:
                if not line.startswith(f"{key}:"):
                    f.write(line)

# Testujemy
db = KeyValueStore()

db.set("username", "Alice")
db.set("email", "alice@example.com")

print(db.get("username"))  # Alice
print(db.get("email"))     # alice@example.com

db.delete("username")
print(db.get("username"))  # None
