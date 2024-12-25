const fs = require('node:fs/promises');
async function appendToLogs() {
  try {
    const content = 'Some content via async/await!';
    await fs.appendFile('logs.txt', content);
  } catch (err) {
    console.log(err);
  }
}
appendToLogs();