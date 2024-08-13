from discord.ext import commands
from utils.func_loader import *
from utils.loader import chrome, find, skins_module
from utils.functions import name_verifier
import json
class Reloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def reload(self, ctx):
        await ctx.send('Wait... Verifying')
        name_verifier(chrome, find)
        json_cogname = json.load(open('varContent.json'))
        cogjsoname = json_cogname['verifier']
        cogjsonskins = json_cogname['skins_name']
        if cogjsoname == cogjsonskins:
            await ctx.send('Same skins')
        else:
            await ctx.send('Reloading... This may take a few minutes')
            skins_module(chrome, find)
        
async def setup(bot):
    await bot.add_cog(Reloader(bot))