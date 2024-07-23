from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from random import randint
from time import sleep
import requests
import discord
from discord.ext import commands
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
find = chrome.find_element



# FAZ AS CONTAS DO PREÇO (CONVERSÃO) E É A FUNÇÃO PRINCIPAL

def get_price(xpath):
    economyapi = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    request = requests.get(economyapi)
    response = request.json()
    low = float(response['USDBRL']['high'])
    find = chrome.find_element
    price = find(By.XPATH, xpath).text
    price = float(price[1:-4].replace(',', ''))
    preco = float(price*low)
    real = locale.currency(preco, grouping=True, symbol=None)
    return real

def main(id):
    find(By.ID, id).click()
    site()


# IMPRIME O CONTEÚDO DA PÁGINA (QUE PRECISA)

def content(price, real):
    intents = discord.Intents.all()
    intents.message_content = True  
    client = commands.Bot(command_prefix='!', intents=intents)
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
        verifier = None
        client.main_content_1 = content_1
        client.main_content_2 = content_2
        try:
            if katowice in stickers:
                if nametag_var in nametag_display:
                    print(content_1)
                    verifier = True
                    return True
                else:
                    print(content_2)
                    verifier = False
                    return False 
            else:
                print('\033[1;31mNAME TAG DETECTED\033[m')   
                stop_loop_nv = True
        except NoSuchElementException:
            print('a')
            stop_loop_nv = True
        return verifier


# VERIFICA SE O SITE FOI CARREGADO CORRETAMENTE

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



# FUNÇÃO DE SEGURANÇA CASO O ITEM FOR OUTRA COISA QUE NÃO QUER

def security():
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

# FUNÇÃO PARA ENTRAR NO SITE

def inf():
    sleep(1.0)
    chrome.get('https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p75_price_asc')
    sleep(1.0)