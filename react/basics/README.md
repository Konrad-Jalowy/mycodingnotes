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

## using e target dataset
```js
import { useState } from "react"
function Counter2(){
    const [count, setCount] = useState(0);
    function onClickHandler(e){
        if(e.target.dataset.action === "inc"){
            setCount(prev => prev + 1);
        }
        else if(e.target.dataset.action === "dec"){
            setCount(prev => prev - 1);
        }
    }
    return (
        <>
        <p>Count: {count}</p>
        <button data-action="inc" onClick={onClickHandler}>Increment + 1</button>
        <button data-action="dec" onClick={onClickHandler}>Decrement - 1</button>
        </>
    );
};

export {Counter2}
```