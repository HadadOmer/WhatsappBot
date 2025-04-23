from src.rule import Rule
from typing import Callable
from src.rule import FromMeMessageRule

class Action:
    def __init__(self, rules: list[Rule], callback: Callable, ignore_from_me: bool = True):
        self.rules = rules
        self.callback = callback
        self.ignore_from_me = ignore_from_me
        if self.ignore_from_me:
            self.ignore_from_me_rule = FromMeMessageRule([])

    def evaluate_and_invoke(self, payload) -> bool:
        if self.ignore_from_me and self.ignore_from_me_rule.evaluate(payload):
            print(f"Ignoring message from me")
            return False
        if self.evaluate(payload):
            self.invoke_callback(payload)
            return True
        return False

    def evaluate(self, payload) -> bool:
        for rule in self.rules:
            if not rule.evaluate(payload):
                print(f"Haven't met rule conditions for rule: {rule.__class__.__name__}")
                return False
        return True
    
    def invoke_callback(self, payload):
        self.callback(payload)

