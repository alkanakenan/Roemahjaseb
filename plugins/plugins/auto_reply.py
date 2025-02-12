from telethon import events
from utama import bot  # Impor bot dari `utama.py`

@bot.on(events.NewMessage(pattern="(?i)halo"))
async def auto_reply(event):
    await event.reply("Halo! Ada yang bisa saya bantu?")
