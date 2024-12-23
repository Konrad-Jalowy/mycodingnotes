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

## useRenderCount
real, working with no issues render counter
```js
import { useEffect, useRef } from "react";
export function useRenderCount(){
    const count = useRef(1)
    const rendered = useRef(false);
    
    useEffect(() => {
        if(rendered.current === false){
            rendered.current = true;
            return;
        }
        count.current++;
    })
    return count.current;
};
```

## usePrevHook
Tbh interesting hook
```js
import { useRef } from "react";

export function usePrev(reactiveVariable){

    const currentValue = useRef(reactiveVariable);
    const previousValue = useRef();

    if(currentValue.current !== reactiveVariable){
        previousValue.current = currentValue.current;
        currentValue.current = reactiveVariable;
    }
    
    return previousValue.current;
};
```

## useInterval
```js
import { useEffect, useRef } from "react";

export function useInterval(callback, delay){

    const callbackRef = useRef();
    const intervalID = useRef(null);

    useEffect(() => {
        callbackRef.current = callback;
    }, [callback])

    useEffect(() => {
        const tick = () => {
          callbackRef.current();
        }
        if (delay !== null) {
          intervalID.current = setInterval(tick, delay);
          return () => clearInterval(intervalID.current);
        }
      }, [delay]);

    const stopIntervalNow = () => {
        clearInterval(intervalID.current);
        intervalID.current = null;
    }

    return stopIntervalNow;
};
```