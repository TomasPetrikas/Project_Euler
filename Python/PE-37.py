# Truncatable primes
#
# https://projecteuler.net/problem=37

from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

def truncation(number):
    if not isPrime(number):
        return False
    n1 = str(number)
    n2 = str(number)
    while len(n1) != 1:
        n1 = n1[1:]
        n2 = n2[:-1]
        if not isPrime(int(n1)) or not isPrime(int(n2)):
            return False
    return True

numbers = []
for i in range(11, 1000000, 2):
    digits = list(str(i))
    # Don't check for 2 because it's prime
    if "0" in digits or "4" in digits or "6" in digits or "8" in digits:
        continue
    if truncation(i):
        numbers.append(i)

print(numbers)
print(sum(numbers))
