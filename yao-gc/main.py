import random
import os
import pdb

import utils

random_values = utils.pick_random_values(6)
a_0, _, _, b_1, c_0, c_1 = random_values


def create_initial_table():
    table = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 1]
    ]
    return table


def create_modified_table(random_values):
    a_0, a_1, b_0, b_1, c_0, c_1 = random_values

    table = [
        [a_0, b_0, c_0],
        [a_0, b_1, c_0],
        [a_1, b_0, c_0],
        [a_1, b_1, c_1],
    ]

    return table


def create_garbled_table(table):
    """d 
    Create a following table:
    table = [
        encrypt(a_0, b_0, c_0),
        encrypt(a_0, b_1, c_0),
        encrypt(a_1, b_0, c_0),
        encrypt(a_1, b_1, c_1),
    ]
    """

    table = [utils.encrypt(row[2], row[0], row[1]) for row in table]
    random.shuffle(table)
    return table


def check_garbled_table(garbled_table):
    Alice_A = a_0
    Bob_B = b_1

    print(f'Expected result -> \n{c_0}')

    successfully_decrypted = []

    for cryptogram in garbled_table:
        try:
            a = utils.decrypt(cryptogram, Alice_A, Bob_B)

            if a == c_0:
                successfully_decrypted.append(a)
            # print(a == c_1)
            # print(a == c_0)
        except:
            ...

    print(f'Got -> \n{a}')
    assert successfully_decrypted[0] == c_0


def main():
    # 1) Create initial truth table
    initial_table = create_initial_table()

    # 2) Create modified table
    table = create_modified_table(random_values)

    # 3) Create garbled table
    garbled_table = create_garbled_table(table)

    # Additional) Check garbled table
    check_garbled_table(garbled_table)


if __name__ == '__main__':
    main()
