import { useState } from "react";

export default function useArray(defaultValue){

    const [arr, setArr] = useState(defaultValue);

    function push(el){
        setArr(prev => [...prev, el]);
    }

    function filter(callback){
        setArr(a => a.filter(callback));
    }

    function update(index, newElement) {
        setArr(a => [
          ...a.slice(0, index),
          newElement,
          ...a.slice(index + 1, a.length),
        ]);
      }
    
      function remove(index) {
        setArr(a => [...a.slice(0, index), ...a.slice(index + 1, a.length)]);
      }
    
      function clear() {
        setArr([]);
      }


      return { arr, set: setArr, push, filter, update, remove, clear };
};