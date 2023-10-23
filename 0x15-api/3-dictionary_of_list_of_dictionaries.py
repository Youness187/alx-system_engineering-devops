#!/usr/bin/python3
"""
Python script that, using this JSONPlaceholder,
for a given employee ID,
export data in the CSV format.
"""

if __name__ == "__main__":
    import requests
    import json

    id = 1
    data = {}
    url = "https://jsonplaceholder.typicode.com"

    while True:
        usr_api = requests.get(f"{url}/users/{id}").json()
        if not usr_api:
            break
        task_api = requests.get(f"{url}/todos?userId={id}").json()
        name = usr_api.get("username")
        data[id] = []
        for task in task_api:
            info = {
                "username": name,
                "completed": task.get("completed"),
                "task": task.get("title"),
            }
            data[id].append(info)
        id += 1

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(data))
