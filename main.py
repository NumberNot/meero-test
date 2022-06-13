import json

file_name = "log.txt"
file = open(file_name, "r")
data = []
process = ["date", "time", "operation", "name", "condition"]

for line in file.readlines():
    line = line.replace("T", " ",1)
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(process, details)}
    data.append(structure)
    # data.append(details)
print(data)
# for entry in data:
#     print(json.dumps(entry, indent = 4))

