import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Uzyskanie katalogu bieżącego pliku (dla ESM)
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Katalog do monitorowania
const directoryToWatch = path.join(__dirname, 'watched_folder');

// Plik do logowania zmian
const logFile = path.join(__dirname, 'file_changes.log');

// Upewnij się, że katalog istnieje
if (!fs.existsSync(directoryToWatch)) {
  fs.mkdirSync(directoryToWatch);
  console.log(`Utworzono katalog: ${directoryToWatch}`);
}

// Funkcja logująca zmiany do pliku
function logToFile(message) {
  const timestamp = new Date().toISOString();
  const logMessage = `[${timestamp}] ${message}\n`;

  fs.promises
    .appendFile(logFile, logMessage)
    .catch((err) => console.error('Błąd zapisu do pliku:', err));
}

// Watcher plików
console.log(`Monitorowanie katalogu: ${directoryToWatch}`);
fs.watch(directoryToWatch, (eventType, filename) => {
  if (filename) {
    const fullPath = path.join(directoryToWatch, filename);

    // Sprawdź, czy plik istnieje (dla nowych plików)
    fs.promises
      .stat(fullPath)
      .then((stats) => {
        if (eventType === 'rename' && stats.isFile()) {
          console.log(`Dodano nowy plik: ${filename}`);
          logToFile(`Dodano nowy plik: ${filename}`);
        } else if (eventType === 'change') {
          console.log(`Zmodyfikowano plik: ${filename}`);
          logToFile(`Zmodyfikowano plik: ${filename}`);
        }
      })
      .catch((err) => {
        if (err.code === 'ENOENT') {
          console.log(`Usunięto plik: ${filename}`);
          logToFile(`Usunięto plik: ${filename}`);
        } else {
          console.error('Błąd sprawdzania pliku:', err);
        }
      });
  } else {
    console.log('Nieznana zmiana w katalogu');
  }
});
