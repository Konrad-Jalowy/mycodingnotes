const fs = require('fs');
getCurrentFilenames();

function getCurrentFilenames() {
    console.log("Current filenames:");
    fs.readdirSync(__dirname)
        .forEach(file => {
            console.log(file);
        });
}
