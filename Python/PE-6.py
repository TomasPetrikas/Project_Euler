# Sum square difference
#
# https://projecteuler.net/problem=6

sumOfSquares = 0
squareOfSum = 0

for i in range(1, 101):
    sumOfSquares += i ** 2
    squareOfSum += i

squareOfSum *= squareOfSum
# print(sumOfSquares)
# print(squareOfSum)
print(squareOfSum - sumOfSquares)
