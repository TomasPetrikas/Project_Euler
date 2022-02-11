# Lexicographic permutations
#
# https://projecteuler.net/problem=24

# There are 10! = 3628800 permutations

from itertools import permutations

perms = list(permutations(range(10)))
answer = ''.join(str(n) for n in perms[999999])
print(answer)
