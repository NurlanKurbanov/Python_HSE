class ConvMan:
    def __init__(self, csv_data, line_with_title=0, delimiter=','):
        self.title = csv_data[line_with_title]
        self.values = csv_data[0:line_with_title] + csv_data[line_with_title + 1:]
        self.delimiter = delimiter

    def prepare_title(self):
        title = self.title.strip().split(self.delimiter)
        return title

    def prepare_row_values(self):
        values = [row.strip().split(self.delimiter) for row in self.values]  #2d-массив, строки - элементы строк
        return values

    def make_json_block(self, data):
        json_pairs = ",".join([f'"{key}": "{value}"' for key, value in data.items()])
        return f"{{ {json_pairs} }}"

    def to_json(self):
        title = self.prepare_title()
        row_values = self.prepare_row_values()

        self.check_data(title, row_values)

        result = [self.make_json_block(dict(zip(title, row))) for row in row_values]  #json blocks
        return "[{}]".format(",".join(result))

    def check_data(self, title, row_values):
        len_title = len(title)
        for row in row_values:
            assert len_title == len(row), "Column count is not equals value count"


