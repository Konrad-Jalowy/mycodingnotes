const expression = "3 + 5 * (2 - 8)";
const tokens = expression.match(/\d+|\+|\-|\*|\/|\(|\)/g);
console.log(tokens); // ['3', '+', '5', '*', '(', '2', '-', '8', ')']
