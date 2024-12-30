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

## Props and forwardRef
### Example 1
```js
import { forwardRef } from "react";
const EventRFC = forwardRef(function EventRFC({idx, dates, datesFirst}, ref){
    const eventText = datesFirst ? dates[idx].event : dates[idx].date;
    return (
        <p ref={ref} className="event-rfc ani-fadein">{eventText}</p>
    )
});
export default EventRFC;
```
### Example 2
```js
import { forwardRef } from "react";
const DateRFC = forwardRef(function DateRFC2({idx, dates, datesFirst}, ref){
    const dateText = datesFirst ? dates[idx].date : dates[idx].event
   
    return (
        <p ref={ref} className="date-rfc ani-fadein">{dateText}</p>
    );
});

export default DateRFC;
```
### usnig context
```js
import { createContext, useContext, useReducer } from 'react';

const initialState = {
    shuffle: false,
    title: null,
    firstIdx: 0,
    lastIdx: null,
    take: null,
    datesFirst: true,
    dates: [],
    loopMode: 'fileNotSent'
};

function appContextReducer(state, action){
    switch (action.type) {
        case 'toggleShuffle': {
          return {
            ...state, 
            shuffle: !state.shuffle
          };
        }
        case 'toggleDatesFirst': {
            return {
              ...state, 
              datesFirst: !state.datesFirst
            };
          }
          case 'setTitle': {
            return {
              ...state, 
              title: action.payload
            };
          }
          case 'setDates': {
            return {
              ...state, 
              dates: [...action.payload]
            };
          }
          case 'setTake': {
            return {
              ...state, 
              take: action.payload
            };
          }
          case 'setLastIdx': {
            return {
              ...state, 
              lastIdx: action.payload
            };
          }
          case 'setLoopMode': {
            return {
              ...state, 
              loopMode: action.payload
            };
          }
          case 'prepare': {
            return {
              ...state, 
              loopMode: 'started',
              title: action.payload.title,
              take: action.payload.take,
              datesFirst: action.payload.datesFirst,
              shuffle: action.payload.shuffle,
              dates: action.payload.dates
            };
          }
          case 'reset': {
            return {   
            shuffle: false,
            title: null,
            firstIdx: 0,
            lastIdx: null,
            take: null,
            datesFirst: true,
            dates: [],
            loopMode: 'fileNotSent'
            };
          }
        
        
        default: {
          throw Error('Unknown action: ' + action.type);
        }
      }
    }
    

    const AppContext = createContext(null);
    
    const AppDispatchContext = createContext(null);
    
    export function AppProvider({ children }) {
        const [state, dispatch] = useReducer(appContextReducer, initialState);
      
        return (
          <AppContext.Provider value={state}>
            <AppDispatchContext.Provider value={dispatch}>
              {children}
            </AppDispatchContext.Provider>
          </AppContext.Provider>
        );
      }
    
      export function useApp() {
        return useContext(AppContext);
      }
      
      export function useAppDispatch() {
        return useContext(AppDispatchContext);
      }
    
      export function useAppWithDispatch(){
        return [useContext(AppContext), useContext(AppDispatchContext) ];
      }
```
## Timer (from quiz app project)
```js
import { useState, useEffect } from 'react';

export default function Timer({ timeout, onTimeout, blocked}) {
  const [remainingTime, setRemainingTime] = useState(timeout);

  useEffect(() => {
    let timer;

    timer = setTimeout(onTimeout, timeout);

    return () => {
      clearTimeout(timer);
    };
  }, [timeout, onTimeout]);

  useEffect(() => {
    let interval;
    if(blocked === false){
        interval = setInterval(() => {
            setRemainingTime((prevRemainingTime) => prevRemainingTime - 100);
          }, 100);
    } else {
        clearInterval(interval);
    }
    
    return () => {
      clearInterval(interval);
    };
  }, [blocked]);

    return (
        <progress
          id="timer"
          max={timeout}
          value={remainingTime}
        />
      );
};
```

## Timer controller
from quiz app project
```js
import React from 'react'
import Timer from './Timer'
export default function TimerController({timeout, onTimeout, blocked, idx, shouldRender}) {
  return (
    <>
      {shouldRender ?  
            <Timer 
            key={idx+1} 
            timeout={timeout} 
            onTimeout={onTimeout} 
            blocked={blocked}
            /> : null }
    </>
  )
}
```

## Score controller
from quiz app project
```js
function Score({score}){
    return (
        <div className="score">
            <p>Score: {score}</p>
        </div>
        
    )
};

function ScoreController({score, shouldRender}){
    return (
        <>
        {shouldRender ? <Score score={score} /> : null}
        </>
    )
}

export {Score, ScoreController};
```

## Simple Summary
from quiz app project
```js
import LIST from "../../utils/list2";

function SimpleSummary({idx}){
    
    return (
        <>
        <span>Question {idx + 1} / {LIST.length}</span>
        </>
    )
};

export {SimpleSummary};
```

## PercentSummary
```js
function PercentSummary({answers, score}){

    let max = answers.length

    let correct = [...answers].filter((answer) => answer.isCorrect === true ).length;
    let correctPercent = Math.round((correct / max) * 100);

    let wrong = [...answers].filter((answer) => answer.isCorrect === false ).length;
    let wrongPercent = Math.round((wrong / max) * 100)

    let skipped = [...answers].filter((answer) => answer.isSkipped === true ).length;
    let skippedPercent = Math.round((skipped / max) * 100)
   
    return (
        <>
        <div className="percentSummary">
            <p>Score: {score}pt / {max}pt</p>
            <p className="correct">Correct: {correct} / {max} ({correctPercent}%)</p>
            <p className="wrong">Wrong: {wrong} / {max} ({wrongPercent}%)</p>
            <p className="skipped">Skipped: {skipped} / {max} ({skippedPercent}%)</p>
        </div>
        </>
    )
};

export {PercentSummary}
```

## PassedOrFailed
```js
import { useQuiz } from "../../context/quizcontext";

function PassedOrFailed({score}){
    const {passingScore} = useQuiz();

    const passed = (score >= passingScore);
    let message = passed ? `❎You passed!` : `You failed!`;

    return (
        <>
        <h3 className={passed ? 'passed' : 'failed'}>{message}</h3>
        <p className="minimum-to-pass">Minimum to pass the test is {passingScore}pt!</p>
        </>
    )
};

export {PassedOrFailed};
```