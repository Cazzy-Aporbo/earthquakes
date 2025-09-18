import requests 
import json
import pprint

data = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
data = data.json()
print(type(data))
print(len(data))
print(data.keys())

feature = data["features"]
print(len(feature))

coor = feature[0]["geometry"]["coordinates"]
print(coor)

print(data)
pprint.pprint(data)