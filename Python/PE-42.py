# Coded triangle numbers
#
# https://projecteuler.net/problem=42

def triangleWord(word):
    letters = list(word)
    alphabet = {"A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,  "G": 7,  "H": 8,  "I": 9,  "J": 10,
                "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
                "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    # PRECOMPUTATION IS A USEFUL OPTIMIZATION
    # It's the exact minimum number of terms necessary as well, any fewer and it gives the wrong output
    triangle = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171]
    sum = 0
    for letter in letters:
        sum += alphabet[letter]
    if sum in triangle:
        return True
    else:
        return False

f = open("PE-42.txt", "r")
words = f.readline()
words = words.split(",")

i = 0
for word in words:
    if triangleWord(word):
        i += 1

print(i)
