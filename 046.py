import math

primes = [3,5,7]

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_valid(num):
    for i in primes:
        root = math.sqrt((num - i) // 2)
        if root == int(root):
            return False
    return True

current = 11
while True:
    if is_prime(current):
        primes.append(current)
    elif is_valid(current):
        break
    current += 2

print(current)

