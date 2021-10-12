# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from
# the JSON data, compute the sum of the numbers in the file and enter the sum below:

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl


#! Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1363781.json"
data = urllib.request.urlopen(url, context=ctx).read().decode()

try:
    js = json.loads(data)
except:
    js = None

total = 0
for num in js["comments"]:
    count = num["count"]
    icount = int(count)
    total = total + icount

print(total)
