# Lattice paths
#
# https://projecteuler.net/problem=15

# Did this one entirely without programming. Worked out that the answer is this:
# (2n)! / (n! * n!), n = 20
#
# Promptly afterwards I found out I basically reverse engineered n choose k. Yay?
# https://en.wikipedia.org/wiki/Binomial_coefficient

# OEIS sequence:
# http://oeis.org/A000984

from math import factorial

n = 20

print(factorial(2 * n) // factorial(n)**2)
