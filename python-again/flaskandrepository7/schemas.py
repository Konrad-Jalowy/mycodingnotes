from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    """Schemat walidacji dla użytkownika"""
    username = fields.String(required=True)  # Pole 'username' wymagane
    email = fields.Email(required=True)  # Pole 'email' musi być poprawnym adresem e-mail
