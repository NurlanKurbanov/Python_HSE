import salary


def main():
    # c = salary.Cash(2)
    # print(c.get(1))
    # c.add(1, 'aaa')
    # print(c.get(1))
    # c.add(2, 'bbb')
    # print(c.get(2))
    # c.add(3, 'ccc')
    # print(c.get(1), c.get(2), c.get(3))

    s = salary.Salary(2)
    print(s.get('{"year": 2016, "month": "JULY", "salary": 1000000}'))
    print(s.get('{"year": 2016, "month": "JULY", "salary": 1000000}'))
    print(s.cash.cash)
    print(s.get('{"year": 2016, "month": "JUNE", "salary": 1000000}'))
    print(s.cash.cash)
    print(s.get('{"year": 2017, "month": "JUNE", "salary": 2000000}'))
    print(s.cash.cash)



if __name__ == '__main__':
    main()

