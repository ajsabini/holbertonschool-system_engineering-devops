#!/usr/bin/python3
"""export api to csv"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        if argv[1].isnumeric():
            iu = argv[1]
            resp = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}'.format(
                        iu))
            if resp.status_code == 200:
                no = resp.json().get('name')
                urlTs = 'https://jsonplaceholder.typicode.com/todos?userId={}'
                response_todos = requests.get(urlTs.format(iu))
                tasks = len(response_todos.json())
                todos = response_todos.json()

                with open("{}".format(iu) + ".json", "w", newline='') as f:
                    obj = []
                    for tk in todos:
                        obj.append({'task': tk.get('title'),
                                    'completed': tk.get('completed'),
                                    'username': resp.json().get('username')})
                    fileObj = {'{}'.format(iu): obj}
                    json.dump(fileObj, f)
            else:
                print("Hubo un error, Codigo {}".format(response.status_code))
        else:
            print("El argumneto debe ser un numero")
    else:
        print("Falta el argumento")
