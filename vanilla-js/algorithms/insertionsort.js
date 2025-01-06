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