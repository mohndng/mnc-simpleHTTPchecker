import requests
import colorama
from colorama import Fore, Back, Style

response = requests.get("http://monding.hopto.org")

print(Fore.YELLOW + "Raymund is checking...")
print(Style.RESET_ALL)
print(Fore.GREEN, Style.BRIGHT, response.status_code)
