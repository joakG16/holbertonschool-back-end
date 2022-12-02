#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export user's data in the CSV format.
API used: https://jsonplaceholder.typicode.com/
"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    num = argv[1]  # remember python3 does not count as argument

    user_query = {'id': num}  # this is added as query parameter
    # that are appended to the endpoint URL
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users",
                              params=user_query)  # endpoint URL

    todo_query = {'userId': num}  # match todo list with user specified
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                              params=todo_query)

    user = response_1.json()  # .json() is a builtin JSON decoder
    # from request module, returning a list of dictionaries in this case
    todo_list = response_2.json()

    uid_filename = f'{num}.csv'
    username = user[0].get('username')

    # remember the 'w' will overwrite any data existing in given file
    with open(uid_filename, mode='w') as employee_file:
        ''' creating writer oject to convert my data into a delimeted string'''
        ''' csv.QUOTE_ALL - Specifies the writer object to write CSV
        file with quotes around all the entries, non and numeric ones'''
        row_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL,
                                delimiter=',')

        for task in todo_list:
            ''' converting data and then writing it into the .csv file '''
            row_writer.writerow((task.get('userId'), username,
                                 task.get('completed'), task.get('title')))
