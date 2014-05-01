
def cancel(a,b):
    a1 = a % 10
    a2 = a // 10
    b1 = b %10
    b2 = b//10
    if a1==b1 and a1 != 0:
        return a2,b2
    if a1==b2 and a1 != 0:
        return a2,b1
    return 0,0

result = []

numerator = 1
denominator = 1
for a in range(10,100):
    for b in range(a+1,100):
        c,d = cancel(a,b)
        if c!=0 and a*d==b*c:
            numerator *= a
            denominator *= b
            result.append(repr(a) + '/' + repr(b))

print(result)
print(numerator)
print(denominator)

