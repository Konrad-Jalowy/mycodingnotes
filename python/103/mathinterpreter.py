import re

class Expression:
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Divide(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

class Parser:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expression)
        self.current_token_index = 0

    def parse(self):
        return self._parse_expression()

    def _parse_expression(self):
        left = self._parse_term()
        while self._current_token() in ('+', '-'):
            operator = self._current_token()
            self._consume_token()
            right = self._parse_term()
            if operator == '+':
                left = Add(left, right)
            elif operator == '-':
                left = Subtract(left, right)
        return left

    def _parse_term(self):
        left = self._parse_factor()
        while self._current_token() in ('*', '/'):
            operator = self._current_token()
            self._consume_token()
            right = self._parse_factor()
            if operator == '*':
                left = Multiply(left, right)
            elif operator == '/':
                left = Divide(left, right)
        return left

    def _parse_factor(self):
        if self._current_token() == '(':
            self._consume_token()
            expression = self._parse_expression()
            self._consume_token()  # Consume ')'
            return expression
        else:
            number = Number(int(self._current_token()))
            self._consume_token()
            return number

    def _current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def _consume_token(self):
        self.current_token_index += 1

# Przykład użycia
parser = Parser("2 + 2 * 2")
expression = parser.parse()
print(expression.interpret())  # Output: 6

parser = Parser("(2 + 2) * 2")
expression = parser.parse()
print(expression.interpret())  # Output: 8
