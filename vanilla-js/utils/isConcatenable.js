function isConcatenable(obj){
    return Object.getPrototypeOf(obj).hasOwnProperty("concat");
}