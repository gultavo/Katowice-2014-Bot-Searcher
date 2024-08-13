from utils.functions import load, returner, jsonloader, check_names, cartridge

def skins_module(chrome, find):
    l_array = []
    c_array = []
    for x in range(1, 9):
        loader = load(chrome, find, f'//*[@id="result_{x}"]/div[1]/div[2]/span[1]/span[1]', f'result_{x}_name')
        chrome.get(cartridge)
        checknames = check_names(chrome, find, f'result_{x}_name')
        l_array.append(loader)
        c_array.append(checknames)
        l_str = ''.join(map(str, l_array))
    returner(l_str, c_array)
    jsonloader()