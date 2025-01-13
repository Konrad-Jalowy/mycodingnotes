function createObject(strings, ...values) {
    const obj = {};
    strings.forEach((str, i) => {
        obj[str.trim()] = values[i] !== undefined ? values[i] : null;
    });
    return obj;
}

const name = 'Alice';
const age = 30;
const userObj = createObject`name ${name} age ${age}`;
console.log(userObj); 
// Output: { name: 'Alice', age: 30, "": null}
//todo - naprawić falsy values