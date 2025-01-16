<?php

class JsonResponse {
    private int $statusCode;
    private array $headers;
    private array $data;

    public function __construct(int $statusCode = 200, array $data = [], array $headers = []) {
        $this->statusCode = $statusCode;
        $this->data = $data;
        $this->headers = $headers;

        // Set default headers for JSON response
        $this->headers['Content-Type'] = 'application/json';
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
        $this->data = $data;
    }

    // Get response data
    public function getData(): array {
        return $this->data;
    }

    // Send the JSON response
    public function send(): void {
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
$response->send();

?>