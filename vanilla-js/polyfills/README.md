# Vanilla JS Polyfills
My Polyfills...

## Filter polyfill
```js
Array.prototype.myFilter = function(callback, thisArg){

    var context = thisArg || globalThis;

    var arr = [];

    for(i=0; i< this.length; i++){
        if(callback.call(context, this[i], i, this)){

            arr.push(this[i])
        }
    }
    return arr;
}
```

## ForEach polyfill
```js
Array.prototype.myForEach = function(callback, thisArg){
    var array = this;
    thisArg = thisArg || this;
    for (var i = 0; i < this.length; i++) {
       callback.call(thisArg, array[i], i, array);
    }   
 }
```

## My map
super simple
```js
Array.prototype.myMap = function(callbackFn, thisArg) {

    var context = thisArg || globalThis;

    var arr = [];              
    for (var i = 0; i < this.length; i++) { 
      arr.push(callbackFn.call(context, this[i], i, this));
    }
    return arr;
  }
```

## My Reduce
```js
Array.prototype.myReduce= function(callbackFn, initialValue) {
    var accumulator = initialValue;
  for (var i = 0; i < this.length; i++) {
      if (accumulator !== undefined) {
        accumulator = callbackFn.call(undefined, accumulator, this[i],   i, this);
      } else {
        accumulator = this[i];
      }
    }
    return accumulator;
  }
```
## my reduce right
```js
Array.prototype.myReduceRight= function(callbackFn, initialValue) {
    var accumulator = initialValue;
  for (var i = this.length - 1; i >= 0; i--) {
      if (accumulator !== undefined) {
        accumulator = callbackFn.call(undefined, accumulator, this[i],   i, this);
      } else {
        accumulator = this[i];
      }
    }
    return accumulator;
  }
```
## My Trim
more than polyfill, in js you can only trim spaces (idk why...)
```js
String.prototype.myTrim = function(trimmedChar = " "){
    
    if(trimmedChar.length < 1)
        trimmedChar = " ";

    if(trimmedChar.length > 1)
        trimmedChar = trimmedChar[0];

    let left = 0;
    let right = this.length - 1;

    while(this[left] === trimmedChar){
        left++;
    }

    while(this[right] === trimmedChar){

        if(this[right -1] !== trimmedChar)
            break;

        right--;
    }

    if(left > right)
        return "";

    return this.substring(left, right);
}
```

## My call
```js
Function.prototype.myCall = function(obj, ...args){
    let fn=this;
    if(typeof fn !== "function"){
        throw new Error('Invalid function provided for binding.');
      }
    let myFn = Symbol('myFn');
    obj[myFn] = this;
    let result = obj[myFn](...args);
    return result;
    
}
```
## My Apply
```js
Function.prototype.myApply = function(obj, args){
    let fn=this;
    if(typeof fn !== "function"){
        throw new Error('Invalid function provided for binding.');
      }
    let myFn = Symbol('myFn');
    obj[myFn] = this;
    let result = obj[myFn](...args);
    return result;
    
}
```

## My bind
```js
Function.prototype.myBind = function(refObj, ...args){
    const fn = this;
    return function(){
        fn.call(refObj, args);
    }
}
```
## My Get el by id
```js
Document.prototype.myGetElementById = function(id) {
    
    var result = null;
    function traverse(node) {
      if(node == null) 
        return;
      if(node.id === id) {
            result = node;
            return;
        }
      for(var child of node.children) 
        traverse(child);
    }
    traverse(this.documentElement); 
    return result;
  }
```