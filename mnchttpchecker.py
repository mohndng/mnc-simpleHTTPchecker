import requests
import time
import colorama
from colorama import Fore, Style

m = 'MnCHTTPCHECKER v0.5'
n = 'Please wait for a while..'
c = 'Success!'
mon = requests.get('http://mncreation.cf',allow_redirects=False)

time.sleep(0.5)
print(Fore.RED, m); time.sleep(1)
print(Fore.BLACK, n); time.sleep(4)
print(Fore.GREEN, c, Style.BRIGHT, mon.status_code)
print(Style.RESET_ALL)
