# Prime permutations
#
# https://projecteuler.net/problem=49

from math import sqrt

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

def isPerm(number1, number2):
    number1, number2 = str(number1), str(number2)
    if sorted(number1) == sorted(number2):
        return True
    else:
        return False

for i in range(1009, 9999, 2):  # 1009 - first 4 digit prime
    if not isPrime(i):
        continue
    n = 1000
    while i + n < 9999:
        if isPerm(i, i + n) and isPerm(i, i + 2 * n) and isPrime(i + n) and isPrime(i + 2 * n):
            print(str(i) + str(i + n) + str(i + 2 * n))
            if (i > 1487):
                quit()
        n += 2
