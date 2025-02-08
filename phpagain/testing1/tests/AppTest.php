<?php

use PHPUnit\Framework\TestCase;
use App\App;

class AppTest extends TestCase {
    public function testRun() {
        $app = new App();
        $this->assertEquals("Hello from App!", $app->run());
    }
}
