# import json

# with open("superheroes.json") as superheroes_file:
#     superheroes_list = json.load(superheroes_file)
#     for superhero in superheroes_list:
#         print(superhero)

import csv

# with open("dc-wikia-data.csv") as superheroes_file:
#     superheroes_list = csv.DictReader(superheroes_file)
#     print(superheroes_list)
#     for superhero in superheroes_list:
#         print(superhero["name"])

with open("dc-wikia-data.csv") as superheroes_file:
    header, *superheroes_list = csv.reader(superheroes_file)
    print(header)
    for heroe in superheroes_list:
        print(heroe)
