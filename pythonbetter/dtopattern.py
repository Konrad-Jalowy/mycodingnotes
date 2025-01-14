class UserDTO:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

# Użycie
user_dto = UserDTO(1, "John Doe", "john@example.com")
print(user_dto.__dict__)
# Output: {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}