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