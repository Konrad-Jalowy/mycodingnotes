# React custom hooks
My notes on React custom hooks

## useToggle
self-descriptive
```js
import { useState } from "react";
export const useToggle = (initialValue) => {

    const [state, setState] = useState(() => !!initialValue);

    const toggle = () => setState((prev) => !prev);

    return [state, toggle];
};
```

## useTimeout
here full description in my custom-react-hooks project
```js
import { useEffect, useRef, useCallback } from "react";

export function useTimeout(cb, delay){

    const cbRef = useRef(cb);
    const timeoutRef = useRef();

    useEffect(() => {
        cbRef.current = cb
      }, [cb]);
    
    const set = useCallback(() => {
        timeoutRef.current = setTimeout(() => cbRef.current(), delay)
      }, [delay])
    
    const clear = useCallback(() => {
        timeoutRef.current && clearTimeout(timeoutRef.current)
      }, [])
    

      useEffect(() => {
        set()
        return clear
      }, [delay, set, clear])
    
      const reset = useCallback(() => {
        clear()
        set()
      }, [clear, set])
    
    return { reset, clear }
}
```