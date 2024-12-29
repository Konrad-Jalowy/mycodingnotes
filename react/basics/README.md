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

## Another exercise (updater funcs)
```js
import { useState } from "react"
function Counter3(){
    const [count, setCount] = useState(0);
    const [by, setBy] = useState(1);
    function onClickHandler(e){
        if(e.target.dataset.action === "inc"){
            setCount(prev => prev + (1*by));
        }
        else if(e.target.dataset.action === "dec"){
            setCount(prev => prev - (1*by));
        }
    }
    return (
        <>
        <p>Count: {count}</p>
        <button data-action="inc" onClick={onClickHandler}>Increment + {by}</button>
        <button data-action="dec" onClick={onClickHandler}>Decrement - {by}</button>
        <input type="range" min={1} value={by} onChange={(e) => setBy(e.target.value)} />
        </>
    );
};

export {Counter3}
```
## Props
Example of component using props
```js
function IdxRFC({idx, maxDate}){
  
    return (
        <p className="idx-rfc">Data {idx + 1} / {maxDate} </p>
    );
};

export default IdxRFC;
```