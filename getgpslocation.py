import urllib.request
import json
import sys
import time
import datetime

# URL to the tomtom api
apiURL      = "https://api.tomtom.com/routing/1/calculateRoute/"
# apiKey
apiKey      = "G89haUklUHcqMVpq4kM2QDyGV54GlqTh"

#[coordinates]
sourceLat   = 51.5560241
sourceLon   = -0.2817075
destLat     = 53.4630621
destLon     = -2.2935288

#tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % 
#(apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)
tomsearchUrl="https://api.tomtom.com/search/2/geocode/my+location.json?key=G89haUklUHcqMVpq4kM2QDyGV54GlqTh"

getData = urllib.request.urlopen(tomsearchUrl).read()
jsonTomsearchDict = json.loads(getData)
print(jsonTomsearchDict)