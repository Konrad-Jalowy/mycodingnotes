class Expression {
    interpret() {}
}

class Number extends Expression {
    constructor(value) {
        super();
        this.value = value;
    }

    interpret() {
        return this.value;
    }
}

class Add extends Expression {
    constructor(left, right) {
        super();
        this.left = left;
        this.right = right;
    }

    interpret() {
        return this.left.interpret() + this.right.interpret();
    }
}

class Subtract extends Expression {
    constructor(left, right) {
        super();
        this.left = left;
        this.right = right;
    }

    interpret() {
        return this.left.interpret() - this.right.interpret();
    }
}

// Przykład użycia
const expr = new Add(
    new Number(5),
    new Subtract(new Number(10), new Number(2))
);
console.log(expr.interpret()); // Output: 13
