from discord.ext import commands
class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def helper(self, ctx):
        await ctx.send('''COMMANDS:
.list | To show the skins 
.reload | To reload the skins''')
        
async def setup(bot):
    await bot.add_cog(Helper(bot))