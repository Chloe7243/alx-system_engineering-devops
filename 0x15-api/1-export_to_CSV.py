#!/usr/bin/python3
"""Gather data from an API"""
import csv
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
        with open(f"{uid}.csv", 'w') as file:
            w = csv.writer(file, quoting=csv.QUOTE_ALL)
            for t in tasks:
                w.writerow([uid, user['username'], t['completed'], t['title']])
