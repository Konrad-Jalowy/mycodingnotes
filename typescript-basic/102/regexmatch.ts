const pattern: RegExp = /\d+/g;
const text: string = "Znajdź liczby 42 i 123 w tym tekście.";

const matches: string[] | null = text.match(pattern);
console.log(matches);  // Output: ['42', '123']