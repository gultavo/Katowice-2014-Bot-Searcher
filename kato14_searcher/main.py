from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from random import randint
from time import sleep
from datetime import datetime
import requests
import os
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
economyapi = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
request = requests.get(economyapi)
response = request.json()
low = float(response['USDBRL']['high'])
options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
find = chrome.find_element
discord_token = 'MTI0NjQ1NjU2NjgyNDMwODg1OA.GDlA2t.xH5J28PWYmyh17j9cYw_90lPV0jMebiSWcyO2w'
# channel_id = '1246458149482004524'
intents = discord.Intents.all()
intents.message_content = True  
client = commands.Bot(command_prefix='!', intents=intents)

verifier = None

def main(id, xpath):
    global price, real, preco
    price = find(By.XPATH, xpath).text
    price = float(price[1:-4].replace(',', ''))
    preco = float(price*low)
    real = locale.currency(preco, grouping=True, symbol=None)
    # real =  round(preco, 2)
    find(By.ID, id).click()

    verifier = While()

    site()

    return verifier

def content():
    stop_loop_nv = None
    while stop_loop_nv != True:
        name = find(By.XPATH, '//*[@id="largeiteminfo_item_name"]').text
        exterior = find(By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]/div[1]').text
        nametag = find(By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]/div[3]').text
        katowice = 'Katowice 2014'
        stickers = find(By.XPATH, '//*[@id="sticker_info"]/center').text
        nametag_display = find(By.CLASS_NAME, 'item_desc_description').text
        nametag_var = 'Name Tag:'
        content_1 = str(f'''\n
        Skin: {name}
{exterior}
{nametag}
**{stickers}**
        \n
Price: $ {price}
Preço: R$ {real}
        \n''')
        content_2 = str(f'''\n
        Skin: {name}
{exterior}
**{stickers}**
        \n
Price: $ {price}
Preço: R$ {real}
        \n''')
        client.main_content_1 = content_1
        client.main_content_2 = content_2
        try:
            if katowice in stickers:
                if nametag_var in nametag_display:
                    print(content_1)
                    return True
                else:
                    print(content_2)
                    return False 
            else:
                print('\033[1;31mNAME TAG DETECTED\033[m')   
                stop_loop_nv = True
        except NoSuchElementException:
            print('a')
            stop_loop_nv = True

def site():
    stop_loop = None
    while stop_loop != True:
        try:
            if find(By.XPATH, '//*[@id="result_0"]/div[2]/span[2]') is not True:
                print('Steam loaded...')
            stop_loop = True
        except NoSuchElementException:
            #print('Reloading Steam...')
            chrome.refresh()
            sleep(randint(3, 6))
            stop_loop = False

def While():
    while True:
        try:
            sleep(2.0)
            find(By.CLASS_NAME, 'hover_item_name') is not True
            try:
                sticker_steam = 'Sticker' or 'Adesivo'
                capsule = 'EMS'
                sleep(2.0)            
                if sticker_steam in find(By. CLASS_NAME, 'hover_item_name').text:
                    print('\033[1;33mSOLID STICKER\033[m')
                    return False
                elif capsule in find(By. XPATH, '//*[@id="largeiteminfo_item_name"]').text:
                    print('\033[1;34mCAPSULE\033[m')
                    return False     
                else:
                    content()
                inf()
                return False
            except NoSuchElementException:
                #print('Reloading...')
                chrome.refresh()
        except NoSuchElementException:
            chrome.refresh()
    
# VOLTA
def inf():
    sleep(1.0)
    chrome.get('https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p75_price_asc')
    sleep(1.0)

chrome.get('https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p75_price_asc')

sleep(2.0)


# ENTRAR NO SITE

site()

# BUSCAR SKINS
# main('result_0', '//*[@id="result_0"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_1', '//*[@id="result_1"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
# main('result_2', '//*[@id="result_2"]/div[1]/div[2]/span[1]/span[1]')
# print('\n' * 2, current_time)
main('result_3', '//*[@id="result_3"]/div[1]/div[2]/span[1]/span[1]')
print('\n' * 2, current_time)
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
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await client.load_extension(f'cogs.{arquivo[:-3]}')

async def main():
    await load_cogs()
    await client.start(discord_token)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

asyncio.run(main())
