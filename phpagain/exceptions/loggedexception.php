<?php
class LoggedException extends Exception {
    public function __construct($message, $code = 0, Throwable $previous = null) {
        parent::__construct($message, $code, $previous);
        $this->logError();
    }

    private function logError(): void {
        file_put_contents("error_log.txt", "[" . date('Y-m-d H:i:s') . "] " . $this->getMessage() . "\n", FILE_APPEND);
    }
}
throw new LoggedException("Coś poszło nie tak!");
