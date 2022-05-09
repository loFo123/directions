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
sourceLat   = 10.426689
sourceLon   = 76.330303
destLat     = 10.425771
destLon     = 76.319124

tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)

getData = urllib.request.urlopen(tomtomURL).read()
#json data
jsonTomTomDict = json.loads(getData)
routes=jsonTomTomDict['routes']
# routes is a list
main_route=routes[0]
#main route is dictionary
legs=main_route["legs"]
# points is a key
point =legs[0]["points"]
print(point)
