import json
from discord.ext import commands
class List(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def list(self, ctx:commands.Context):
        json_cog = json.load(open('./json/varContent.json'))
        cogjson = json_cog['content']
        if len(cogjson) > 30:
            await ctx.send(cogjson)
        else: 
            await ctx.send('No skin was found')
async def setup(bot):
    await bot.add_cog(List(bot))
