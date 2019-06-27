from charm.toolbox.symcrypto import SymmetricCryptoAbstraction


def pick_random_values(no_of_values, size_of_values=64):
    return [get_random_bytes(size_of_values) for _ in range(no_of_values)]


def get_random_bytes(no_of_bytes):
    with open("/dev/random", "rb") as f:
        return f.read(no_of_bytes)


def encrypt(message, key1, key2):
    k1 = SymmetricCryptoAbstraction(key1)
    k2 = SymmetricCryptoAbstraction(key2)
    c0 = k1.encrypt(message)
    c1 = k2.encrypt(c0)
    return c1


def decrypt(cryptogram, key1, key2):
    k1 = SymmetricCryptoAbstraction(key1)
    k2 = SymmetricCryptoAbstraction(key2)
    m0 = k2.decrypt(cryptogram)
    m1 = k1.decrypt(m0)
    return m1
