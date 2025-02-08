<?php

require 'vendor/autoload.php';

use App\HttpClient;

$client = new HttpClient();

// 1️⃣ Pobieranie danych (GET)
$responseGet = $client->fetch('https://jsonplaceholder.typicode.com/posts/1');
echo "<h2>📥 Pobranie posta (GET)</h2>";
echo "<pre>" . print_r(json_decode($responseGet, true), true) . "</pre>";

// 2️⃣ Wysyłanie nowego posta (POST)
$newPostData = [
    'title' => 'Mój nowy post',
    'body' => 'Treść nowego posta',
    'userId' => 123
];

$responsePost = $client->post('https://jsonplaceholder.typicode.com/posts', $newPostData);
echo "<h2>📤 Tworzenie posta (POST)</h2>";
echo "<pre>" . print_r(json_decode($responsePost, true), true) . "</pre>";

// 3️⃣ Aktualizacja posta (PUT)
$updateData = [
    'title' => 'Zaktualizowany tytuł',
    'body' => 'Nowa treść posta'
];

$responsePut = $client->put('https://jsonplaceholder.typicode.com/posts/1', $updateData);
echo "<h2>🔄 Aktualizacja posta (PUT)</h2>";
echo "<pre>" . print_r(json_decode($responsePut, true), true) . "</pre>";