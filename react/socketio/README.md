# React socketio
React + socketio notes

## How to connect
```js
import './App.css';
import io from "socket.io-client";
import {  useRef } from "react";
import { MessagesController } from './components/MessagesController';


function App() {

  
  const socket = useRef(null);

  if(socket.current === null){
    socket.current = io.connect("http://localhost:3001");
  }

  return (
    <div className="App">
      <MessagesController socket={socket.current}/>
    </div>
  );
}

export default App;
```