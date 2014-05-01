level = 5
def get_limit():
    for n in range(1,100):
        if n*9**level < 10**(n+1)-1:
            return 10**(n+1)

result = []
for n in range(2, get_limit()):
    total = 0
    i = n
    while True:
        total += (i%10)**level
        i = i // 10
        if i == 0:
            break
    if total == n:
        result.append(n)

print(sum(result))