import csv
import requests
from fake_useragent import UserAgent
from requests_html import HTMLSession
from colorama import Fore, Back, Style

session = HTMLSession()

url = 'https://www.proxydocker.com/en/proxylist/country/Taiwan'



i = 1
iplist = []
headers = {'User-Agent':'Mozilla/5.0'}
while 1:
    try:
        r = session.get(url, headers=headers)
        code = r.status_code
        print(code)
        r.html.render(sleep=1, keep_page=True, scrolldown=1)
        ip = r.html.xpath(f'//*[@id="proxylist_table"]/tr[{i}]/td[1]', first=True).text
        port = r.html.xpath(f'//*[@id="proxylist_table"]/tr[{i}]/td[2]', first=True).text
        if 'SOCK' not in port:
            port = port.lower()
        iplist.append(str(port) + '://' + str(ip))
        i+=1
    except Exception as e:
        print(e)
        print(Fore.GREEN + "IP list be downloaded is success!\n" + Style.RESET_ALL)
        break


ValidIpList = []
for ip in iplist:
    try:
        res = requests.get('https://www.youtube.com/?hl=zh-TW&gl=TW', proxies={'http':ip, 'https':ip}, timeout=5)
        ValidIpList.append(ip)
        print(Fore.GREEN + 'SUCCESS',Style.RESET_ALL + ip)
    except:
        print(Fore.RED + 'FAIL',Style.RESET_ALL + ip)

with open('ip.csv', 'w') as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerow(ValidIpList)

print(Fore.YELLOW + "Valid ip list has been completed." + Style.RESET_ALL)


    