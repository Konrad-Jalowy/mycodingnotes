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

    public function createTable(string $table, array $columns): bool
    {
        $columnDefinitions = array_map(
            fn($name, $type) => "$name $type",
            array_keys($columns),
            $columns
        );
        $query = "CREATE TABLE IF NOT EXISTS $table (" . implode(", ", $columnDefinitions) . ", id INT AUTO_INCREMENT PRIMARY KEY)";
        return $this->connection->exec($query) !== false;
    }

    public function beginTransaction(): void
    {
        $this->connection->beginTransaction();
    }

    public function commit(): void
    {
        $this->connection->commit();
    }

    public function rollback(): void
    {
        $this->connection->rollBack();
    }
}

abstract class Model
{
    protected ORM $orm;
    protected string $table;

    public function __construct(ORM $orm)
    {
        $this->orm = $orm;
    }

    public function find(int $id): ?array
    {
        return $this->orm->find($this->table, $id);
    }

    public function findAll(array $conditions = []): array
    {
        return $this->orm->findAll($this->table, $conditions);
    }

    public function save(array $data): int
    {
        if (isset($data['id'])) {
            $this->orm->update($this->table, $data['id'], $data);
            return $data['id'];
        }
        return $this->orm->insert($this->table, $data);
    }

    public function delete(int $id): bool
    {
        return $this->orm->delete($this->table, $id);
    }

    public static function createTable(ORM $orm, array $columns): bool
    {
        $instance = new static($orm);
        return $orm->createTable($instance->table, $columns);
    }
}

?>