target = 2000000

import math

list = list(range(1, target))

root = int(math.sqrt(target))+1

for i in range(2, root,1):
    if list[i-1] > 0:
        j = 2
        while i*j <= len(list):
            list[i*j-1]=0
            j+=1

print(sum(list)-1)