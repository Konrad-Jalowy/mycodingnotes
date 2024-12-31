# OOP Vanilla JS
Notes on OOP in Vanilla JS

## Classes
- **RippleEffect** - from some old project done while learning JS, shows how JS OOP is used in vanilla js

## Constructor function
```js
class Person {
    constructor(name, age){
        this.age = age;
        this.name = name;
    }
}
```

## new.target
```js
function Person(name, age){

  if(!new.target)
      return new Person(name, age);
    
  this.name = name;
  this.age = age;
}

let jim =  Person("Jim", 20);

console.log(jim);
//Object { name: "Jim", age: 20 }
```

## Mixins in JS
```js
let myMixin = {
    mixinMethod(){
        console.log("mixin!");
    }
}

function mixin(...mixins) {

    const fn = function() {};

    Object.assign(fn.prototype, ...mixins);

    return fn;

}

class ClsWithMixins extends mixin(myMixin) {
    constructor(){
        super();
        this.name = "John";
    }
}

let john1 = new ClsWithMixins();
john1.mixinMethod();
//mixin!
```