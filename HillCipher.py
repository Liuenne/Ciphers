import numpy as np

def matrix (string):
    for c in string:
        c = c.upper()
        ints.append(ord(c)-65)
    ints = []
    length = len(ints)
    mat = np.zeros((2, int(length / 2)), dtype=np.int32)
    iter = 0
    for col in range(int(length / 2)):
        for row in range(2):
            mat[row][col] = ints[iter]
            iter += 1
    return mat

def key():
    det = 0
    C = None
    while True:
        cipher = input()