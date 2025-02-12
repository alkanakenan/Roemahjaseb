from telethon import events
import requests

@bot.on(events.NewMessage(pattern=r"\.resi (\w+)", outgoing=True))
async def cek_resi(event):
    resi = event.pattern_match.group(1)
    url = f"https://api.rajaongkir.com/starter/waybill?waybill={resi}&courier=jne"

    headers = {"key": "API_RAJAONGKIR"}  # Ganti dengan API Key RajaOngkir
    response = requests.get(url, headers=headers).json()

    if response["rajaongkir"]["status"]["code"] == 200:
        hasil = response["rajaongkir"]["result"]["summary"]
        await event.reply(f"📦 **Cek Resi:**\n{hasil}")
    else:
        await event.reply("❌ Resi tidak ditemukan!")
