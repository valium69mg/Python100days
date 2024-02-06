import pandas

data = pandas.read_csv("PythonDay25/2018_Central_Park_Squirrel_Census.csv")

data_furr_gray = data[data['Primary Fur Color'] == 'Gray']
gray_squirrel_count = len(data_furr_gray) # Number of gray squirrels

data_furr_black = data[data['Primary Fur Color']=='Black']
black_squirrel_count = len(data_furr_black)

data_furr_cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
cinnamon_squirrel_count = len(data_furr_cinnamon)

data_dict = {
    "Fur Color": ["Gray","Black","Cinnamon"],
    "Count": [gray_squirrel_count,black_squirrel_count,cinnamon_squirrel_count]
}

df = pandas.DataFrame(data_dict)
print(df)
# df.to_csv("squirrel_count.csv")