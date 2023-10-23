#!/usr/bin/python3
"""
Python script that, using this JSONPlaceholder,
for a given employee ID,
export data in the CSV format.
"""

if __name__ == "__main__":
    import requests
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    usr_api = requests.get(f"{url}/users/{id}").json()
    task_api = requests.get(f"{url}/todos?userId={id}").json()
    name = usr_api.get("username")

    with open(f"{id}.csv", "w") as f:
        for task in task_api:
            data = f'"{id}","{name}","{task.get("completed")}",'
            data2 = f'"{task.get("title")}"\n'
            f.write(data + data2)
