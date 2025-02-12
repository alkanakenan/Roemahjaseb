from telethon import events
import asyncio

@bot.on(events.NewMessage(pattern=r"!delayspam (\d+[smhd]) (\d+) (.+)", outgoing=True))
async def delay_spam(event):
    time_unit_map = {"s": 1, "m": 60, "h": 3600, "d": 86400}

    time_value, jumlah, pesan = event.pattern_match.groups()
    jumlah = int(jumlah)
    time_unit = time_value[-1]
    
    if time_unit not in time_unit_map:
        return await event.reply("🚫 Format waktu salah. Gunakan s/m/h/d.")

    delay = int(time_value[:-1]) * time_unit_map[time_unit]

    await event.reply(f"📢 Memulai spam {jumlah} kali dengan jeda {time_value}...\n📌 Pesan: {pesan}")

    for i in range(jumlah):
        await event.respond(pesan)
        await asyncio.sleep(delay)
    
    await event.reply("✅ Spam selesai!")
