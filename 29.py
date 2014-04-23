import math
high = 100
low = 2
total = int(math.pow((high-low+1),2))

for i in range(low,int(math.sqrt(high))+1):
    for j in range(low,high+1):
        if math.pow(i,j) <= high:
            total -= high//j - 1
        else:
           break

print(total)

result = []
for i in range(low, high+1):
    for j in range(low, high+1):
        result.append(int(math.pow(i,j)))

print(len(set(result)))
