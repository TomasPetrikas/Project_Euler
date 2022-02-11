# Double-base palindromes
#
# https://projecteuler.net/problem=36

def binary(number):
    return str(bin(number))[2:]

def palindrome(number):
    return str(number) == str(number)[::-1]

numbers = []
for i in range(1, 1000000):
    if palindrome(i) and palindrome(binary(i)):
        numbers.append(i)

print(numbers)
print(sum(numbers))
