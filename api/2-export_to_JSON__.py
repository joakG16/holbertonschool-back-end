#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export user's data in the JSON format.
API used: https://jsonplaceholder.typicode.com/
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id_num = argv[1]  # Remember python3 does not count as argument

    ''' Extracting desired user/employee '''
    user_query = {'id': id_num}  # This is added as query parameter
    # that are appended to the endpoint URL
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users",
                              params=user_query)  # Endpoint URL

    ''' Extracting desired user's TODO list'''
    todo_query = {'userId': id_num}  # Match todo list with user specified
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                              params=todo_query)

    user = response_1.json()  # .json() is a builtin JSON decoder
    # from request module, returning a list of dictionaries in this case
    user_todo_list = response_2.json()

    username = user[0].get('username')
    ''' Creating list of dictionaries (user's tasks) (list comprehension)'''
    task = [{"task": task.get('title'), "username": username,
            "completed": task.get('completed')} for task in user_todo_list]

    # Creating dictionary with user as key and respective tasks as its values
    user_todo_dict = {}
    user_todo_dict[id_num] = task

    # Serializing json
    json_object = json.dumps(user_todo_dict)

    uid_filename = f'{id_num}.json'
    # Writing to json file
    with open(uid_filename, "w") as jsonfile:
        jsonfile.write(json_object)
