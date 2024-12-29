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