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