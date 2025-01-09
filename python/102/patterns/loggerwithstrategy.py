class LogStrategy:
    def log(self, message):
        raise NotImplementedError

class FileLog(LogStrategy):
    def log(self, message):
        print(f"Writing to file: {message}")

class ConsoleLog(LogStrategy):
    def log(self, message):
        print(f"Logging to console: {message}")

class Logger:
    def __init__(self, strategy):
        self.strategy = strategy

    def log(self, message):
        self.strategy.log(message)

logger = Logger(ConsoleLog())
logger.log("Application started.")  # Logging to console: Application started.