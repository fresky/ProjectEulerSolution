a = 1
b = 1
current = 2
while True:
    c = a + b
    current += 1
    if len(repr(c)) >= 1000:
        break
    a = b
    b = c

print(c)
print(current)