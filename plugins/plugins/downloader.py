from telethon import events
import youtube_dl
import instaloader

@bot.on(events.NewMessage(pattern=r"\.yt (.+)", outgoing=True))
async def yt_download(event):
    url = event.pattern_match.group(1)
    ydl_opts = {'format': 'best'}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        await event.reply(f"**Judul:** {info['title']}\n🔗 {info['url']}")

@bot.on(events.NewMessage(pattern=r"\.ig (.+)", outgoing=True))
async def ig_download(event):
    url = event.pattern_match.group(1)
    loader = instaloader.Instaloader()

    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        await event.reply(f"**Post dari:** {post.owner_username}\n🔗 {post.url}")
    except Exception as e:
        await event.reply(f"❌ Error: {str(e)}")
