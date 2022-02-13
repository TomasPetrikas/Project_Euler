# 10001st prime
#
# https://projecteuler.net/problem=7

# Querying WolframAlpha with "10001st prime" also works
# https://www.wolframalpha.com/input?i=10001st+prime

from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
n = 2

while len(primes) < 10001:
    if isPrime(n):
        primes.append(n)
    n += 1

print(primes[10000])
