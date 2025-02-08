<?php
function myExceptionHandler(Throwable $e) {
    echo "Wystąpił błąd: " . $e->getMessage();
}

set_exception_handler('myExceptionHandler');

throw new Exception("To jest testowy wyjątek!");
