<?php
namespace App;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;

class HttpClient {
    private Client $client;

    public function __construct() {
        $this->client = new Client();
    }

    public function fetch(string $url): string {
        try {
            $response = $this->client->request('GET', $url);
            return $response->getBody()->getContents();
        } catch (RequestException $e) {
            return "Błąd: " . $e->getMessage();
        }
    }

    public function post(string $url, array $data): string {
        try {
            $response = $this->client->request('POST', $url, [
                'json' => $data
            ]);
            return $response->getBody()->getContents();
        } catch (RequestException $e) {
            return "Błąd: " . $e->getMessage();
        }
    }

    public function put(string $url, array $data): string {
        try {
            $response = $this->client->request('PUT', $url, [
                'json' => $data
            ]);
            return $response->getBody()->getContents();
        } catch (RequestException $e) {
            return "Błąd: " . $e->getMessage();
        }
    }
}
