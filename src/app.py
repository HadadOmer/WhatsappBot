from flask import Flask, request, jsonify
from src.action import Action
from src.rule import SenderMessageRule, GroupMessageRule
import os
from src.waha_bridge import reply_private_message

app = Flask(__name__)
PHONE_NUMBER = os.getenv('PHONE_NUMBER')
GROUP_NUMBER = os.getenv('GROUP_NUMBER')

actions = [
    Action([SenderMessageRule([f'{PHONE_NUMBER}@c.us']), GroupMessageRule([True ,f'{GROUP_NUMBER}@g.us'])], reply_private_message)
]

@app.route('/', methods=['GET'])
def blank():
    return jsonify({}), 200

@app.route('/webhooks/messages', methods=['POST'])
def wake_device():
    data = request.get_json()
    payload = data["payload"]
    print(f'Evaluation and invoke result is {actions[0].evaluate_and_invoke(payload)}')
    return data, 200
