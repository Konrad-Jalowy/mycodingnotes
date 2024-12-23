import { useEffect, useRef } from "react"

export default function useClickOutside(ref, cb) {

  const callbackRef = useRef(cb)

  useEffect(() => {
    callbackRef.current = cb
  }, [cb])

  useEffect(() => {
    const handler = e => {
        if(ref.current === null || ref.current.contains(e.target)) return;
        callbackRef.current(e);
    } 
    document.addEventListener('click', handler)

    return () => document.removeEventListener('click', handler)
  }, [ref]);
}