<?php
$files = glob("public/*.php");

foreach ($files as $file) {
    echo basename($file) . "<br>";
}
