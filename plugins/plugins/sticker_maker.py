from telethon import events
import os

@bot.on(events.NewMessage(pattern="!sticker", outgoing=True))
async def make_sticker(event):
    reply = await event.get_reply_message()
    if reply and reply.media:
        file = await bot.download_media(reply.media)
        output_file = file.replace(".jpg", ".webp").replace(".png", ".webp")

        os.system(f"convert {file} {output_file}")
        await bot.send_file(event.chat_id, output_file, force_document=False, caption="✅ Stiker berhasil dibuat!")
        os.remove(file)
        os.remove(output_file)
    else:
        await event.reply("🚫 Balas gambar untuk dijadikan stiker.")
