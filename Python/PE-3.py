# Largest prime factor
#
# https://projecteuler.net/problem=3

def primeFactors(n):
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
    return factors

print(primeFactors(600851475143))
print(max(primeFactors(600851475143)))
