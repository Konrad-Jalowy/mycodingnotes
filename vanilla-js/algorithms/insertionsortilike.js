function insertionSort(arr) {
    let i, temp, j;
    for(i = 1; i <arr.length; i++) {
        temp = arr[i];
        j = i;
        while(j > 0 && arr[j-1] > temp){
            arr[j] = arr[j-1];
            j--;
        }
        arr[j] = temp;
    }
    return arr;
}

console.log(insertionSort([2,1,9,76,4]))
//[ 1, 2, 4, 9, 76 ]