import datetime as dt
import logging

logging.basicConfig(level=logging.DEBUG)

file_to_open = r"log.txt"
data_list = []
unique_tasks_list = []

def read_file(name):
    process = ["date", "operation", "name", "condition"]
    with open(name, 'r') as opened_file:
        opened_file = opened_file.readlines()
    for line in opened_file:
        details = line.split(" ")
        details = [x.strip() for x in details]
        # structure = {key: value for key, value in zip(process, details)}
        data_list.append(details)
    return(data_list)

def get_unique_tasks(raw_data):
# TODO get rid of this for and use something like
# unique_data = [list(x) for x in set(tuple(raw_data[x][2]) for x in range(len(raw_data)))]
    for x in range(len(raw_data)):
        if raw_data[x][2] not in unique_tasks_list:
            unique_tasks_list.append(raw_data[x][2])
    return(unique_tasks_list)


def slurp_data(slurp_data_list, slurp_unique_tasks_list):
    return()

def main():
    read_file(file_to_open)
    get_unique_tasks(data_list)
    slurp_data(data_list, unique_tasks_list)

if __name__ == "__main__":
    main()
