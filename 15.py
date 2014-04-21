__author__ = 'Dawei'

import time

def getLatticeByRecursive(m,n):
    if m==0 or n==0:
        return 1
    return getLatticeByRecursive(m-1,n)+getLatticeByRecursive(m,n-1)

def getLatticeByDP(row,col):
    m=row+1
    n=col+1
    result = [([0] * n) for i in range(m)]

    result[0] = [1]*n
    for i in range(m):
        result[i][0]=1

    for i in range(1,m):
        for j in range(1,n):
            result[i][j]=result[i-1][j]+result[i][j-1]

    return result[m-1][n-1]

print(getLatticeByDP(2,2))
print(getLatticeByDP(20,20))

start = time.clock()
print(getLatticeByRecursive(10,10))
print('time: ' + repr(time.clock()-start))

start = time.clock()
print(getLatticeByDP(10,10))
print('time: ' + repr(time.clock()-start))

