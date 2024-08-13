from time import sleep
from utils.functions import cartridge, site
from utils.chrome_find import *
from utils.func_loader import *

chrome.get(cartridge)
sleep(4.0)
site(find, chrome)

from utils.bot import *