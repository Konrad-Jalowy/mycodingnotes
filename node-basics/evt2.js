const EventEmitter = require("events");

var emitter = new EventEmitter();

emitter.setMaxListeners(0);

emitter.on("message", function(msg) {

    console.log("Message: " + msg);

});

emitter.emit("message", "Hello World!");