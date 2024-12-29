Array.prototype.myMap = function(callbackFn, thisArg) {

    var context = thisArg || globalThis;

    var arr = [];              
    for (var i = 0; i < this.length; i++) { 
      arr.push(callbackFn.call(context, this[i], i, this));
    }
    return arr;
  }