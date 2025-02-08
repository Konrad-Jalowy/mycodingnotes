<?php
if (isset($_GET['file'])) {
    $file = "files/" . basename($_GET['file']);

    if (file_exists($file) && is_file($file)) {
        unlink($file);
        echo "✅ Plik został usunięty! <a href='index.php'>Powrót</a>";
    } else {
        echo "❌ Plik nie istnieje!";
    }
}
?>
