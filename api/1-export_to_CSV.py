#!/usr/bin/python3
""" export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url).json()

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(url).json()

    uid_filename = f'{num}.csv'
    with open(uid_filename, mode='w') as employee_file:
        row_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL,
                                delimiter=',')
        for task in todo_list:
            row_writer.writerow((task.get('userId'), user[0].get('username'),
                                 task.get('completed'), task.get('title')))
