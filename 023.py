import math
def get_abundant():
    result = []
    for i in range(12, 28123):
        divisors = get_divisors(i)
        if sum(divisors) > i:
            result.append(i)
    return result

def get_divisors(num):
    result = set([1])
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            result.add(i)
            result.add(num//i)
    return result

all_numbers = list(range(1,28123+1))
all_abundants = get_abundant()
length = len(all_abundants)

all_sum_abundants = set([])
for i in range(length):
    for j in range(i,length):
        number = all_abundants[i] + all_abundants[j]
        if number > 28123:
            break
        all_sum_abundants.add(number)
print((1+28123)*28123//2-sum(all_sum_abundants))
# print(sum(all_sum_abundants))

