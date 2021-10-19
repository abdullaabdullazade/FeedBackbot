from discord.ext import commands

Bot = commands.Bot(command_prefix="/")


@Bot.event
async def on_ready():
    print("Hazıram!")

@Bot.command()
async def start(msg):
    await msg.send("Bota müraciət yazmaq üçün /sorgu adınız birdə mesaj yazın.Məsələn:/sorgu fr13nd_7 ......")
@Bot.command()
async def sorgu(ctx, member, *, msg):
    with open("sorgu.txt", "a+", encoding="utf-8") as a:
        print(f"{member}:{msg}", file=a)
    await ctx.send("Sorğunuz qəbul edildi.")


Bot.run('ODg5MDMwMDE5Mzk2MDI2NDI4.YUbTug.LzzBTW_GUzBhm2UIXjpT7eLOt2w')
