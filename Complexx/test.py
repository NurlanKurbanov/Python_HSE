import unittest
from complex import Complex


class TestComplex(unittest.TestCase):
    # def setUp(self):
    #     self.complex = Complex()

    def test_equal(self):
        first = Complex(1, 2)
        second = Complex(1, 2)
        self.assertEqual(first, second)

    def test_equal_with_null_re(self):
        first = Complex(0, 2)
        second = Complex(0, 2)
        self.assertEqual(first, second)

    def test_equal_with_null_im(self):
        first = Complex(1)
        second = Complex(1)
        self.assertEqual(first, second)

    def test_not_equal(self):
        first = Complex(1, 2)
        second = Complex(1, 5)
        self.assertNotEqual(first, second)

    def test_str(self):
        first = Complex(1, 2)
        second = Complex(1, 2)
        self.assertEqual(str(first), str(second))

    def test_str_null_im(self):
        first = Complex(1)
        second = Complex(1, 0)
        self.assertEqual(str(first), str(second))

    def test_str_null_re(self):
        first = Complex(0, -3)
        second = Complex(0, -3)
        self.assertEqual(str(first), str(second))

    def test_add(self):
        first = Complex(1, 2)
        second = Complex(2, 1)
        self.assertEqual(first.add(second), Complex(3, 3))

    def test_add_null_re(self):
        first = Complex(1, 2)
        second = Complex(0, 1)
        self.assertEqual(first.add(second), Complex(1, 3))

    def test_add_null_im(self):
        first = Complex(1, 0)
        second = Complex(2, 1)
        self.assertEqual(first.add(second), Complex(3, 1))

    def test_sub(self):
        first = Complex(3, 2)
        second = Complex(2, 1)
        self.assertEqual(first.sub(second), Complex(1, 1))

    def test_sub_null_im(self):
        first = Complex(3, 2)
        second = Complex(4, 0)
        self.assertEqual(first.sub(second), Complex(-1, 2))

    def test_sub_null_re(self):
        first = Complex(0, 2)
        second = Complex(4, 0)
        self.assertEqual(first.sub(second), Complex(-4, 2))

    def test_mul(self):
        first = Complex(1, 3)
        second = Complex(2, -2)
        self.assertEqual(first.mul(second), Complex(8, 4))

    def test_mul_0(self):
        first = Complex(1, 3)
        second = Complex(0)
        self.assertEqual(first.mul(second), Complex(0))

    def test_div(self):
        first = Complex(2, 1)
        second = Complex(1, -1)
        self.assertEqual(first.div(second), Complex(0.5, 1.5))

    def test_div_0(self):
        first = Complex(2, 1)
        second = Complex(0)
        self.assertEqual(first.div(second), None)

    def test_abs(self):
        self.assertEqual(Complex(3, 4).abs(), 5)

    def test_abs_null_im(self):
        self.assertEqual(Complex(3, 0).abs(), 3)

    def test_abs_null_re(self):
        self.assertEqual(Complex(0, 4).abs(), 4)


if __name__ == "__main__":
    unittest.main()
