import pandas
import csv

#Temperatures in CSV file
with open("PythonDay25\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if (row[1] != 'temp'):
            temperatures.append(int(row[1]))


data = pandas.read_csv("Python day 25\weather_data.csv")
print(data) #Table
print("============================")
print("Temperature on monday: "+ str(data.iloc[0].temp))
print("Condition on friday: " + str(data.iloc[4].condition))
#Temp table
print(data.temp)