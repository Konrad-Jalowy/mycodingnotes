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
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['create'])) {
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

// update.php - Edycja użytkownika
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update'])) {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $email = $_POST['email'];

    // MySQLi Update
    $stmt = $mysqli->prepare("UPDATE users SET name = ?, email = ? WHERE id = ?");
    $stmt->bind_param("ssi", $name, $email, $id);
    $stmt->execute();
    $stmt->close();

    // PDO Update
    $stmt = $pdo->prepare("UPDATE users SET name = :name, email = :email WHERE id = :id");
    $stmt->execute(['name' => $name, 'email' => $email, 'id' => $id]);
    
    echo "Dane użytkownika zaktualizowane!";
}

// Pobranie danych użytkownika do edycji
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
    $stmt->execute(['id' => $id]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Lista użytkowników</title>
</head>
<body>
    <h2>Lista użytkowników</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Imię</th>
            <th>Email</th>
            <th>Data dodania</th>
            <th>Akcje</th>
        </tr>
        <?php
        $result = $mysqli->query("SELECT * FROM users");
        while ($row = $result->fetch_assoc()) {
            echo "<tr>"
                . "<td>" . $row['id'] . "</td>"
                . "<td>" . $row['name'] . "</td>"
                . "<td>" . $row['email'] . "</td>"
                . "<td>" . $row['created_at'] . "</td>"
                . "<td><a href='?id=" . $row['id'] . "'>Edytuj</a></td>"
            . "</tr>";
        }
        ?>
    </table>
    
    <?php if (isset($user)) { ?>
    <h2>Edytuj użytkownika</h2>
    <form method="post">
        <input type="hidden" name="id" value="<?php echo $user['id']; ?>">
        Imię: <input type="text" name="name" value="<?php echo $user['name']; ?>" required><br>
        Email: <input type="email" name="email" value="<?php echo $user['email']; ?>" required><br>
        <button type="submit" name="update">Zapisz zmiany</button>
    </form>
    <?php } ?>
    
    <h2>Dodaj nowego użytkownika</h2>
    <form method="post">
        Imię: <input type="text" name="name" required><br>
        Email: <input type="email" name="email" required><br>
        <button type="submit" name="create">Dodaj</button>
    </form>
</body>
</html>
