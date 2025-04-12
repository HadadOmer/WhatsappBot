from src.rule import Rule
from typing import Callable

class Action:
    def __init__(self, rules: list[Rule], callback: Callable):
        self.rules = rules
        self.callback

    def evaluate_and_invoke(self, payload):
        if(self.evaluate(payload)):
            self.invoke_callback()

    def evaluate(self, payload) -> bool:
        for rule in self.rules:
            if not rule.evaluate(payload):
                print(f"Haven't met rule conditions for rule: {rule.__class__.__name__}")
                return False
        return True
    
    def invoke_callback():
        print(f"Action invokes is not yet functional")
