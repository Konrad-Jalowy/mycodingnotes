import { useState, useEffect } from "react";
import { Messages } from "./Messages";
import { EnterName } from "./EnterName";
import { UsrNames } from "./UsrNames";
import { UsrNumber } from "./UsrNumber";
import { SendMessage } from "./SendMessage";

function MessagesController({socket}){
    const [messages, setMessages] = useState([]);
    const [name, setName] = useState(null);

    useEffect(() => {
        socket.on("receive_message", (data) => {
          setMessages(prev => [...prev, data]);
        });
      }, [socket]);
      console.log(messages)

    let user_joined = false;
    if(name !== null){
        user_joined = true;
    }

    return (<div className="app-content">
    <h1>My Chat App</h1>
    {(!user_joined) && <EnterName socket={socket} setName={setName}/>}
    <div className="info-group">
        {(user_joined) && <p>Your name: {name}</p>}
        <UsrNumber socket={socket} />
        <UsrNames socket={socket} />
    </div>
    <Messages messages={messages} />
    {(user_joined) && <SendMessage socket={socket}/>}
    </div>
    );
};

export {MessagesController};