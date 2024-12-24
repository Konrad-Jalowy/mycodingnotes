# node basics notes
Notes on basics of node js, its builtins and so on

## Events
### Emiting and listening
```js
const EventEmitter = require("events");

var emitter = new EventEmitter();

emitter.on("message", function(msg) {

    console.log("Message: " + msg);

});

emitter.emit("message", "Hello World!");
```

### Set max listeners
By default you can add 10 listeners. You can disable the limit
```js
var emitter = new EventEmitter();

emitter.setMaxListeners(0);
```

### Default number of listeners
They advise to use that approach
```js
require('events').EventEmitter.defaultMaxListeners = 15;
```
there are different opinios though...

## buffer
### Basics
```js
var buff = Buffer.from("Hello World");

console.log(buff); //<Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64>
console.log(buff.toString()); //Hello World
```