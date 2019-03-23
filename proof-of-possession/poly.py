import pdb
from functools import reduce

class Polynomial():


	def __init__(self, coefficients):
		self.coefficients = coefficients


	def compute(self, x): 
		return reduce(lambda acc, a: acc * x + a, reversed(self.coefficients))
		# y = 0
		# pdb.set_trace() ### BREAKPOINT ###
		# for power, coeff in enumerate(reversed(self.coefficients)):
		# 	y = y + coeff * (x ** power)
		# return y 


	def __getitem__(self, i):
		return self.coefficients[i]


	def __setitem__(self, i, value):
		self.coefficients[i] = value

