# Largest product in a grid
#
# https://projecteuler.net/problem=11

def compare(a, b, c, d, largest):
    prod = a * b * c * d
    if prod > largest:
        largest = prod
    return largest

with open('PE-11.txt') as f:
    nums = []
    for line in f:
        nums.append([int(x) for x in line.split()])

# print(nums)

largest = 0
for i in range(0, 17):
    for j in range(0, 17):
        largest = compare(nums[i][j], nums[i+1][j], nums[i+2][j], nums[i+3][j], largest)
        largest = compare(nums[i][j], nums[i][j+1], nums[i][j+2], nums[i][j+3], largest)
        largest = compare(nums[i][j], nums[i+1][j+1], nums[i+2][j+2], nums[i+3][j+3], largest)
        if j >= 3:
            largest = compare(nums[i][j], nums[i+1][j-1], nums[i+2][j-2], nums[i+3][j-3], largest)
        if i >= 3:
            largest = compare(nums[i][j], nums[i-1][j+1], nums[i-2][j+2], nums[i-3][j+3], largest)

print(largest)
