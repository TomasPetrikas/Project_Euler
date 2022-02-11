# Distinct primes factors
#
# https://projecteuler.net/problem=47

def distinctPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))

n = 2
while True:
    if (n % 10000 == 0):
        print(n)
    f1 = distinctPrimeFactors(n)
    f2 = distinctPrimeFactors(n + 1)
    f3 = distinctPrimeFactors(n + 2)
    f4 = distinctPrimeFactors(n + 3)
    if len(f1) >= 4 and len(f2) >= 4 and len(f3) >= 4 and len(f4) >= 4:
        print(n)
        quit()
    n += 1
