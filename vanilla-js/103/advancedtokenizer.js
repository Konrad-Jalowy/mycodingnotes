class Tokenizer {
    constructor(code) {
        this.code = code;
        this.tokenSpec = [
            { type: "KEYWORD", regex: /\b(if|else|while)\b/ }, // Słowa kluczowe
            { type: "IDENTIFIER", regex: /^[a-zA-Z_][a-zA-Z0-9_]*/ }, // Zmienne i funkcje
            { type: "NUMBER", regex: /^\d+(\.\d+)?/ }, // Liczby całkowite i zmiennoprzecinkowe
            { type: "OPERATOR", regex: /^[+\-*/]/ }, // Operatory
            { type: "PAREN", regex: /^[()]/ }, // Nawiasy
            { type: "SEMICOLON", regex: /^;/ }, // Znak końca instrukcji
            { type: "WHITESPACE", regex: /^\s+/ }, // Ignorowane białe znaki
        ];
    }

    tokenize() {
        const tokens = [];
        let pos = 0;

        while (pos < this.code.length) {
            let matched = false;

            for (let { type, regex } of this.tokenSpec) {
                const substr = this.code.slice(pos);
                const match = substr.match(regex);

                if (match) {
                    const value = match[0];
                    if (type !== "WHITESPACE") {
                        tokens.push({ type, value });
                    }
                    pos += value.length; // Przeskok do następnego tokenu
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                console.error(`Unexpected token at position ${pos}: "${this.code[pos]}"`);
                throw new Error(`Unexpected token at position ${pos}`);
            }
        }

        return tokens;
    }
}

// Testowanie poprawionego tokenizatora
const code = "if (x + 3.14)";
try {
    const tokenizer = new Tokenizer(code);
    console.log(tokenizer.tokenize());
} catch (error) {
    console.error("Błąd tokenizacji:", error.message);
}

// [
//   { type: 'KEYWORD', value: 'if' },
//   { type: 'PAREN', value: '(' },
//   { type: 'IDENTIFIER', value: 'x' },
//   { type: 'OPERATOR', value: '+' },
//   { type: 'NUMBER', value: '3.14' },
//   { type: 'PAREN', value: ')' }
// ]
