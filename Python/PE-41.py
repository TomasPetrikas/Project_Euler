# Pandigital prime
#
# https://projecteuler.net/problem=41

from itertools import permutations
from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

done = False
for i in range(10, 3, -1):
    perms = list(permutations(range(1, i)))
    j = 1
    for j in range(1, len(perms) + 1):
        x = str(perms[len(perms) - j])
        x = x.replace("(", "")
        x = x.replace(", ", "")
        x = x.replace(")", "")
        if isPrime(int(x)):
            print(x)
            done = True
            break
        j += 1
    if done:
        break
