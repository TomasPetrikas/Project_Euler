# Digit factorials
#
# https://projecteuler.net/problem=34

from math import factorial

def factSum(number):
    digits = list(str(number))
    sumDigits = 0
    for digit in digits:
        sumDigits += factorial(int(digit))
    if number == sumDigits:
        return True
    else:
        return False

numbers = []
for i in range(3, 50000):
    if factSum(i) == True:
        numbers.append(i)

print(numbers)
print(sum(numbers))
