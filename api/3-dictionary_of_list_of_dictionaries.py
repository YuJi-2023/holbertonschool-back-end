#!/usr/bin/python3
"""create a REST API export data into json format"""
import json
import requests
import sys


if __name__ == "__main__":

    url_employee = "https://jsonplaceholder.typicode.com/users"
    response_employee = requests.get(url_employee)

    output_dict = {}
    if response_employee.status_code == 200:
        employee_data = response_employee.json()
        for employee in employee_data:
            user_name = employee.get("username")
            user_id = employee.get("id")

            url_todos = f"{url_employee}/{user_id}/todos"
            response_todos = requests.get(url_todos)
            if response_todos.status_code == 200:
                todos_data = response_todos.json()

            task_list = []
            for todo in todos_data:
                task_description = {
                    'username': user_name,
                    'task': todo.get("title"),
                    'completed': todo.get("completed"),
                    }
                task_list.append(task_description)
            output_dict[user_id] = task_list

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(output_dict))
