<?php 
#[Attribute]
class ExampleAttribute {
    public function __construct(public string $info) {}
}

#[ExampleAttribute("This is an example class")]
class MyClass {}

$reflection = new ReflectionClass(MyClass::class);
$attributes = $reflection->getAttributes();

foreach ($attributes as $attribute) {
    $instance = $attribute->newInstance();
    echo $instance->info; // Wypisze: This is an example class
}

