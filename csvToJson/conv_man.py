class ConvMan:
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
        file.write(data)
        file.close()

    def split_data(self, data):
        line_with_title = 0
        title = data.pop(line_with_title).strip().split(';')
        return title, data

    def convert_row_to_pretty_json(self, keys, row):
        values = row.strip().split(';')
        s = ['    {']
        for elem in dict(zip(keys, values)).items():
            s.append(f'        "{elem[0]}": "{elem[1]}",')
        s[-1] = s[-1][:-1]
        s.append("    }")
        return '\n'.join(s)

    def join_blocks(self, blocks):
        return '\n'.join(['[', ', \n'.join(blocks), ']'])

    def csv_to_json(self, data):
        title, content = self.split_data(data)
        if len(data) == 0:
            return "[]"
        blocks = [self.convert_row_to_pretty_json(title, row) for row in data]
        res = self.join_blocks(blocks)
        return res

    def convert(self):
        content = self.read_data_to_list()
        res = self.csv_to_json(content)
        self.write_data(res)
