import unittest
from salary import Salary


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.salary = Salary(2)

    def test_valid(self):
        a = self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        s1 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "6250.00"}'
        s2 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "5952.38"}'
        s3 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "5681.82"}'
        s4 = '{"year": 2016, "month": "JULY", "salary": 1000000, "hour_income": "5434.78"}'
        self.assertEqual(a in (s1+s2+s3+s4), True)

    def test_cah_size1(self):
        a = self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        a = self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        self.assertEqual(len(self.salary.cash.cash), 1)

    def test_cah_size3(self):
        a = self.salary.get('{"year": 2016, "month": "JULY", "salary": 1000000}')
        b = self.salary.get('{"year": 2016, "month": "JUNE", "salary": 1000000}')
        c = self.salary.get('{"year": 2017, "month": "JULY", "salary": 1000000}')
        self.assertEqual(len(self.salary.cash.cash), 2)
