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
