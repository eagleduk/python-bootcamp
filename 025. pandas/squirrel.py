import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250317.csv")

temp_dict = {}
for d in data["Primary Fur Color"]:
    if d != "NaN" and temp_dict.get(d) is None:
        temp_dict[d] = 0
    else:
        temp_dict[d] += 1

data_dict = {
    "Fur Color": [],
    "Counts": []
}

for k in temp_dict.keys():
    data_dict["Fur Color"].append(k)
    data_dict["Counts"].append(temp_dict[k])

df = pandas.DataFrame(data_dict)
print(df)
