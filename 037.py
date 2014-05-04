import math
import time

start = time.time()

primes=[2,3,5,7]
result=[]

def is_prime(number):
    for i in primes:
        if i > math.sqrt(number)+1:
            break
        if number % i == 0:
            return False
    return True

def is_truncatable_prime(number):
    base = 10
    a = number // base
    b = number % base

    while a > 0:
        if a in primes and b in primes:
            base *= 10
            a = number // base
            b = number % base
        else:
            return False
    return True



current = 11
while True:
    if is_prime(current):
        primes.append(current)
        if is_truncatable_prime(current):
            result.append(current)
            if len(result) == 11:
                break
    current += 2

print(sum(result))
print(result)
print(time.time()-start)