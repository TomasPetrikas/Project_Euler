# Circular primes
#
# https://projecteuler.net/problem=35

from math import sqrt

def isPrime(number):
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            return False
    else:
        return True

def rotations(number):
    digits = list(str(number))
    rotationsList = [number]
    for i in range(1, len(digits)):
        new = []
        for j in range(0, len(digits)):
            if j == len(digits) - 1:
                new.append(int(digits[0]))
            else:
                new.append(int(digits[j+1]))
        rot = int("".join(map(str,new)))
        if rot not in rotationsList:
            rotationsList.append(rot)
        digits = list(str(rot))
    return rotationsList

numbers = [2]
for i in range(3, 1000000, 2):
    digits = list(str(i))
    if "0" in digits or "2" in digits or "4" in digits or "6" in digits or "8" in digits:
        continue
    circular = True
    rotationsList = rotations(i)
    for rot in rotationsList:
        if isPrime(rot) == False:
            circular = False
            break
    if circular == True:
        numbers.append(i)

print(numbers)
print(len(numbers))
