import urllib.request
import json
url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&avoid=highways&mode=bicycling&key=AIzaSyB0pIAbFzRkYFY0nEsDMjzbKLNseUQH61A"

payload={}
headers = {}

response = urllib.request.request("GET", url, headers=headers, data=payload)

print(response.text)