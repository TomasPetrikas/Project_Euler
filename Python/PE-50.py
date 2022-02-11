# Consecutive prime sum
#
# https://projecteuler.net/problem=50

from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

def primeGen(limit):
    primes = []
    primes.append(2)
    for p in range(3, limit + 1, 2):
        for i in range(2, int(sqrt(p) + 1)):
            if p % i == 0:
                break
        else:
            primes.append(p)
    return primes

limit = 1000000
primes = primeGen(limit)
print("Primes generated")

i = 0
maxTerms = 0
while primes[i] < limit // 20:
    sum = primes[i]
    j = 1
    terms = 1
    while sum < limit:
        if isPrime(sum) and terms > maxTerms:
            maxPrime = sum
            maxTerms = terms
        sum += primes[i+j]
        j += 1
        terms += 1
    i += 1

print(str(maxPrime) + " with " + str(maxTerms) + " consecutive primes")
print(maxPrime)
