Function.prototype.myBind = function(refObj, ...args){
    const fn = this;
    return function(){
        fn.call(refObj, args);
    }
}