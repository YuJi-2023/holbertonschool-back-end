#!/usr/bin/python3
"""create a REST API export data into json format"""
import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    employee_id = int(employee_id)

    url = "https://jsonplaceholder.typicode.com/"
    url_employee = f"{url}users/{employee_id}/"
    response_employee = requests.get(url_employee)
    url_todos = f"{url}users/{employee_id}/todos"

    if response_employee.status_code == 200:
        employee_data = response_employee.json()
        user_name = employee_data.get("username")
        user_id = employee_id

        response_todos = requests.get(url_todos)
        if response_todos.status_code == 200:
            todos_data = response_todos.json()

        task_list = []
        for todo in todos_data:
            task_description = {
                'task': todo.get("title"),
                'completed': todo.get("completed"),
                'username': user_name
                }
            task_list.append(task_description)
    output_dict = {
            user_id: task_list
            }
    filename = str(user_id) + ".json"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(output_dict))
