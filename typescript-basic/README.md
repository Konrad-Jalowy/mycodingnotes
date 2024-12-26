# typescript basic
basics of typescrip

# quick start
## start project
```sh
npx tsc --init
```
## run ts file in command line
```sh
npx ts-node src/foo.ts
```
## compile files
remember to specify outDir or it will compile them in cwd
```sh
npx tsc
```
## compile watch flag
```sh
npx tsc -w
```

## ts type aliases
nice reminder how they work code from the internet
```ts
type stringOrNumber = string | number

type stringOrNumberArray = (string | number)[]

type Guitarist = {
    name?: string,
    active: boolean,
    albums: stringOrNumberArray
}

type UserId = stringOrNumber

// Literal types
let myName: 'Dave'

let userName: 'Dave' | 'John' | 'Amy'
userName = 'Amy'
```

## simple funcs annotations
```ts
const add = (a: number, b: number): number => {
    return a + b
}

const logMsg = (message: any): void => {
    console.log(message)
}

let subtract = function (c: number, d: number): number {
    return c - d
}
```

## func type and func interface
id prefer type
```ts
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
```

## type guards in ts
```ts
function stringOrNumber(arg: string|number){
    if(typeof arg === "string"){
        return arg.toUpperCase();
    }
    if(typeof arg === "number"){
        return arg + 42;
    }
}
console.log(stringOrNumber("hello world")) //HELLO WORLD
console.log(stringOrNumber(10)) //52
```

## rest params in ts
```ts
function introduce(salutation: string, ...names: string[]): string {
    return `${salutation} ${names.join(", ")}.`;
  }

console.log(introduce("Hello", "John", "Jane", "Jim"));
//Hello John, Jane, Jim.
```