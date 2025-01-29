import os

class MyDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.index = {}
        if not os.path.exists(filename):
            open(filename, 'w').close()
        self.build_index()

    def build_index(self):
        """Tworzy indeks na podstawie pliku"""
        self.index = {}
        with open(self.filename, "r") as f:
            while True:
                pos = f.tell()  # Zapamiętujemy pozycję przed odczytem linii
                line = f.readline()  # Odczytujemy linię
                if not line:
                    break  # Koniec pliku
                id, _, _ = line.strip().split(",")
                self.index[id] = pos  # Zapisujemy indeks

    def insert(self, id, name, age):
        """Dodaje rekord i aktualizuje indeks"""
        with open(self.filename, "a") as f:
            pos = f.tell()
            f.write(f"{id},{name},{age}\n")
        self.index[str(id)] = pos  # Aktualizujemy indeks

    def select_by_id(self, search_id):
        """Szybsze wyszukiwanie dzięki indeksowi"""
        if str(search_id) not in self.index:
            return None
        with open(self.filename, "r") as f:
            f.seek(self.index[str(search_id)])  # Skaczemy bezpośrednio do rekordu
            return f.readline().strip().split(",")

# Testujemy
db = MyDatabase("data.db")
db.insert(3, "Charlie", 40)
print(db.select_by_id(3))  # ('3', 'Charlie', '40')
