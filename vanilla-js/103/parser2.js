class Parser {
    constructor(tokens) {
        this.tokens = tokens;
        this.current = 0;
    }

    parse() {
        return this.parseExpression();
    }

    parseExpression() {
        let node = this.parseTerm();
        while (this.currentToken() === '+' || this.currentToken() === '-') {
            const operator = this.currentToken();
            this.consumeToken();
            const right = this.parseTerm();
            node = { type: operator === '+' ? 'Add' : 'Subtract', left: node, right: right };
        }
        return node;
    }

    parseTerm() {
        let node = this.parseFactor();
        while (this.currentToken() === '*' || this.currentToken() === '/') {
            const operator = this.currentToken();
            this.consumeToken();
            const right = this.parseFactor();
            node = { type: operator === '*' ? 'Multiply' : 'Divide', left: node, right: right };
        }
        return node;
    }

    parseFactor() {
        const token = this.currentToken();
        if (token === '(') {
            this.consumeToken();
            const node = this.parseExpression();
            this.consumeToken(); // Consume ')'
            return node;
        } else {
            this.consumeToken();
            return { type: 'Number', value: parseInt(token, 10) };
        }
    }

    currentToken() {
        return this.tokens[this.current];
    }

    consumeToken() {
        this.current++;
    }
}

// Przykład
const tokens = ['(', '2', '+', '2', ')', '*', '2']
const parser = new Parser(tokens);
const ast = parser.parse();
console.log(JSON.stringify(ast, null, 2));

// {
//   "type": "Multiply",
//   "left": {
//     "type": "Add",
//     "left": {
//       "type": "Number",
//       "value": 2
//     },
//     "right": {
//       "type": "Number",
//       "value": 2
//     }
//   },
//   "right": {
//     "type": "Number",
//     "value": 2
//   }
// }
