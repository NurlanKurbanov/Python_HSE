class StrategyDeal:
    def __init__(self, bank, entry, close, target1, target2, target3):
        self.bank = bank
        self.entry = entry
        self.close = close
        self.target1 = target1
        self.target2 = target2
        self.target3 = target3

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        pass

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def parse_data(data):
    blocks = [block.strip() for block in data.split('----') if len(block.strip() > 0)]
    bank_start_stop = []

    arr = []
    for block in blocks:
        for line in block.split('\n'):
            if line.startswith('Bank'):
                bank = line.split()[-1]
                bank = bank[:-3]
                bank = round(int(bank), 3)
            elif line.startswith('Entry'):
                entry = line.split()[-1]
                entry = entry[:-3]
                entry = round(int(entry), 3)
            elif line.startswith('Close'):
                close = line.split()[-1]
                close = close[:-3]
                close = round(int(close), 3)
            elif line.startswith('Target'):
                targets = line.split()

                target1 = targets[1]
                target1 = target1[:-4]
                target1 = round(int(target1), 3)

                target2 = targets[2]
                target2 = target2[:-4]
                target2 = round(int(target2), 3)

                target3 = targets[3]
                target3 = target3[:-3]
                target3 = round(int(target3), 3)

        arr.append((bank, entry, close, target1, target2, target3))

    return arr


def main():
    content = read_data('deals.txt')
    arr_with_block_values = parse_data(content)
    for elem in arr_with_block_values:
        s = StrategyDeal(elem(0), elem(1), elem(2), elem(3), elem(4), elem(5))
    # write_data('out.txt', result)


if __name__ == '__main__':
    main()

