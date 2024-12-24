const fs = require('fs');
var stream = fs.createReadStream("./text.txt")

stream.on("data", function(chunk) {
    console.log(chunk.toString());
});

stream.on("end", function() {
    console.log("Reading finished");
});