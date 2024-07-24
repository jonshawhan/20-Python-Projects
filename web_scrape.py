import requests
from bs4 import BeautifulSoup

url = "https://www.codewithtomi.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all("h2", {"class":"post-title"})

print(r)
print(title)