from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

async def main():
    print("Bot is running...")
    await client.run_until_disconnected()  # Menjaga bot tetap berjalan

with client:
    client.loop.run_until_complete(main())
