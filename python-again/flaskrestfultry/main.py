from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = {}  # Prosta baza danych w pamięci

class UserResource(Resource):
    def get(self, user_id):
        """Pobiera użytkownika po ID"""
        if user_id not in users:
            return {"error": "User not found"}, 404
        return users[user_id]

    def post(self, user_id):
        """Dodaje nowego użytkownika"""
        data = request.json
        if "username" not in data:
            return {"error": "Missing username"}, 400
        users[user_id] = data
        return {"message": "User created"}, 201

    def delete(self, user_id):
        """Usuwa użytkownika"""
        if user_id not in users:
            return {"error": "User not found"}, 404
        del users[user_id]
        return {"message": "User deleted"}, 200

# Rejestrujemy endpointy
api.add_resource(UserResource, "/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)