# Vanilla JS Algos
Notes on algorithms in JS
## Factorial
### Factorial Recursive
```js
function factorialRec(num){
    if(num < 0)
        return -1;
    if(num === 1 || num === 0)
        return 1;
    return num * factorialRec(num-1);
}
```
### Factorial Iterative
```js
function factorialIter(num){

    let result = num;

    if(num < 0)
        return -1;
    if(num === 1 || num === 0)
        return num;

    while(num > 1){

        num--;
        result = result * num;
    }

    return result;

}
```