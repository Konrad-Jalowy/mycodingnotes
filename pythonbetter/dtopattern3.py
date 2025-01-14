class UserDTO:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class UserModel:
    def __init__(self, id: int = 0, name: str = "", email: str = ""):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def from_dto(cls, dto: UserDTO):
        return cls(**dto.__dict__)

    def to_dto(self) -> UserDTO:
        return UserDTO(**self.__dict__)

# Przykład użycia
dto = UserDTO(1, "John Doe", "john@example.com")
model = UserModel.from_dto(dto)

print(model.__dict__)  # Model domenowy
print(model.to_dto().__dict__)  # DTO