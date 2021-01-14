from discord.ext import commands
from mcstatus import MinecraftServer


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='minecraft', aliases=['ping'], help='Se om nån server är uppe och om nån fellow gamer är online')
    async def _minecraft(self, ctx, *, msg: str):

        for ip in msg.split():
            if ':' in ip:
                address = ip
            elif ip == 'spektrum.mcserver.io':
                address = 'spektrum.mcserver.io'
            else:
                address = f'{ip}:25565'

            try:
                server = MinecraftServer.lookup(address)
                status = server.status()
                await ctx.send(f'{address} has {status.players.online} players and replied in {status.latency} ms')
            except:
                await ctx.send(f'{address} is offline')

def setup(bot):
    bot.add_cog(Minecraft(bot))
