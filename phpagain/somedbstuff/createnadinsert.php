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

// create.php - Dodawanie użytkownika
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];

    // MySQLi Insert
    $stmt = $mysqli->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
    $stmt->bind_param("ss", $name, $email);
    $stmt->execute();
    $stmt->close();

    // PDO Insert
    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    $stmt->execute(['name' => $name, 'email' => $email]);
    
    echo "Użytkownik dodany!";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dodaj użytkownika</title>
</head>
<body>
    <h2>Dodaj nowego użytkownika</h2>
    <form method="post">
        Imię: <input type="text" name="name" required><br>
        Email: <input type="email" name="email" required><br>
        <button type="submit">Dodaj</button>
    </form>
</body>
</html>
