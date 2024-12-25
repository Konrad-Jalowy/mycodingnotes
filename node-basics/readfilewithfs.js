const fs = require("fs");
const path = require("path");

fs.readFile(path.join(__dirname, "logs.txt"), "utf8", function(err, data) {
    if(err) 
        console.log(`An error occurred: ${err.message}.`);
    console.log(data);
});