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