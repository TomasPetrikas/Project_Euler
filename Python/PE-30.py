# Digit fifth powers
#
# https://projecteuler.net/problem=30

# 6 * (9^5) = 354294
# Therefore, we definitely don't need to search above that

numbers = []
for i in range(10, 354295):
    digits = list(str(i))
    sumDigits = 0
    for digit in digits:
        sumDigits += int(digit) ** 5
    if sumDigits == i:
        numbers.append(i)

print(numbers)
print(sum(numbers))
