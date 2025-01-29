import os
import json

class KeyValueStore:
    def __init__(self, filename="store.db", index_filename="store.index"):
        self.filename = filename
        self.index_filename = index_filename
        self.index = {}

        if not os.path.exists(filename):
            open(filename, 'w').close()

        self.load_index()

    def load_index(self):
        """Ładuje indeks z pliku lub buduje nowy"""
        if os.path.exists(self.index_filename):
            with open(self.index_filename, "r") as f:
                self.index = json.load(f)
        else:
            self.build_index()

    def build_index(self):
        """Tworzy indeks na podstawie pliku i zapisuje go"""
        self.index = {}
        with open(self.filename, "r") as f:
            while True:
                pos = f.tell()  # Pozycja przed odczytem linii
                line = f.readline()
                if not line:
                    break
                key, _ = line.strip().split(":", 1)
                self.index[key] = pos  # Zapisujemy indeks

        # Zapisujemy indeks do pliku
        with open(self.index_filename, "w") as f:
            json.dump(self.index, f)

    def set(self, key, value):
        """Dodaje nową wartość lub nadpisuje istniejącą"""
        if key in self.index:
            # Odczytujemy wszystkie linie i nadpisujemy istniejącą wartość
            lines = []
            with open(self.filename, "r") as f:
                lines = f.readlines()

            with open(self.filename, "w") as f:
                for line in lines:
                    if not line.startswith(f"{key}:"):  # Zachowujemy inne klucze
                        f.write(line)
                # Dopisujemy nową wartość
                pos = f.tell()
                f.write(f"{key}:{value}\n")
                self.index[key] = pos  # Aktualizujemy indeks
        else:
            # Normalnie dopisujemy na koniec
            with open(self.filename, "a") as f:
                pos = f.tell()
                f.write(f"{key}:{value}\n")
            self.index[key] = pos  # Aktualizujemy indeks

        self.save_index()  # Zapisujemy indeks do pliku

    def get(self, key):
        """Odczytuje wartość z pliku na podstawie indeksu"""
        if key not in self.index:
            return None  # Klucz nie istnieje

        with open(self.filename, "r") as f:
            f.seek(self.index[key])  # Skaczemy do właściwej pozycji
            line = f.readline().strip()

            if ":" not in line:  # Jeśli nie znaleźliśmy dwukropka, coś jest nie tak
                return None

            stored_key, stored_value = line.split(":", 1)
            return stored_value

    def delete(self, key):
        """Usuwa klucz i aktualizuje indeks"""
        if key not in self.index:
            return False
        lines = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            for line in lines:
                if not line.startswith(f"{key}:"):
                    f.write(line)

        del self.index[key]
        self.save_index()  # Zapisujemy nowy indeks
        return True

    def save_index(self):
        """Zapisuje indeks do pliku"""
        with open(self.index_filename, "w") as f:
            json.dump(self.index, f)

# Testujemy
db = KeyValueStore()

db.set("username", "Alice")
db.set("email", "alice@example.com")

print(db.get("username"))  # Alice
print(db.get("email"))     # alice@example.com

db.delete("username")
print(db.get("username"))  # None
