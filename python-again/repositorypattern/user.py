class User:
    """Encja użytkownika."""
    def __init__(self, id=None, username=None, email=None):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"
