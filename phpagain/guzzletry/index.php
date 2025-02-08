<?php

require 'vendor/autoload.php';

use App\HttpClient;

$client = new HttpClient();
$response = $client->fetch('https://jsonplaceholder.typicode.com/posts/1');

echo "<pre>";
print_r(json_decode($response, true));
echo "</pre>";
