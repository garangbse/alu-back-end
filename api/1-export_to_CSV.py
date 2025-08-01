#!/usr/bin/python3
"""Export employee TODO data to CSV format."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export employee TODO data to CSV file."""
    try:
        # Fetch employee data
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todos_url = f"{base_url}/users/{employee_id}/todos"

        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        # Prepare CSV filename
        filename = f"{employee_id}.csv"

        # Write to CSV file
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    employee_id,
                    user['username'],
                    str(task['completed']),
                    task['title']
                ])

    except requests.exceptions.RequestException:
        sys.exit("Error fetching data")
    except ValueError:
        sys.exit("Invalid employee ID")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

    export_to_csv(sys.argv[1])
    