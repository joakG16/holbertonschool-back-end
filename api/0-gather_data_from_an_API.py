#!/usr/bin/python3
"""
A script that, for a given employee ID, returns
information about his/her TODO list progress.
API used: https://jsonplaceholder.typicode.com/
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    num = argv[1]
    user_query = {'id': num}  # this is added as query parameter
    # that are appended to the endpoint URL
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users",
                              params=user_query)  # endpoint URL

    todo_query = {'userId': num}  # match todo list with user specified
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                              params=todo_query)

    user = response_1.json()  # .json() is a built in decoder
    # from request module, returning a list of dictionaries

    todo_list = response_2.json()

    employee_name = user[0].get('name')

    completed_tasks = 0
    total_tasks = 0
    completed_task_title = []
    for task in todo_list:
        if task.get('completed') is True:
            completed_task_title.append(task.get('title'))
            completed_tasks += 1
            total_tasks += 1
        else:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for title in completed_task_title:
        print("{} {}".format('\t', title))
