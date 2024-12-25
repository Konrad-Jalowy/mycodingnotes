const fs = require('node:fs/promises');
const path = require("path");

const _path = path.join(__dirname, "textasyncawait.txt");

async function example() {
    try {
      const content = 'written using async await function';
      await fs.writeFile(_path, content);
      console.log("written successfully")
    } catch (err) {
      console.log(err);
    }
  }
example();