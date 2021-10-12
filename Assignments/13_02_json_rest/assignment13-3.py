# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve
# the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

#! Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://py4e-data.dr-chuck.net/json?"

while True:
    address = input("Enter location: ")
    key = 42
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    parms["key"] = key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retreiveing", url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(js["results"][0]["place_id"])
