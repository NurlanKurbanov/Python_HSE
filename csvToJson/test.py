import unittest
from conv_man import ConvMan
from conv_imp import ConvImp


class TestConv(unittest.TestCase):
    def test_valid_man(self):
        json_man = ConvMan(['id,name,birth,salary,dep\n', '1,Ivan,1980,150,1\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,'
                                                                                                        '130,8'])
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200","dep": "5" '
                                             '},{ "id": "3","name": "Ivan","birth": "2000","salary": "130","dep": "8" '
                                             '}]')

    def test_empty_file_man(self):
        json_man = ConvMan(['id,name,birth,salary,dep'])
        self.assertEqual(json_man.to_json(), '[]')

    def test_title_at_second_line_man(self):
        json_man = ConvMan(['1,Ivan,1980,150,1\n', 'id,name,birth,salary,dep\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'], line_with_title=1)
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200",'
                                             '"dep": "5" },{ "id": "3","name": "Ivan","birth": "2000",'
                                             '"salary": "130","dep": "8" }]')

    def test_with_empty_field_man(self):
        json_man = ConvMan(['id,name,birth,salary,dep\n', '1,Ivan,1980,,1\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'])
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "","dep": "1" },'
                                             '{ "id": "2","name": "Alex","birth": "1960","salary": "200","dep": "5" '
                                             '},{ "id": "3","name": "Ivan","birth": "2000","salary": "130",'
                                             '"dep": "8" }]')

    def test_with_other_delimiter_man(self):
        json_man = ConvMan(['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '3;Ivan;2000;130;8'], delimiter=';')
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200",'
                                             '"dep": "5" },{ "id": "3","name": "Ivan","birth": "2000",'
                                             '"salary": "130","dep": "8" }]')

    def test_with_other_delimiter_imp(self):
        json_imp = ConvImp(['id;name;birth;salary;dep\n', '1;Ivan;1980;150;1\n', '2;Alex;1960;200;5\n', '3;Ivan;2000;130;8'], delimiter=';')
        self.assertEqual(json_imp.to_json(), """[
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
        "id": "3",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_valid_imp(self):
        json_imp = ConvImp(['id,name,birth,salary,dep\n', '1,Ivan,1980,150,1\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,'
                                                                                                        '130,8'])
        self.assertEqual(json_imp.to_json(), """[
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
        "id": "3",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_empty_file_imp(self):
        json_imp = ConvImp(['id,name,birth,salary,dep'])
        self.assertEqual(json_imp.to_json(), '[]')

    def test_title_at_second_line_imp(self):
        json_imp = ConvImp(['1,Ivan,1980,150,1\n', 'id,name,birth,salary,dep\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'], line_with_title=1)
        self.assertEqual(json_imp.to_json(), """[
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
        "id": "3",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_with_empty_field_imp(self):
        json_imp = ConvImp(['id,name,birth,salary,dep\n', '1,Ivan,1980,,1\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'])
        self.assertEqual(json_imp.to_json(),"""[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "",
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
        "id": "3",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")


if __name__ == "__main__":
    unittest.main()
