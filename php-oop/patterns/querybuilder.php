<?php


class QueryBuilder {
    private $collection;

    public function __construct(array $collection) {
        $this->collection = $collection;
    }

    public function where(callable $condition) {
        $this->collection = array_filter($this->collection, $condition);
        return $this;
    }

    public function select(callable $transform) {
        $this->collection = array_map($transform, $this->collection);
        return $this;
    }

    public function toArray() {
        return $this->collection;
    }

    public function first() {
        return reset($this->collection);
    }
}

// Przykład użycia
$data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

$query = new QueryBuilder($data);
$result = $query
    ->where(fn($x) => $x > 5)
    ->where(fn($x) => $x % 2 === 0)
    ->select(fn($x) => $x * 2)
    ->toArray();

print_r($result); // [12, 16, 20]