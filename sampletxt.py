import urllib.request
import json
# endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
# api_key = 'AIzaSyB0pIAbFzRkYFY0nEsDMjzbKLNseUQH61A'
# origin = input('Where r u ').replace(' ','+')
# destination = input('where to ').replace(' ','+')
# nav_request = 'origin={}&destination{}&key={} '.format(origin,destination,api_key)
# req = endpoint + nav_request
url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&avoid=highways&mode=bicycling&key=AIzaSyB0pIAbFzRkYFY0nEsDMjzbKLNseUQH61A"
response = urllib.request.urlopen(url).read()
directions = json.loads(response)
print(directions)
