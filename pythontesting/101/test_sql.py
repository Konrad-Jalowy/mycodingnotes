# test_sqlalchemy.py

import pytest
from models import User, SessionLocal

@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()

def test_create_user(db_session):
    user = User(name="Jan Kowalski")
    db_session.add(user)
    db_session.commit()

    user_from_db = db_session.query(User).filter_by(name="Jan Kowalski").first()
    assert user_from_db is not None
    assert user_from_db.name == "Jan Kowalski"
