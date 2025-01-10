import json
from typing import Dict, Callable

class LogPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step: Callable[[Dict], Dict]) -> "LogPipeline":
        self.steps.append(step)
        return self

    def execute(self, log: Dict) -> Dict:
        for step in self.steps:
            log = step(log)
        return log

# Kroki przetwarzania logów
def add_timestamp(log: Dict) -> Dict:
    from datetime import datetime
    log["timestamp"] = datetime.utcnow().isoformat()
    return log

def filter_level(level: str):
    def step(log: Dict) -> Dict:
        if log["level"] != level:
            raise ValueError("Filtered out")
        return log
    return step

def to_json(log: Dict) -> Dict:
    log["json"] = json.dumps(log)
    return log

# Pipeline logowania
log_pipeline = LogPipeline() \
    .add_step(add_timestamp) \
    .add_step(filter_level("INFO")) \
    .add_step(to_json)

# Przykład logu
try:
    log = log_pipeline.execute({"message": "System started", "level": "INFO"})
    print(log)
except ValueError:
    print("Log został odfiltrowany")
