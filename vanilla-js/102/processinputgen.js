function* processInput() {
    let sum = 0;
    
    // Generator prosi o liczbę i sumuje je
    while (true) {
        let value = yield `Current sum: ${sum}. Provide a number to add:`;
        sum += value;
    }
}

const generator = processInput();
console.log(generator.next().value);  // Current sum: 0. Provide a number to add:

console.log(generator.next(5).value);  // Current sum: 5. Provide a number to add:
console.log(generator.next(10).value); // Current sum: 15. Provide a number to add:
console.log(generator.next(20).value); // Current sum: 35. Provide a number to add: