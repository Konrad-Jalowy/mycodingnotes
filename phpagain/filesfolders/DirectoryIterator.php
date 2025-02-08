<?php
$directory = new DirectoryIterator("public/");

foreach ($directory as $file) {
    if ($file->isFile()) {
        echo $file->getFilename() . "<br>";
    }
}
