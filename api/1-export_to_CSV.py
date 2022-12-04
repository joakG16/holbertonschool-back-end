#!/usr/bin/python3
""" export data in the CSV format """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    num = argv[1]
    user_query = {'id': num}
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users",
                              params=user_query)
    todo_query = {'userId': num}
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                              params=todo_query)
    user = response_1.json()
    todo_list = response_2.json()

    uid_filename = f'{num}.csv'
    with open(uid_filename, mode='w') as employee_file:
        row_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL,
                                delimiter=',')
        for task in todo_list:
            row_writer.writerow((task.get('userId'), user[0].get('username'),
                                 task.get('completed'), task.get('title')))
