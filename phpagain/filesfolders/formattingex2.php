<?php 
$directory = "public/";
$files = scandir($directory);

echo "<table border='1'>";
echo "<tr><th>Plik</th><th>Rozmiar</th><th>Data modyfikacji</th></tr>";

foreach ($files as $file) {
    if ($file !== "." && $file !== "..") {
        $size = filesize($directory . $file);
        $modified = date("Y-m-d H:i:s", filemtime($directory . $file));
        echo "<tr><td>$file</td><td>$size B</td><td>$modified</td></tr>";
    }
}

echo "</table>";
