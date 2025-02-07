<?php
// config.php - Dane do bazy danych
$host = 'localhost';
$dbname = 'crud_php';
$username = 'root';
$password = '';

// MySQLi
$mysqli = new mysqli($host, $username, $password, $dbname);
if ($mysqli->connect_error) {
    die("Błąd połączenia z MySQLi: " . $mysqli->connect_error);
}

// PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Błąd połączenia z PDO: " . $e->getMessage());
}

// Tworzenie tabeli użytkowników (jeśli nie istnieje)
$createTableSQL = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
$mysqli->query($createTableSQL);
$pdo->exec($createTableSQL);

?>
