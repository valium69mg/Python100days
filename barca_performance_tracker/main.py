import json 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open("player_stats.json","r") as file:
    data = json.loads(file.read())

df_all_players = pd.read_json("player_stats.json")
df_important_players = df_all_players.loc[:20]
df_goals_per_minute = df_important_players.loc[:20,["name","goals","minutes"]]
df_goals_per_minute = df_goals_per_minute.sort_values(by=["goals"],ascending=False)

names_list = []
minutes_list = []
goals_list = []
for i in range(len(df_goals_per_minute)):
    df_names = df_goals_per_minute.loc[:,["name"]]
    df_goals = df_goals_per_minute.loc[:,["name","goals"]]
    df_minutes = df_goals_per_minute.loc[:,["name","minutes"]]
    # NAMES
    name = df_names.iloc[i].item()
    names_list.append(name)
    # GOALS
    goals_per_player = df_goals.loc[df_goals["name"] == name]
    goals = goals_per_player.iat[0,1]
    goals_list.append(goals)
    # MINUTES
    minutes_per_player = df_minutes.loc[df_minutes["name"] == name]
    minutes = minutes_per_player.iat[0,1]
    minutes_list.append(minutes)

goals_list = np.array(goals_list)
minutes_list = np.array(minutes_list)

print(goals_list)
print(minutes_list)


fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

plt.scatter(x=minutes_list,y=goals_list,s=300)
plt.xticks(rotation=90)


for i,txt in enumerate(names_list):
    ax.text(minutes_list[i],goals_list[i],txt)

plt.show()