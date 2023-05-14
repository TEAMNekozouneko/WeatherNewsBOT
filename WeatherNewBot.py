import discord
from discord.ext import commands
import aiohttp
import time

basho = ["016010","040010","130010","120010","170010","270000","390010","340010","400010","460010","471010"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def otenki(ctx):
    while True:
        embed = discord.Embed(title="全国のお天気ヒャッハー",description="どおもお天気大好きくんだよおおお。お天気教えちゃいますよっ！",color=discord.Colour.yellow())
        embed.set_thumbnail(url="https://3.bp.blogspot.com/-xQNOYwWqg0c/UguJadClyhI/AAAAAAAAXa0/OkBpN_x_SNM/s800/nihonchizu.png")

        for id in basho:
            jsond = await otenki(id)
            tenki = jsond["forecasts"][0]["telop"]
            city = jsond["location"]["city"]
            embed.add_field(name=city, value=tenki)
        await ctx.send(embed=embed)

        time.sleep(1800)

async def otenki(id):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://weather.tsukumijima.net/api/forecast/city/"+id) as resp:
            jsond = await resp.json()
            return jsond


bot.run("TOKEN")
