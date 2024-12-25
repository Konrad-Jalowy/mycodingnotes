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
### pipe stream to stdout
```js
const fs = require('fs');

var stream = fs.createReadStream("./docs1.txt", {
    highWaterMark: 32 * 1024
});

stream.pipe(process.stdout);
```

## Console
```js
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
```

## gzip
### gzip file in node
```js
const {
    createReadStream,
    createWriteStream,
  } = require('node:fs');
  const process = require('node:process');
  const { createGzip } = require('node:zlib');
  const { pipeline } = require('node:stream');
  
  const gzip = createGzip();
  const source = createReadStream('input.txt');
  const destination = createWriteStream('input.txt.gz');
  
  pipeline(source, gzip, destination, (err) => {
    if (err) {
      console.error('An error occurred:', err);
      process.exitCode = 1;
    }
  });
```

## body parsing
body parsing in node
```js
const http = require('node:http');

const server = http.createServer((req, res) => {
  // `req` is an http.IncomingMessage, which is a readable stream.
  // `res` is an http.ServerResponse, which is a writable stream.

  let body = '';
  // Get the data as utf8 strings.
  // If an encoding is not set, Buffer objects will be received.
  req.setEncoding('utf8');

  // Readable streams emit 'data' events once a listener is added.
  req.on('data', (chunk) => {
    body += chunk;
  });

  // The 'end' event indicates that the entire body has been received.
  req.on('end', () => {
    try {
      const data = JSON.parse(body);
      // Write back something interesting to the user:
      res.write(typeof data);
      res.end();
    } catch (er) {
      // uh oh! bad json!
      res.statusCode = 400;
      return res.end(`error: ${er.message}`);
    }
  });
});

server.listen(1337);

// $ curl localhost:1337 -d "{}"
// object
// $ curl localhost:1337 -d "\"foo\""
// string
// $ curl localhost:1337 -d "not json"
// error: Unexpected token 'o', "not json" is not valid JSON 
```

## Readline
### rl.write and rl.close
Always close, if not, code is blocked...
```js
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });

rl.write("Hello world");
rl.close();
```
### Readline question
```js
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });

rl.question('What do you think of Node.js? ', (answer) => {
  
  console.log(`Thank you for your valuable feedback: ${answer}`);

  rl.close();
});
```
### on line
writes hello world then repeats every line
```js
const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });

rl.write("Hello world\n");

rl.on('line', (input) => {
    console.log(`Received: ${input}`);
  }); 
```

## exists
checking if file exists
```js
const fs = require("fs");
const path = require("path");

fs.exists(path.join(__dirname, "docs1.txt"), function(exists) {

    if(exists) {
        console.log("File exists!");
    } else {
        console.log("File doesnt exist!");
    }

});

```

## stats of a file
### error-first
```js
const fs = require("fs");
const path = require("path");

fs.stat(path.join(__dirname, "docs1.txt"), function(err, stats) {

    if(err) {
        console.log(`Some error happened: ${err.message}.`);
        throw err;
    }

    console.log(`Created: ${stats.birthtime}`);
    console.log(`Last modified: ${stats.mtime}`);
    console.log(`isFile: ${stats.isFile()}`);
    console.log(`isDirectory: ${stats.isDirectory()}`);

});
```
### sync + try-catch
```js
const fs = require("fs");
const path = require("path");
try {
    var stats = fs.statSync(path.join(__dirname, "docs1.txt"));
    console.log(stats);
} catch(e) {
    console.log(`An error occurred: ${e.message}.`);
}
```

## readdir
```js
const fs = require("fs");
const path = require("path");


fs.readdir(__dirname, function(err, files) {

    if(err) {
        console.log(`An error occurred: ${err.message}.`);
    }

    files.forEach(function(filename) {

        fs.stat(path.join(__dirname, filename), function(err, stats) {

            if(err) {
                console.log(`An error occurred: ${err.message}.`);
            }

            console.log(`File ${filename}:`);
            console.log(`Created (year): ${stats.birthtime.getFullYear()}`);
            console.log("")

        });

    });

});

console.log("Readdir is async...");
```

## reading file with fs
example of error first callback
```js
const fs = require("fs");
const path = require("path");

fs.readFile(path.join(__dirname, "logs.txt"), "utf8", function(err, data) {
    if(err) 
        console.log(`An error occurred: ${err.message}.`);
    console.log(data);
});
```

## creating a directory
```js
const fs = require("fs");
const path = require("path");

fs.mkdir(path.join(__dirname, "files"), function(err) {
    if(err) {
        if(err.code === "EEXIST") {
            console.log("Directory already exists");
            return;
        }
        console.log(`Directory not created, an error occurred: ${err.message}.`);
    }
    console.log("Directory files created");
});
```

## writing files using fs module
### writing files sync
```js
const fs = require('node:fs');
const path = require("path");

const content = 'Some content sync!';
const _path = path.join(__dirname, "textsync.txt");

try {
    fs.writeFileSync(_path, content);
    console.log("written successfully")
  } catch (err) {
    console.error(err);
}
```
### writing files async (callback err first)
```js
const fs = require('node:fs');
const path = require("path");

const content = 'Some content!';
const _path = path.join(__dirname, "text.txt");

fs.writeFile(_path, content, err => {
  if (err) {
    console.error(err);
  } else {
    console.log("written successfully")
  }
});
```
### writing async/await using fs promises
```js
const fs = require('node:fs/promises');
const path = require("path");

const _path = path.join(__dirname, "textasyncawait.txt");

async function example() {
    try {
      const content = 'written using async await function';
      await fs.writeFile(_path, content);
      console.log("written successfully")
    } catch (err) {
      console.log(err);
    }
  }
example();
```
### appending to file (fs module)
```js
const fs = require('node:fs');
const content = 'Some content!';
fs.appendFile('logs.txt', content, err => {
  if (err) {
    console.error(err);
  } else {
    // done!
  }
});
```

### appending to file (async await fs promises)
```js
const fs = require('node:fs/promises');
async function appendToLogs() {
  try {
    const content = 'Some content via async/await!';
    await fs.appendFile('logs.txt', content);
  } catch (err) {
    console.log(err);
  }
}
appendToLogs();
```