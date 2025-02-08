<?php
$directory = new RecursiveDirectoryIterator("src/");
$iterator = new RecursiveIteratorIterator($directory);

foreach ($iterator as $file) {
    if ($file->isFile()) {
        echo $file->getPathname() . "<br>";
    }
}
