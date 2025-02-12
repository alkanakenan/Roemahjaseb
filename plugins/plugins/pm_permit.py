from telethon import events
import asyncio

# Default pesan auto-reply untuk pengguna baru
PM_PERMIT_MESSAGE = "🔹 *Halo!*\n\nBot ini otomatis menyaring pesan dari orang asing.\nSilakan tunggu, atau ketik `!izin` untuk melanjutkan."

@bot.on(events.NewMessage(incoming=True, private=True))
async def auto_pm_reply(event):
    """ Auto-reply untuk DM pertama kali dari pengguna yang belum diizinkan """
    sender = await event.get_sender()
    user_id = sender.id

    if user_id in PM_PERMIT_USERS:
        return

    # Kirim auto-reply hanya untuk pesan pertama kali
    await event.respond(PM_PERMIT_MESSAGE)

@bot.on(events.NewMessage(pattern="!setpm (.+)", outgoing=True))
async def set_pm_permit_message(event):
    """ Mengubah pesan auto-reply PM Permit """
    global PM_PERMIT_MESSAGE
    new_message = event.pattern_match.group(1)

    PM_PERMIT_MESSAGE = new_message
    await event.respond(f"✅ *Pesan PM Permit diubah menjadi:*\n\n{new_message}")
