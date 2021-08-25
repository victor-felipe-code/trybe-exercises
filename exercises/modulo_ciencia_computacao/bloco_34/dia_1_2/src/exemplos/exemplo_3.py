from abc import ABC, abstractmethod
import json
import csv
from typing import List


class SalesReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    def build(self):
        return [
            {"Coluna 1": "Dado 1", "Coluna 2": "Dado 2", "Coluna 3": "Dado 3"},
            {"Coluna 1": "Dado A", "Coluna 2": "Dado B", "Coluna 3": "Dado C"},
        ]

    @abstractmethod
    def serialize(self):
        raise NotImplementedError


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + ".json", "w") as file:
            json.dump(self.build(), file)


class SalesReportCSV(SalesReport):
    def serialize(self):
        with open(self.export_file + ".csv", "w") as file:
            f = csv.writer(file, dialect=List)
            f.writerow(self.build())


class_json = SalesReportJSON("./pokedex_t")
class_csv = SalesReportCSV("./pokedex_csv")
class_json.serialize()
class_csv.serialize()
