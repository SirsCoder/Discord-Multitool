import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("Nuck V1 | Made by .aku_ccp| Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)