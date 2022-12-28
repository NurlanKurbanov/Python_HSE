class StrategyDeal:
    def __init__(self, bank, entry, close, targets):
        self.bank = bank
        self.entry = entry
        self.close = close
        self.targets = targets

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round((target/self.entry - 1) * 100, 3) for target in self.get_targets()]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        return [round(self.bank*(1 + percents/100), 3) for percents in self.get_target_percents()]

    def __str__(self):
        # текстовое представление сделки
        targets = self.get_targets()
        percents = self.get_target_percents()
        target_banks = self.get_target_banks()

        s = f"""
            BANK: {self.bank}
            START_PRICE = {self.entry}
            STOP_PRICE = {self.close}
        
            """

        for i in range(len(targets)):
            s +=f"""
                {i + 1} target: {targets[i]}
                Percent: {percents[i]}%
                Bank: {target_banks[i]}
                
                """

        s += """
            
            ----
            
            """

        return s


def read_data(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def parse_data(data):
    blocks = [block.strip() for block in data.split('-----') if len(block.strip()) > 0]

    arr = []
    for block in blocks:
        for line in block.split('\n'):
            if line.startswith('Bank'):
                bank = line.split()[-1]
                bank = bank[:-3]
                bank = round(float(bank), 3)
            elif line.startswith('Entry'):
                entry = line.split()[-1]
                entry = entry[:-3]
                entry = round(float(entry), 3)
            elif line.startswith('Close'):
                close = line.split()[-1]
                close = close[:-3]
                close = round(float(close), 3)
            elif line.startswith('Target'):
                targets_float = []
                for target in line.split()[1:]:
                    if target[-1] == ';':
                        targets_float.append(round(float(target[:-4]), 3))
                    else:
                        targets_float.append(round(float(target[:-3]), 3))

        arr.append((bank, entry, close, targets_float))

    return arr


def prepare_txt(arr):
    res = """"""
    for elem in arr:
        cls = StrategyDeal(elem[0], elem[1], elem[2], elem[3])
        res += cls.__str__()
    return res


def main():
    content = read_data('deals.txt')
    arr_with_block_values = parse_data(content)
    res = prepare_txt(arr_with_block_values)
    write_data('out.txt', res)


if __name__ == '__main__':
    main()

