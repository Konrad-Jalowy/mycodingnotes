from models.user import User
from database.db_connector import db

class UserRepository:
    """Repozytorium dla operacji na użytkownikach"""

    @staticmethod
    def add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users(username=None, email=None, page=1, limit=10):
        """Pobiera użytkowników z opcjonalnym filtrowaniem i paginacją"""
        query = User.query

        if username:
            query = query.filter(User.username.ilike(f"%{username}%"))  # Wyszukiwanie częściowe (LIKE)
        if email:
            query = query.filter(User.email.ilike(f"%{email}%"))

        paginated_users = query.paginate(page=page, per_page=limit, error_out=False)

        return paginated_users.items, paginated_users.total  # Zwracamy wyniki + liczbę użytkowników

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
