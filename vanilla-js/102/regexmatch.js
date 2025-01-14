const pattern = /\d+/g;  // Dopasowanie jednej lub więcej cyfr
const text = "Znajdź liczby 42 i 123 w tym tekście.";

const matches = text.match(pattern);
console.log(matches);  // Output: ['42', '123']
