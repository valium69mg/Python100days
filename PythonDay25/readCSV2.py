import pandas

data = pandas.read_csv("Python day 25\weather_data.csv")

data_dict = data.to_dict()

#AVG temp simplified
temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)

#Max value
max_temp = data["temp"].max()
#Max value with row 
max_temp_day = data[data.temp == data.temp.max()]


def celsius_to_farenheit(celsius):
    temperature_farenheit = (9/5)*celsius+32
    return temperature_farenheit

# Max_temp_day to farenheit
max_temp_celsius = max_temp_day.temp.to_list()[0]
max_temp_farenheit =celsius_to_farenheit(max_temp_celsius)

# Create data frame from scratch
data_dict = {
    "students": ["Amy","Angela","James"],
    "scores": [76,56,65]
}

data_from_dict = pandas.DataFrame(data_dict)
print(data_from_dict)