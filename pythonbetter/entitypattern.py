class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def update_email(self, new_email: str):
        if "@" not in new_email:
            raise ValueError("Invalid email address.")
        self.email = new_email

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

# Przykład użycia
user1 = User(1, "Alice", "alice@example.com")
user2 = User(1, "Alice", "alice@example.com")

print(user1 == user2)  # Output: True (te same encje, bo id są takie same)
user1.update_email("new_email@example.com")
print(user1)
