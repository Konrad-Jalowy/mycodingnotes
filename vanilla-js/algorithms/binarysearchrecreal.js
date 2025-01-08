

function binarySearch(arr, target){
    return _binarySearch(arr, target, 0, arr.length - 1);
}
function _binarySearch(arr, target, left, right){
    if(left > right)
        return -1;
    let middle = Math.floor((left + right)/2);
    let potentialMatch = arr[middle];
    if(target < potentialMatch){
        return _binarySearch(arr,target,left, middle-1)
    } else if (target === potentialMatch){
        return middle;
    } else {
        return _binarySearch(arr,target,middle+1, right)
    }
}
console.log(binarySearch([2,5,6,9,13,15,28,30], 6))