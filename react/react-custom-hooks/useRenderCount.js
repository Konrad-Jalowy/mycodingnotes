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