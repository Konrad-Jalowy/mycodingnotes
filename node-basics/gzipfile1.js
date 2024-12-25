const {
    createReadStream,
    createWriteStream,
  } = require('node:fs');
  const process = require('node:process');
  const { createGzip } = require('node:zlib');
  const { pipeline } = require('node:stream');
  
  const gzip = createGzip();
  const source = createReadStream('input.txt');
  const destination = createWriteStream('input.txt.gz');
  
  pipeline(source, gzip, destination, (err) => {
    if (err) {
      console.error('An error occurred:', err);
      process.exitCode = 1;
    }
  });