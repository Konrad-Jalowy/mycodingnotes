<?php 
class ValidationException extends Exception {
    private array $errors;

    public function __construct(string $message, array $errors = [], int $code = 0, Throwable $previous = null) {
        parent::__construct($message, $code, $previous);
        $this->errors = $errors;
    }

    public function getErrors(): array {
        return $this->errors;
    }
}

try {
    throw new ValidationException("Dane są niepoprawne", ["email" => "Nieprawidłowy format"]);
} catch (ValidationException $e) {
    echo "Błąd walidacji: " . $e->getMessage() . "\n";
    print_r($e->getErrors());
}
