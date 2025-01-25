<?php 
$local = stream_socket_server("tcp://127.0.0.1:8000", $errno, $errstr);
if (!$local) {
    echo "Nie udało się otworzyć lokalnego socketu: $errstr ($errno)\n";
    exit(1);
}

while ($client = stream_socket_accept($local)) {
    $remote = stream_socket_client("tcp://example.com:80", $errno, $errstr);
    if ($remote) {
        // Logowanie żądań od klienta
        $request = stream_get_contents($client);
        file_put_contents("proxy.log", "Żądanie:\n" . $request . "\n", FILE_APPEND);

        // Przekazywanie żądania do serwera
        fwrite($remote, $request);

        // Odpowiedź serwera do klienta
        $response = stream_get_contents($remote);
        file_put_contents("proxy.log", "Odpowiedź:\n" . $response . "\n", FILE_APPEND);
        fwrite($client, $response);

        fclose($remote);
    }
    fclose($client);
}
