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
        """Ładuje indeks z pliku lub buduje nowy, jeśli indeks jest uszkodzony"""
        if os.path.exists(self.index_filename):
            try:
                with open(self.index_filename, "r") as f:
                    self.index = json.load(f)

                # Sprawdzamy, czy indeks jest zgodny z `store.db`
                if not self.is_index_valid():
                    print("⚠️ Indeks niepoprawny! Odbudowuję...")
                    self.build_index()
            except (json.JSONDecodeError, KeyError):
                print("⚠️ Błąd odczytu indeksu! Odbudowuję...")
                self.build_index()
        else:
            self.build_index()

    def is_index_valid(self):
        """Sprawdza, czy indeks pokrywa się z plikiem `store.db`"""
        with open(self.filename, "r") as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()  # Pobieramy wielkość pliku
            return all(0 <= pos < file_size for pos in self.index.values())

    def build_index(self):
        """Tworzy indeks od nowa na podstawie `store.db`"""
        self.index = {}
        with open(self.filename, "r") as f:
            while True:
                pos = f.tell()
                line = f.readline()
                if not line:
                    break
                if ":" in line:
                    key, _ = line.strip().split(":", 1)
                    self.index[key] = pos  # Zapisujemy indeks klucza

        self.save_index()  # Zapisujemy nowy indeks do pliku

    def save_index(self):
        """Zapisuje indeks do pliku"""
        with open(self.index_filename, "w") as f:
            json.dump(self.index, f)

    def set(self, key, value):
        """Dodaje nową wartość lub nadpisuje istniejącą"""
        if key in self.index:
            lines = []
            with open(self.filename, "r") as f:
                lines = f.readlines()

            with open(self.filename, "w") as f:
                for line in lines:
                    if not line.startswith(f"{key}:"):
                        f.write(line)
                pos = f.tell()
                f.write(f"{key}:{value}\n")
                self.index[key] = pos
        else:
            with open(self.filename, "a") as f:
                pos = f.tell()
                f.write(f"{key}:{value}\n")
            self.index[key] = pos

        self.save_index()  # Zapisujemy indeks

    def get(self, key):
        """Odczytuje wartość z pliku na podstawie indeksu"""
        if key not in self.index:
            return None  # Klucz nie istnieje

        with open(self.filename, "r") as f:
            f.seek(self.index[key])  # Skaczemy do właściwej pozycji
            line = f.readline().strip()

            if ":" not in line:  # Jeśli linia jest niepoprawna, zwracamy None
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
        self.save_index()
        return True


# Testujemy
# db = KeyValueStore()

# Pierwsze uruchomienie
# db.set("username", "Alice")
# db.set("email", "alice@example.com")

# Restart programu – teraz nie wykonujemy `set()`, tylko próbujemy `get()`
db = KeyValueStore()
print(db.get("username"))  # Alice
print(db.get("email"))  # alice@example.com