<?php
$targetDirectory = "files/";

if ($_FILES['file']['error'] === 0) {
    $targetFile = $targetDirectory . basename($_FILES["file"]["name"]);

    if (move_uploaded_file($_FILES["file"]["tmp_name"], $targetFile)) {
        echo "✅ Plik został przesłany! <a href='index.php'>Powrót</a>";
    } else {
        echo "❌ Błąd podczas przesyłania pliku.";
    }
} else {
    echo "❌ Wystąpił błąd podczas przesyłania pliku.";
}
?>
