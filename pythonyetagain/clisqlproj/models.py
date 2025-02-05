from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Baza danych SQLite
DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL, echo=False)

# Klasa bazowa dla modeli
Base = declarative_base()

# Tabela pośrednia dla Task <-> Hashtag (Many-to-Many)
task_hashtag = Table(
    "task_hashtag", Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id")),
    Column("hashtag_id", Integer, ForeignKey("hashtags.id"))
)

# Model użytkownika
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relacja 1:1 z Address
    address = relationship("Address", back_populates="user", uselist=False, cascade="all, delete")

    # Relacja 1:N z Task
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

# Model adresu (1:1 z User)
class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relacja odwrotna do User
    user = relationship("User", back_populates="address")

# Model zadania (1:N z User, N:M z Hashtag)
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relacja 1:N do User
    user = relationship("User", back_populates="tasks")

    # Relacja N:M do Hashtag
    hashtags = relationship("Hashtag", secondary=task_hashtag, back_populates="tasks")

# Model hasztagu (N:M z Task)
class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relacja N:M do Task
    tasks = relationship("Task", secondary=task_hashtag, back_populates="hashtags")

# Tworzenie tabel
Base.metadata.create_all(engine)

# Sesja do bazy danych
SessionLocal = sessionmaker(bind=engine)
