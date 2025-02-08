<?php
function bfsScan($directory) {
    $queue = [$directory]; // Kolejka katalogów do odwiedzenia

    while (!empty($queue)) {
        $currentDir = array_shift($queue); // Pobieramy pierwszy element kolejki
        echo "📂 Folder: " . $currentDir . "<br>";

        foreach (new DirectoryIterator($currentDir) as $file) {
            if (!$file->isDot()) {
                if ($file->isDir()) {
                    $queue[] = $file->getPathname(); // Dodajemy foldery do kolejki
                } else {
                    echo "📄 Plik: " . $file->getFilename() . "<br>";
                }
            }
        }
    }
}
bfsScan("files");
