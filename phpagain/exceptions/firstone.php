<?php class MyException extends Exception {}

try {
    throw new MyException("Coś poszło nie tak!");
} catch (MyException $e) {
    echo "Błąd: " . $e->getMessage();
}
