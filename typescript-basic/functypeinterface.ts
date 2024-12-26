type mathFunction = (a: number, b: number) => number

interface IMathFunction {
    (a: number, b: number): number
}

let multiply: mathFunction = function (c, d) {
    return c * d;
}

let divide: IMathFunction = function(x, y) {
    return x/y;
}

console.log(multiply(2,4))
console.log(divide(10,2))