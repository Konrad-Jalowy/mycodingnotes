const fs = require('node:fs');

fs.rmdir('./somedir', {recursive: true}, (err) => {
  if (err) throw err;
  console.log('directory removed');
}); 