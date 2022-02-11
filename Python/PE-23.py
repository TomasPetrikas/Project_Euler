# Non-abundant sums
#
# https://projecteuler.net/problem=23

# https://en.wikipedia.org/wiki/Abundant_number#Properties
# Every integer greater than 20161 can be written as the sum of two abundant numbers

from math import sqrt

def divisors(number):
    div = set([1])
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            div.add(i)
            div.add(number // i)
    return div

abundant = set(i for i in range(1, 20170) if sum(divisors(i)) > i)
sumSet = set(x + y for x in abundant for y in abundant)
numbers = set(range(1, 20170))

print(sum(numbers - sumSet))
