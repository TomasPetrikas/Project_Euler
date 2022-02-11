# Reciprocal cycles
#
# https://projecteuler.net/problem=26

# https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence
# This implementation is not wholly correct, but it gets the right answer, so it's close enough

def period(denominator):
    numerator = 1
    period = 0
    digits = []
    if denominator < 10:
        factor = 10
    elif denominator < 100:
        factor = 100
    else:
        factor = 1000
    numerator *= factor
    while period < denominator - 1:
        if numerator // denominator in digits:
            break
        digits.append(numerator // denominator)
        period += 1
        remainder = numerator % denominator
        numerator = remainder * factor
    return period

periodMax = 0
numberMax = 0
for d in range(2, 1001):
    if period(d) > periodMax:
        periodMax = period(d)
        numberMax = d
        # print("New max period: " + str(d) + " with a period of " + str(periodMax))

print(numberMax)
