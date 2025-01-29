import os

class KeyValueStore:
    def __init__(self, filename="store.db"):
        self.filename = filename
        self.index = {}
        if not os.path.exists(filename):
            open(filename, 'w').close()
        self.build_index()

    def build_index(self):
        """Tworzy indeks w pamięci"""
        self.index = {}
        with open(self.filename, "r") as f:
            while True:
                pos = f.tell()  # Zapamiętujemy pozycję przed odczytem
                line = f.readline()  # Odczytujemy linię
                if not line:
                    break  # Koniec pliku
                key, _ = line.strip().split(":", 1)
                self.index[key] = pos  # Zapisujemy pozycję klucza w pliku

    def set(self, key, value):
        """Dodaje nową wartość i aktualizuje indeks"""
        with open(self.filename, "a") as f:
            pos = f.tell()
            f.write(f"{key}:{value}\n")
        self.index[key] = pos  # Aktualizujemy indeks

    def get(self, key):
        """Odczytuje wartość z pliku, ale korzysta z indeksu"""
        if key not in self.index:
            return None
        with open(self.filename, "r") as f:
            f.seek(self.index[key])  # Skaczemy do właściwej pozycji
            stored_key, stored_value = f.readline().strip().split(":", 1)
            return stored_value

    def delete(self, key):
        """Usuwa klucz z pliku i aktualizuje indeks"""
        if key not in self.index:
            return False
        lines = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            for line in lines:
                if not line.startswith(f"{key}:"):
                    f.write(line)

        del self.index[key]  # Usuwamy klucz z indeksu
        return True

# Testujemy
db = KeyValueStore()

db.set("username", "Alice")
db.set("email", "alice@example.com")

print(db.get("username"))  # Alice
print(db.get("email"))     # alice@example.com

db.delete("username")
print(db.get("username"))  # None
