class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im == 0 and self.re == 0:
            return "0"
        elif self.im == 0:
            return f"{self.re}"
        elif self.re == 0:
            return f"{self.im}i"
        elif self.im < 0:
            return f"{self.re} - {abs(self.im)}i"
        return f"{self.re} + {self.im}i"

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def add(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def sub(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def mul(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def div(self, other):
        if other.re != 0 or other.im != 0:
            denom_conj = Complex(other.re, -other.im)
            new_denom = other.mul(denom_conj)
            new_num = self.mul(denom_conj)
            return Complex(new_num.re / new_denom.re, new_num.im / new_denom.re)

    def abs(self):
        return (self.re * self.re + self.im * self.im)**0.5
