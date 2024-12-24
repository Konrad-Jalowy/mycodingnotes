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