base = 10000000000

result = 0
for i in range(1,1001):
    product = i
    for j in range(1,i):
        product = (product * i) %base
    result = (result + product)%base

print(result)
