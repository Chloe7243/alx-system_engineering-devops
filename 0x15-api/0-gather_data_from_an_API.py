#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        uid = argv[1]
        response = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{uid}")
        user = response.json()
        response2 = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{uid}/todos")
        tasks = response2.json()
        td = list(filter(lambda task : task['completed'] == True, tasks))
        tl = len(tasks)
        result = f"Employee {user['name']} is done with tasks({len(td)}/{tl}):"
        print(result)
        for task in td:
            print(f"\t {task['title']}")
