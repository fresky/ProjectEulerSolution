row = 1001
start = 3
step = 2
stop = 3 + 3*step

result = 1
for i in range(row//2):
    result += (start+stop)*2
    step += 2
    start = stop + step
    stop = start + 3*step

print(result)
