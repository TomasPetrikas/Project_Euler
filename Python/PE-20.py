# Factorial digit sum
#
# https://projecteuler.net/problem=20

from math import factorial

digits = [int(i) for i in list(str(factorial(100)))]

print(sum(digits))
