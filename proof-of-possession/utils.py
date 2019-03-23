import hashlib
import functools


def ID(x):
	x = x.encode('utf-8')
	return hashlib.sha1(x).hexdigest()


def product(l):
	return functools.reduce(lambda x, y : x * y, l)


def LI_EXP(x, phi):
	# x - punkt w ktorym liczymy 
	# A = (m_i, g**r) - phi
	value = 0.0

	for m, grLx in phi:
		exp = product((x - m_j) / (m - m_j) for m_j, _ in phi if m != m_j) 
		grLx = grLx ** exp
		value = value * grLx
	return value

