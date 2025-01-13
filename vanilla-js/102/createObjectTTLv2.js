function createObject(strings, ...values) {
    const obj = {};
    
    // Zaczynamy od pierwszego elementu w "strings", pomijając pierwszy pusty string
    strings.forEach((str, i) => {
        if (i < strings.length - 1) { // Pomijamy ostatni pusty string
            obj[str.trim()] = values[i] !== undefined ? values[i] : null;
        }
    });
    return obj;
}

const name = 'Alice';
const age = 30;
const userObj = createObject`name ${name} age ${age}`;
console.log(userObj); 
// Output: { name: 'Alice', age: 30 }