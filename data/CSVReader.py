import csv

class CSVReader:
    def read(self, path):
        with open(path, newline='', encoding='utf-8') as csvfile:
            rd = csv.reader(csvfile, delimiter=';')
            return [row for row in rd]
