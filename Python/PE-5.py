# Smallest multiple
#
# https://projecteuler.net/problem=5

# OEIS sequence:
# https://oeis.org/A003418

x = 2520
done = False

while True:
    for i in range(2, 21):
        if x % i != 0:
            break
        elif i == 20:
            done = True
    if done:
        print(x)
        break
    else:
        x += 2520
