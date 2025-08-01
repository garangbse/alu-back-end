#!/usr/bin/python3
"""Export employee TODO data to JSON format."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export employee TODO data to JSON file."""
    try:
        # Fetch employee data
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/users/{employee_id}/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        # Prepare data structure
        tasks_data = {
            employee_id: [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user["username"]
                }
                for task in todos
            ]
        }

        # Write to JSON file
        filename = f"{employee_id}.json"
        with open(filename, 'w') as jsonfile:
            json.dump(tasks_data, jsonfile)

    except requests.exceptions.RequestException:
        sys.exit("Error fetching data")
    except ValueError:
        sys.exit("Invalid employee ID")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./2-export_to_JSON.py <employee_id>")

    export_to_json(sys.argv[1])
