__author__ = 'aditya'

import json
import os
import csv
from bs4 import BeautifulSoup

files = next(os.walk("../Filtered/Premier League/"))[2]
fp = open('../data.csv', 'w')
writer = csv.writer(fp)
writer.writerow('Season,Competition,GameWeek,Kick-off Time,' +
             'Home Team Name,Home Team Abbr,Home Team id,' +
             'Away Team Name,Away Team Abbr,Away Team id,' +
             'Home Score,Away Score,HT Home Score,HT Away Score,Outcome' +
             'Ground Name,Ground Location,Ground Id,Attendance' +
             'Referee Name,Referee Id')

for name in files:
    page = open('../Filtered/Premier League/'+name, 'r', encoding = 'utf-8')
    soup = BeautifulSoup(page)
    print(name)
    op = open('../Output/'+name[:len(name)-4]+'.json','w')
    data = soup.find('div', class_ = 'mcTabsContainer').get('data-fixture')
    jdata = json.loads(data)
    row = []
    entry = {}

    season = jdata["gameweek"]["compSeason"]['label']
    comp = jdata["gameweek"]["compSeason"]['competition']['description']
    gw = jdata["gameweek"]["gameweek"]
    kotime =  jdata["kickoff"]["label"]
    homeLong = jdata["teams"][0]['team']["name"]
    homeabbr = jdata["teams"][0]['team']["club"]["abbr"]
    homescore = jdata["teams"][0]["score"]
    homeid = jdata["teams"][0]['team']["club"]["id"]
    awayLong = jdata["teams"][1]['team']["name"]
    awayabbr = jdata["teams"][1]['team']["club"]["abbr"]
    awayscore = jdata["teams"][1]["score"]
    awayid = jdata["teams"][1]['team']["club"]["id"]
    ground = jdata["ground"]["name"]
    groundloc = jdata["ground"]["city"]
    groundid = jdata["ground"]["id"]
    outcome = jdata['outcome']
    attendance = jdata['attendance']
    refereename = jdata['matchOfficials'][0]['name']['display']
    refid = jdata['matchOfficials'][0]['matchOfficialId']
    halftimescorehome = jdata['halfTimeScore']['homeScore']
    halftimescoreaway = jdata['halfTimeScore']['awayScore']

    row = [season, comp, gw, kotime,
           homeLong, homeabbr, homeid,
           awayLong, awayabbr, awayid,
           homescore, awayscore, halftimescorehome, halftimescoreaway, outcome,
           ground, groundloc, groundid, attendance,
           refereename, refid]
    entry['season'] = season
    entry['competition'] = comp
    entry['gameweek'] = gw
    entry['koTime'] = kotime
    entry['homeTeamName'] = homeLong
    entry['homeTeamAbbr'] = homeabbr
    entry['homeTeamId'] = homeid
    entry['awayTeamName'] = awayLong
    entry['awayTeamAbbr'] = awayabbr
    entry['awayTeamId'] = awayid
    entry['homeScore'] = homescore
    entry['awayScore'] = awayscore
    entry['htHomeScore'] = halftimescorehome
    entry['htAwayScore'] = halftimescoreaway
    entry['outcome'] = outcome
    entry['ground'] = ground
    entry['groundLoc'] = groundloc
    entry['groundId'] = groundid
    entry['attendance'] = attendance
    entry['referee'] = refereename
    entry['refereeId'] = refid
    op.write(str(entry))
    op.close()
    writer.writerow(row)


fp.close()

