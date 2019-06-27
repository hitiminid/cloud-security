import pdb
from functools import reduce


class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def compute(self, x):
        return reduce(lambda prev, curr: curr * x + prev, self.coefficients)

    def __getitem__(self, i):
        return self.coefficients[i]

    def __setitem__(self, i, value):
        self.coefficients[i] = value
