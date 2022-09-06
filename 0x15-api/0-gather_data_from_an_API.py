#!/usr/bin/python3
"""sahda"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) > 1:
        if argv[1].isnumeric():
            idUsuario = argv[1]
            response = requests.get("https://jsonplaceholder.typicode.com\
                                   /users/{}".format(idUsuario))
            if response.status_code == 200:
                nombre = response.json().get('name')
                todos = requests.get('https://jsonplaceholder.typicode.com\
                                      /todos?userId={}'.format(idUsuario))
                tasks = len(todos.json())
                completas = 0
                for task in todos.json():
                    if task.get('completed') is True:
                        completas += 1
                        titulo = task.get('title')
                print("Employee {} is done with tasks({}/{})".
                      format(nombre, completas, tasks))
                print("\t {}".format(titulo))
            else:
                print("Hubo un error, Codigo {}".format(response.status_code))
        else:
            print("El argumneto debe ser un numero")
    else:
        print("Falta el argumento")
