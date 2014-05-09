import math
import time

primes = [2,3,5,7]



def is_prime(num):
    for i in primes:
        if i > int(math.sqrt(num)):
            break
        if num % i == 0:
            return False
    return True

def is_factors(num, target):
    factors = 0
    for i in primes:
        if i > num//2:
            break
        if num % i == 0:
            factors += 1
            if factors > target:
                return False
    return factors == target


def is_consecutive(num, target):
    loop = 0
    while loop < target:
        if not is_factors(num-loop, target):
            return False,loop
        loop += 1
    return True,-1

def get_consecutive(target):
    current = 10
    guess = 0
    current_target = target
    while True:
        if is_prime(current):
            primes.append(current)
            guess = 0
            current_target = target
        elif guess == current_target:
            consecutive, done = is_consecutive(current, target)
            current_target = target - done
            if consecutive:
                break
            else:
                guess = -1
        current += 1
        guess += 1
    return current-target+1

start = time.time()
print(get_consecutive(4))
print(time.time()-start)