from decimal import *

getcontext().prec = 100000

import re

regex = re.compile(r'0.0+(?P<num>\d+?)\1')

biggest = 0
result = 0

limit = 1000
for i in range(2, limit):
    str = repr(Decimal(1) / Decimal(i))
    search = regex.search(str)
    if search != None:
        repeat = search.group('num')
        if len(repeat) > biggest:
            biggest = len(repeat)
            result = i

print(result)
