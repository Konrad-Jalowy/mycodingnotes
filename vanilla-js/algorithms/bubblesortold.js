function bubbleSort(arr){
    for(var i = arr.length; i > 0; i--){
      for(var j = 0; j < i - 1; j++){
        console.log(arr, arr[j], arr[j+1]);
        if(arr[j] > arr[j+1]){
          var temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;         
        }
      }
    }
    return arr;
  }