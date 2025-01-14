<?php

namespace Framework;

use PDO;
use PDOException;

class ORM
{
    private PDO $connection;

    public function __construct(string $dsn, string $username, string $password, array $options = [])
    {
        try {
            $this->connection = new PDO($dsn, $username, $password, $options);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new RuntimeException("Database connection error: " . $e->getMessage());
        }
    }

    public function find(string $table, int $id): ?array
    {
        $stmt = $this->connection->prepare("SELECT * FROM $table WHERE id = :id");
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        return $result ?: null;
    }

    public function findAll(string $table, array $conditions = []): array
    {
        $query = "SELECT * FROM $table";
        if (!empty($conditions)) {
            $placeholders = array_map(fn($key) => "$key = :$key", array_keys($conditions));
            $query .= " WHERE " . implode(" AND ", $placeholders);
        }
        $stmt = $this->connection->prepare($query);
        foreach ($conditions as $key => $value) {
            $stmt->bindValue(":$key", $value);
        }
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function insert(string $table, array $data): int
    {
        $columns = implode(", ", array_keys($data));
        $placeholders = implode(", ", array_map(fn($key) => ":$key", array_keys($data)));
        $query = "INSERT INTO $table ($columns) VALUES ($placeholders)";
        $stmt = $this->connection->prepare($query);
        foreach ($data as $key => $value) {
            $stmt->bindValue(":$key", $value);
        }
        $stmt->execute();
        return (int)$this->connection->lastInsertId();
    }

    public function update(string $table, int $id, array $data): bool
    {
        $placeholders = implode(", ", array_map(fn($key) => "$key = :$key", array_keys($data)));
        $query = "UPDATE $table SET $placeholders WHERE id = :id";
        $stmt = $this->connection->prepare($query);
        foreach ($data as $key => $value) {
            $stmt->bindValue(":$key", $value);
        }
        $stmt->bindValue(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    }

    public function delete(string $table, int $id): bool
    {
        $stmt = $this->connection->prepare("DELETE FROM $table WHERE id = :id");
        $stmt->bindValue(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    }
}

?>
