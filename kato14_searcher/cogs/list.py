from discord.ext import commands

class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def list(self, ctx:commands.Context):
        await ctx.send(self.bot.main_content_2)
async def setup(bot):
    await bot.add_cog(List(bot))


