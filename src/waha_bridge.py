from common.http_wrapper import send_request
import os
import asyncio

WAHA_ADDRESS=os.getenv('WAHA_ADDRESS')

def reply_private_message(payload):
    async def _send():
        url = f"{WAHA_ADDRESS}/api/sendText"
        request_type = "POST"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        post_data = {
            "chatId": payload["participant"],
            "reply_to": payload["id"],
            "text": "Hi there!",
            "linkPreview": True,
            "linkPreviewHighQuality": False,
            "session": "default"
        }

        response = await send_request(url, request_type, headers, post_data=post_data)
        print(f"Status for replying to private message: {response.status}")

    try:
        asyncio.run(_send())
    except RuntimeError:
        asyncio.create_task(_send())