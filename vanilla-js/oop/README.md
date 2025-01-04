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

## Something close to abstract classes in JS
```js
class AbstractPerson {

    constructor(name, age){
         if(new.target === AbstractPerson){
            throw new Error("Abstract class cant be instantiated");
         }
         this.name = name; 
         this.age = age;
    }
}


class Worker extends AbstractPerson{
    constructor(name, age, dept){
        super(name, age);
        this.dept = dept;
    }
}

let worker = new Worker("John", 30, "HR");
console.log(worker);
//Object { name: "John", age: 30, dept: "HR" }

let person = new AbstractPerson("John", 30);
//Uncaught Error: Abstract class cant be instantiated
```

## How to approach writing OOP with DOM and vanilla JS
```js
class Shop {
    constructor() {
      this.render();
    }
  
    render() {
      this.cart = new ShoppingCart('app');
      new ProductList('app');
    }
  }
  
  class App {
    static cart;
  
    static init() {
      const shop = new Shop();
      this.cart = shop.cart;
    }
  
    static addProductToCart(product) {
      this.cart.addProduct(product);
    }
  }
  
  App.init();
```

## nice idea for component class
```js
class Component {
  constructor(renderHookId, shouldRender = true) {
    this.hookId = renderHookId;
    if (shouldRender) {
      this.render();
    }
  }

  render() {}

  createRootElement(tag, cssClasses, attributes) {
    const rootElement = document.createElement(tag);
    if (cssClasses) {
      rootElement.className = cssClasses;
    }
    if (attributes && attributes.length > 0) {
      for (const attr of attributes) {
        rootElement.setAttribute(attr.name, attr.value);
      }
    }
    document.getElementById(this.hookId).append(rootElement);
    return rootElement;
  }
}
```

## More modular and better organized component
```js
class Component {
  constructor(hostElementId, insertBefore = false) {
    if (hostElementId) {
      this.hostElement = document.getElementById(hostElementId);
    } else {
      this.hostElement = document.body;
    }
    this.insertBefore = insertBefore;
  }

  detach() {
    if (this.element) {
      this.element.remove();
      // this.element.parentElement.removeChild(this.element);
    }
  }

  attach() {
    this.hostElement.insertAdjacentElement(
      this.insertBefore ? 'afterbegin' : 'beforeend',
      this.element
    );
  }
}
```

## DOMHelper class
```js
class DOMHelper {
  static clearEventListeners(element) {
    const clonedElement = element.cloneNode(true);
    element.replaceWith(clonedElement);
    return clonedElement;
  }

  static moveElement(elementId, newDestinationSelector) {
    const element = document.getElementById(elementId);
    const destinationElement = document.querySelector(newDestinationSelector);
    destinationElement.append(element);
  }
}
```