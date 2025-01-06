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

## Bubble sort
### Explanation
- Outer loop (i): i from last idx of array to 1 
- Inner loop (j): j from 0 idx of array to i - 1
- if arr[j] > arr[j+1] then swap

### Unoptimized
```js
function bubbleSort(arr) {
  const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  };

  for (let i = arr.length; i > 0; i--) {
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
      }
    }
  }
  return arr;
}
```
### Optimized
```js
function bubbleSort(arr) {
  const swap = (arr, idx1, idx2) => {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
  };
  let noswaps;
  for (let i = arr.length; i > 0; i--) {
      noswaps = true;
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
        noswaps = false;
      }
    }
    if(noswaps) break;
  }
  return arr;
}
```
### Time complexity
Unoptimized - On^2 (nested loop)
Optimized with nearly sorted array - more like linear

## Selection sort
### Code
```js
function selectionSort(arr) {
  const swap = (arr, idx1, idx2) =>
    ([arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]);

  for (let i = 0; i < arr.length; i++) {
    let lowest = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[lowest] > arr[j]) {
        lowest = j;
      }
    }
    if (i !== lowest) swap(arr, i, lowest);
  }

  return arr;
}
```
### Explanation
Go from left to right and store smallest on the left. </br>
- Outer loop (i): from 0 to arr.length, set lowest variable to i
- Inner loop (j): from i+1 to arr.length, check if arr[lowest] > arr[j], if so, set lowest to j
- Once inner loop done, check if i !== lowest, if so, swap i with the lowest
Again, it works like this:
- Main loop (i) goes from left to right
- Main loop creates variable lowest set to i
- Main loop creates nested loop j
- Nested loop (j) goes from i + 1 to right
- If arr[i] > arr[j] we have update on lowest 
- once nested is finished we check if i is lowest
- if i is not lowest we swap i and j
- purpose of inner loop is to check if i is lowest (in the right place) or not and find the lowest (its index)
- purpose of main loop is to go from left to right and swap if its needed, put the lowest on the left
### Time complexity
- Time complexity O n^2 (nested loops)
- Why better than bubble sort: less swaps. Say you bubble sort arr that has 9 at the start, then some numbers (less that 9). To push 9 to the end you swap, swap, swap... In selection sort you put the lowest at the first... you swap once. One swap per one run of the outer loop... thats the only difference...

## Insertion sort
Edit: found better code
### Code
```js
const insertionSort = (array) => {
  for (let i = 1; i < array.length; i++) {
    let currentElement = array[i];
    let lastIndex = i - 1;

    while (lastIndex >= 0 && array[lastIndex] > currentElement) {
      array[lastIndex + 1] = array[lastIndex];
      lastIndex--;
    }
    array[lastIndex + 1] = currentElement;
  }

  return array;
};

console.log(insertionSort([2,1,9,76,4]))
```
### another explanation
- Ok array 5,9,3, bla bla bla
- take 9
- 5 not > 9, take 3
- make 3 temp
- 9 > 3, its 5,9,9 right now
- 5 > 9 its, 5,5,9 right now
- inner loop finished, last index = -1
- lastindex + 1 = temp (somehow put 3 in idx 0 which gives 3,5,9, somehow it works)

### Better explanation
- We split array to sorted and unsorted part
- We start our main loop at index 1 (second element) and go in  right direction
- inner loop goes from i - 1 to left direction
- we basically check if our number before is bigger than our current number
- we replace our current number with the number before
- we go and keep replacing numbers that are bigger with current one
- somehow it works that you put the last one (temp) and set lastidx + 1 at the end of outer loop to temp
### Explanation
- We start loop from second element
- And we go in right direction
- Then nested while loop goes opposite direction (from 1 left to current outer in left direction)

