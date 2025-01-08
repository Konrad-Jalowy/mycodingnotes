
function binarySearch(arr, target){
    let left = 0;
    let right = arr.length - 1;
   
    while(left <= right){
         let middle = Math.floor((left+right)/2);
         let potentialMatch = arr[middle];
         if(target === potentialMatch){
             return middle;
         }
         else if (target < potentialMatch){
             right = middle - 1;
         }
         else {
             left = middle + 1;
         }
    }
    return -1;
}

console.log(binarySearch([2,5,6,9,13,15,28,30], 6))