# Sub-string divisibility
#
# https://projecteuler.net/problem=43

from itertools import permutations

temp = list(permutations(range(0, 10)))
perms = []
i = 0
for t in temp:
    x = str(temp[i])
    x = x.replace("(", "")
    x = x.replace(", ", "")
    x = x.replace(")", "")
    i += 1
    if int(x) >= 1023456789:
        perms.append(x)
print("Permutations generated")

sum = 0
primes = [2, 3, 5, 7, 11, 13, 17]
flag = True
for perm in perms:
    for i in range(0, 7):
        x = int(perm[i+1]) * 100 + int(perm[i+2]) * 10 + int(perm[i+3])
        if x % primes[i] != 0:
            flag = False
            break
    if flag:
        sum += int(perm)
    flag = True

print(sum)
