from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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

    # Relacja 1:N → jeden użytkownik może mieć wiele zadań
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __str__(self):
        return f"ID: {self.id} | {self.first_name} {self.last_name} | Email: {self.email} | Wiek: {self.age}"

# Model zadania
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="pending")  # "pending", "in progress", "completed"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relacja N:1 → każde zadanie jest przypisane do jednego użytkownika
    user = relationship("User", back_populates="tasks")

    def __str__(self):
        return f"ID: {self.id} | {self.title} | Status: {self.status} | Użytkownik: {self.user.first_name} {self.user.last_name}"

# Tworzenie tabeli (jeśli nie istnieje)
Base.metadata.create_all(engine)
