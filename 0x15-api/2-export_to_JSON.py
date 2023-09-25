#!/usr/bin/python3
"""Gather data from an API"""
import json
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

        def task_data(t):
            return {"task": t['title'],
                    "completed": t['completed'], "username": user['username']}
        data = {uid: list(map(task_data, tasks))}
        with open(f"{uid}.json", 'w') as file:
            json.dump(data, file)
