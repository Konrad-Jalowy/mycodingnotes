# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Receiver
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart. Current items: {self.items}")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"Removed {item} from the cart. Current items: {self.items}")

# Concrete Commands
class AddItemCommand(Command):
    def __init__(self, cart, item):
        self.cart = cart
        self.item = item

    def execute(self):
        self.cart.add_item(self.item)

    def undo(self):
        self.cart.remove_item(self.item)

class RemoveItemCommand(Command):
    def __init__(self, cart, item):
        self.cart = cart
        self.item = item

    def execute(self):
        self.cart.remove_item(self.item)

    def undo(self):
        self.cart.add_item(self.item)

# Invoker
class CommandManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("Nothing to undo!")

# Client Code
cart = ShoppingCart()
command_manager = CommandManager()

# Create commands
add_apple = AddItemCommand(cart, "Apple")
add_banana = AddItemCommand(cart, "Banana")
remove_apple = RemoveItemCommand(cart, "Apple")

# Execute commands
command_manager.execute_command(add_apple)   # Add Apple
command_manager.execute_command(add_banana) # Add Banana
command_manager.execute_command(remove_apple) # Remove Apple

# Undo commands
command_manager.undo_last_command()  # Undo remove Apple
command_manager.undo_last_command()  # Undo add Banana
command_manager.undo_last_command()  # Undo add Apple
command_manager.undo_last_command()  # Nothing to undo
