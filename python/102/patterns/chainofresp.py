class Handler:
    """Abstrakcyjna klasa bazowa dla wszystkich handlerów."""
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class AuthHandler(Handler):
    def handle(self, request):
        if request.get("authenticated"):
            print("AuthHandler: User authenticated.")
            return super().handle(request)
        else:
            print("AuthHandler: Authentication failed.")
            return "403 Forbidden"


class LoggingHandler(Handler):
    def handle(self, request):
        print(f"LoggingHandler: Logging request: {request}")
        return super().handle(request)


class DataValidationHandler(Handler):
    def handle(self, request):
        if request.get("data"):
            print("DataValidationHandler: Data validated.")
            return super().handle(request)
        else:
            print("DataValidationHandler: Invalid data.")
            return "400 Bad Request"


# Tworzenie łańcucha
chain = AuthHandler(
    LoggingHandler(
        DataValidationHandler()
    )
)

# Testowanie żądań
request = {"authenticated": True, "data": "Valid payload"}
print(chain.handle(request))

print("\n")

request = {"authenticated": False, "data": "Valid payload"}
print(chain.handle(request))
