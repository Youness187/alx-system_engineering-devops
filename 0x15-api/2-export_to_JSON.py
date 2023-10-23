#!/usr/bin/python3
"""
Python script that, using this JSONPlaceholder,
for a given employee ID,
export data in the CSV format.
"""

if __name__ == "__main__":
    import requests
    import json
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    usr_api = requests.get(f"{url}/users/{id}").json()
    task_api = requests.get(f"{url}/todos?userId={id}").json()
    name = usr_api.get("username")
    data = {id: []}

    for task in task_api:
        info = {
            "username": name,
            "completed": task.get("completed"),
            "task": task.get("title"),
        }
        data[id].append(info)
    with open(f"{id}.json", "w") as f:
        f.write(json.dumps(data))
