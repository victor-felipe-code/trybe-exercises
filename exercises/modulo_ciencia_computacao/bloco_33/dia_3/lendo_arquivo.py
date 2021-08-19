import csv
from typing import List


def read(path):
    result = list()

    with open(path) as superheroes_file:
        header, *superheroes_list = csv.reader(superheroes_file)
        for heroe in superheroes_list:
            temp_heroe = dict()
            for index in range(len(heroe)):
                temp_heroe[header[index]] = heroe[index]
            result.append(temp_heroe)
    return result


def reduce_filter(acc: list, current, column: str) -> list:
    column_type = str(current[column])
    if acc.count(column_type) == 0 and column_type != "":
        acc.append(column_type)
        return acc
    return acc


def filter_types(data: List[dict], type_filter: str) -> list:
    acc = []
    temp = []
    for item in data:
        temp = reduce_filter(acc, item, type_filter).copy()
        acc.clear()
        acc = temp.copy()
        temp.clear()
    return acc


path = "jobs.csv"


data = read(path)
