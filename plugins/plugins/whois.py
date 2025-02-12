from telethon import events
import requests

@bot.on(events.NewMessage(pattern=r"\.whois (.+)", outgoing=True))
async def whois_lookup(event):
    query = event.pattern_match.group(1)
    api_url = f"https://api.whoislookup.com/?query={query}"

    response = requests.get(api_url).json()
    info = response.get("result", "Tidak ditemukan.")

    await event.reply(f"🔍 **Hasil Whois:**\n{info}")
