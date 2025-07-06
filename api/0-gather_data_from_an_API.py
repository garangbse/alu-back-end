import requests
import sys

#!/usr/bin/python3
"""
Script that fetches and displays employee TODO list progress from a REST API
"""



def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from JSONPlaceholder API
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Get employee information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')
        
        # Get employee's todos
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo.get('completed')]
        number_of_done_tasks = len(completed_tasks)
        
        # Display results
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        
        # Display completed task titles
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)