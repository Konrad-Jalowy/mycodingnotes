<?php

namespace Framework;

use PDO;
use PDOException;

class ORM
{
    private PDO $connection;
    private string $table;
    private array $conditions = [];
    private array $orderBy = [];
    private int $limit = 0;
    private int $offset = 0;

    public function __construct(string $dsn, string $username, string $password, array $options = [])
    {
        try {
            $this->connection = new PDO($dsn, $username, $password, $options);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            throw new RuntimeException("Database connection error: " . $e->getMessage());
        }
    }

    public function table(string $table): self
    {
        $this->table = $table;
        $this->conditions = [];
        $this->orderBy = [];
        $this->limit = 0;
        $this->offset = 0;
        return $this;
    }

    public function where(string $column, string $operator, $value): self
    {
        $this->conditions[] = ["column" => $column, "operator" => $operator, "value" => $value];
        return $this;
    }

    public function orderBy(string $column, string $direction = "ASC"): self
    {
        $this->orderBy[] = "$column $direction";
        return $this;
    }

    public function limit(int $limit): self
    {
        $this->limit = $limit;
        return $this;
    }

    public function offset(int $offset): self
    {
        $this->offset = $offset;
        return $this;
    }

    public function get(): array
    {
        $query = "SELECT * FROM {$this->table}";

        if (!empty($this->conditions)) {
            $query .= " WHERE " . implode(" AND ", array_map(fn($cond) => "{$cond['column']} {$cond['operator']} :{$cond['column']}", $this->conditions));
        }

        if (!empty($this->orderBy)) {
            $query .= " ORDER BY " . implode(", ", $this->orderBy);
        }

        if ($this->limit > 0) {
            $query .= " LIMIT {$this->limit}";
        }

        if ($this->offset > 0) {
            $query .= " OFFSET {$this->offset}";
        }

        $stmt = $this->connection->prepare($query);
        foreach ($this->conditions as $cond) {
            $stmt->bindValue(":" . $cond['column'], $cond['value']);
        }

        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function first(): ?array
    {
        $this->limit(1);
        $result = $this->get();
        return $result[0] ?? null;
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
        return $this->orm->table($this->table)->where('id', '=', $id)->first();
    }

    public function findAll(array $conditions = []): array
    {
        $query = $this->orm->table($this->table);
        foreach ($conditions as $column => $value) {
            $query->where($column, '=', $value);
        }
        return $query->get();
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
