# Special Pythagorean triplet
#
# https://projecteuler.net/problem=9

for a in range(1, 1000):
    for b in range(a+1, 1000):
        if a + b >= 1000:
            break
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
            print(a *b * c)
            quit()
