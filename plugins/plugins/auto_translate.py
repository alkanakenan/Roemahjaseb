from telethon import events
from googletrans import Translator

translator = Translator()

@bot.on(events.NewMessage(pattern=r"\.translate (\w+)", outgoing=True))
async def translate_text(event):
    args = event.pattern_match.group(1)
    reply = await event.get_reply_message()

    if not reply:
        await event.reply("❌ Balas pesan yang ingin diterjemahkan!")
        return

    try:
        translated = translator.translate(reply.text, dest=args)
        await event.reply(f"**Hasil Terjemahan ({args}):**\n{translated.text}")
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
