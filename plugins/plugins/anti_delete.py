from telethon import events
from utama import bot

@bot.on(events.MessageDeleted())
async def anti_delete(event):
    for msg in event.deleted_ids:
        await event.respond(f"❌ Pesan dengan ID {msg} telah dihapus, tapi aku masih menyimpannya!")
