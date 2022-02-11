# Highly divisible triangular number
#
# https://projecteuler.net/problem=12

# OEIS sequence:
# https://oeis.org/A000217

from math import sqrt

def divisors(number):
    count = 0
    root = int(sqrt(number))
    for i in range(1, root + 1):
        if number % i == 0:
            count += 2 # counting both i and number / i
    if root**2 == number:
        count -= 1 # if sqrt is a factor, then we counted it twice
    return count

number = 1
i = 1
max = 0

while True:
    div = divisors(number)
    if div > 500:
        print(number)
        break
    elif div > max:
        max = div
        print("Divisors: " + str(max) + " (" + str(number) + ")")
    i += 1
    number += i
