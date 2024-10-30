# from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import json
import asyncio
from time import sleep
import requests
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
economyapi = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
request = requests.get(economyapi)
response = request.json()
low = float(response['USDBRL']['high'])
cartridge = 'https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=zany&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p3_price_asc'

# FAZ AS CONTAS DO PREÇO (CONVERSÃO) E É A FUNÇÃO PRINCIPAL
async def get_price(chrome, xpath):
    global price, real
    await asyncio.sleep(4.0)
    while True:
        try:
            find = chrome.find_element
            price_x = find(By.XPATH, xpath).text
            price = float(price_x[1:-4].replace(',', ''))
            preco = float(price*low)
            real = locale.currency(preco, grouping=True, symbol=None)
            return real, price
        except NoSuchElementException:
            chrome.refresh()
            await asyncio.sleep(6.0)

async def check_names(chrome, find):
    global c_array
    for num in range(0, 10):
        stop_loop = False
        while stop_loop != True:
            try:
                check = find(By. ID, f'result_{num}_name').text
                print(num)
                c_array.append(check)
                stop_loop = True
            except NameError:
                c_array = []
                stop_loop = False
            except NoSuchElementException:
                chrome.refresh()
                await asyncio.sleep(6.0)

async def pre_security(chrome, find, seid):
    global security_ver
    security_ver = None
    sticker_steam = 'Sticker' or 'Adesivo'
    capsule = 'EMS'
    while True:
        try:
            check_name = find(By. ID, seid).text
            if sticker_steam in check_name:
                print('STICKER')
                security_ver = True
                return security_ver
            elif capsule in check_name:
                print('CAPSULA')
                security_ver = True
                return security_ver
            break
        except NoSuchElementException:
            chrome.refresh()
            await asyncio.sleep(5.0)


def main(seid, find):
    find(By.ID, seid).click()

def content(chrome, find):
    global content_1, content_2, check_content_var
    check_content_var = None
    url = chrome.current_url
    while True:
        try:
            name = find(By.XPATH, '//*[@id="largeiteminfo_item_name"]').text
            exterior = find(By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]/div[1]').text
            nametag = find(By.XPATH, '//*[@id="largeiteminfo_item_descriptors"]/div[3]').text
            stickers = find(By.XPATH, '//*[@id="sticker_info"]/center').text
            nametag_display = find(By.CLASS_NAME, 'item_desc_description').text
            nametag_var = 'Name Tag:'
            if stickers:
                if nametag_var in nametag_display:
                    content_1 = (f'''
Skin: {name}
{exterior}
{nametag}
**{stickers}**
Price: $ {price}
Preço: R$ {real}
{url}

''')
                    print(content_1)
                    check_content_var = True
                    break
                else:
                    content_2 = (f'''
Skin: {name}
{exterior}
**{stickers}**
Price: $ {price}
Preço: R$ {real}
{url}

''')
                    print(content_2)
                    check_content_var = False
                    break
            else:
                print('unexpected error')
        except NoSuchElementException:
            sleep(6.0)
            chrome.refresh()

def site(find, chrome):
    stop_loop = None
    while stop_loop != True:
        try:
            if find(By.XPATH, '//*[@id="result_0"]/div[2]/span[2]') is not True:
                print('Steam loaded...')
            stop_loop = True
        except NoSuchElementException:
            chrome.refresh()
            sleep(6.0)
            stop_loop = False

async def security(chrome, find):
    global security_ver
    while True:
        try:
            namerror = find(By.CLASS_NAME, 'hover_item_name').text
            if len(namerror) != 0:
                try:
                    stickers = find(By.XPATH, '//*[@id="sticker_info"]/center').text
                    katowice = 'Katowice 2014'
                    await asyncio.sleep(2.0)
                    if katowice not in stickers:
                        print('\033[1;31mNAME TAG DETECTED\033[m')
                        security_ver = True
                    return security_ver
                except NoSuchElementException:
                    print('\033[1;31mNAME TAG DETECTED\033[m')
                    security_ver = True
                    return security_ver
            else:
                chrome.refresh()
                await asyncio.sleep(3.0)
        except NoSuchElementException:
            chrome.refresh()
            await asyncio.sleep(4.0)

async def autofinder(chrome, find):
    while True:
        await name_verifier(chrome, find)
        jsonload = json.load(open('./json/varContent.json'))
        jsonverifier = jsonload['verifier']
        jsonname = jsonload['skins_name']
        jsonregist = json.load(open('./json/autofindRegist.json'))['cancel']
        if len(jsonload) < 30:
            if jsonregist == 'True':
                break
            elif jsonname == jsonverifier:
                await asyncio.sleep(15.0)
                continue
            else:
                while len(json.load(open('./json/varContent.json'))['content']) < 30:
                    await skins_module(chrome, find)
                    break
                else: break
        return

async def load(chrome, find, xpath, seid):
    global l_array
    stop_loop = None
    await pre_security(chrome, find, seid)
    while stop_loop != True:
            if security_ver == True:
                try:
                    l_array.append('')
                    return
                except NameError:
                    l_array = []
            else:
                await get_price(chrome, xpath)
                main(seid, find)
                await security(chrome, find)
                while stop_loop != True:
                    try:
                        if security_ver == True:
                            chrome.get(cartridge)
                            l_array.append('')
                            return
                    except NameError:
                        l_array = []
                        stop_loop = False
                    else:              
                        content(chrome, find)
                        while stop_loop != True:
                            try:
                                if check_content_var == True:
                                    l_array.append(content_1)
                                    return
                                elif check_content_var == False:
                                    l_array.append(content_2)
                                    return
                            except NameError:
                                l_array = []
                                stop_loop = False
            

async def name_verifier(chrome, find):
    global names, reload_names
    chrome.refresh()
    await asyncio.sleep(3.0)
    names = []
    reload_names = []
    while True:
        try:
            find(By. ID, 'result_3_name')
            break
        except NoSuchElementException:
            chrome.refresh()
            await asyncio.sleep(7.0)
    for num in range(0, 10):
        try:
            namecontrol = find(By. ID, f'result_{num}_name').text
            names.append(namecontrol)
            reload_names.append(namecontrol)
        except NoSuchElementException:
            chrome.refresh()
            await asyncio.sleep(6.0)
    if json.load(open('./json/reloaderRegist.json'))['reloader'] == 'True':
        jsonreloader('True', reload_names)
        reload_names = None
    jsonloader()
    
async def returner(chrome, find, l_str):
    global skin, ver_name, names, l_array, c_array
    await check_names(chrome, find)
    skin = None
    names = None
    skin = l_str
    ver_name = c_array
    c_array = []
    l_array = []
    return skin

def jsonloader():
    dictionary = {
        'content': skin,
        'verifier': ver_name,
        'skins_name': names
    }

    data = json.dumps(dictionary, indent=1)
    with open('./json/varContent.json', 'w') as f:
        f.write(data)

def jsonregister(value, cancel):
    regist = {
        'register': value,
        'cancel': cancel
    }
    with open('./json/autofindRegist.json', 'w') as f:
        f.write(json.dumps(regist, indent=1))

def jsonreloader(reload_ver, reload_names):
    reload = {
        'reloader': reload_ver,
        'skins_name': reload_names
    }
    with open('./json/reloaderRegist.json', 'w') as f:
        f.write(json.dumps(reload, indent=1))


async def skins_module(chrome, find):
    for x in range(0, 10):
        jsonregist = json.load(open('./json/autofindRegist.json'))['cancel']
        if jsonregist == 'True':
            break 
        await load(chrome, find, f'//*[@id="result_{x}"]/div[1]/div[2]/span[1]/span[1]', f'result_{x}_name')
        chrome.get(cartridge)
    l_str = ''.join(map(str, l_array))
    await returner(chrome, find, l_str)
    jsonloader()
