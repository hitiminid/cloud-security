import hashlib
import functools
import pdb
from charm.toolbox.integergroup import integer


def ID(x):
	return hashlib.sha1(str(x).encode('utf-8')).hexdigest()


def product(l):
	return functools.reduce(lambda x, y : x * y, l)


def LI_EXP(x, phi):
	return product(
        grLx ** product((x - mj) / (m - mj) for mj, _ in phi if mj != m)
        for m, grLx in phi
		)


def LI_EXP_no_lambda(x, phi, G):
	value = integer(1, G.q)
	for m, grLx in phi:
		exp = product((x - m_j) / (m - m_j) for m_j, _ in phi if m_j != m)
		temp = grLx ** exp
		temp = integer(temp, G.q)
		value = integer(value * temp, G.q)
	return integer(value, G.q)
