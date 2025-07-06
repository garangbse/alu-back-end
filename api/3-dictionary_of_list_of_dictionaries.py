#!/usr/bin/python3
"""Exports data of all employees to JSON format"""

import json
import requests


def export_all_employees_todo():
    """Export all employees' TODO list to JSON"""
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Get all todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create dictionary to store all employee data
    all_employees = {}

    # Process each user
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')

        # Get todos for this user
        user_todos = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                user_todos.append(todo)

        # Format todos for this user
        formatted_todos = []
        for todo in user_todos:
            formatted_todos.append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

        all_employees[user_id] = formatted_todos

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_employees, jsonfile)


if __name__ == "__main__":
    export_all_employees_todo()
