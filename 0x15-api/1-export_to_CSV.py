#!/usr/bin/python3
"""export api to csv"""
import csv
import requests
from sys import argv
import csv

if __name__ == "__main__":

    if len(argv) > 1:
        if argv[1].isnumeric():
            iu = argv[1]
            response = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}'.format(
                        idUsuario))
            if response.status_code == 200:
                no = response.json().get('name')
                urlTs = 'https://jsonplaceholder.typicode.com/todos?userId={}'
                response_todos = requests.get(urlTs.format(idUsuario))
                tasks = len(response_todos.json())
                todos = response_todos.json()

                with open("{}".format(idUsuario) + ".csv", "w") as file:
                    writing = csv.writer(file, dialect='unix')
                    for tk in todos:
                        writing.writerow(
                                [iu, no, tk.get('completed'), tk.get('title')]
                                )
            else:
                print("Hubo un error, Codigo {}".format(response.status_code))
        else:
            print("El argumneto debe ser un numero")
    else:
        print("Falta el argumento")
