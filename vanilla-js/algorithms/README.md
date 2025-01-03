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

## Sum
### Sum Iterative
```js
function sumIter(x, y){
    if(x === 0 || y === 0)
        return Math.max(x,y);

    let bigger = Math.max(x, y);
    let smaller = Math.min(x, y);

    while(smaller > 0){
        bigger++;
        smaller--;
    }

    return bigger;
}
```
### Sum Recursive
```js
function sumRec(x, y){
    if(x === 0 || y === 0)
        return Math.max(x,y);
    if(y > x)
        return sumRec(y, x);
    return sumRec(x+1, y-1);
}
```

## flatten array
```js
const flatten = (nestedArr) => {
    
    const flatArr = [];

    const _flatten = (arr) => {

      let counter = 0

      while (counter < arr.length) {

        const val = arr[counter];

        if (Array.isArray(val)) 
          _flatten(val);
        else 
          flatArr.push(val);
        
        counter++;
      }
    
    }

    _flatten(nestedArr);

    return flatArr;
  }
```

## Binary Search
### Iterative Bin. Search
```js
function binarySearch(arr, target) {
    let start = 0
    let end = arr.length - 1
    while (start <= end) {
      let middle = Math.floor((start + end) / 2)
      if (arr[middle] < target) {
        start = middle + 1
      } else if (arr[middle] > target) {
        end = middle - 1
      } else if (arr[middle] === target) {
        return middle
      }
    }
    
    return -1
  }
```
### Recursive Binary Search
```js
function recursiveBinarySearch(n, arr) {
    let mid = Math.floor(arr.length / 2);
  if (arr.length === 1 && arr[0] != n) {
      return false;
    }
    if (n === arr[mid]) {
      return true;
    } else if (n < arr[mid]) {
      return recursiveBinarySearch(n, arr.slice(0, mid));
    } else if (n > arr[mid]) {
      return recursiveBinarySearch(n, arr.slice(mid));
    }
}
```

## Power
### Power Recursive
```js
function power(base, exponent){

    if(exponent === 0)
        return 1;
    
    return base * power(base, exponent-1);

}
```

## Decimal to bin
### Decimal to bin rec
```js
function decimalToBinRec(num){

    let binaryArr = [];

    function _decToBinRec(num){
        if(num <= 0)
            return;

        binaryArr.unshift(num % 2);
        _decToBinRec(Math.floor(num / 2));
    }
    
    _decToBinRec(num);

    return "0b" + binaryArr.join("");
}
```