#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


if __name__ == "__main__":
    
    data = {}

    response = requests.get(
            f"https://jsonplaceholder.typicode.com/users")
    users = response.json()
    user = None

    def task_data(t):
        return {
                "username": user['username'],
                "task": t['title'],
                "completed": t['completed']
                }

    def user_data(u):
        res = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{u['id']}/todos")
        tasks = res.json()
        return list(map(task_data, tasks))

    for u in users:
        user = u
        data[u['id']] = user_data(u)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)
