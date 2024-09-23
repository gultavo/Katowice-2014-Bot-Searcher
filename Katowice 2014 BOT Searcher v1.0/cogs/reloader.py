from discord.ext import commands
from utils.functions import c_array, jsonreloader
from run import skins_module
from selenium import webdriver
from utils.functions import name_verifier, skins_module, cartridge
import json
import asyncio
options = webdriver.ChromeOptions()
# options.add_argument('headless')
chrome_re = webdriver.Chrome(options=options)
find_re = chrome_re.find_element
chrome_re.get(cartridge)
jsonreloader('False', None)
class Reloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def reload(self, ctx):
        global c_array
        reload_ver = json.load(open('reloaderRegist.json'))['reloader']
        autofind_ver = json.load(open('autofindRegist.json'))['register']
        while True:
            if reload_ver == 'True':
                await ctx.send('Verifier is already activated')
                break
            elif autofind_ver == 'True':
                await ctx.send('Autofinder is activated, no reason for reloading.')
            jsonreloader('True', None)
            await ctx.send('Wait... Verifying')
            c_array = []
            verifier = asyncio.create_task(name_verifier(chrome_re, find_re))
            await verifier
            json_cogname = json.load(open('varContent.json'))
            cogjsoname = json_cogname['verifier']
            reloadjsonskins = json.load(open('reloaderRegist.json'))['skins_name']
            if cogjsoname == reloadjsonskins:
                await ctx.send('Same skins')
                jsonreloader('False', None)
                break
            else:
                await ctx.send('Reloading... This may take a few minutes')
                await skins_module(chrome_re, find_re)
                json_cogname = json.load(open('varContent.json'))
                content = json_cogname['content']
                if len(content) > 30:
                    await ctx.send(content)
                    jsonreloader('False', None)
                    break
                else:
                    await ctx.send('Couldnt find any skin')
                    jsonreloader('False', None)
                    break
        
async def setup(bot):
    await bot.add_cog(Reloader(bot))