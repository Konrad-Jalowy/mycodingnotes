function *range(from, to) {

    let i = from;

    while(i <= to) {
        yield i++;
    }

}

for(let value of range(5, 10)) {
    console.log(value);
}