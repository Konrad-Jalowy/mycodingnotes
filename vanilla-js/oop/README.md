# OOP Vanilla JS
Notes on OOP in Vanilla JS

## Classes
- **EachLetterEffect** - very old class i wrote to have each letter effect
- **ScrollEffect** - another very old class i wrote, to have smooth scroll on anchors that point to website (you can have it via pure css right now)
- **RippleEffect** - from some old project done while learning JS, shows how JS OOP is used in vanilla js
- **AnchorConfirm** - example of super-simple web component
- **AnchorScroll** - another simple web component

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

## Inheritance in JS
```js
function Person(name, age){
        this.name = name;
        this.age = age;
  }

class Worker extends Person {
    constructor(name, age, dept){
        super(name, age);
        this.dept = dept;
    }
}

let w1 = new Worker("John", 30, "HR");
console.log(w1);
//{ name: "John", age: 30, dept: "HR" }
```