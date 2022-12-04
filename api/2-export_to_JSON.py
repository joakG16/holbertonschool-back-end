#!/usr/bin/python3
""" extend your Python script to export data in the CSV format """


if __name__ == '__main__':
    import requests
    from sys import argv

    u_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(u_id)
    response = requests.get(api_url).json()
    EMPLOYEE_NAME = response.get('username')
    response = requests.get(api_url2).json()
    f_name = u_id + '.csv'
    with open(f_name, 'w', encoding='utf-8') as f:
        for info in response:
            TASK_COMPLETED_STATUS = info.get("completed")
            TASK_TITLE = info.get("title")
            f.write('"{}","{}","{}","{}"\n'.format(
                u_id, EMPLOYEE_NAME, TASK_COMPLETED_STATUS, TASK_TITLE))
