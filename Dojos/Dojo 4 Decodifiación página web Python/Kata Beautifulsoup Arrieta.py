import urllib.request
from bs4 import BeautifulSoup

url = "https://www.diariodecadiz.es/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

tags = soup.find("main").find_all('a', class_="lnk")

for tag in tags:
    print(tag.get_text())