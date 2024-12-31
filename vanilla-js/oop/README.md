# OOP Vanilla JS
Notes on OOP in Vanilla JS

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