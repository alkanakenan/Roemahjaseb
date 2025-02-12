from telethon import events

REACTION_KEYWORDS = {
    "halo": "👋",
    "terima kasih": "🙏",
    "lol": "😂",
    "mantap": "🔥"
}

@bot.on(events.NewMessage(incoming=True))
async def auto_react(event):
    for keyword, emoji in REACTION_KEYWORDS.items():
        if keyword in event.raw_text.lower():
            await event.message.react(emoji)
            break
