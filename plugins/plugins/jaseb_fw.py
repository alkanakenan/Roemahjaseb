from telethon import events
import asyncio

@bot.on(events.NewMessage(pattern=r"\.fw (.+) (\d+) (\d+)"))
async def jaseb_fw(event):
    args = event.pattern_match.groups()
    
    if len(args) < 3:
        await event.reply("**Format Salah!**\nGunakan: `.fw (lpm) (jeda) (jumlah sebar)`")
        return

    lpm, jeda, jumlah = args
    try:
        jeda = int(jeda)
        jumlah = int(jumlah)
    except ValueError:
        await event.reply("**Error:** Jeda dan jumlah harus angka!")
        return

    await event.reply(f"**Memulai Auto-Forward:**\nPesan: `{lpm}`\nJeda: `{jeda}s`\nJumlah: `{jumlah}`")
    
    for
