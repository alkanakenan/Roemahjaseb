import os
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load konfigurasi dari file config.env
load_dotenv()

# Ambil variabel dari config.env
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inisialisasi Telegram Client
bot = TelegramClient("RoemahJaseb", API_ID, API_HASH).start(bot_token=STRING_SESSION)

# Contoh fitur auto-reply
@bot.on(events.NewMessage(pattern="(?i)halo"))
async def handler(event):
    await event.reply("Hai! Selamat datang di RoemahJaseb Userbot.")

# Jalankan bot
logger.info("Bot sedang berjalan...")
bot.run_until_disconnected()
