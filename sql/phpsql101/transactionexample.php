<?php
$pdo = new PDO("mysql:host=localhost;dbname=users_db", "root", "");

// Rozpoczynamy transakcję
$pdo->beginTransaction();

try {
    // Dodajemy zamówienie
    $stmt = $pdo->prepare("INSERT INTO orders (user_id, total_price) VALUES (?, ?)");
    $stmt->execute([1, 250.00]);

    // Aktualizujemy stan magazynowy
    $stmt = $pdo->prepare("UPDATE products SET stock = stock - 1 WHERE product_id = ?");
    $stmt->execute([5]);

    // Jeśli wszystko się udało, zatwierdzamy transakcję
    $pdo->commit();
    echo "Zamówienie zostało dodane!";
} catch (Exception $e) {
    // Jeśli był błąd, cofamy zmiany
    $pdo->rollback();
    echo "Błąd: " . $e->getMessage();
}
