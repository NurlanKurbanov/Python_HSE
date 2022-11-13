from conv_man import ConvMan
from conv_imp import ConvImp


def main():
    ConvMan('excel.csv', "output.json").convert()
    ConvImp('excel.csv', "output2.json").convert()


if __name__ == "__main__":
    main()
