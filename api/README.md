# alu-back-end

## API Scripts Overview

This project contains a collection of Python scripts in the `api/` folder that interact with the JSONPlaceholder REST API to manage and export employee TODO list data:

### Scripts Description

**0-gather_data_from_an_API.py**
- Fetches and displays an employee's TODO list progress from the JSONPlaceholder API
- Takes an employee ID as a command-line argument
- Shows the employee's name, completion ratio (completed/total tasks), and lists all completed task titles
- Usage: `python3 0-gather_data_from_an_API.py <employee_id>`

**1-export_to_CSV.py**
- Exports a specific employee's TODO list to a CSV file
- Takes a user ID as a command-line argument
- Creates a CSV file named `<user_id>.csv` containing user ID, username, completion status, and task title for each TODO item
- Usage: `python3 1-export_to_CSV.py <user_id>`

**2-export_to_JSON.py**
- Exports a specific employee's TODO list to a JSON file
- Takes an employee ID as a command-line argument  
- Creates a JSON file named `<employee_id>.json` with structured data including task details, completion status, and username
- Usage: `python3 2-export_to_JSON.py <employee_id>`

**3-dictionary_of_list_of_dictionaries.py**
- Exports ALL employees' TODO lists to a single JSON file
- Fetches data for all users from the API automatically (no command-line arguments needed)
- Creates a comprehensive JSON file named `todo_all_employees.json` containing organized TODO data for every employee
- Usage: `python3 3-dictionary_of_list_of_dictionaries.py`

All scripts use the JSONPlaceholder API (https://jsonplaceholder.typicode.com) as the data source and include proper error handling for API requests and data processing.