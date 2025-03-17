import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(sum(temp_list) / len(temp_list), data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

#Create a Dataframe from scratch
data_dict = {
    "students": ["A", "B", "C"],
    "scores": [33,53,65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")