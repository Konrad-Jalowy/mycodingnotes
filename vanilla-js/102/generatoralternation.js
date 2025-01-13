function* firstGenerator() {
    let counter = 0;
    while (true) {
        yield counter;  // Zwracamy liczbę
        counter += 2;   // Kolejna liczba parzysta
    }
}

function* secondGenerator() {
    let counter = 1;
    while (true) {
        yield counter;  // Zwracamy liczbę
        counter += 2;   // Kolejna liczba nieparzysta
    }
}

function* masterGenerator() {
    const gen1 = firstGenerator();
    const gen2 = secondGenerator();

    // Naprzemienne generowanie wartości
    while (true) {
        yield gen1.next().value; // Zwracamy liczbę z pierwszego generatora
        yield gen2.next().value; // Zwracamy liczbę z drugiego generatora
    }
}

const gen = masterGenerator();

console.log(gen.next().value); // 0 (parzysta)
console.log(gen.next().value); // 1 (nieparzysta)
console.log(gen.next().value); // 2 (parzysta)
console.log(gen.next().value); // 3 (nieparzysta)
console.log(gen.next().value); // 4 (parzysta)
console.log(gen.next().value); // 5 (nieparzysta)
