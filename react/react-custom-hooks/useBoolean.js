import { useRef } from "react";

export function useBoolean(reactiveVariable){
    const currentRef = useRef(reactiveVariable);
    const asBoolean = useRef(!!reactiveVariable);
    
    if(currentRef.current !== reactiveVariable){
        currentRef.current = reactiveVariable;
        asBoolean.current = !!(currentRef.current);
    }
    //console.log(currentRef.current, asBoolean.current);

    return asBoolean.current;
};