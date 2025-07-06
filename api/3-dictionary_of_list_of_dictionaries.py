import json
import requests

#!/usr/bin/python3
"""Exports data of all employees to JSON format"""



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
        user_id = str(user['id'])
        username = user['username']
        
        # Get todos for this user
        user_todos = [todo for todo in todos if todo['userId'] == user['id']]
        
        # Format todos for this user
        formatted_todos = []
        for todo in user_todos:
            formatted_todos.append({
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            })
        
        all_employees[user_id] = formatted_todos
    
    # Write to JSON file
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_employees, jsonfile)


if __name__ == "__main__":
    export_all_employees_todo()
