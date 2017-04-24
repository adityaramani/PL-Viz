import time
import requests
http_proxy = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy = "ftp://10.10.1.10:3128"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.premierleague.com/match/"


with open('missing.txt') as fp:
    content = fp.readlines()

for i in content:
    i= i.strip()
    path = url+str(i)
    res = requests.get(path,timeout=40,headers=headers)
    fp = open("NewPages/match - "+str(i)+".html",'wb')
    for j in res.iter_content(1000):
        fp.write(j)

    print(i)
    fp.close()
    time.sleep(10)

