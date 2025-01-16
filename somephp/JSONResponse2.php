<?php

class JsonResponse {
    private int $statusCode;
    private array $headers;
    private array $data;
    private bool $logEnabled = false;
    private string $logFile = __DIR__ . '/json_response.log';


    public function __construct(int $statusCode = 200, array $data = [], array $headers = []) {
        $this->statusCode = $statusCode;
        $this->data = $data;
        $this->headers = $headers;

        // Set default headers for JSON response
        $this->headers['Content-Type'] = 'application/json';
        $this->validateData($data);
    }

    // Validate JSON data
    private function validateData(array $data): void {
        if (json_encode($data) === false) {
            throw new InvalidArgumentException('Invalid data: unable to encode to JSON');
        }
    }

    // Set the HTTP status code
    public function setStatusCode(int $statusCode): void {
        $this->statusCode = $statusCode;
    }

    // Get the HTTP status code
    public function getStatusCode(): int {
        return $this->statusCode;
    }

    // Add or update a header
    public function setHeader(string $key, string $value): void {
        $this->headers[$key] = $value;
    }

    // Get all headers
    public function getHeaders(): array {
        return $this->headers;
    }

    // Set response data
    public function setData(array $data): void {
        $this->validateData($data);
        $this->data = $data;
    }

    // Get response data
    public function getData(): array {
        return $this->data;
    }

    // Enable CORS
    public function enableCORS(string $origin = '*', string $methods = 'GET, POST, PUT, DELETE', string $headers = 'Content-Type, Authorization'): void {
        $this->setHeader('Access-Control-Allow-Origin', $origin);
        $this->setHeader('Access-Control-Allow-Methods', $methods);
        $this->setHeader('Access-Control-Allow-Headers', $headers);
    }

    // Enable logging
    public function enableLogging(string $logFile = null): void {
        $this->logEnabled = true;
        if ($logFile) {
            $this->logFile = $logFile;
        }
    }

    private function logResponse(): void {
        if ($this->logEnabled) {
            file_put_contents($this->logFile, json_encode([
                'statusCode' => $this->statusCode,
                'headers' => $this->headers,
                'data' => $this->data
            ]) . PHP_EOL, FILE_APPEND);
        }
    }

    // Send the JSON response
    public function send(): void {
        // Log response if enabled
        $this->logResponse();

        // Set the HTTP status code
        http_response_code($this->statusCode);

        // Set headers
        foreach ($this->headers as $key => $value) {
            header("$key: $value");
        }

        // Send JSON-encoded data
        echo json_encode($this->data);
    }
}

// Example usage
$response = new JsonResponse(200, [
    'success' => true,
    'message' => 'Operation successful',
    'data' => [
        'id' => 1,
        'name' => 'Example'
    ]
]);
$response->enableCORS();
$response->enableLogging();
$response->send();

?>
