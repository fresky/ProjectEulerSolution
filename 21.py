import math
def get_divisors(number):
    result = 0
    for i in range(int(math.sqrt(number))+1, 0, -1):
        if number % i == 0:
            if i != math.sqrt(number) and i != 1:
                result +=number//i
            result+=i
    return result

divisors = {}
for i in range(10000):
    divisors[i] = get_divisors(i)

result = 0
for i in range(10000):
    if divisors[i] != i and divisors[i] in divisors and divisors[divisors[i]] == i:
        result += i

print(result)