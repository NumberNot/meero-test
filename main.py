from ast import Index
import datetime as dt

today = dt.date.today()

file_name = "log.txt"
file = open(file_name, "r")
data = []
unique_lst = []
process = ["date", "operation", "name", "condition"]

def occur (unique_item):
    for unique_item in data:
        if unique_item["name"] == item:
            unique_lst.append(unique_item)
    return(unique_lst)

for line in file.readlines():
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(process, details)}
    data.append(structure)

# time = [dt.datetime.strptime(
#     sub['date'], '%Y-%m-%dT%H:%M') for sub in data]
res = set([sub['name'] for sub in data])

for item in res:
    occur(item)
    print(unique_lst)
    for items in range(len(unique_lst)):
        a = [sub['condition'] for sub in unique_lst]
        try:
            if str(a[items]) == "Start" and str(a[items+1]) == "End":
                print(a[items])
                print(a[items+1])
        except:
            print("No end")
        time_period = [dt.datetime.strptime(
            sub['date'], '%Y-%m-%dT%H:%M') for sub in unique_lst]
        # print(time_period[items])
    unique_lst = []

