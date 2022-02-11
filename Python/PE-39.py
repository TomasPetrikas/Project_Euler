# Integer right triangles
#
# https://projecteuler.net/problem=39

solutionsMax = 0
for i in range(1, 1001):
    if i % 100 == 0:
        print(i)
    solutions = 0
    for a in range(1, i // 3 + 1):
        for b in range(a, i // 2 + 1):
            if a**2 + b**2 == (i - a - b)**2:
                solutions += 1
    if solutions > solutionsMax:
        solutionsMax = solutions
        valueMax = i

print("The value of " + str(valueMax) + " has " + str(solutionsMax) + " solutions")
print(valueMax)
