<?php

class BookCollection implements Iterator {
    private $books = [];
    private $index = 0;

    public function addBook(string $book) {
        $this->books[] = $book;
    }

    // Iterator methods
    public function current(): string {
        return $this->books[$this->index];
    }

    public function key(): int {
        return $this->index;
    }

    public function next(): void {
        $this->index++;
    }

    public function rewind(): void {
        $this->index = 0;
    }

    public function valid(): bool {
        return isset($this->books[$this->index]);
    }
}

// Użycie wzorca Iterator
$collection = new BookCollection();
$collection->addBook("1984");
$collection->addBook("Brave New World");
$collection->addBook("Fahrenheit 451");

foreach ($collection as $book) {
    echo $book . PHP_EOL;
}
