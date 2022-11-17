from conv_man import ConvMan
from conv_imp import ConvImp


def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()


def main():
    data = read_data_to_list("excel.csv")
    manual_conv = ConvMan(data)
    res_man = manual_conv.to_json()
    write_data("output.json", res_man)

    import_conv = ConvImp(data, line_with_title=0)
    res_imp = import_conv.to_json()
    write_data("output2.json", res_imp)


if __name__ == "__main__":
    main()
