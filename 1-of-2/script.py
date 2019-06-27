import random
import pdb

from charm.schemes.pkenc.pkenc_rsa import RSA
from charm.toolbox.integergroup import IntegerGroupQ, integer


RSA_LEN = 2048
NUMBER_OF_MESSAGES = 20
SECURITY_PARAM = 20

G = IntegerGroupQ()
G.paramgen(SECURITY_PARAM)


def generate_messages(g, N):
    messages = [g ** G.random(N) for _ in range(NUMBER_OF_MESSAGES)]
    return messages


def generate_RSA_stuff():
    pk, sk = RSA().keygen(RSA_LEN)
    return sk['d'], pk['N'], pk['e']


def compute_v(x_b, k, e, N):
    v = (x_b + (k ** e))
    return v


def compute_ks(v, random_messages, d):
    return [(v - r_msg) ** d for r_msg in random_messages]


def compute_m_prims(messages, ks):
    m_prims = [m + k for m, k in zip(messages, ks)]
    return m_prims


def decrypt_m_b(m_prims, b, k):
    return m_prims[b] - k


def main():

    # generate RSA stuff
    d, N, e = generate_RSA_stuff()

    # messages to be sent
    g = G.random(N)
    messages = generate_messages(g, N)

    # generate N random messages
    random_messages = generate_messages(g, N)

    # pick b and generate random k
    b = random.randint(0, NUMBER_OF_MESSAGES-1)
    k = G.random(N)

    # compute v
    x_b = random_messages[b]
    v = compute_v(x_b, k, e, N)

    # compute ks
    ks = compute_ks(v, random_messages, d)

    # compute m'
    m_prims = compute_m_prims(messages, ks)

    # decrypt m_b
    m_b = decrypt_m_b(m_prims, b, k)

    assert m_b == messages[b]


if __name__ == "__main__":
    main()
