# 1000-digit Fibonacci number
#
# https://projecteuler.net/problem=25

# print("F1 - 1")
# print("F2 - 1")
a = 1
b = 1
index = 3
while len(str(b)) != 1000:
    b += a
    a = b - a
    # print("F" + str(index) + " - " + str(b))
    index += 1

print(index)
