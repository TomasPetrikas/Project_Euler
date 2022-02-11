# Even Fibonacci numbers
#
# https://projecteuler.net/problem=2

a = 1
b = 2
sum = 0 + b
temp = 0

while True:
    temp = b
    b += a
    a = temp
    if b >= 4000000:
        break
    if b % 2 == 0:
        sum += b

print(sum)
