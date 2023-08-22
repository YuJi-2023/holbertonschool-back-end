#!/usr/bin/python3
"""create a REST API to return employee info"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    url_employee = f"{url}users/{sys.argv[1]}/"
    url_todos = f"{url}users/{sys.argv[1]}/todos"
    response_employee = requests.get(url_employee)
    response_todos = requests.get(url_todos)
    employee_data = response_employee.json()
    todos_data = response_todos.json()

    user_id = sys.argv[1]
    user_name = employee_data.get("username")

    task_list = []
    for todo in todos_data:
        todo_description = {
            'USER_ID': str(user_id),
            'USERNAME': user_name,
            'TASK_COMPLETED_STATUS': todo.get('completed'),
            'TASK_TITLE': todo.get('title')
            }
        task_list.append(todo_description)
    filename = user_id + ".csv"
    with open(filename, 'w', newline='') as f:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        writer.writerows(task_list)
