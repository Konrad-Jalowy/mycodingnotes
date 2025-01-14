class UserDTO:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id', 0),
            name=data.get('name', ''),
            email=data.get('email', '')
        )

    def to_dict(self) -> dict:
        return vars(self)

# Przykład użycia
data = {
    "id": 2,
    "name": "Alice",
    "email": "alice@example.com"
}

user_dto = UserDTO.from_dict(data)
print(user_dto.to_dict())
# {'id': 2, 'name': 'Alice', 'email': 'alice@example.com'}