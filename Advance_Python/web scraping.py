import requests
from bs4 import BeautifulSoup

url="https://www.rcpit.ac.in/"
req=request.get(url)
soup=BeautifulSoup(req.content,"html.parser")
print(soup)

