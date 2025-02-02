from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Inicjalizacja ORM
DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Model użytkownika
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        """Zwraca reprezentację do debugowania."""
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', age={self.age})>"

    def __str__(self):
        """Zwraca czytelny string użytkownika (do printowania)."""
        return f"ID: {self.id} | {self.first_name} {self.last_name} | Email: {self.email} | Wiek: {self.age}"

# Tworzenie tabeli (jeśli nie istnieje)
Base.metadata.create_all(engine)

