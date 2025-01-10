<?php

abstract class Handler
{
    protected ?Handler $nextHandler;

    public function __construct(?Handler $nextHandler = null)
    {
        $this->nextHandler = $nextHandler;
    }

    public function handle(array $request)
    {
        if ($this->nextHandler) {
            return $this->nextHandler->handle($request);
        }
        return null;
    }
}

class AuthHandler extends Handler
{
    public function handle(array $request)
    {
        if (!empty($request['authenticated'])) {
            echo "AuthHandler: User authenticated.\n";
            return parent::handle($request);
        } else {
            echo "AuthHandler: Authentication failed.\n";
            return "403 Forbidden";
        }
    }
}

class LoggingHandler extends Handler
{
    public function handle(array $request)
    {
        echo "LoggingHandler: Logging request: " . json_encode($request) . "\n";
        return parent::handle($request);
    }
}

class DataValidationHandler extends Handler
{
    public function handle(array $request)
    {
        if (!empty($request['data'])) {
            echo "DataValidationHandler: Data validated.\n";
            return parent::handle($request);
        } else {
            echo "DataValidationHandler: Invalid data.\n";
            return "400 Bad Request";
        }
    }
}

// Tworzenie łańcucha
$chain = new AuthHandler(
    new LoggingHandler(
        new DataValidationHandler()
    )
);

// Testowanie żądań
$request = ["authenticated" => true, "data" => "Valid payload"];
echo $chain->handle($request) . "\n\n";

$request = ["authenticated" => false, "data" => "Valid payload"];
echo $chain->handle($request) . "\n";