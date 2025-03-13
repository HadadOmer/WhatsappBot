from yowsup.env import YowsupEnv
from yowsup.stacks import YowsupStackBuilder
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

class PollBot:
    def __init__(self, credentials):
        stack_builder = YowsupStackBuilder()
        self.stack = stack_builder.pushDefaultLayers(True).build()
        self.stack.setCredentials(credentials)

    def start(self):
        print("📢 Poll Bot is now running...")
        self.stack.loop()

    def on_message(self, message):
        if message.getBody().lower() == "!poll":
            self.send_message(message.getFrom(), "📊 *New Poll:* \n1️⃣ Yes \n2️⃣ No \n\nReply with 1 or 2.")

    def send_message(self, recipient, text):
        msg = TextMessageProtocolEntity(text, to=recipient)
        self.stack.send(msg)

if __name__ == "__main__":
    import os
    PHONE = os.getenv("PHONE")
    PASSWORD = os.getenv("PASSWORD")

    if not PHONE or not PASSWORD:
        print("❌ Error: PHONE and PASSWORD environment variables are required!")
        exit(1)

    bot = PollBot((PHONE, PASSWORD))
    bot.start()