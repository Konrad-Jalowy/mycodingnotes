# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Receiver
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

# Concrete Commands
class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        self.tv.turn_off()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        self.tv.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

# Client Code
tv = TV()

turn_on = TurnOnCommand(tv)
turn_off = TurnOffCommand(tv)

remote = RemoteControl()

# Turn the TV ON
remote.set_command(turn_on)
remote.press_button()

# Undo action
remote.press_undo()

# Turn the TV OFF
remote.set_command(turn_off)
remote.press_button()

# Undo action
remote.press_undo()
