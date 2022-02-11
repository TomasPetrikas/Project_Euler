# Amicable numbers
#
# https://projecteuler.net/problem=21

from math import sqrt

def divisors(number):
    div = [1]
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            div.append(i)
            div.append(number // i)
    return list(set(div))

print(divisors(16))

numbers = [int(i) for i in range(2, 10000)]
amicable = []

for number in numbers:
    a = sum(divisors(number))
    b = sum(divisors(a))
    if b == number and b != a:
        if a and b not in amicable:
            print(str(a) + " and " + str(b))
            amicable.append(a)
            amicable.append(b)

print(sum(amicable))
