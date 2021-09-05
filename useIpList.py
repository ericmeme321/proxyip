import csv
import requests
from colorama import Fore, Back, Style

headers = {'User-Agent':'Mozilla/5.0'}
with open('ip.csv','r') as f:
    lines = csv.reader(f)
    for i in lines:
        ip = i
        break
    for i in range(len(ip)):
        try:
            res = requests.get('https://www.youtube.com/?hl=zh-TW&gl=TW', proxies={'http':ip[i], 'https':ip[i]}, timeout=5)
            print(Fore.GREEN + 'SUCCESS',Style.RESET_ALL + ip[i])
        except:
            print(Fore.RED + 'FAIL',Style.RESET_ALL + ip[i])