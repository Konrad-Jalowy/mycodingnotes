const fs = require("fs");
const path = require("path");
try {
    var stats = fs.statSync(path.join(__dirname, "docs1.txt"));
    console.log(stats);
} catch(e) {
    console.log(`An error occurred: ${e.message}.`);
}