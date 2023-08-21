#!/usr/bin/python3
"""create a REST API to return employee info"""
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
        e_name = employee_data.get("name")
        response_todos = requests.get(url_todos)
        if response_todos.status_code == 200:
            todos_data = response_todos.json()
            todos_total = len(todos_data)
            todos_completed = 0
            for todo in todos_data:
                if todo.get("completed") is True:
                    todos_completed += 1
            print(f"Employee {e_name} is done with tasks({todos_completed}\
/{todos_total}):")
            for todo in todos_data:
                if todo.get("completed") is True:
                    print(f"\t {todo.get('title')}")
