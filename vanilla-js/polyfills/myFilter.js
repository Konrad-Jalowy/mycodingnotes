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