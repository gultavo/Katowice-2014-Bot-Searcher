# from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import json
from time import sleep
import requests
import locale
from datetime import datetime
current_time = datetime.now().strftime("%H:%M:%S")

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
economyapi = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
request = requests.get(economyapi)
response = request.json()
low = float(response['USDBRL']['high'])

cartridge = 'https://steamcommunity.com/market/search?descriptions=1&category_730_ItemSet%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=&q=%22Katowice+2014%22#p3_price_asc'

# FAZ AS CONTAS DO PREÇO (CONVERSÃO) E É A FUNÇÃO PRINCIPAL
def get_price(chrome, xpath):
    global price, real
    sleep(4.0)
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
            sleep(6.0)

def check_names(chrome, find, seid):
    while True:
        try:
            check = find(By. ID, seid).text
            return check
        except NoSuchElementException:
            chrome.refresh()
            sleep(6.0)

def pre_security(chrome, find, seid):
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
            sleep(5.0)


def main(seid, find):
    find(By.ID, seid).click()


# IMPRIME O CONTEÚDO DA PÁGINA (QUE PRECISA)

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


# VERIFICA SE O SITE FOI CARREGADO CORRETAMENTE

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

# FUNÇÃO DE SEGURANÇA CASO O ITEM FOR OUTRA COISA QUE NÃO QUER

def security(chrome, find):
    global security_ver
    while True:
        try:
            namerror = find(By.CLASS_NAME, 'hover_item_name').text
            if (len(namerror) != 0):
                try:
                    stickers = find(By.XPATH, '//*[@id="sticker_info"]/center').text
                    katowice = 'Katowice 2014'
                    sleep(2.0)
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
                sleep(3.0)
        except NoSuchElementException:
            chrome.refresh()
            sleep(4.0)

def load(chrome, find, xpath, seid):
    pre_security(chrome, find, seid)
    if security_ver == True:
        return ''
    else:
        get_price(chrome, xpath)
        main(seid, find)
        security(chrome, find)
        if security_ver == True:
            chrome.get(cartridge)
            return ''
        else:
            content(chrome, find)
            if check_content_var == True:
                return content_1
            elif check_content_var == False:
                return content_2

def name_verifier(chrome, find):
    global names
    chrome.refresh()
    names = []
    while True:
        try:
            find(By. ID, 'result_3_name')
            break
        except NoSuchElementException:
            chrome.refresh()
            sleep(6.0)
    for num in range(1, 9):
        try:
            namecontrol = find(By. ID, f'result_{num}_name').text
            names.append(namecontrol)
        except NoSuchElementException:
            chrome.refresh()
            sleep(6.0)
    jsonloader()
    
def returner(l_str, c_array):
    global skin, ver_name, names
    skin = None
    names = None
    skin = l_str
    ver_name = c_array
    return skin

def jsonloader():
    dictionary = {
        'content': skin,
        'time': current_time,
        'verifier': ver_name,
        'skins_name': names
    }

    data = json.dumps(dictionary, indent=1)
    with open('varContent.json', 'w') as f:
        f.write(data)