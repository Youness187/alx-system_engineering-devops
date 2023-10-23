#!/usr/bin/python3
"""
Python script that, using this JSONPlaceholder,
for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    usr_api = requests.get(f"{url}/users/{id}").json()
    task_api = requests.get(f"{url}/todos?userId={id}").json()
    done_api = requests.get(f"{url}/todos?userId={id}&completed=true").json()

    name = usr_api.get("name")
    total = len(task_api)
    done = len(done_api)

    print(f'Employee {name} is done with tasks({done}/{total}):')
    for task in done_api:
        print("\t "+task.get("title"))
