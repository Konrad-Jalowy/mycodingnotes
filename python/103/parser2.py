class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        return self._parse_expression()

    def _parse_expression(self):
        node = self._parse_term()
        while self._current_token() in ('+', '-'):
            operator = self._current_token()
            self._consume()
            right = self._parse_term()
            if operator == '+':
                node = ('Add', node, right)
            elif operator == '-':
                node = ('Subtract', node, right)
        return node

    def _parse_term(self):
        node = self._parse_factor()
        while self._current_token() in ('*', '/'):
            operator = self._current_token()
            self._consume()
            right = self._parse_factor()
            if operator == '*':
                node = ('Multiply', node, right)
            elif operator == '/':
                node = ('Divide', node, right)
        return node

    def _parse_factor(self):
        token = self._current_token()
        if token == '(':
            self._consume()
            node = self._parse_expression()
            self._consume()  # Consume ')'
            return node
        else:
            self._consume()
            return ('Number', int(token))

    def _current_token(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else None

    def _consume(self):
        self.current += 1

# Przykład
tokens = ['2', "+", '2', "*", '2']
parser = Parser(tokens)
ast = parser.parse()
print(ast)
# ('Add', ('Number', 2), ('Multiply', ('Number', 2), ('Number', 2)))