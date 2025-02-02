from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Inicjalizacja ORM
DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL, echo=False)  # Wyłączamy wypisywanie SQL
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

# Tworzenie tabeli (jeśli nie istnieje)
Base.metadata.create_all(engine)