import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/known_by_Saffa.html"
link_line = int(input("Enter position: ")) - 1
count = int(input("Enter count: "))

while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    print(url)
    url = tags[link_line].get("href", None)
    count = count - 1
