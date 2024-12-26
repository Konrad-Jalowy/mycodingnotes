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