list = [2,3]
target = 10001
number = 4

import math
while number>0:
    isprime = True
    for i in list:
        if math.sqrt(number)+1<i:
            break
        if number%i==0:
            isprime = False
            break
    if isprime:
        list.append(number)
        if len(list)==target:
            break
    number+=1

print(number)