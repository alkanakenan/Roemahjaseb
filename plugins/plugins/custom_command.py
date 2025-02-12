from telethon import events

CUSTOM_COMMANDS = {
    ".halo": "Halo juga! 😊",
    ".info": "Saya adalah RoemahJaseb Ubot.",
    ".help": "Daftar perintah:\n.halo\n.info\n.help"
}

@bot.on(events.NewMessage(outgoing=True))
async def custom_commands(event):
    if event.text in CUSTOM_COMMANDS:
        await event.reply(CUSTOM_COMMANDS[event.text])
