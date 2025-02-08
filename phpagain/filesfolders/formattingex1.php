<?php 
echo "<ul>";
foreach (scandir("public/") as $file) {
    if ($file !== "." && $file !== "..") {
        echo "<li><a href='public/$file'>$file</a></li>";
    }
}
echo "</ul>";
