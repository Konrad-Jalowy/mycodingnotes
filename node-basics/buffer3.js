var buff1 = Buffer.from("Hello World\n");
var buff2 = Buffer.from("Lorem ipsum");

var newBuffer = Buffer.concat([buff1, buff2]);

console.log(newBuffer.toString());
// Hello World
// Lorem ipsum