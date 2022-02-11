# Longest Collatz sequence
#
# https://projecteuler.net/problem=14

# OEIS sequence:
# http://oeis.org/A006877

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

maxChain = 0
maxNumber = 0
for i in range(2, 1000000):
    if (i % 100000 == 0):
        print(i)
    n = i
    chain = 1
    while n != 1:
        n = collatz(n)
        chain += 1
    if chain > maxChain:
        maxChain = chain
        maxNumber = i

print(str(maxNumber) + " with a chain of length " + str(maxChain))
print(maxNumber)
