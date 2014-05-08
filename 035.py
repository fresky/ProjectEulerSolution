import math
import time

start = time.time()

target = 1000000
primes = [[2,3],[],[],[],[],[]]


def is_prime(num):
    for i in primes:
        for j in i:
            if j > math.sqrt(num):
                break
            if num % j == 0:
                return False
    return True

a = 6-1
b = 6+1
while a < target and b < target:
    if is_prime(a):
        primes[len(repr(a))-1].append(a)
    if is_prime(b):
        primes[len(repr(b))-1].append(b)
    a += 6
    b += 6


def is_circular(num):
    str_num = repr(num)
    length = len(str_num)
    if str_num.find('0') > 0 or str_num.find('2') > 0 or str_num.find('4') > 0 or str_num.find('5') > 0 \
        or str_num.find('6') > 0 or str_num.find('8') > 0  > 0:
        return False
    current = num
    while True:
        circular = current // 10 + (current%10)*(10**(length-1))
        if circular == num:
            break
        if circular not in primes[length-1]:
            return False
        current = circular
    return True

result = 0
for i in primes:
    for j in i:
        if is_circular(j):
            result += 1

print(result)

print('time: ', time.time() - start)