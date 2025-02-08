<?php 
class FileReadException extends Exception {
    public function __construct($message, Throwable $previous = null) {
        parent::__construct($message, 0, $previous);
    }
}

try {
    try {
        throw new Exception("Błąd dostępu do pliku!");
    } catch (Exception $e) {
        throw new FileReadException("Nie można wczytać pliku", $e);
    }
} catch (FileReadException $e) {
    echo "Błąd pliku: " . $e->getMessage() . "\n";
    echo "Oryginalny błąd: " . $e->getPrevious()->getMessage() . "\n";
}
