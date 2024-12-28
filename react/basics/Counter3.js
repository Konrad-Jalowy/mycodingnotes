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