# Goldbach's other conjecture
#
# https://projecteuler.net/problem=46

from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

primes = [2]
n = 3
flag = True
while True:
    if isPrime(n):
        primes.append(n)
        n += 2
        continue
    for prime in primes:
        i = 1
        while prime + 2 * i ** 2 <= n:
            if prime + 2 * i ** 2 == n:
                flag = False
            i += 1
    if flag:
        print(n)
        quit()
    flag = True
    n += 2
