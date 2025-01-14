<?php

interface Expression {
    public function interpret(): int;
}

class Number implements Expression {
    private $value;

    public function __construct(int $value) {
        $this->value = $value;
    }

    public function interpret(): int {
        return $this->value;
    }
}

class Add implements Expression {
    private $left;
    private $right;

    public function __construct(Expression $left, Expression $right) {
        $this->left = $left;
        $this->right = $right;
    }

    public function interpret(): int {
        return $this->left->interpret() + $this->right->interpret();
    }
}

class Subtract implements Expression {
    private $left;
    private $right;

    public function __construct(Expression $left, Expression $right) {
        $this->left = $left;
        $this->right = $right;
    }

    public function interpret(): int {
        return $this->left->interpret() - $this->right->interpret();
    }
}

// Przykład użycia
$expr = new Add(new Number(5), new Subtract(new Number(10), new Number(2)));
echo $expr->interpret(); // Output: 13
?>