<?php 
function myErrorHandler($errno, $errstr, $errfile, $errline) {
    throw new ErrorException($errstr, $errno, 0, $errfile, $errline);
}

function myExceptionHandler(Throwable $e) {
    echo "Wystąpił problem: " . $e->getMessage();
}

set_error_handler("myErrorHandler");
set_exception_handler("myExceptionHandler");

echo notExistingFunction(); // Wywoła Error
