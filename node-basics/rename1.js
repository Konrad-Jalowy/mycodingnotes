const fs = require('fs');
getCurrentFilenames();

// Rename the file 
fs.rename(
    'hello.txt',
    'world.txt',
    () => {
        console.log("\nFile Renamed!\n");
        getCurrentFilenames();
    });


function getCurrentFilenames() {
    console.log("Current filenames:");
    fs.readdirSync(__dirname)
        .forEach(file => {
            console.log(file);
        })
    }