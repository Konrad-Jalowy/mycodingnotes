//TBH I STILL ENCOUNTER CODE LIKE THIS EVERY NOW AND THEN SO I DECIDED TO NOTE THAT DOWN
//LOOKS LIKE WE BORROW THE CONSTRUCTOR (PRE-ES6 INHERITANCE) BUT ALSO NEED THAT INHERITS UTIL 
//SO THAT EVERYTHING WORKS OK

const util = require('node:util');
const EventEmitter = require('node:events');

function MyStream() {
  EventEmitter.call(this);
}

util.inherits(MyStream, EventEmitter);

MyStream.prototype.write = function(data) {
  this.emit('data', data);
};

const stream = new MyStream();

console.log(stream instanceof EventEmitter); // true
console.log(MyStream.super_ === EventEmitter); // true

stream.on('data', (data) => {
  console.log(`Received data: "${data}"`);
});
stream.write('It works!'); // Received data: "It works!" 