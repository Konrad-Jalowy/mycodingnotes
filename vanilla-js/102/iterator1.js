const makeIterator = function() {

    var numbers = [1, 2, 3, 4, 5],
        index = 0;

    return {
        next: function() {
            return {
                done: (index === numbers.length) ? true : false,
                value: numbers[index++]
            };
        }
    };

};

let iterator = makeIterator();
for(let o = iterator.next(); o.done !== true; o = iterator.next()) {
    console.log(o.value);
}