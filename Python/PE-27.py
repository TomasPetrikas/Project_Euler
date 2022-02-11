# Quadratic primes
#
# https://projecteuler.net/problem=27

from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

maxN = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            if isPrime(n * n + a * n + b) == False:
                break
            else:
                n += 1
        if n > maxN:
            maxN = n
            maxA = a
            maxB = b

print("a = " + str(maxA) + " and b = " + str(maxB))
print("These coefficients produce " + str(maxN + 1) + " primes in a row.")
print(maxA * maxB)
