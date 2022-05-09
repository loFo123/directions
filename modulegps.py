# get geolocation using ip
#import urllib.request
#import json

#apistack_key = "d8105a271b914d3574b81aecb70d4a36"
#location_req = "http://api.ipstack.com/check?access_key={}".format(apistack_key)
#geo_req = urllib.request.urlopen(location_req)
#geo_json = json.loads(geo_req.text)
#print(geo_json)

from geopy.geocoders import Nominatim
import time
from pprint import pprint
app = Nominatim(user_agent="tutorial")
location = app.geocode("My+Location").raw
pprint(location)