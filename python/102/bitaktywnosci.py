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
                if not self.is_index_valid():
                    self.build_index()
            except (json.JSONDecodeError, KeyError):
                self.build_index()
        else:
            self.build_index()

    def is_index_valid(self):
        """Sprawdza, czy indeks pokrywa się z plikiem `store.db`"""
        with open(self.filename, "r") as f:
            f.seek(0, os.SEEK_END)
            file_size = f.tell()
            return all(0 <= pos < file_size for pos in self.index.values())

    def build_index(self):
        """Tworzy indeks na podstawie `store.db`"""
        self.index = {}
        with open(self.filename, "r") as f:
            while True:
                pos = f.tell()
                line = f.readline()
                if not line:
                    break
                if ":" in line:
                    active, key, _ = line.strip().split(":", 2)
                    if active == "0":  # Tylko aktywne wpisy
                        self.index[key] = pos
        self.save_index()

    def save_index(self):
        """Zapisuje indeks do pliku"""
        with open(self.index_filename, "w") as f:
            json.dump(self.index, f)

    def set(self, key, value):
        """Zamiast nadpisywać, dopisujemy nową wersję wpisu i oznaczamy starą jako nieaktywną"""
        if key in self.index:
            with open(self.filename, "r+") as f:
                f.seek(self.index[key])
                f.write("1")  # Oznaczamy stary wpis jako usunięty

        with open(self.filename, "a") as f:
            pos = f.tell()
            f.write(f"0:{key}:{value}\n")

        self.index[key] = pos
        self.save_index()

    def get(self, key):
        """Odczytuje wartość z pliku, ale ignoruje usunięte wpisy"""
        if key not in self.index:
            return None
        with open(self.filename, "r") as f:
            f.seek(self.index[key])
            flag, stored_key, stored_value = f.readline().strip().split(":", 2)
            return stored_value if flag == "0" else None  # Tylko aktywne wpisy

    def delete(self, key):
        """Oznacza wpis jako usunięty zamiast go usuwać"""
        if key in self.index:
            with open(self.filename, "r+") as f:
                f.seek(self.index[key])
                f.write("1")  # Zmieniamy flagę aktywności na "1"
            del self.index[key]
            self.save_index()

    def compact(self):
        """Usuwa nieaktywne wpisy i odbudowuje plik"""
        new_lines = []
        new_index = {}
        with open(self.filename, "r") as f:
            pos = 0
            for line in f:
                parts = line.strip().split(":", 2)
                if parts[0] == "0":  # Tylko aktywne wpisy
                    new_lines.append(line)
                    new_index[parts[1]] = pos
                    pos += len(line)
        with open(self.filename, "w") as f:
            f.writelines(new_lines)
        self.index = new_index
        self.save_index()

# Testowanie systemu
db = KeyValueStore("store.db")

db.set("username", "Alice")
db.set("email", "alice@example.com")
print(db.get("username"))  # Alice
print(db.get("email"))     # alice@example.com

db.delete("username")
print(db.get("username"))  # None (bo usunięty)

db.compact()
print(db.get("email"))  # alice@example.com (plik oczyszczony)