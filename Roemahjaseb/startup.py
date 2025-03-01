import sys
from telethon.utils import get_peer_id
from Roemahjaseb.events import ajg
from Roemahjaseb import BOT_TOKEN

# Cek apakah BOT_VER ada, jika tidak gunakan default
try:
    from Roemahjaseb import BOT_VER as version
except ImportError:
    version = "1.0"

from Roemahjaseb import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklist,
    bot,
    tgbot,
)
from Roemahjaseb.modules.gcast import GCAST_BLACKLIST as GBL

# Pesan Startup
EOL = "Roemahjaseb-Ubot v{} - 2025 • https://github.com/alkanakenan/Roemahjaseb"
MSG_BLACKLIST = "Roemahjaseb-Ubot v{}\nhttps://github.com/alkanakenan/Roemahjaseb"

async def startup_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)

def startup():
    global version  # Gunakan versi global agar tidak menyebabkan UnboundLocalError
    
    if not version:
        LOGS.warning("BOT_VER tidak ditemukan! Menggunakan versi default.")
        version = "1.0"

    if 6037364404 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)

    if -1001287188817 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)

    if 6037364404 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    
    if STRING_SESSION:
        try:
            bot.start()
            LOOP.run_until_complete(ajg())
            LOOP.run_until_complete(startup_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION terdeteksi!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklist:
                LOGS.warning(MSG_BLACKLIST.format(version))
                sys.exit(1)
        except Exception as e:
            LOGS.error(f"Error saat menjalankan bot: {str(e)}")

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN terdeteksi!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.error(f"Error saat mengakses BOT_TOKEN: {str(e)}")

    if not STRING_SESSION:
        LOGS.warning("STRING_SESSION tidak ditemukan! Harap periksa kembali.")
