Array.prototype.myForEach = function(callback, thisArg){
    var array = this;
    thisArg = thisArg || this;
    for (var i = 0; i < this.length; i++) {
       callback.call(thisArg, array[i], i, array);
    }   
 }