const fs = require('node:fs');
const path = require("path");

const content = 'Some content!';
const _path = path.join(__dirname, "text.txt");

fs.writeFile(_path, content, err => {
  if (err) {
    console.error(err);
  } else {
    console.log("written successfully")
  }
});