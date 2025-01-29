import os

class MyDatabase:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            open(filename, 'w').close()  # Tworzymy plik, jeśli nie istnieje

    def insert(self, id, name, age):
        """Dodaje rekord do pliku"""
        with open(self.filename, "a") as f:
            f.write(f"{id},{name},{age}\n")

    def select_all(self):
        """Odczytuje wszystkie rekordy"""
        with open(self.filename, "r") as f:
            return [line.strip().split(",") for line in f.readlines()]

    def select_by_id(self, search_id):
        """Odczytuje rekord o konkretnym ID"""
        with open(self.filename, "r") as f:
            for line in f:
                id, name, age = line.strip().split(",")
                if id == str(search_id):
                    return (id, name, age)
        return None

# Test działania
db = MyDatabase("data.db")

# Dodajemy dane
db.insert(1, "Alice", 25)
db.insert(2, "Bob", 30)

# Pobieramy wszystkie wpisy
print(db.select_all())  # [['1', 'Alice', '25'], ['2', 'Bob', '30']]

# Pobieramy wpis po ID
print(db.select_by_id(1))  # ('1', 'Alice', '25')
