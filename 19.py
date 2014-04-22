
result = 0

current = 1
year = 1900
month = 1

while True:
    if current % 7 == 0 and year >= 1901:
        print(repr(year) + "  " + repr(month))
        result += 1
    if month == 9 or month == 4 or month == 6 or month == 11:
        current += 30
    elif month == 2:
        if year % 400 == 0 or year % 4 ==0 and year % 100 !=0:
            current += 29
        else:
            current += 28
    else:
        current += 31

    if year == 2000 and month == 12:
        break
    month += 1
    if month == 13:
        month = 1
        year += 1

print(result)
