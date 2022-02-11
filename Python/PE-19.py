# Counting Sundays
#
# https://projecteuler.net/problem=19

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = 1
sundays = 0

for year in range(1901, 2001):
    for month in months:
        # Clause for leap years
        if month == 28 and year % 4 == 0 and year != 2000:
            month += 1
        for day in range(1, month + 1):
            weekday += 1
            if weekday == 8:
                weekday = 1
            if day == 1 and weekday == 7:
                sundays += 1

print(sundays)
