from typing import Final, List, Dict
from whatsapp_api_client_python import API
import os
from dotenv import load_dotenv

load_dotenv('.env')
INSTANCE_ID: Final[str] = os.getenv('INSTANCE_ID')
API_TOKEN_INSTANCE: Final[str] = os.getenv('API_TOKEN_INSTANCE')
PHONE_NUMBER : Final[str] = os.getenv('PHONE_NUMBER')

greenAPI: API.GreenAPI = API.GreenAPI(INSTANCE_ID, API_TOKEN_INSTANCE)

OPTIONS = [
    {"optionName": "Red"},
    {"optionName": "Green"},
    {"optionName": "Blue"}
]
QUESTION = "Please choose a color:"

def send_pole(question: str, options: List[Dict[str, str]], phone_number: str):
    response = greenAPI.sending.sendPoll(
    f"{phone_number}@c.us",
    question,
    options,
    multipleAnswers=True
    )
    print(response.data)


def main() -> None:
    send_pole(QUESTION, OPTIONS, PHONE_NUMBER)


if __name__ == '__main__':
    main()