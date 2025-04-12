from flask import Flask, request, jsonify
from src.action import Action
from src.rule import SenderMessageRule, GroupMessageRule

app = Flask(__name__)

actions = [
    Action([SenderMessageRule(['972546772491@c.us']), GroupMessageRule([])], )
]

@app.route('/', methods=['GET'])
def blank():
    return jsonify({}), 200

@app.route('/webhooks/messages', methods=['POST'])
def wake_device():
    data = request.get_json()
    payload = data["payload"]
    print(f'Evaluation result is {actions[0].evaluate(payload)}')
    return data, 200
