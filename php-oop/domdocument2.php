<?php

// Bazowa klasa węzła
abstract class Node {
    abstract public function render(int $indent = 0): string;
}

// Liść: Węzeł tekstowy
class TextNode extends Node {
    private string $text;

    public function __construct(string $text) {
        $this->text = $text;
    }

    public function render(int $indent = 0): string {
        return str_repeat(" ", $indent) . htmlspecialchars($this->text);
    }
}

// Kompozyt: Węzeł elementu
class ElementNode extends Node {
    private string $tag;
    private array $attributes = [];
    private array $children = [];

    public function __construct(string $tag) {
        $this->tag = $tag;
    }

    public function setAttribute(string $name, string $value): self {
        $this->attributes[$name] = $value;
        return $this; // Fluent Interface
    }

    public function addChild(Node $child): self {
        $this->children[] = $child;
        return $this; // Fluent Interface
    }

    public function render(int $indent = 0): string {
        $attrs = "";
        foreach ($this->attributes as $key => $value) {
            $attrs .= " {$key}=\"" . htmlspecialchars($value) . "\"";
        }

        $result = str_repeat(" ", $indent) . "<{$this->tag}{$attrs}>\n";
        foreach ($this->children as $child) {
            $result .= $child->render($indent + 2) . "\n";
        }
        $result .= str_repeat(" ", $indent) . "</{$this->tag}>";
        return $result;
    }
}

// Klasa zarządzająca dokumentem
class DOMDocument2 {
    private ?Node $root = null;

    public function createElement(string $tag): ElementNode {
        return new ElementNode($tag);
    }

    public function createTextNode(string $text): TextNode {
        return new TextNode($text);
    }

    public function setRoot(Node $root): self {
        $this->root = $root;
        return $this; // Fluent Interface
    }

    public function render(): string {
        if ($this->root === null) {
            return "";
        }
        return $this->root->render();
    }
}
$doc = new DOMDocument2();

$root = $doc->createElement("html");
$body = $doc->createElement("body")->setAttribute("class", "main-body");
$p = $doc->createElement("p")->setAttribute("id", "intro");
$text = $doc->createTextNode("Hello, World!");

$p->addChild($text);
$body->addChild($p);
$root->addChild($body);

$doc->setRoot($root);

echo $doc->render();
