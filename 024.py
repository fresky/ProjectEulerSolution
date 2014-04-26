target = 1000000-1
start = 10

digits = list(range(start))

while True:
    result = 1
    for i in range(1, start):
        result *= i
    current = target // result
    # print(start)
    # print(result)
    # print(current)
    print(digits[current], end='')
    digits.remove(digits[current])
    target = target%result
    start -= 1
    if start == 1:
        break

for i in digits:
    print(i, end='')





