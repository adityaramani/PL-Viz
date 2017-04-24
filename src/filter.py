__author__ = 'aditya'

import os
from bs4 import BeautifulSoup
import json

path = "/media/aditya/New Volume/Coding/Web Development/FootBall Data/Filtered/"
newPath ="/media/aditya/New Volume/Coding/Web Development/FootBall Data/Filtered/Premier League/"
pages = next(os.walk(path))

for name in pages[2]:
    url = path + name
    fp = open(url, 'r', encoding='utf-8')
    soup = BeautifulSoup(fp)
    div = soup.find('div', class_='mcTabsContainer')
    if(div):
        data = json.loads(div.get('data-fixture'), encoding='utf-8')
        if(data['gameweek']['compSeason']['competition']['description']=='Premier League'):
            os.rename(url, newPath+name)







