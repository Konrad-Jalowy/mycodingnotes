const expression: string = "3 + 5 * (2 - 8)";
const tokens: string[] = expression.match(/\d+|\+|\-|\*|\/|\(|\)/g) || [];
console.log(tokens); // ['3', '+', '5', '*', '(', '2', '-', '8', ')']
