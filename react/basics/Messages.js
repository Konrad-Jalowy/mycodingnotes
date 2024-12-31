function Messages({messages}){
    return (<ul className="messages-list">
        {messages.map((msg) => {
            const _time = new Date(msg.time);
            let _h = `${_time.getHours()}`.padStart(2, "0");
            let _m = `${_time.getMinutes()}`.padStart(2, "0");
            let _s = `${_time.getSeconds()}`.padStart(2, "0");
            const formattedTime = `${_h}:${_m}:${_s}`;
            return <li key={_time}><span className="time-badge">{formattedTime}</span> <span className="user-badge">{msg.name}</span><span className="message">{msg.message}</span></li>
        })}

    </ul>);
};

export {Messages};