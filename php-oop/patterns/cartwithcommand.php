<?php

// Command Interface
interface Command {
    public function execute(): void;
    public function undo(): void;
}

// Receiver
class ShoppingCart {
    private array $items = [];

    public function addItem(string $item): void {
        $this->items[] = $item;
        echo "Added $item to the cart. Current items: [" . implode(', ', $this->items) . "]\n";
    }

    public function removeItem(string $item): void {
        $index = array_search($item, $this->items, true);
        if ($index !== false) {
            unset($this->items[$index]);
            $this->items = array_values($this->items); // Reindex array
            echo "Removed $item from the cart. Current items: [" . implode(', ', $this->items) . "]\n";
        } else {
            echo "Item $item not found in the cart.\n";
        }
    }
}

// Concrete Commands
class AddItemCommand implements Command {
    private ShoppingCart $cart;
    private string $item;

    public function __construct(ShoppingCart $cart, string $item) {
        $this->cart = $cart;
        $this->item = $item;
    }

    public function execute(): void {
        $this->cart->addItem($this->item);
    }

    public function undo(): void {
        $this->cart->removeItem($this->item);
    }
}

class RemoveItemCommand implements Command {
    private ShoppingCart $cart;
    private string $item;

    public function __construct(ShoppingCart $cart, string $item) {
        $this->cart = $cart;
        $this->item = $item;
    }

    public function execute(): void {
        $this->cart->removeItem($this->item);
    }

    public function undo(): void {
        $this->cart->addItem($this->item);
    }
}

// Invoker
class CommandManager {
    private array $history = [];

    public function executeCommand(Command $command): void {
        $command->execute();
        $this->history[] = $command;
    }

    public function undoLastCommand(): void {
        if (!empty($this->history)) {
            $lastCommand = array_pop($this->history);
            $lastCommand->undo();
        } else {
            echo "Nothing to undo!\n";
        }
    }
}

// Client Code
$cart = new ShoppingCart();
$commandManager = new CommandManager();

// Create commands
$addApple = new AddItemCommand($cart, "Apple");
$addBanana = new AddItemCommand($cart, "Banana");
$removeApple = new RemoveItemCommand($cart, "Apple");

// Execute commands
$commandManager->executeCommand($addApple);    // Add Apple
$commandManager->executeCommand($addBanana);  // Add Banana
$commandManager->executeCommand($removeApple); // Remove Apple

// Undo commands
$commandManager->undoLastCommand(); // Undo remove Apple
$commandManager->undoLastCommand(); // Undo add Banana
$commandManager->undoLastCommand(); // Undo add Apple
$commandManager->undoLastCommand(); // Nothing to undo
