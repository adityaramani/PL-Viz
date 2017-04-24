__author__ = 'aditya'


import json
import csv
import collections

fp = open('team data/Arsenal-1.csv', 'r')
reader = csv.reader(fp)
headings = next(reader)

id= 1
outcome =[]
homescore = []
awayscore = []
for row in reader:
        outcome.append(row[14])
        homescore.append(int(row[10]))
        awayscore.append(int(row[11]))

played = len(outcome)
outcome = collections.Counter(outcome)
print(outcome)
goalsscored = sum(homescore)
goalsconceded = sum(awayscore)
cleansheets = awayscore.count(0)
homewins = outcome['H']
awaywins = outcome['A']
draws = outcome['D']
pointswon =  3*homewins

d = {
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

fo = open(str(id)+'.json', 'w')

fo.write(str(jdata))