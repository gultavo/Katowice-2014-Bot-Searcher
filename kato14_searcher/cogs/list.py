from discord.ext import commands
from utils.functions import content_1, content_2, verifier

class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def list(self, ctx:commands.Context):
        if verifier == True:
            await ctx.send(content_1)
        else:
            await ctx.send(content_2)
async def setup(bot):
    await bot.add_cog(List(bot))