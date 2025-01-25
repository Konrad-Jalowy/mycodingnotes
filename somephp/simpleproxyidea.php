<?php

if (!isset($_GET['url'])) {
    die("Podaj URL w formularzu.");
}

// Pobieranie URL-a z formularza
$url = $_GET['url'];

// Walidacja URL-a
if (!filter_var($url, FILTER_VALIDATE_URL)) {
    die("Nieprawidłowy URL.");
}

// Pobieranie zawartości strony
$response = file_get_contents($url);
if ($response === false) {
    die("Nie udało się pobrać strony: $url");
}

// Funkcja do modyfikacji linków w HTML-u
function modify_links($html, $proxy_url) {
    // Przerabiamy linki <a href="..."> na wersję przez proxy
    $html = preg_replace_callback(
        '/<a\s+href="([^"]+)"/i',
        function ($matches) use ($proxy_url) {
            $original_link = $matches[1];
            $proxy_link = $proxy_url . '?url=' . urlencode($original_link);
            return '<a href="' . $proxy_link . '"';
        },
        $html
    );

    // Przerabiamy obrazki <img src="..."> na wersję przez proxy
    $html = preg_replace_callback(
        '/<img\s+src="([^"]+)"/i',
        function ($matches) use ($proxy_url) {
            $original_src = $matches[1];
            $proxy_src = $proxy_url . '?url=' . urlencode($original_src);
            return '<img src="' . $proxy_src . '"';
        },
        $html
    );

    return $html;
}

// Modyfikujemy zawartość strony
$proxy_url = "http://127.0.0.1:8000/index.php"; // URL proxy
$modified_html = modify_links($response, $proxy_url);

// Wyświetlamy zmodyfikowaną stronę
echo $modified_html;
