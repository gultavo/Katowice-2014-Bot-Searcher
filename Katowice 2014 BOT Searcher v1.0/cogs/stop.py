from discord.ext import commands
from utils.functions import jsonregister
import json
class Stop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def stop(self, ctx):
        regist = json.load(open('./json/autofindRegist.json'))
        register = regist['register']
        if register == 'True':
            await ctx.send('Stopping autofinder...')
            jsonregister('False', 'True')
        else:
            await ctx.send('Autofinder isnt activated, to activate it send .autofind')
async def setup(bot):
    await bot.add_cog(Stop(bot))
