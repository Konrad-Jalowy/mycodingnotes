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

## Clickable summary
from quiz app project
```js
import { useState, useRef } from "react";
import { SkippedAnswer } from "./answers/SkippedAnswer";
import { WrongAnswer } from "./answers/WrongAnswer";
import { CorrectAnswer } from "./answers/CorrectAnswer";
import LIST from "../../utils/list2";
function ClickableSummary({answers}){

    const [index, setIndex] = useState(0);
    const answer = useRef(null);
    const maxIndex = LIST.length - 1;

    function nextClickHandler(){
        setIndex(p => p + 1);
    }

    function prevClickHandler(){
        setIndex(p => p - 1);
    }

    answer.current = answers[index];
    console.log(answer.current);


    return (
        <>
        {answer.current.isSkipped && <SkippedAnswer idx={index} /> }
        {answer.current.isCorrect && <CorrectAnswer idx={index}/>}
        {(answer.current.isCorrect === false) && <WrongAnswer idx={index} chosen={answer.current.chosenAnswer}/>}
        <div className="summaryButtons">
        <button onClick={prevClickHandler} disabled={index === 0}>Previous</button>
        <button onClick={nextClickHandler} disabled={index === maxIndex}>Next</button>
        </div>
        </>
    )
};

export {ClickableSummary};
```

## Correct answer
from quiz app project
```js
import LIST from "../../../utils/list2";

function CorrectAnswer({idx}){
    let answersRaw = LIST[idx].answers;
    let answers = [...Object.entries(answersRaw)];
    let correctOne = LIST[idx].correct;
    return (
        <>
        <div className="summaryHeading">
        <h3><span className="index-correct">Question {idx+1}: </span> <em>{LIST[idx].question}</em></h3>
        <h5 className="good">❎Good answer!</h5>
        </div>
        
        <ul className="answersListSummary">
            {answers.map(([key, val]) => {
                return <li key={key} className={key === correctOne ? "correct-one chosen-one" : ""}>{val}</li>
            })}
        </ul>
        </>
    );
};

export {CorrectAnswer};
```

## Skipped answer
```js
import LIST from "../../../utils/list2";

function SkippedAnswer({idx}){
    let answersRaw = LIST[idx].answers;
    let answers = [...Object.entries(answersRaw)];
    let correctOne = LIST[idx].correct;
    return (
        <>
        <div className="summaryHeading">
        <h3><span className="index-skipped">Question {idx+1}: </span> <em>{LIST[idx].question}</em></h3>
        <h5 className="skipped">∅ You skipped!</h5>
        </div>
        
        <ul className="answersListSummary">
            {answers.map(([key, val]) => {
                return (<li 
                    key={key} 
                    className={key === correctOne ? "correct-one" : ""}>{val}</li>)
            })}
        </ul>
        </>
    );
};

export {SkippedAnswer};
```

## WrongAnswer
from quiz app project
```js
import LIST from "../../../utils/list2";

function WrongAnswer({idx, chosen}){
    let answersRaw = LIST[idx].answers;
    let answers = [...Object.entries(answersRaw)];
    console.log(answers);
    let correctOne = LIST[idx].correct;
    return (
        <>
        <div className="summaryHeading">
        <h3><span className="index-wrong">Question {idx+1}: </span><em>{LIST[idx].question}</em></h3>
        <h5 className="wrong">&#10060;Wrong answer!</h5>
        </div>
        
        <ul className="answersListSummary">
            {answers.map(([key, val]) => {
                console.log(key, val);
                if(key === chosen){
                    return <li key={key} className="wrong-one chosen-one">{val}</li> 
                }
                return <li key={key} className={key === correctOne ? "correct-one" : ""}>{val}</li>
            })}
        </ul>
        </>
    );
}

export {WrongAnswer};
```

## AnswersList
from quiz app project
```js
import { useRef, useState, useEffect } from "react";
import LIST from "../../utils/list2";
import './AnswersList.css';
import { SimpleSummary } from "../summary/SimpleSummary";
function AnswersList({idx, shuffle, setNextQuestion, skipQuestion, setTimerBlocked, showCorrect}){

    const answers = useRef(null);

    const correct = useRef(null);

    const chosenAnswerRef = useRef(null);

    const [mode, setMode] = useState(null);
    
    if(correct.current === null){
        correct.current = LIST[idx].correct;
    }

    if(answers.current === null){

        const rawAnswers = LIST[idx].answers;
        const readyAnswers = [...Object.entries(rawAnswers)];

        if(shuffle){
            readyAnswers.sort(() => Math.random() - 0.5);
        }
        answers.current = [...readyAnswers];
    }

    useEffect(() => {
        let timer;
        switch(mode){
            case null:
                break;
            case 'chosen':
                chosenAnswerRef.current.className = 'selectedAnswer';
                if(showCorrect === false){
                    setTimerBlocked(true);
                    timer = setTimeout(() => {
                        setNextQuestion(chosenAnswerRef.current.dataset.idx);
                    },700)
                    break;
                }
                
                setMode('waiting');
                setTimerBlocked(true);
                break;
            case 'waiting':
                timer = setTimeout(() => {
                let cls = chosenAnswerRef.current.dataset.idx === correct.current ? 'correctAnswer' : 'wrongAnswer';
                chosenAnswerRef.current.className = cls;
                setMode('feedbackSent')
                },2000);
                break;
            case 'feedbackSent':
                timer = setTimeout(() => {
                    setNextQuestion(chosenAnswerRef.current.dataset.idx);
                },1000);
                break;
            default:
                break;
        }

        return () => {
            clearTimeout(timer);
          };

    }, [mode, setNextQuestion, setTimerBlocked, showCorrect]);


    function handleClick(e){
        if(chosenAnswerRef.current === null){
            chosenAnswerRef.current = e.target;
            setMode('chosen');
        }
    }
    

    return (
        <> 
            <ul className="answersList">
            {answers.current.map((item) => {
                const [key,value] = item;
               return (
               <li 
               key={key} 
               data-idx={key} 
               onClick={(e) => handleClick(e)}
               className={mode === null ? 'hoverable' : ''}
               >{value}</li>)
            })}
            </ul>
            <div className="answersControls">
            <button 
            disabled={mode !== null}
            onClick={() => skipQuestion()}
            >Skip</button>
            <SimpleSummary idx={idx} />
            </div>
            
        </>
    );
}

export {AnswersList};
```