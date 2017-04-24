__author__ = 'aditya'

import sys
import json
import csv
import collections

id= sys.argv[1].strip()
sys.stdout.flush()
fp = open('./public/team data/' +id +'.csv', 'r')
reader = csv.reader(fp)
headings = next(reader)

outcome =[]
homescore = []
awayscore = []


for row in reader:
        outcome.append(row[14])
        homescore.append(int(row[10]))
        awayscore.append(int(row[11]))

played = len(outcome)
outcome = collections.Counter(outcome)
goalsscored = sum(homescore)
goalsconceded = sum(awayscore)
cleansheets = awayscore.count(0)
homewins = outcome['H']
awaywins = outcome['A']
draws = outcome['D']
pointswon =  3*homewins

d = {
    'teamName' : row[4],
    'stadium' : row[15],
    'played': played,
    'goalsScored' : goalsscored,
    'goalsConceded' : goalsconceded,
    'cleanSheets' : cleansheets,
    'win':homewins,
    'lose':awaywins,
    'draws':draws,
    'points':pointswon
}

jdata = json.dumps(d)

fp.close()
print(jdata)
