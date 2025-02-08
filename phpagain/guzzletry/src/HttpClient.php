<?php

namespace App;

use GuzzleHttp\Client;

class HttpClient {
    private Client $client;

    public function __construct() {
        $this->client = new Client();
    }

    public function fetch(string $url): string {
        $response = $this->client->request('GET', $url);
        return $response->getBody()->getContents();
    }
}
