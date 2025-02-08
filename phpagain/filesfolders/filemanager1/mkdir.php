<?php
if (isset($_POST['folder_name'])) {
    $folderName = preg_replace('/[^a-zA-Z0-9_-]/', '', $_POST['folder_name']); // Bezpieczna nazwa folderu
    $path = "files/" . $folderName;

    if (!is_dir($path)) {
        mkdir($path, 0777, true);
        echo "✅ Folder został utworzony! <a href='index.php'>Powrót</a>";
    } else {
        echo "❌ Folder już istnieje!";
    }
}
?>
