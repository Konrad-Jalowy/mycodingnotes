<?php 
$stmt = $pdo->prepare("CALL GetUserOrderCount(:userId, @orderCount)");
$stmt->bindParam(':userId', $userId, PDO::PARAM_INT);
$userId = 1;
$stmt->execute();

// Pobranie wartości zwracanej przez procedurę
$result = $pdo->query("SELECT @orderCount")->fetch(PDO::FETCH_ASSOC);
echo "Liczba zamówień: " . $result["@orderCount"];
