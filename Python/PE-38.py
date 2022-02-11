# Pandigital multiples
#
# https://projecteuler.net/problem=38

def pandigital(string):
    digits = "".join(sorted(string))
    if digits == "123456789":
        return True
    else:
        return False

largest = 0
numbers = []
for i in range(1, 10000):
    product = str(i)
    j = 2
    while len(product) < 9:
        product += str(i*j)
        j += 1
    if pandigital(product):
        numbers.append(i)
        if int(product) > largest:
            largest = int(product)

print(numbers)
print(largest)
