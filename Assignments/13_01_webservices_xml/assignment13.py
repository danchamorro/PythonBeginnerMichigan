# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from
# the XML data, compute the sum of the numbers in the file.

# ** Primary research link: https://www.datacamp.com/community/tutorials/python-xml-elementtree found inter() to use.
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl


#! Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1363780.xml"
xml = urllib.request.urlopen(url, context=ctx)

tree = ET.parse(xml)
root = tree.getroot()

total = 0
for num in root.iter('count'):
    inum = int(num.text)
    total = total + inum
print(total)
