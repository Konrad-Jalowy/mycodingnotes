from typing import Callable, List

# Pipeline Step Type
PipelineStep = Callable[[str], str]

class Pipeline:
    def __init__(self):
        self.steps: List[PipelineStep] = []

    def add_step(self, step: PipelineStep) -> "Pipeline":
        self.steps.append(step)
        return self  # umożliwia łańcuchowe dodawanie

    def execute(self, input: str) -> str:
        result = input
        for step in self.steps:
            result = step(result)
        return result

# Funkcje reprezentujące kroki pipeline
def trim(input: str) -> str:
    return input.strip()

def to_uppercase(input: str) -> str:
    return input.upper()

def add_prefix(prefix: str) -> Callable[[str], str]:
    def step(input: str) -> str:
        return f"{prefix}{input}"
    return step

# Tworzymy pipeline
text_pipeline = Pipeline() \
    .add_step(trim) \
    .add_step(to_uppercase) \
    .add_step(add_prefix("Processed: "))

# Przykład użycia
result = text_pipeline.execute("   hello world   ")
print(result)  # "Processed: HELLO WORLD"
