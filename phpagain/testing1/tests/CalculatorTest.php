<?php

use PHPUnit\Framework\TestCase;
use App\Utils\Calculator;

class CalculatorTest extends TestCase {
    public function testAddition() {
        $calc = new Calculator();
        $this->assertEquals(5, $calc->add(2, 3));
        $this->assertEquals(0, $calc->add(-1, 1));
    }
}
