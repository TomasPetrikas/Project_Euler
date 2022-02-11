# Pentagon numbers
#
# https://projecteuler.net/problem=44

pSet = set()
dictionary = {}

n = 0
p = 0
while True:
    p += 3 * n + 1
    if p in dictionary:
        print(dictionary[p])
        quit()

    for previous in pSet:
        diff = p - previous
        if diff in pSet:
            dictionary[p + previous] = diff

    pSet.add(p)
    n += 1
