# Summation of primes
#
# https://projecteuler.net/problem=10

from math import sqrt

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = [2]
n = 3

while n < 2000000:
    if isPrime(n):
        primes.append(n)
    n += 2

print(sum(primes))
