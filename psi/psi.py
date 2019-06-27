import random
import pdb

from charm.schemes.pkenc.pkenc_rsa import RSA
from charm.toolbox.integergroup import IntegerGroupQ, integer

SECURITY_PARAM = 20
X_SIZE = 10
Y_SIZE = 10

G = IntegerGroupQ()
G.paramgen(SECURITY_PARAM)
N = 127
g = G.random()


def generate_sets(number_of_mutual):

    mutual_elements = generate_elements(number_of_mutual)

    X = generate_elements(X_SIZE)
    Y = [e for e in generate_elements(Y_SIZE) if e not in X]

    X += mutual_elements
    Y += mutual_elements

    # shuffle sets
    # random.shuffle(X)
    # random.shuffle(Y)

    return X, Y, mutual_elements


def generate_elements(number_of_elements):
    return [g ** G.random() for _ in range(number_of_elements)]


def generate_Gs(X):

    # hash each element of the set
    gs = [G.hash(x) for x in X]

    # pick a random a
    a = G.random()

    # generate big G = g ** a
    Gs = [g ** a for g in gs]

    return Gs, a


def generate_Hs_and_Bs(Y, Gs):

    # hash each element of the set
    hs = [G.hash(x) for x in Y]

    # pick a random b
    b = G.random()

    # generate big H = h ** b
    Hs = [h ** b for h in hs]

    # generate Bs
    Bs = [G ** b for G in Gs]

    return Hs, Bs


def generate_As(Hs, a):
    As = [H ** a for H in Hs]
    return As


def main():

    number_of_mutual = 2

    # generate sets
    X, Y, mutual = generate_sets(number_of_mutual)

    # generate Gs
    Gs, a = generate_Gs(X)

    # generate Hs and Bs
    Hs, Bs = generate_Hs_and_Bs(Y, Gs)

    # generate As
    As = generate_As(Hs, a)

    # A side compares
    a_mutual = [el1 for el1, el2 in zip(X, Bs) if el2 in As]

    # B side compares
    b_mutual = [el1 for el1, el2 in zip(Y, As) if el2 in Bs]

    assert a_mutual == b_mutual == mutual


if __name__ == "__main__":
    main()
