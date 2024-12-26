const fs = require('node:fs');

fs.unlink('./deleteme.txt', (err) => {
  if (err) throw err;
  console.log('file deleted');
}); 