from bs4 import BeautifulSoup
import requests
import json
import time

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://www.premierleague.com/match/"
var = 3666
for j in range(4940,    6000 ):
    path = url + str(j)
    res = requests.get(path,timeout=40,headers=headers)
    fp = open("Pages/match - "+str(j)+".html",'wb')
    for i in res.iter_content(1000):
        fp.write(i)

    fp.close()
    fp = open("Pages/match - "+str(j)+".html",'r',encoding="utf-8")
    soup = BeautifulSoup(fp)

    data = soup.find("div",class_="mcTabsContainer")
    try:
        data = data.get('data-fixture')
    except Exception as e:
        continue

    y= data
    data1 = json.loads(data)

    try:
        hometeam = soup.find("div",class_ ="team home").find(class_ = "short").text

    except Exception as e:
            hometeam =""
    try:
        awayteam = soup.find("div",class_ ="team away").find(class_ = "short").text
    except Exception as e:
        awayteam = ""

    time1 = data1["kickoff"]["label"]
    time1 = time1[0 : time1.index(",")]
    time1.replace(" ","")

    op = open("Output/"+hometeam+awayteam+time1+".json",'w')
    op.write(data)
    op.close()
    time.sleep(15)
