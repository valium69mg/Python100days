import os 
from bs4 import BeautifulSoup

os.chdir("Python 100 DAYS/web_scraping")

with open(file="website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

# print the title
title_str = soup.title.string
# print first paragraph
first_paragraph = soup.p
# find all anchor tags
all_anchors = soup.find_all(name="a")

# find all strings inside anchor tag
for tag in all_anchors:
    # get the text str
    a_text = tag.getText()
    print(a_text)
    # get the link
    print(tag.get("href"))

# find particular  element
section_heading = soup.find(name="h3",class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a") # CSS SELECT0R
print(company_url)