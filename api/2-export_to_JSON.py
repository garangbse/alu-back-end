import json
import requests
import sys

#!/usr/bin/python3
"""
Script that exports employee TODO list progress to JSON format
"""



def export_employee_todo_to_json(employee_id):
    """
    Export employee TODO list to JSON format
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get user information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return
    
    user_data = user_response.json()
    username = user_data.get("username")
    
    # Get todos for the user
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        return
    
    todos_data = todos_response.json()
    
    # Prepare data for JSON export
    tasks_list = []
    for todo in todos_data:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)
    
    # Create the final JSON structure
    json_data = {str(employee_id): tasks_list}
    
    # Export to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_to_json(employee_id)
    except ValueError:
        sys.exit(1)