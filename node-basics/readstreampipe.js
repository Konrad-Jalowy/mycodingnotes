const fs = require('fs');

var stream = fs.createReadStream("./docs1.txt", {
    highWaterMark: 32 * 1024
});

stream.pipe(process.stdout);