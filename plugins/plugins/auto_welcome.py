from telethon import events

WELCOME_MSG = "👋 Selamat datang di grup! Jangan lupa baca peraturan ya."

@bot.on(events.ChatAction)
async def welcome_new_member(event):
    if event.user_joined or event.user_added:
        await event.reply(WELCOME_MSG)
