from bs4 import BeautifulSoup
import requests
"""
WE WILL BE SCRAPING A LIVE PAGE
WE WILL BE SCRAPING A A BIBLE VERSE
FROM THE WEBSITE BELOW
"""

URL = "https://dailyverses.net/random-bible-verse"

res = requests.get(url=URL)
res.raise_for_status()
contents = res.text
soup = BeautifulSoup(contents,"html.parser")
verse = soup.find(name="span",class_="v1").getText()
title = soup.find(name="a",class_="vc").getText()

print("\n"+title)
print(verse)