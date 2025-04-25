from typing import Any

class Rule:
    def __init__(self, parameters: list[Any]):
        self.parameters = parameters

    def evaluate(self, payload):
        if not payload.get("from"):
            print("invalid message")
            return False 
        return True
    
class GroupMessageRule(Rule):
    def __init__(self, parameters: list[Any]):
        super().__init__(parameters) 

    def evaluate(self, payload):
        if not super().evaluate(payload):
            return False
        from_value = payload.get("from", "")
        is_filter_by_group = self.parameters[0] if self.parameters else False
        if(is_filter_by_group):
            return from_value == self.parameters[1]
        else:
            return "g.us" in from_value
    
class SenderMessageRule(Rule):
    def __init__(self, parameters: list[Any]):
        super().__init__(parameters)
        self.group_message_rule = GroupMessageRule([])

    def evaluate(self, payload):
        if not super().evaluate(payload):
            return False
        is_group_message = self.group_message_rule.evaluate(payload)
        expected_sender = self.parameters[0]
        if is_group_message:
            return payload.get("participant", "") == expected_sender
        else:
            return payload.get("from", "") == expected_sender
        
class FromMeMessageRule(Rule):
    def __init__(self, parameters: list[Any]):
        super().__init__(parameters)

    def evaluate(self, payload):
        if not super().evaluate(payload):
            return False
        return payload.get("fromMe", False)