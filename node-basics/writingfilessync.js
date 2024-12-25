const fs = require('node:fs');
const path = require("path");

const content = 'Some content sync!';
const _path = path.join(__dirname, "textsync.txt");

try {
    fs.writeFileSync(_path, content);
    console.log("written successfully")
  } catch (err) {
    console.error(err);
}