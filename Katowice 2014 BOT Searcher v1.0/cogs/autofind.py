from discord.ext import commands
import json
import asyncio
from utils.functions import autofinder, jsonregister
from run import chrome, find
class Autofinder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def autofind(self, ctx):
        while True:
            if json.load(open('autofindRegist.json'))['register'] == 'True':
                await ctx.send('Autofinder is already activated')
                break
            elif json.load(open('autofindRegist.json'))['cancel'] == 'True':
                jsonregister('False', 'False')
                break
            await ctx.send('Autofinder activated, when the bot finds a skin he will return it through discord. Remember, to stop the automatic search just send .stop')
            jsonregister('True', 'False')
            while True:
                jsoncontent = json.load(open('varContent.json'))['content']
                jsoncancel = json.load(open('autofindRegist.json'))['cancel']
                jsonlen =  len(jsoncontent)
                if jsonlen < 30:
                    if jsoncancel == 'True':
                        await ctx.send('Autofinder has been successfully cancelled')
                        break
                    autofind = asyncio.create_task(autofinder(chrome, find))
                    await autofind
                    jsoncontent = json.load(open('varContent.json'))['content']
                    jsonlen = len(jsoncontent)
                    if jsonlen > 30:
                        await ctx.send(jsoncontent)
                        return
                    continue
                else: 
                    await ctx.send('A skin has already been searched, to display send .list, or manually use .reload to reload again.')
                    break
                

async def setup(bot):
    await bot.add_cog(Autofinder(bot))