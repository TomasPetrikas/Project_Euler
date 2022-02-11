# Number letter counts
#
# https://projecteuler.net/problem=17

def numberName(number):
    # It's ugly and could be simplified a ton, but it works so... eh
    name = ""
    ones = {1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"}
    teens = {10: "ten",
             11: "eleven",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen"}
    tens = {2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"}
    hundreds = {1: "one hundred",  # Took far too long to realize this isn't needed, but again... eh
                2: "two hundred",
                3: "three hundred",
                4: "four hundred",
                5: "five hundred",
                6: "six hundred",
                7: "seven hundred",
                8: "eight hundred",
                9: "nine hundred"}
    if number < 10:
        return ones[number]
    if number < 20:
        return teens[number]
    if number < 100:
        name += tens[number // 10]
        if number % 10 != 0:
            name += " " + ones[number % 10]
        return name
    if number % 100 == 0:
        return hundreds[number // 100]
    if number > 100:
        name += hundreds[number // 100] + " and "
        if number // 10 % 10 == 1:
            name += teens[number % 100]
            return name
        elif number // 10 % 10 != 0:
            name += tens[number // 10 % 10]
            if number % 10 == 0:
                return name
            else:
                name += " " + ones[number % 10]
                return name
        else:
            name += ones[number % 10]
            return name

def letterCount(string):
    string = string.replace(" ", "")
    return len(string)

letters = 0
for i in range(1, 1000):
    letters += letterCount(numberName(i))
    # print(i, letters)
letters += 11  # "One thousand"

print(letters)
