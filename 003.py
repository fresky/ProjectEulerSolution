import math

target = 600851475143

def is_prime(number):
    for i in range(int(math.sqrt(number))+1, 1, -1):
        if number%i==0:
            return i
    return 1

print(math.sqrt(target))

for i in range(int(math.sqrt(target))+1, 1,-1):
   if target%i==0 and is_prime(i)==1:
        print(i)
        break

