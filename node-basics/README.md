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
### write
write overwites
```js
var buff = Buffer.from("Hello World");

console.log(buff); //<Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64>
console.log(buff.toString()); //Hello World

buff.write("lorem ipsum") //write overwrites!

console.log(buff.toString()) //lorem ipsum
```

### concat buffers
just use concat
```js
var buff1 = Buffer.from("Hello World\n");
var buff2 = Buffer.from("Lorem ipsum");

var newBuffer = Buffer.concat([buff1, buff2]);

console.log(newBuffer.toString());
// Hello World
// Lorem ipsum
```

### buffer encoding
looks like we dont have to do that but still we can
```js
var buff = Buffer.from("Hello World ąźśćę", "utf8");

console.log(buff.toString()); 
```

## readstream
### readstream - data, end
```js
const fs = require('fs');
var stream = fs.createReadStream("./text.txt")

stream.on("data", function(chunk) {
    console.log(chunk.toString());
});

stream.on("end", function() {
    console.log("Reading finished");
});
```

### chunk size in KB
```js
const fs = require('fs');
var stream = fs.createReadStream("./docs1.txt")

stream.on("data", function(chunk) {
    console.log("Size: " + Math.round( (chunk.length / 1024) ) + "KB");
});

stream.on("end", function() {
    console.log("Reading finished");
});
```

### setting max chunk size for buffer in KB
```js
const fs = require('fs');

var stream = fs.createReadStream("./docs1.txt", {
    highWaterMark: 32 * 1024
});

stream.on("data", function(chunk) {
    console.log("Size: " + Math.round( (chunk.length / 1024) ) + "KB");
});

stream.on("end", function() {
    console.log("Reading finished");
});
```