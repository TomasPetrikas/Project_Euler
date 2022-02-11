# Distinct powers
#
# https://projecteuler.net/problem=29

numbers = []
for a in range(2, 101):
    for b in range(2, 101):
        if a ** b not in numbers:
            numbers.append(a ** b)

print(len(numbers))
