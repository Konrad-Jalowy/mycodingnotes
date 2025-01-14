class UserRepository:
    def __init__(self):
        self._users = {}  # Wirtualna baza danych (słownik)

    def find_by_id(self, user_id: int):
        return self._users.get(user_id)

    def save(self, user):
        self._users[user.id] = user

    def delete(self, user_id: int):
        if user_id in self._users:
            del self._users[user_id]

# Przykład użycia
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"{self.id} {self.name}"

repo = UserRepository()
user = User(1, "Alice")
repo.save(user)

print(repo.find_by_id(1))  # Output: 1 Alice
repo.delete(1)
