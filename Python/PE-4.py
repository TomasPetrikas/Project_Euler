# Largest palindrome product
#
# https://projecteuler.net/problem=4

x = 0
largest = 0
largest1 = 0
largest2 = 0

for i in range(900, 1000):
    for j in range(900, 1000):
        x = i * j
        if str(x) == str(x)[::-1] and x > largest:
            largest = x
            largest1 = i
            largest2 = j

print(str(largest1) + " * " + str(largest2))
print(largest)
