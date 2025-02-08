<?php
function deleteFolder($folderPath) {
    foreach (new DirectoryIterator($folderPath) as $file) {
        if (!$file->isDot()) {
            if ($file->isDir()) {
                deleteFolder($file->getPathname());
            } else {
                unlink($file->getPathname());
            }
        }
    }
    rmdir($folderPath);
}

$baseDirectory = "files/";

if (isset($_GET['file'])) {
    $file = $baseDirectory . basename($_GET['file']);

    if (file_exists($file) && is_file($file)) {
        unlink($file);
        echo "✅ Plik został usunięty! <a href='index.php'>Powrót</a>";
    } else {
        echo "❌ Plik nie istnieje!";
    }
}

if (isset($_GET['folder'])) {
    $folder = $baseDirectory . basename($_GET['folder']);

    if (is_dir($folder)) {
        deleteFolder($folder);
        echo "✅ Folder został usunięty! <a href='index.php'>Powrót</a>";
    } else {
        echo "❌ Folder nie istnieje!";
    }
}
?>
