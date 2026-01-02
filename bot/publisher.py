import os
from telegram import Bot

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

def send_message(title, link):
    message = f"📰 {title}\n{link}"
    bot.send_message(chat_id=CHAT_ID, text=message)
