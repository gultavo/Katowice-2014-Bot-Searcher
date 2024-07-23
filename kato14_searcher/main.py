from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime
from os import listdir
import discord
from discord.ext import commands
import asyncio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(options=options)#,service=Service(ChromeDriverManager().install()))
find = chrome.find_element
discord_token = 'MTI0NjQ1NjU2NjgyNDMwODg1OA.GDlA2t.xH5J28PWYmyh17j9cYw_90lPV0jMebiSWcyO2w'
intents = discord.Intents.all()
intents.message_content = True  
client = commands.Bot(command_prefix='!', intents=intents)

from utils.functions import main, site, get_price, security, content, inf

chrome.get('https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p75_price_asc')

sleep(2.0)


# ENTRAR NO SITE

site(find, chrome)

# BUSCAR SKINS
get_price(chrome, '//*[@id="result_0"]/div[1]/div[2]/span[1]/span[1]')
main('result_0', find)
security(chrome, find)
content(find)
inf(chrome)
print('\n' * 2, current_time)
# main('result_1', '//*[@id="result_1"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_2', '//*[@id="result_2"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# get_price(chrome, '//*[@id="result_3"]/div[1]/div[2]/span[1]/span[1]')
# main('result_3', find)
# security(chrome, find)
# content(find)
# inf(chrome)
# print('\n' * 2, current_time)
# main('result_4', '//*[@id="result_4"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_5', '//*[@id="result_5"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_6', '//*[@id="result_6"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_7', '//*[@id="result_7"]/div[1]/div[2]/span[1]/span[1]')
# print('\n'* 2, current_time)
# main('result_8', '//*[@id="result_8"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_9', '//*[@id="result_9"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
print('\033[1;32mSUCCESS\033[m')
print(f'LAST VERIFIED ON: {current_time}')
        
async def load_cogs():
    for arquivo in listdir('cogs'):
        if arquivo.endswith('.py'):
            await client.load_extension(f'cogs.{arquivo[:-3]}')

async def main():
    await load_cogs()
    await client.start(discord_token)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

asyncio.run(main())
