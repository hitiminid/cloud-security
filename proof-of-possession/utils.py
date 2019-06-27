import hashlib
import functools
import pdb
from charm.toolbox.integergroup import integer


def ID(x):
    return hashlib.sha1(str(x).encode('utf-8')).hexdigest()


def product(l):
    return functools.reduce(lambda x, y: x * y, l)


def LI_EXP(x, phi):
    return product(
        grLx ** product((x - mj) / (m - mj) for mj, _ in phi if mj != m)
        for m, grLx in phi
    )