import time
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def get_length(target):
    total = 1
    primes = 0

    current = 1
    step = 2
    while True:
        for i in range(1,5):
            next_one = current + i*step
            total += 1
            if is_prime(next_one):
                primes += 1
        percent = primes / total
        if percent < target:
            return step+1
        step += 2
        current = next_one

start = time.time()
print(get_length(0.1))
print('time: ', time.time() - start)
