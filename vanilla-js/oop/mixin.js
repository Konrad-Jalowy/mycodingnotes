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