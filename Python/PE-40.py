# Champernowne's constant
#
# https://projecteuler.net/problem=40

string = ""
for i in range(1, 1000000):
    string += str(i)
x = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])
print(x)
