<?php

// Produkt
interface Button {
    public function render(): string;
}

// Konkretne produkty
class WebButton implements Button {
    public function render(): string {
        return "<button>Web Button</button>";
    }
}

class DesktopButton implements Button {
    public function render(): string {
        return "[Desktop Button]";
    }
}

// Fabryka abstrakcyjna
interface ButtonFactory {
    public function createButton(): Button;
}

// Konkretne fabryki
class WebButtonFactory implements ButtonFactory {
    public function createButton(): Button {
        return new WebButton();
    }
}

class DesktopButtonFactory implements ButtonFactory {
    public function createButton(): Button {
        return new DesktopButton();
    }
}

// Klient
function renderButton(ButtonFactory $factory) {
    $button = $factory->createButton();
    echo $button->render() . "\n";
}

// Testowanie
$webFactory = new WebButtonFactory();
$desktopFactory = new DesktopButtonFactory();

echo "Web Button:\n";
renderButton($webFactory);

echo "\nDesktop Button:\n";
renderButton($desktopFactory);
