__author__ = 'aditya'

import csv

fp = open('../data.csv' , 'r')
reader = csv.reader(fp)
heading = next(reader)

data = []
for row in reader:
    data.append(row)
fp.close()
homeid = set( [ (i[6], i[4]) for i in data ])

for id in homeid:
    fo = open('../team data/'+str(id[0]) +'.csv' , 'w', newline='' )
    w = csv.writer(fo)
    w.writerow(heading)
    for row in data:
        if(row[6] == id[0]):
            w.writerow(row)

    fo.close()