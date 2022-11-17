import csv
import json


class ConvImp:
    def __init__(self, csv_data, line_with_title=0, delimiter=','):
        self.title = csv_data[line_with_title]
        self.values = csv_data[0:line_with_title] + csv_data[line_with_title + 1:]
        self.delimiter = delimiter

    def prepare_title(self):
        title = self.title.strip().split(self.delimiter)
        return title

    def to_json(self):
        title = self.prepare_title()

        self.check_data(title)

        csvReader = csv.DictReader(self.values, fieldnames=title, delimiter=self.delimiter)
        res = [row for row in csvReader]
        jsonString = json.dumps(res, indent=4)
        return jsonString

    def check_data(self, title):
        values = [row.strip().split(self.delimiter) for row in self.values]

        len_title = len(title)
        for row in values:
            assert len_title == len(row), "Column count is not equals value count"
