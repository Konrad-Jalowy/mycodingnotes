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

class Multiply extends Expression {
    constructor(left, right) {
        super();
        this.left = left;
        this.right = right;
    }

    interpret() {
        return this.left.interpret() * this.right.interpret();
    }
}

class Divide extends Expression {
    constructor(left, right) {
        super();
        this.left = left;
        this.right = right;
    }

    interpret() {
        return this.left.interpret() / this.right.interpret();
    }
}

class Parser {
    constructor(expression) {
        this.tokens = expression.match(/\d+|\+|\-|\*|\/|\(|\)/g);
        this.currentTokenIndex = 0;
    }

    parse() {
        return this.parseExpression();
    }

    parseExpression() {
        let left = this.parseTerm();
        while (this.currentToken() === '+' || this.currentToken() === '-') {
            const operator = this.currentToken();
            this.consumeToken();
            const right = this.parseTerm();
            if (operator === '+') {
                left = new Add(left, right);
            } else if (operator === '-') {
                left = new Subtract(left, right);
            }
        }
        return left;
    }

    parseTerm() {
        let left = this.parseFactor();
        while (this.currentToken() === '*' || this.currentToken() === '/') {
            const operator = this.currentToken();
            this.consumeToken();
            const right = this.parseFactor();
            if (operator === '*') {
                left = new Multiply(left, right);
            } else if (operator === '/') {
                left = new Divide(left, right);
            }
        }
        return left;
    }

    parseFactor() {
        if (this.currentToken() === '(') {
            this.consumeToken();
            const expression = this.parseExpression();
            this.consumeToken(); // Consume ')'
            return expression;
        } else {
            const number = new Number(parseInt(this.currentToken(), 10));
            this.consumeToken();
            return number;
        }
    }

    currentToken() {
        return this.tokens[this.currentTokenIndex];
    }

    consumeToken() {
        this.currentTokenIndex++;
    }
}

// Przykład użycia
const parser = new Parser("2 + 2 * 2");
const expression = parser.parse();
console.log(expression.interpret()); // Output: 6

const parser2 = new Parser("(2 + 2) * 2");
const expression2 = parser2.parse();
console.log(expression2.interpret()); // Output: 8