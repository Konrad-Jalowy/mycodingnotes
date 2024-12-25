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