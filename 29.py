import math
_high = 100
_low = 2



def getCountByCompuation(low, high):
    result = set([])
    for i in range(low, high+1):
        for j in range(low, high+1):
            result.add(int(math.pow(i,j)))
    return len(result)

print(getCountByCompuation(_low, _high))
