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