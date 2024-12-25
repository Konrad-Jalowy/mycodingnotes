const fs = require('node:fs');
const content = 'Some content!';
fs.appendFile('logs.txt', content, err => {
  if (err) {
    console.error(err);
  } else {
    // done!
  }
});