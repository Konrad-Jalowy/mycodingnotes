<?php
$expression = "3 + 5 * (2 - 8)";
preg_match_all('/\d+|\+|\-|\*|\/|\(|\)/', $expression, $tokens);
print_r($tokens[0]); // ['3', '+', '5', '*', '(', '2', '-', '8', ')']
?>

