function *generateId() {
    let id = 1;
    
    while(true){
        const increment = yield id;
        if(increment != null)
        {
            id += increment;
        } else {
            id++;
        }
    }
}

const genObj = generateId();
console.log(genObj.next()); //{ value: 1, done: false }
console.log(genObj.next()); //{ value: 2, done: false }
console.log(genObj.next(10)); //{ value: 12, done: false }
