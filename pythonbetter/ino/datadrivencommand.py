from typing import Callable, Dict

class DataDrivenCommand:
    def __init__(self, static_params: Dict, dynamic_logic: Callable):
        self.static_params = static_params
        self.dynamic_logic = dynamic_logic

    def execute(self, context: Dict):
        # Dynamicznie generuje decyzje na podstawie kontekstu
        dynamic_decision = self.dynamic_logic(context)
        print(f"Executing command with params: {self.static_params}, decision: {dynamic_decision}")

# Przykładowa logika dynamiczna
def logistics_logic(context):
    if context["traffic"] == "heavy":
        return "Choose alternative route"
    elif context["weather"] == "rainy":
        return "Delay delivery"
    else:
        return "Proceed as planned"

# Tworzenie i wykonanie command
command = DataDrivenCommand(
    static_params={"delivery_id": 123, "priority": "high"},
    dynamic_logic=logistics_logic
)

# Symulacja kontekstu
context = {"traffic": "heavy", "weather": "clear"}
command.execute(context)
