import csv
import json


class ConvImp:
    def __init__(self, inp, output):
        self.inp = inp
        self.output = output

    def read_data_to_list(self):
        file = open(self.inp)
        content = file.readlines()
        file.close()
        return content

    def write_data(self, data):
        file = open(self.output, 'w')
        # jsonString = json.dumps(data, indent=4)
        file.write(data)
        file.close()

    def split_data(self, data):
        line_with_title = 0
        title = data.pop(line_with_title).strip().split(';')
        return title, data

    def csv_to_json(self, data):
        title, content = self.split_data(data)
        csvReader = csv.DictReader(content, fieldnames=title, delimiter=';')
        res = []
        for row in csvReader:
            res.append(row)
        jsonString = json.dumps(res, indent=4)
        return jsonString

    def convert(self):
        content = self.read_data_to_list()
        res = self.csv_to_json(content)
        self.write_data(res)
