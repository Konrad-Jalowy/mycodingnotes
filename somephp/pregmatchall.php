<?php
$pattern = '/\d+/';
$text = "Znajdź liczby 42 i 123 w tym tekście.";

preg_match_all($pattern, $text, $matches);
print_r($matches[0]);  // Output: Array ( [0] => 42 [1] => 123 )
?>

