import requests
import colorama
from colorama import Fore, Back, Style

response = requests.get("http://monding.hopto.org")

print(Fore.YELLOW, Back.BLUE + "RESPONSE CODE")
print(Style.RESET_ALL)
print(Fore.GREEN, Style.BRIGHT, response.status_code)
