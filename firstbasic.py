import urllib.request
import json
import sys
import time
import datetime

from geographiclib.geodesic import Geodesic

# URL to the tomtom api
apiURL      = "https://api.tomtom.com/routing/1/calculateRoute/"
# apiKey
apiKey      = "G89haUklUHcqMVpq4kM2QDyGV54GlqTh"

geod = Geodesic.WGS84

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
coordinates =legs[0]["points"]

current_point = coordinates[0]
total_length=0

# this functions gives directions
def getDirection(angle,distance):
     if angle < 0:
        angle = 360 + angle 
        print(str(angle))
     else :
        print(str(angle))


for x in range(1,(len(coordinates) -1)):
   next_point = coordinates[x]
   g = geod.Inverse(current_point['latitude'],current_point['longitude'],next_point['latitude'],next_point['longitude'])
   total_length += g['s12']
   getDirection(g['azi2'],g['s12'])
   print()
   current_point = coordinates[x]
print()
print("reached destination")
print("total distance covered :" + str(total_length))
print()
     
