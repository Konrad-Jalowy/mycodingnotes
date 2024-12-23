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