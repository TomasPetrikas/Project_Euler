# Pandigital products
#
# https://projecteuler.net/problem=32

def pandigital(string):
    digits = "".join(sorted(string))
    if digits == "123456789":
        return True
    else:
        return False

mult1 = []
mult2 = []
numbers = []
for a in range(1, 10000):
    for b in range(1, 10000):
        product = a * b
        string = str(a) + str(b) + str(product)
        if len(string) > 9:
            break
        if pandigital(string) == True and product not in numbers:
            mult1.append(a)
            mult2.append(b)
            numbers.append(product)

i = 0
for number in numbers:
    print(str(mult1[i]) + " * " + str(mult2[i]) + " = " + str(number))
    i += 1
print(sum(numbers))
