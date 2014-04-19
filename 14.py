__author__ = 'Dawei'
import math


longest = 1
longestStart = 1

computed = {1:1}

def getCount(i):


    number = i
    count = 0
    while True:
        if number in computed:
            return computed[number]

        if number % 2 == 0:
            lognumber = math.log2(number)
            intlognumber = int(lognumber)
            if lognumber == intlognumber:
                count += lognumber + 1
                break
            else:
                divide = math.pow(2, int(lognumber))
                while number % divide != 0:
                    divide /= 2
                number = (number / divide)*3+1
                count += int(math.log2(divide))+1
        else:
            number = number * 3 + 1
            count += 1
    computed[i] = count
    return count

for i in range(500000, 1000000):
    if (i-1)%3 == 0 and (i-1)%6!=0:
        continue
    lognumber = math.log2(i)
    intlognumber = int(lognumber)
    if lognumber == intlognumber:
        count = lognumber+1
    else:
        count = getCount(i)
    if count > longest:
        longest = count
        longestStart = i

print(longest)
print(longestStart)

