# Number spiral diagonals
#
# https://projecteuler.net/problem=28

sum = 1
i = 1
d = 2
while True:
    for n in range(4):
        i += d
        sum += i
    if i == 1001 ** 2:
        break
    d += 2

print(sum)
