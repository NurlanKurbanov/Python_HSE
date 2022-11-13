import unittest
from conv_man import ConvMan
from conv_imp import ConvImp


class TestConv(unittest.TestCase):
    def test_valid1(self):
        x1 = ConvMan('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '4;Ivan;2000;130;8']
        self.assertEqual(x1.csv_to_json(inp), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150",
        "dep": "1"
    }, 
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200",
        "dep": "5"
    }, 
    {
        "id": "4",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_valid2(self):
        x2 = ConvImp('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '4;Ivan;2000;130;8']
        self.assertEqual(x2.csv_to_json(inp), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150",
        "dep": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200",
        "dep": "5"
    },
    {
        "id": "4",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_missed_field1(self):
        x1 = ConvMan('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '4;Ivan;;130;8']
        self.assertEqual(x1.csv_to_json(inp), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150",
        "dep": "1"
    }, 
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200",
        "dep": "5"
    }, 
    {
        "id": "4",
        "name": "Ivan",
        "birth": "",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_missed_field2(self):
        x2 = ConvImp('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '4;Ivan;;130;8']
        self.assertEqual(x2.csv_to_json(inp), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150",
        "dep": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200",
        "dep": "5"
    },
    {
        "id": "4",
        "name": "Ivan",
        "birth": "",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_empty1(self):
        x1 = ConvMan('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep']
        self.assertEqual(x1.csv_to_json(inp), "[]")

    def test_empty2(self):
        x2 = ConvImp('excel.csv', "output.json")
        inp = ['id;name;birth;salary;dep']
        self.assertEqual(x2.csv_to_json(inp), "[]")


if __name__ == "__main__":
    unittest.main()
