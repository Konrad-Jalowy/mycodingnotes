// Command Interface
interface Command {
    execute(): void;
    undo(): void;
}

// Receiver
class ShoppingCart {
    private items: string[] = [];

    addItem(item: string): void {
        this.items.push(item);
        console.log(`Added ${item} to the cart. Current items: [${this.items.join(', ')}]`);
    }

    removeItem(item: string): void {
        const index = this.items.indexOf(item);
        if (index !== -1) {
            this.items.splice(index, 1);
            console.log(`Removed ${item} from the cart. Current items: [${this.items.join(', ')}]`);
        } else {
            console.log(`Item ${item} not found in the cart.`);
        }
    }
}

// Concrete Commands
class AddItemCommand implements Command {
    constructor(private cart: ShoppingCart, private item: string) {}

    execute(): void {
        this.cart.addItem(this.item);
    }

    undo(): void {
        this.cart.removeItem(this.item);
    }
}

class RemoveItemCommand implements Command {
    constructor(private cart: ShoppingCart, private item: string) {}

    execute(): void {
        this.cart.removeItem(this.item);
    }

    undo(): void {
        this.cart.addItem(this.item);
    }
}

// Invoker
class CommandManager {
    private history: Command[] = [];

    executeCommand(command: Command): void {
        command.execute();
        this.history.push(command);
    }

    undoLastCommand(): void {
        if (this.history.length > 0) {
            const lastCommand = this.history.pop();
            lastCommand?.undo();
        } else {
            console.log("Nothing to undo!");
        }
    }
}

// Client Code
const cart = new ShoppingCart();
const commandManager = new CommandManager();

// Create commands
const addApple = new AddItemCommand(cart, "Apple");
const addBanana = new AddItemCommand(cart, "Banana");
const removeApple = new RemoveItemCommand(cart, "Apple");

// Execute commands
commandManager.executeCommand(addApple);    // Add Apple
commandManager.executeCommand(addBanana);  // Add Banana
commandManager.executeCommand(removeApple); // Remove Apple

// Undo commands
commandManager.undoLastCommand(); // Undo remove Apple
commandManager.undoLastCommand(); // Undo add Banana
commandManager.undoLastCommand(); // Undo add Apple
commandManager.undoLastCommand(); // Nothing to undo
