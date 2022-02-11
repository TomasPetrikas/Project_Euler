# Triangular, pentagonal, and hexagonal
#
# https://projecteuler.net/problem=45

from math import sqrt

n = 1
while True:
    T = n * (n + 1) // 2
    P = (sqrt(24 * T + 1) + 1) / 6
    H = (sqrt(8 * T + 1) + 1) / 4
    if P == int(P) and H == int(H):
        print(T)
        if T > 40755:
            quit()
    n += 1
