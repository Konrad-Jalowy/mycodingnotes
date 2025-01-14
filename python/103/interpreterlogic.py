class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Context:
    def __init__(self):
        self.variables = {}

    def assign(self, var, value):
        self.variables[var.name] = value

    def lookup(self, var):
        return self.variables[var.name]

class Expression:
    def interpret(self, context):
        pass

class And(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)

class Or(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)

class Literal(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value

class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable

    def interpret(self, context):
        return context.lookup(self.variable)

# Przykład użycia
context = Context()
varA = Variable("A", None)
varB = Variable("B", None)
context.assign(varA, True)
context.assign(varB, False)

expr = And(VariableExpression(varA), Or(Literal(True), VariableExpression(varB)))
print(expr.interpret(context))  # Output: True
