import { useEffect, useRef } from "react"

export default function useEventListener(
  evtType,
  cb,
  el = window
) {
  const callbackRef = useRef(cb)

  useEffect(() => {
    callbackRef.current = cb
  }, [cb])

  useEffect(() => {
    if (el == null) return
    const handler = e => callbackRef.current(e)
    el.addEventListener(evtType, handler)

    return () => el.removeEventListener(evtType, handler)
  }, [evtType, el]);
}