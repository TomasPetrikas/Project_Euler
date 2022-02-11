# Largest product in a series
#
# https://projecteuler.net/problem=8

f = open("PE-8.txt", "r")

number = f.read()
product = 1
largest = 1

for i in range(12, 1000):
    for j in range(0, 13):
        product *= int(number[i-j])
    if product > largest:
        largest = product
    product = 1

print(largest)
