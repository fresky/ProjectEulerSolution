import time

start = time.time()
factorials = {0:1,1:1}
for i in range(2,10):
    factorials[i] = factorials[i-1]*i

def get_limit():
    limit = 2
    while True:
        if 10**limit-1 >factorials[9]*limit:
            return limit
        limit += 1

hig_limit = get_limit()*factorials[9]

def get_list(num):
    list = []
    while num > 0:
        list.append(num%10)
        num = num//10
    list.sort(reverse=True)
    return list

def is_valid(num):
    digits = get_list(num)
    total = 0
    for j in digits:
        total += factorials[j]
        if total>num:
            return False
    return total == num

result = []
for i in range(3,hig_limit):
    if is_valid(i):
        result.append(i)

print(sum(result))
print('time: ', time.time() - start)