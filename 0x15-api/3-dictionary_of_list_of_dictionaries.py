#!/usr/bin/python3
"""export api to csv"""
import json
import requests

if __name__ == "__main__":

    respUsers = requests.get(
            'https://jsonplaceholder.typicode.com/users').json()
    respTodos = requests.get(
            'https://jsonplaceholder.typicode.com/todos').json()

    objs = {}
    unames = {}

    for user in respUsers:
        unames[str(user.get('id'))] = user.get('username')

    for task in respTodos:
        if str(task.get('userId')) not in objs:
            objs[str(task.get('userId'))] = []
        objs[str(task.get('userId'))].append({
                'username': unames.get(str(task.get('userId'))),
                'task': task.get('title'),
                'completed': task.get('completed')
            })

    with open('todo_all_employees.json', "w", newline='') as f:
        json.dump(objs, f)
