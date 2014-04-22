
result = 1
for i in range(1, 101):
    result *= i

sum = 0
for i in [int(s) for s in repr(int(result))]:
    sum += i

print(sum)