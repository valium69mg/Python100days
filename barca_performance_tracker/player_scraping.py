import requests
from bs4 import BeautifulSoup
import json 

URL_FBREF = "https://fbref.com/es/equipos/206d90db/Estadisticas-de-Barcelona"

res = requests.get(url=URL_FBREF)
res.raise_for_status()
contents = res.text
soup = BeautifulSoup(contents,"html.parser")
content = soup.find(id="div_stats_standard_12")
tables = content.find("table",class_="stats_table")
body = tables.find("tbody") # BODY OF TABLE
rows = body.find_all("tr") # ROWS OF BODY 
data = []

# SET 1 OF PLAYERS
for i in range(0,20):
    row = rows[i] #tr
    name = row.find("th").text
    country = row.find("span").text
    games = row.find(attrs={"data-stat":"games"}).text
    position = row.find(attrs={"data-stat":"position"}).text
    age = row.find(attrs={"data-stat":"age"}).text
    goals = row.find(attrs={"data-stat":"goals"}).text
    minutes = row.find(attrs={"data-stat":"minutes"}).text
    minutes = minutes.replace(",", "")
    assists = row.find(attrs={"data-stat":"assists"}).text
    goals_and_assists = row.find(attrs={"data-stat":"goals_assists"}).text
    yellow_card = row.find(attrs={"data-stat":"cards_yellow"}).text
    red_card = row.find(attrs={"data-stat":"cards_red"}).text
    non_penalty_goals = row.find(attrs={"data-stat":"goals_pens"}).text
    expected_goals = row.find(attrs={"data-stat":"xg"}).text
    #INT MANAGEMENT
    if (goals == "" or minutes == "" or assists == "" or goals_and_assists == ""):
        goals = 0
        minutes = 0
        assists = 0
        goals_and_assists = 0
    player = {
        "name":name,
        "country":country,
        "games":int(games),
        "position":position[2:],
        "age":int(age[:2]),
        "goals":int(goals),
        "minutes":int(minutes),
        "assists":int(assists),
        "goals_and_assists":int(goals_and_assists),
        "yellow_card":yellow_card,
        "red_card":red_card,
        "non_penalty_goals":non_penalty_goals,
        "expected_goals":expected_goals
    }

    data.append(player)


json_data = json.dumps(data,indent=13)

with open("player_stats.json","w") as file:
    file.write(json_data)


