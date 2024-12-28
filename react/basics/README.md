# React basics
React total basics notes.

## Super-simple counter
```js
import { useState } from "react"
function Counter1(){
    const [count, setCount] = useState(0)
    return (
        <>
        <p>Count: {count}</p>
        <button onClick={() => setCount(count + 1)}>Increment + 1</button>
        </>
    );
};

export {Counter1}
```