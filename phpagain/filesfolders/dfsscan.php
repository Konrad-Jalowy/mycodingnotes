<?php
function dfsScan($directory, $depth = 0) {
    foreach (new DirectoryIterator($directory) as $file) {
        if (!$file->isDot()) {
            echo str_repeat("  ", $depth) . "📄 " . $file->getFilename() . "<br>";
            if ($file->isDir()) {
                dfsScan($file->getPathname(), $depth + 1); // REKURENCJA
            }
        }
    }
}
dfsScan("files");
