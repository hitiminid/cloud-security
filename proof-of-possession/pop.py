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


def generate_f(n, z, NUMBER_OF_BLOCKS):
	# f = []
	# for i in range(NUMBER_OF_BLOCKS):
	# 	m = integer(random.randrange(2 ** n), G.q)
	# 	f.append(m)
	# return f

	return [integer(random.randrange(2 ** n), G.q) for _ in range(z)]


def create_f_ID(f):
	return utils.ID(f)


def create_poly(fid, sk, z):
	random.seed(str(sk) + fid)
	number_of_subblocks = z + 1
	coefficients = []

	for i in range(number_of_subblocks):
		coefficient = integer(random.randrange(G.q), G.q)
		coefficients.append(coefficient)

	for i in range(0, len(coefficients)):
		while coefficients[i] == 0:
			coefficients[i] = integer(random.randrange(G.q), G.q)
	return Polynomial(coefficients)


def generate_tag_block(polynomial, f):
	return [(m, polynomial.compute(m)) for m in f]


def generate_challenge(G, g, sk, fid, z):
	r = G.random()
	xc = G.random() # x_c != m_i
	poly = create_poly(fid, sk, z)

	K_f = g ** (r * poly.compute(xc))
	# K_f = integer(K_f, G.q)
	H = (g ** r, xc, g ** (r * poly[0]))
	return r, xc, K_f, H


def generate_proof(Tf, xc, g, r, poly, H):
	gr, xc, grLf0 = H
	phi = generate_phi_set(grLf0, Tf, gr, poly)
	P_f = utils.LI_EXP(xc, phi) # P_f = utils.LI_EXP_no_lambda(xc, phi, G)
	return P_f


def generate_phi_set(grLf0, Tf, gr, poly):
	phi_set = [(integer(0, G.q), grLf0)]

	for m, t in Tf:
		element = (m, gr ** t)
		phi_set.append(element)
	return phi_set


def check_proof(p_f, k_f):
	print(f"P_f = {p_f}")
	print(f"K_f = {k_f}")
	return p_f == k_f

##############################################

n = 256
G, g, sk = setup(1024)
z = 1
NUMBER_OF_BLOCKS = 1
f = generate_f(n, z, NUMBER_OF_BLOCKS)


poly = create_poly(create_f_ID(f), sk, z)

Tf = generate_tag_block(poly, f)
r, xc, K_f, H = generate_challenge(G, g, sk, create_f_ID(f), z)


P_f = generate_proof(Tf, xc, g, r, poly, H)
print(check_proof(P_f, K_f))
