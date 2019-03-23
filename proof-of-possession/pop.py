import functools
from poly import Polynomial
import utils
from charm.toolbox.integergroup import IntegerGroupQ, integer
import random
import pdb


def setup(security_parameter):
	G = IntegerGroupQ()
	G.paramgen(security_parameter)
	g = G.randomG()
	sk = G.random()
	return G, g, sk

	
def generate_f():
	f = []
	for i in range(NUMBER_OF_BLOCKS):
		m = integer(random.randrange(G.q), G.q)
		f.append(m)
	return f 


def create_f_ID(f):
	f_str = ''.join(str(f))
	return utils.ID(f_str)


def create_poly(f, sk):
	
	random.seed(str(sk) + create_f_ID(f))
	pdb.set_trace() ### BREAKPOINT ###

	number_of_subblocks = len(f)
	coefficients = []

	for i in range(0, number_of_subblocks):
		coefficient = integer(random.randrange(G.q), G.q)
		coefficients.append(coefficient)

	
	for i in range(0, len(coefficients)):
		while coefficients[i] == 0:
			coefficients[i] = integer(random.randrange(G.q), G.q)
	
	return Polynomial(coefficients)


def generate_tag_block(polynomial, f):
	return [(m, polynomial.compute(m)) for m in f]
	

def generate_challenge(G, poly):
	r = G.random()
	xc = G.random() # x_c != m_i
	
	k_f = g ** (r * poly.compute(xc))
	H = (g ** r, xc, g ** (r * poly.compute(0)))
	return k_f, H


def generate_proof(Tf):
	phi_set = generate_phi_set(Tf)


def generate_phi_set(Tf, g, r, poly):
	phi_set = []

	for m, t in Tf: 
		element = (m, g ** r ** t)
		phi_set.append(element)

	last_element = (integer(0, G.q),  g ** (r * poly.compute(0)))
	phi_set = []
	return phi_set




def check_proof(p_f, k_f):
	return p_f == k_f


##############################################


G, g, sk = setup(1024)

NUMBER_OF_BLOCKS = 4
f = generate_f()

# pdb.set_trace() ### BREAKPOINT ### 

poly = create_poly(f, sk)
pdb.set_trace() ### BREAKPOINT ###

Tf = generate_tag_block(poly, f)

pdb.set_trace() ### BREAKPOINT ###

k_f, H = generate_challenge(G, poly)



