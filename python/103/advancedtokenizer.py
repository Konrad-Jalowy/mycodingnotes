import re

class Tokenizer:
    TOKEN_SPECIFICATION = [
        ('NUMBER',      r'\d+(\.\d+)?'),   # Liczby całkowite i zmiennoprzecinkowe
        ('IDENTIFIER',  r'[a-zA-Z_][a-zA-Z0-9_]*'), # Zmienne i funkcje
        ('OPERATOR',    r'[+\-*/]'),       # Operatory
        ('KEYWORD',     r'\b(if|else|while)\b'), # Słowa kluczowe
        ('PAREN',       r'[()]'),         # Nawiasy
        ('SEMICOLON',   r';'),            # Znak końca instrukcji
        ('WHITESPACE',  r'\s+'),          # Białe znaki (ignorowane)
        ('MISMATCH',    r'.'),            # Nieznane znaki (obsługa błędów)
    ]

    def __init__(self, code):
        self.tokens = []
        self.code = code

    def tokenize(self):
        regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.TOKEN_SPECIFICATION)
        for match in re.finditer(regex, self.code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'WHITESPACE':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected token: {value}')
            self.tokens.append((kind, value))
        return self.tokens

# Przykład użycia
code = "if (x + 3.14) while (y - 5);"
tokenizer = Tokenizer(code)
tokens = tokenizer.tokenize()
print(tokens)
# [('IDENTIFIER', 'if'), ('PAREN', '('), ('IDENTIFIER', 'x'), ('OPERATOR', '+'), ('NUMBER', '3.14'), ('PAREN', ')'), 
# ('IDENTIFIER', 'while'), ('PAREN', '('), ('IDENTIFIER', 'y'), ('OPERATOR', '-'),
# ('NUMBER', '5'), ('PAREN', ')'), ('SEMICOLON', ';')]
