import re

expression = "3 + 5 * (2 - 8)"
tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expression)
print(tokens)  # ['3', '+', '5', '*', '(', '2', '-', '8', ')']
