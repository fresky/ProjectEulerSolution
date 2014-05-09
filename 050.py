import time
import math

start = time.time()
primes = [2,3]
sum_primes = [0,2,5]

def is_prime(num):
    for i in primes:
        if i > math.sqrt(num):
            break
        if num % i == 0:
            return False
    return True

first = 6-1
second = 6+1
target = 1000000
while first < target and second < target:
    if is_prime(first):
        primes.append(first)
        sum_primes.append(first + sum_primes[-1])
    if is_prime(second):
        primes.append(second)
        sum_primes.append(second + sum_primes[-1])
    first += 6
    second += 6

total_prime = len(primes)
print(total_prime)

length = 0
answer = -1
pair = 0,0
for begin in range(0,total_prime-length):
    for end in range(total_prime-1, -1, -1):
        temp_len = end - begin
        if temp_len <= length:
            break
        diff = sum_primes[end] - sum_primes[begin]
        if diff in primes and temp_len > length:
            length = temp_len
            answer = diff
            pair = begin,end

print(answer)
print(length)
print(pair)
print(time.time() - start)
