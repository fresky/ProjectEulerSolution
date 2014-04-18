__author__ = 'Dawei'
import math

def get_divisors(number):
    result = 0
    for i in range(int(math.sqrt(number))+1, 0, -1):
        if number % i == 0:
            if i != math.sqrt(number):
                result+=1
            result +=1
    return result

start = 5000

while True:
    if start%2==0:
        n1=start/2
        n2=start+1
    else:
        n1=start
        n2=(start+1)/2

    first = get_divisors(n1)
    second = get_divisors(n2)

    if first *second >500:
        break

    start+=1

print(start*(start+1)/2)
