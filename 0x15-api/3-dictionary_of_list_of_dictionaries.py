#!/usr/bin/python3
"""export api to csv"""
import json
import requests

if __name__ == "__main__":

    respUsers = requests.get(
            'https://jsonplaceholder.typicode.com/todos/').json()
    respTodos = requests.get(
            'https://jsonplaceholder.typicode.com/todos/'
            ).json()

    objs = {}
    unames = {}

    for user in respUsers:
        unames[user.get('id')] = user.get('username')

    for task in respTodos:
        if task.get('userId') not in objs:
            objs[task.get('userId')] = []
        objs[task.get('userId')].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': unames.get(task.get('userId'))
            })

    with open('todo_all_employees.json', "w", newline='') as f:
        json.dump(objs, f)
