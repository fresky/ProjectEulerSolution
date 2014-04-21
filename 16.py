__author__ = 'Dawei'

import math

answer = int(math.pow(2,1000))

strAnswer = str(answer)
result = 0
for i in list(strAnswer):
    result += int(i)

print(result)

result = 0
while answer > 0:
    result += answer%10
    answer = answer//10

print(result)
