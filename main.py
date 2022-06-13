from ast import Index
import datetime as dt
from distutils.log import error

today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        condition = [sub['condition'] for sub in unique_lst]
        time_period = [dt.datetime.strptime(
            sub['date'], '%Y-%m-%dT%H:%M') for sub in unique_lst]
        try:
            if str(condition[items]) == "Start" and str(condition[items+1]) == "End":
                run_time = dt.datetime.strptime(str(time_period[items+1]), '%Y-%m-%d %H:%M:%S')-dt.datetime.strptime(
                    str(time_period[items]), '%Y-%m-%d %H:%M:%S'), dt.timedelta()
                print(str(run_time[0]))
        except:
            run_time = dt.datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S')-dt.datetime.strptime(
                    str(time_period[items]), '%Y-%m-%d %H:%M:%S'), dt.timedelta()
            print(str(run_time[0]))
    unique_lst = []

