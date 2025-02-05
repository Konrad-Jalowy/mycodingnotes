# test_fixtures.py

import pytest

@pytest.fixture
def sample_user():
    return {"name": "Jan", "age": 30}

def test_user_age(sample_user):
    assert sample_user["age"] == 30
