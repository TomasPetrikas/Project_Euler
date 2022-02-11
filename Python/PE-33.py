# Digit cancelling fractions
#
# https://projecteuler.net/problem=33

from math import gcd, prod

def cancel(a, b):
    digitsA = list(str(a))
    digitsB = list(str(b))
    for i in range(1, 10):
        if str(i) in digitsA and str(i) in digitsB:
            digitsA.remove(str(i))
            digitsB.remove(str(i))
            if int(digitsB[0]) == 0:
                return False
            if int(digitsA[0]) / int(digitsB[0]) == a / b:
                return True
            else:
                break
    return False

numerators = []
denominators = []
for a in range(10, 99):
    for b in range(a + 1, 100):
        if cancel(a, b) == True:
            numerators.append(a)
            denominators.append(b)

i = 0
for numerator in numerators:
    print(str(numerator) + " / " + str(denominators[i]))
    i += 1

numerator = prod(numerators)
denominator = prod(denominators)

print(denominator // gcd(numerator, denominator))
