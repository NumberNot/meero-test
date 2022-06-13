import datetime as dt
import json

today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_name = "log.txt"
file = open(file_name, "r")
data = []
unique_lst = []
run_time_count = []
process = ["date", "operation", "name", "condition"]

# function unique tasks
def occur (unique_item):
    for unique_item in data:
        if unique_item["name"] == item:
            unique_lst.append(unique_item)
    return(unique_lst)

# main part starts here
# read fron file
for line in file.readlines():
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(process, details)}
    data.append(structure)

# grab tasks by name from list
res = set([sub['name'] for sub in data])

# slurp tasks
for item in res:
    occur(item)
    print('Task: ', item)
    print(json.dumps(unique_lst, indent=4))
# get condition Start/End for specific task
    for items in range(len(unique_lst)):
        condition = [sub['condition'] for sub in unique_lst]
        time_period = [dt.datetime.strptime(
            sub['date'], '%Y-%m-%dT%H:%M') for sub in unique_lst]
# check tasks without end
        try:
            if str(condition[items]) == "Start" and str(condition[items+1]) == "End":
                run_time = dt.datetime.strptime(str(time_period[items+1]), '%Y-%m-%d %H:%M:%S')-dt.datetime.strptime(
                    str(time_period[items]), '%Y-%m-%d %H:%M:%S')
                print
                print('Task duration: ')
                print(str(run_time))
                print
                run_time_count.append(run_time)
# have a deal with tasks without end
        except:
            run_time = dt.datetime.strptime(str(today), '%Y-%m-%d %H:%M:%S')-dt.datetime.strptime(
                    str(time_period[items]), '%Y-%m-%d %H:%M:%S')
            print
            print('Task duration: ')
            print(str(run_time))
            print
            run_time_count.append(run_time)
    unique_lst = []
print
print("Sum up -----------------------------")
print(sum(run_time_count, dt.timedelta())/len(run_time_count))
