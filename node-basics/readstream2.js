const fs = require('fs');
var stream = fs.createReadStream("./docs1.txt")


stream.on("data", function(chunk) {
    console.log("Size: " + Math.round( (chunk.length / 1024) ) + "KB");
});

stream.on("end", function() {
    console.log("Reading finished");
});