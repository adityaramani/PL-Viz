import csv
import copy

features = []
d ={
"type":"Feature",
"geometry" : {
 "type": "Point",
  "coordinates":[]
},
"properties":{
"name":"",
"home" :"",
"id":""
}
}

fp = open("../stadiums.csv","r")
reader = csv.reader(fp)
next(reader)

for row in reader:
    d["geometry"]["coordinates"] = [  float(row[6]), float(row[5])]
    d["properties"]["name"] = row[3]
    d["properties"]["home"] = row[0]
    d["properties"]["id"] = row[-1]

    features.append(copy.deepcopy(d))


for i in features:
    print(i)


final = {

"type" :"FeatureCollection",
"features" : features
}
import json

fo = open("stadium-info.json" ,"w")
x=json.dumps(final)
fo.write(str(x))
fo.close()
