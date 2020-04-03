import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import json


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    async def send_meme(self, ctx, meme):
        url = f'https://meme-api.herokuapp.com/gimme{meme}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='meme', help='Random')
    async def _meme(self, ctx):
        await ctx.message.add_reaction('🐸')
        await self.send_meme(ctx, "")

    @commands.command(name='fyssa', aliases=['physics', 'fysik'], help='pi=3')
    async def _physics(self, ctx):
        await ctx.message.add_reaction('🖖')
        await self.send_meme(ctx, "/physicsmemes")

    @commands.command(name='mafs', aliases=['math', 'matte'], help='1+2+3+...=-1/12')
    async def _maths(self, ctx):
        await ctx.message.add_reaction('➗')
        await self.send_meme(ctx, "/mathmemes")

    @commands.command(name='dank', help='420')
    async def _dank(self, ctx):
        await ctx.message.add_reaction('🆘')
        await self.send_meme(ctx, "/dankmemes")

    @commands.command(name='gegga', aliases=['geography', 'geografi'], help='60°10\'15.2\"N 24°57\'22.6\"E')
    async def _geography(self, ctx):
        await ctx.message.add_reaction('🌍')
        await self.send_meme(ctx, "/geographymemes")

    @commands.command(name='data', aliases=['cs'], help='01100011 01110011')
    async def _cs(self, ctx):
        await ctx.message.add_reaction('👩‍💻')
        await self.send_meme(ctx, "/ProgrammerHumor")

    @commands.command(name='kemma', aliases=['chemistry', 'kemi'], help='H2O+H2O=H4O')
    async def _chemistry(self, ctx):
        await ctx.message.add_reaction('🧪')
        await self.send_meme(ctx, "/chemistrymemes")

    @commands.command(name='stenar', aliases=['geology', 'geologi'], help='Geologi såklart')
    async def _geology(self, ctx):
        await ctx.message.add_reaction('🗿')
        await self.send_meme(ctx, "/Geologymemes")

def setup(bot):
    bot.add_cog(Memes(bot))
