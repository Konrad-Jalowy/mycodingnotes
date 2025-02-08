<?php
function dfsScanIterative($directory) {
    $stack = [$directory]; // Stos przechowujący katalogi do odwiedzenia

    while (!empty($stack)) {
        $currentDir = array_pop($stack); // Pobieramy ostatni katalog ze stosu
        echo "📂 Folder: " . $currentDir . "<br>";

        foreach (new DirectoryIterator($currentDir) as $file) {
            if (!$file->isDot()) {
                if ($file->isDir()) {
                    $stack[] = $file->getPathname(); // Dodajemy folder na stos
                } else {
                    echo "📄 Plik: " . $file->getFilename() . "<br>";
                }
            }
        }
    }
}
dfsScanIterative("files");
