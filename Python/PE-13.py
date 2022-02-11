# Large sum
#
# https://projecteuler.net/problem=13

f = open("PE-13.txt", "r")
numbers = f.readlines()
numbers = [int(i) for i in numbers]

sum = 0
for i in range(0, 100):
    sum += numbers[i]

print(sum)
print(str(sum)[0:10])
