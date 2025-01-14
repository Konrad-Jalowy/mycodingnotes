abstract class Expression {
    abstract interpret(): number;
}

class NumberExpression extends Expression {
    constructor(private value: number) {
        super();
    }

    interpret(): number {
        return this.value;
    }
}

class AddExpression extends Expression {
    constructor(private left: Expression, private right: Expression) {
        super();
    }

    interpret(): number {
        return this.left.interpret() + this.right.interpret();
    }
}

class SubtractExpression extends Expression {
    constructor(private left: Expression, private right: Expression) {
        super();
    }

    interpret(): number {
        return this.left.interpret() - this.right.interpret();
    }
}

// Przykład użycia
const expr = new AddExpression(
    new NumberExpression(5),
    new SubtractExpression(new NumberExpression(10), new NumberExpression(2))
);
console.log(expr.interpret()); // Output: 13
