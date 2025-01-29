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
                parts = line.strip().split(",")
                if len(parts) == 3:
                    id, _, _ = parts
                    self.index[id] = pos  # Zapisujemy indeks

    def execute(self, query):
        """Obsługuje proste komendy"""
        tokens = query.split()

        if tokens[0].upper() == "INSERT":
            if len(tokens) < 5 or tokens[1].upper() != "INTO":
                raise ValueError("Niepoprawne zapytanie INSERT. Użyj: INSERT INTO users ID NAME AGE")

            table_name = tokens[2]  # Ignorujemy tabelę, na razie mamy tylko jedną
            id = tokens[3]
            name = tokens[4].strip("'")  # Usuwamy apostrofy
            age = tokens[5]

            if not id.isdigit() or not age.isdigit():
                raise ValueError("ID i AGE muszą być liczbami całkowitymi")

            self.insert(int(id), name, int(age))

        elif tokens[0].upper() == "SELECT":
            if "WHERE" in tokens:
                search_id = tokens[-1]
                return self.select_by_id(int(search_id))
            else:
                return self.select_all()

    def insert(self, id, name, age):
        """Dodaje rekord i aktualizuje indeks"""
        with open(self.filename, "a") as f:
            pos = f.tell()
            f.write(f"{id},{name},{age}\n")
        self.index[str(id)] = pos

    def select_all(self):
        """Odczytuje wszystkie rekordy"""
        with open(self.filename, "r") as f:
            return [line.strip().split(",") for line in f.readlines()]

    def select_by_id(self, search_id):
        """Szybsze wyszukiwanie dzięki indeksowi"""
        if str(search_id) not in self.index:
            return None
        with open(self.filename, "r") as f:
            f.seek(self.index[str(search_id)])
            return f.readline().strip().split(",")

# Testujemy nowy system
db = MyDatabase("data.db")

# Dodajemy dane w stylu SQL
db.execute("INSERT INTO users 4 'David' 50")
db.execute("INSERT INTO users 5 'Eve' 22")

# Pobieramy wszystko
print(db.execute("SELECT * FROM users"))
# [['1', 'Alice', '25'], ['2', 'Bob', '30'], ['3', 'Charlie', '40'], ['4', 'David', '50'], ['5', 'Eve', '22']]

# Pobieramy po ID
print(db.execute("SELECT * FROM users WHERE id 4"))  # ['4', 'David', '50']
