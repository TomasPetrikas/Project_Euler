# Permuted multiples
#
# https://projecteuler.net/problem=52

x = 100000
while True:
    flag = True
    digitsX = [int(n) for n in str(x)]
    digitsX.sort()
    for i in range(2, 7):
        y = x * i
        digitsY = [int(n) for n in str(y)]
        digitsY.sort()
        if digitsY != digitsX:
            flag = False
            break
    if flag:
        print(x)
        quit()
    x += 1
