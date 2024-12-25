const fs = require("fs");
const path = require("path");

fs.exists(path.join(__dirname, "docs1.txt"), function(exists) {

    if(exists) {
        console.log("File exists!");
    } else {
        console.log("File doesnt exist!");
    }

});
