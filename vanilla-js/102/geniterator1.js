let it = {
    *[Symbol.iterator]() {

        let numbers = [1, 2, 3, 4, 5];

        for(let number of numbers) {
            yield number;
        }

    }
};

for(let value of it) {
    console.log(value);
}