class ValidationStrategy:
    def validate(self, value):
        raise NotImplementedError

class EmailValidation(ValidationStrategy):
    def validate(self, value):
        return "@" in value and "." in value

class PhoneValidation(ValidationStrategy):
    def validate(self, value):
        return value.isdigit() and len(value) == 9

class Validator:
    def __init__(self, strategy):
        self.strategy = strategy

    def validate(self, value):
        return self.strategy.validate(value)

email_validator = Validator(EmailValidation())
print(email_validator.validate("test@example.com"))  # True