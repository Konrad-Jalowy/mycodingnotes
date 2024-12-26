const fs = require('node:fs');

fs.rmdir('./emptydir', (err) => {
  if (err) throw err;
  console.log('directory removed');
}); 