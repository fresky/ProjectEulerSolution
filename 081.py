file_object = open('081.txt', 'r')
triangle = file_object.readlines()

row = len(triangle)

array = []
for line in triangle:
    array += [int(s) for s in line.split(',')]

import math
import sys
row = int(math.sqrt(len(array)))


for i in range(row):
    for j in range(row):
        if i == 0 and j == 0:
            continue
        if j > 0:
            left = array[i * row + j] + array[i * row + j - 1]
        else:
            left = sys.maxsize
        if i > 0:
            above = array[i * row + j] + array[(i - 1) * row + j]
        else:
            above = sys.maxsize
        array[i*row+j]=min(left, above)

print(array[-1])