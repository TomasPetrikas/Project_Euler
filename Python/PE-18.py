# Maximum path sum I
#
# https://projecteuler.net/problem=18

tree = {0: [75],
        1: [95, 64],
        2: [17, 47, 82],
        3: [18, 35, 87, 10],
        4: [20, 4, 82, 47, 65],
        5: [19, 1, 23, 75, 3, 34],
        6: [88, 2, 77, 73, 7, 63, 67],
        7: [99, 65, 4, 28, 6, 16, 70, 92],
        8: [41, 41, 26, 56, 83, 40, 80, 70, 33],
        9: [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        10: [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        11: [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        12: [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        13: [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        14: [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]}
totals = tree[0]

for i in range(1, 15):
    upper = totals
    lower = tree[i]
    pointer = 0
    temp1 = []
    temp2 = []
    for item in upper:
        temp1.append(item + lower[pointer])
        temp1.append(item + lower[pointer + 1])
        pointer += 1
    temp2.append(temp1[0])
    for i in range(1, len(temp1) - 2, 2):
        temp2.append(max(temp1[i], temp1[i + 1]))
    temp2.append(temp1[len(temp1) - 1])
    totals = temp2

print(max(totals))
