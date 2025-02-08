<?php
$client = new Client();

$response = $client->request('POST', 'https://jsonplaceholder.typicode.com/posts', [
    'json' => [
        'title' => 'Nowy post',
        'body' => 'Treść posta',
        'userId' => 1
    ]
]);

echo $response->getBody();
