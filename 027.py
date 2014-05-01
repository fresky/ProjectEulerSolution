import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def get_primes(limit):
    result = set()
    for i in range(2, limit):
        if is_prime(i):
            result.add(i)
    return result

maximum = 40
answer = 1, 41

b_primes = get_primes(1000)
primes = set(b_primes)


for b in b_primes:
    for a in range(-999, 1000):
        start = maximum - 1
        current = int(math.fabs(start * start + a * start + b))
        if (current < 1000 and current not in primes) or not is_prime(current):
            continue
        start = 1
        while True:
            current = int(math.fabs(start * start + a * start + b))
            if current in primes or (current > 1000 and is_prime(current)):
                start += 1
                primes.add(current)
            else:
                break
        if start + 1 > maximum:
            maximum = start + 1
            answer = a,b

print(maximum)
print(answer)
print(answer[0]*answer[1])

