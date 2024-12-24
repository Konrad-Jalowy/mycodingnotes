const fs = require("fs");
const Console = require("console").Console;

var logs = fs.createWriteStream("./logs.txt");
var errors = fs.createWriteStream("./errors.txt");

const myConsole = new Console(logs, errors);

myConsole.log("hello world");
myConsole.log(`2 + 2 = ${2 + 2}`);
myConsole.error("error");
const count = 5;
myConsole.log('count: %d', count);