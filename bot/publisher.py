import os
import asyncio
from telegram import Bot

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_message(title, text):
    message = f"📰 {title}\n{text}"
    await bot.send_message(chat_id=CHAT_ID, text=message)

def send_message_sync(title, text):
    asyncio.run(send_message(title, text))
