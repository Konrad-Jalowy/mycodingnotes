<?php 
$pdo = new PDO("mysql:host=localhost;dbname=users_db", "root", "");

// Wywołanie procedury składowanej
$stmt = $pdo->prepare("CALL GetUserOrders(:userId)");
$stmt->bindParam(':userId', $userId, PDO::PARAM_INT);

$userId = 1; // Pobieramy zamówienia dla użytkownika o ID 1
$stmt->execute();

// Pobieranie wyników
$orders = $stmt->fetchAll(PDO::FETCH_ASSOC);
print_r($orders);
