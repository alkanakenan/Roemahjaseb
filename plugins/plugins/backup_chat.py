from telethon import events

@bot.on(events.NewMessage(pattern=r"\.backup", outgoing=True))
async def backup_chat(event):
    chat = await event.get_chat()
    messages = await bot.get_messages(chat, limit=100)

    with open("backup_chat.txt", "w", encoding="utf-8") as file:
        for msg in messages:
            file.write(f"{msg.date}: {msg.sender_id} - {msg.text}\n")

    await event.reply("✅ Chat berhasil dibackup!", file="backup_chat.txt")
